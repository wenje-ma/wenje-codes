# $py = "D:\wenje-ma\wenje-codes\.venv-ocr\Scripts\python.exe"
# & $py "D:\wenje-ma\wenje-codes\ocr_books.py" --jobs 2

from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import threading
import time

import pymupdf

from ocr.latex2glyph import flatten
from ocr.ocr_inject import Painter, inject_page


def page_blocks(middle: dict, scale: float = 1.0) -> dict[int, list[dict]]:
  """Line rectangles and flattened text, keyed by index inside the parsed chunk.

  `scale` maps coordinates from an upsampled chunk back to the source page.
  """
  out: dict[int, list[dict]] = {}
  for page in middle["pdf_info"]:
    idx = page.get("page_idx", 0)
    blocks = []
    for block in page.get("para_blocks", []) + page.get("discarded_blocks", []):
      for line in block.get("lines", []):
        pieces = []
        for span in line.get("spans", []):
          content = span.get("content", "")
          if span.get("type") in ("inline_equation", "interline_equation"):
            pieces.append(flatten(content.strip("$ ")))
          else:
            pieces.append(content)
        text = "".join(pieces).strip()
        if text:
          box = [v / scale if k < 4 else v for k, v in enumerate(line["bbox"])]
          blocks.append({"text": text, "bbox": box})
    out[idx] = blocks
  return out


VENV_PY = Path(r"D:\wenje-ma\wenje-codes\.venv-ocr\Scripts\python.exe")


def engine_python() -> str:
  """The interpreter that owns torch and mineru, whatever runs this file."""
  return str(VENV_PY) if VENV_PY.exists() else sys.executable


def upsampled_chunk(src: Path, first: int, last: int, work: Path, scale: float) -> Path:
  """A chunk re-rendered at `scale` times its page size.

  The engine renders a page at a fixed 200 dpi whatever its point size, so a
  doubled page gives it twice the pixels per character and stops it from
  dropping radicals.
  """
  out = work / f"up_{first:05d}_{last:05d}_{scale:g}.pdf"
  if out.exists():
    return out
  src_doc = pymupdf.open(str(src))
  dst = pymupdf.open()
  for pno in range(first, min(last + 1, len(src_doc))):
    page = src_doc[pno]
    pix = page.get_pixmap(matrix=pymupdf.Matrix(scale, scale), colorspace=pymupdf.csGRAY)
    width, height = page.rect.width * scale, page.rect.height * scale
    dst.new_page(width=width, height=height).insert_image(pymupdf.Rect(0, 0, width, height), pixmap=pix)
  dst.save(str(out), garbage=3, deflate=True)
  dst.close()
  src_doc.close()
  return out


LIVE: set[subprocess.Popen] = set()
LIVE_LOCK = threading.Lock()


def run_engine(cmd: list[str], env: dict, timeout: int) -> tuple[int, str]:
  """Run the engine and hold its handle, so Ctrl+C can kill the whole tree.

  A plain `subprocess.run` can be interrupted but leaves the engine running: it is
  a separate process, not a thread, and it will happily burn every core for the
  next hour while the console looks empty.
  """
  proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          text=True, env=env)
  with LIVE_LOCK:
    LIVE.add(proc)
  try:
    _, err = proc.communicate(timeout=timeout)
  except subprocess.TimeoutExpired:
    proc.kill()
    proc.communicate()
    return 1, f"timeout after {timeout}s"
  finally:
    with LIVE_LOCK:
      LIVE.discard(proc)
  return proc.returncode, err or ""


def stop_engines() -> None:
  """Kill every engine still running, children included — `taskkill /T` walks the tree."""
  with LIVE_LOCK:
    procs = list(LIVE)
  for proc in procs:
    if proc.poll() is None:
      subprocess.run(["taskkill", "/PID", str(proc.pid), "/T", "/F"],
                     capture_output=True, text=True)
  with LIVE_LOCK:
    LIVE.clear()


def parse_chunk(src: Path, first: int, last: int, work: Path, backend: str, timeout: int,
                scale: float = 1.0) -> tuple[str, str]:
  cache = work / f"blocks_{first:05d}_{last:05d}_s{scale:g}.json"
  if cache.exists():
    return str(cache), "cached"
  raw = work / f"raw_{first:05d}_{last:05d}"
  raw.mkdir(parents=True, exist_ok=True)
  if scale > 1:
    feed = upsampled_chunk(src, first, last, work, scale)
    start, end = 0, last - first
  else:
    feed, start, end = src, first, last
  cmd = [engine_python(), "-m", "mineru.cli.client", "-p", str(feed), "-o", str(raw),
         "-b", backend, "-m", "ocr", "-l", "ch", "-d", "cpu",
         "-s", str(start), "-e", str(end)]
  env = dict(os.environ, MINERU_MODEL_SOURCE="local",
             OMP_NUM_THREADS=os.environ.get("OCR_THREADS", "3"),
             MKL_NUM_THREADS=os.environ.get("OCR_THREADS", "3"),
             OPENBLAS_NUM_THREADS=os.environ.get("OCR_THREADS", "3"))
  code, err = run_engine(cmd, env, timeout)
  if code != 0:
    return f"{first}-{last} failed: {err[-300:]}", "failed"
  hits = sorted(raw.rglob("*_middle.json"))
  if not hits:
    return f"{first}-{last} no middle json", "failed"
  middle = json.loads(hits[0].read_text(encoding="utf-8"))
  blocks = page_blocks(middle, scale)
  cache.write_text(json.dumps(blocks, ensure_ascii=False), encoding="utf-8")
  if scale > 1:
    feed.unlink(missing_ok=True)
  return str(cache), "ok"


def targets_of(path: Path) -> list[Path]:
  """Every PDF a folder or a single file stands for, our own outputs excluded.

  Virtual environments and node_modules are skipped: they hold generated PDFs that
  are not books, and scanning them turns a 364 file library into a long detour.
  """
  junk = (".venv", "node_modules", "__pycache__")
  if path.is_file():
    return [path] if path.suffix.lower() == ".pdf" and not path.stem.endswith("_ocr") else []
  files = [p for p in path.rglob("*.pdf")
           if p.is_file() and not p.stem.endswith("_ocr")
           and not any(j in str(p).lower() for j in junk)]
  files.sort(key=lambda p: str(p).lower())
  return files


def select_target():
  """The folder dialog the rest of the toolbox uses, floating above the console."""
  try:
    from tkinter import Tk, filedialog
  except ImportError:
    say("No folder dialog on this Python (tkinter missing); pass a path instead.")
    return None
  root = Tk()
  root.withdraw()
  root.attributes("-topmost", True)
  folder = filedialog.askdirectory(
    parent=root, title="Select a folder — every PDF inside it gets processed")
  root.destroy()
  return Path(folder) if folder else None


def page_text(page: pymupdf.Page) -> str:
  """A page's plain text, pinned to `str` so type checkers stop widening it."""
  return str(page.get_text("text"))


def has_real_text_layer(doc: pymupdf.Document, sample: int = 6) -> bool:
  """True when the book already carries a usable text layer of its own.

  Sampled, not exhaustive: a book whose checks come back empty is treated as a
  scan, which is the cheap direction to be wrong in — six blank pages cannot fake
  a real layer, while six dense pages are enough to trust the rest.
  """
  total = len(doc)
  if total == 0:
    return False
  step = max(total // sample, 1)
  probes = [page_text(doc[i]) for i in range(0, total, step)][:sample]
  if not probes:
    return False
  return sum(len(t.strip()) for t in probes) / len(probes) > 40


def text_layer_present(path: Path) -> bool:
  """Sample the file for a real text layer.

  This is the whole "already done" test now that results overwrite the source: a
  processed book carries our injected layer, so a second pass over the same folder
  finds it and moves on.
  """
  try:
    doc = pymupdf.open(str(path))
  except Exception:
    return False
  try:
    return has_real_text_layer(doc)
  finally:
    doc.close()


def save_atomic(doc: pymupdf.Document, out: Path) -> None:
  """Write through `.part`, close, then swap it in.

  Windows refuses to replace a file that still holds an open handle, and the
  target is now often the source itself, so the document has to be closed before
  the rename. `.part` still guarantees an interruption never leaves half a PDF.
  """
  part = out.with_name(out.name + ".part")
  doc.save(str(part), garbage=3, deflate=True)
  doc.close()
  os.replace(str(part), str(out))


def page_ink(page: pymupdf.Page, dpi: int = 48) -> float:
  """Share of dark pixels on a page: a cheap stand-in for how much work it is.

  Rendering at 48 dpi costs milliseconds and reads the same signal the engine
  pays for later — a dense formula page is covered in ink, a page of prose is not.
  """
  pix = page.get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY)
  data = pix.samples
  if not data:
    return 0.0
  return sum(1 for v in data if v < 128) / len(data)


def complexity(path: Path, cache: dict | None = None, probes: int = 4,
               stats: dict | None = None) -> dict:
  """Page count and sampled ink, folded into one sortable score.

  Pages and ink multiply rather than add: a 400 page book of prose still costs
  more than a 40 page book, and a page that takes minutes of formula work is not
  made cheaper by a neighbour that is blank. Scores are cached by size and mtime,
  so the second run over the same library plans in milliseconds.
  """
  key = str(path).lower()
  try:
    stat = path.stat()
  except OSError:
    return {"path": path, "pages": 0, "ink": 0.0, "score": 0.0}
  hit = (cache or {}).get(key)
  if hit and hit.get("size") == stat.st_size and hit.get("mtime") == int(stat.st_mtime):
    if stats is not None:
      stats["cached"] = stats.get("cached", 0) + 1
    return {"path": path, "pages": hit["pages"], "ink": hit["ink"], "score": hit["score"]}
  if stats is not None:
    stats["measured"] = stats.get("measured", 0) + 1
  try:
    doc = pymupdf.open(str(path))
  except Exception:
    return {"path": path, "pages": 0, "ink": 0.0, "score": 0.0}
  total = len(doc)
  if total == 0:
    doc.close()
    return {"path": path, "pages": 0, "ink": 0.0, "score": 0.0}
  step = max(total // probes, 1)
  picks = list(range(0, total, step))[:probes]
  ink = sum(page_ink(doc[i]) for i in picks) / len(picks)
  doc.close()
  entry = {"path": path, "pages": total, "ink": round(ink, 3),
           "score": round(total * (1 + 5 * ink), 1)}
  if cache is not None:
    cache[key] = {"size": stat.st_size, "mtime": int(stat.st_mtime), "pages": total,
                  "ink": entry["ink"], "score": entry["score"]}
  return entry


def page_count(path: Path) -> int:
  """Just the page count, for `--order name` which must not pay for ink sampling."""
  try:
    doc = pymupdf.open(str(path))
  except Exception:
    return 0
  total = len(doc)
  doc.close()
  return total


def order_targets(files: list[Path], mode: str, cache: dict | None = None) -> list[dict]:
  """The queue, cheapest first by default so a pause never strands a half book."""
  plans = []
  stats = {"cached": 0, "measured": 0}
  for i, path in enumerate(files, 1):
    if mode == "name":
      plans.append({"path": path, "pages": page_count(path), "ink": 0.0, "score": 0.0})
    else:
      plans.append(complexity(path, cache, stats=stats))
    if stats["measured"] and stats["measured"] % 25 == 0:
      say(f"plan: measured {stats['measured']}, reused {stats['cached']} ({i}/{len(files)})")
  if mode != "name":
    say(f"plan done: {stats['measured']} measured, {stats['cached']} reused")
  if mode == "easy":
    plans.sort(key=lambda d: (d["score"], str(d["path"]).lower()))
  elif mode == "hard":
    plans.sort(key=lambda d: (-d["score"], str(d["path"]).lower()))
  return plans


def clock(seconds: float) -> str:
  seconds = max(int(seconds), 0)
  hours, rest = divmod(seconds, 3600)
  minutes, secs = divmod(rest, 60)
  return f"{hours}h{minutes:02d}m" if hours else f"{minutes}m{secs:02d}s"


def plan_home() -> Path:
  home = Path(os.environ.get("TEMP", ".")) / "ocr_books"
  home.mkdir(parents=True, exist_ok=True)
  return home


def load_plan_cache() -> dict:
  try:
    return json.loads((plan_home() / "plan.json").read_text(encoding="utf-8"))
  except (OSError, ValueError):
    return {}


def save_plan_cache(cache: dict) -> None:
  """Merge into what is on disk before writing, so parallel consoles keep both."""
  try:
    path = plan_home() / "plan.json"
    try:
      on_disk = json.loads(path.read_text(encoding="utf-8"))
      on_disk.update(cache)
      cache = on_disk
    except (OSError, ValueError):
      pass
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(cache), encoding="utf-8")
    tmp.replace(path)
  except OSError:
    pass


def bar_glyphs() -> tuple[str, str]:
  """Solid blocks when the console can take them, ASCII when it cannot."""
  try:
    "█░".encode(getattr(sys.stdout, "encoding", None) or "utf-8")
    return "█", "░"
  except (UnicodeEncodeError, TypeError, LookupError):
    return "#", "."


class Status:
  """One row of the terminal, rewritten in place — what pip's bar really is.

  A carriage return moves the cursor to column zero without starting a new line,
  so the next write lands on top of the previous one. Log lines therefore have to
  be printed above the bar: the bar is erased first (spaces over its own width),
  the message goes out with a newline, and the next draw starts on a fresh row.

  Anything that is not a terminal (a redirected log, a pipe) gets a plain line
  every `slow` seconds instead, because a bare carriage return in a file is noise.
  """

  def __init__(self):
    self.lock = threading.Lock()
    self.tty = bool(getattr(sys.stdout, "isatty", lambda: False)())
    self.full, self.empty = bar_glyphs()
    self.width = 0
    self.last = 0.0
    self.slow = 0.0 if self.tty else 30.0

  def say(self, msg: str) -> None:
    with self.lock:
      if self.tty and self.width:
        sys.stdout.write("\r" + " " * self.width + "\r")
      sys.stdout.write(msg + "\n")
      self.width = 0
      sys.stdout.flush()

  def draw(self, text: str, force: bool = False) -> None:
    now = time.time()
    if not force and self.slow and now - self.last < self.slow:
      return
    with self.lock:
      if self.tty:
        sys.stdout.write("\r" + text + " " * max(self.width - len(text), 0))
        self.width = len(text)
      else:
        sys.stdout.write(text + "\n")
      sys.stdout.flush()
      self.last = now


STATUS = Status()


def say(msg: str) -> None:
  STATUS.say(msg)


def paint(state: dict, force: bool = False) -> None:
  """Draw the bar: progress, pages done, elapsed, ETA, speed and the current book."""
  with state["lock"]:
    done, total = state["done"], state["total"]
    if not total:
      return
    elapsed = time.time() - state["start"]
    rate = done / elapsed if elapsed > 0 and done else 0
    left = (total - done) / rate if rate else 0
    cells = 20
    filled = int(cells * done / total)
    bar = STATUS.full * filled + STATUS.empty * (cells - filled)
    speed = f"{rate * 60:5.1f} p/min" if elapsed > 30 else "      —    "
    line = (f"[{bar}] {100 * done / total:5.1f}%  {done}/{total}p  "
            f"{clock(elapsed)} elapsed  left ~{clock(left)}  {speed}  "
            f"{state['file']}")
    note = {"done": done, "total": total, "percent": round(100 * done / total, 1),
            "elapsed_s": int(elapsed), "eta_s": int(left), "file": state["file"],
            "tag": state["tag"]}
  STATUS.draw(line, force=force)
  home = plan_home()
  try:
    # One file per run: several consoles on different books must not overwrite
    # each other's numbers. `progress.json` stays as the mirror of the newest run.
    body = json.dumps(note, ensure_ascii=False)
    (home / f"progress_{state['tag']}.json").write_text(body, encoding="utf-8")
    (home / "progress.json").write_text(body, encoding="utf-8")
  except OSError:
    pass


def watch(state: dict, every: int = 5) -> None:
  while not state["stop"].wait(every):
    paint(state)


def build_one(src: Path, out: Path, args, state: dict | None = None) -> dict:
  doc = pymupdf.open(str(src))
  total = len(doc)

  key = hashlib.sha1(str(src.resolve()).lower().encode("utf-8")).hexdigest()[:10]
  work = Path(args.work) if args.work else Path(os.environ.get("TEMP", ".")) / "ocr_books" / f"{src.stem}_{key}"
  work.mkdir(parents=True, exist_ok=True)

  stop = total if args.last < 0 else min(args.last + 1, total)
  specs = [(a, min(a + args.chunk - 1, stop - 1)) for a in range(args.first, stop, args.chunk)]

  started = time.time()
  result = {}
  pool = ThreadPoolExecutor(max_workers=args.jobs)
  try:
    futures = {pool.submit(parse_chunk, src, a, b, work, args.backend, args.timeout,
                           args.scale): (a, b) for a, b in specs}
    for fut in as_completed(futures):
      a, b = futures[fut]
      path, status = fut.result()
      result[a] = (b, path) if status != "failed" else (b, None)
      done = sum(1 for v in result.values() if v[1])
      pages = min(b, total - 1) - a + 1
      if state:
        with state["lock"]:
          state["done"] += pages
          state["file"] = f"{src.name} (chunk {a}-{b})"
      say(f"chunk {a}-{b} of {src.name} {status} "
          f"({done}/{len(specs)} chunks, {time.time()-started:.0f}s)")
      if state:
        paint(state)
  finally:
    pool.shutdown(wait=False, cancel_futures=True)

  painter = Painter()
  empty = []
  for a, (b, path) in sorted(result.items()):
    if not path:
      continue
    blocks = json.loads(Path(path).read_text(encoding="utf-8"))
    for key, bl in blocks.items():
      pno = a + int(key)
      if not bl:
        empty.append(pno)
        continue
      inject_page(doc, pno, bl, painter)
  save_atomic(doc, out)

  report = {"pdf": str(src), "pages": total, "empty_pages": empty,
            "seconds": round(time.time() - started, 1), "out": str(out)}
  (work / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
  say(f"wrote {out}  empty pages: {len(empty)}  {report['seconds']}s")
  return report


def main() -> None:
  ap = argparse.ArgumentParser()
  ap.add_argument("path", nargs="?", default="")
  ap.add_argument("--out-dir", default="")
  ap.add_argument("--chunk", type=int, default=20)
  ap.add_argument("--jobs", type=int, default=2)
  ap.add_argument("--backend", default="pipeline")
  ap.add_argument("--timeout", type=int, default=7200)
  ap.add_argument("--first", type=int, default=0)
  ap.add_argument("--last", type=int, default=-1)
  ap.add_argument("--work", default="")
  ap.add_argument("--scale", type=float, default=2.0)
  ap.add_argument("--force", action="store_true", help="rebuild even when the output already exists")
  ap.add_argument("--ocr-anyway", action="store_true",
                  help="OCR a PDF that already has a text layer instead of copying it")
  ap.add_argument("--order", default="easy", choices=("easy", "hard", "name"),
                  help="queue order: easiest first (default), hardest first, or as found")
  ap.add_argument("--plan-only", action="store_true",
                  help="print the queue and the page total, then exit without touching a page")
  ap.add_argument("--min-pages", type=int, default=1,
                  help="skip PDFs with fewer pages than this (drops cropped figure slices)")
  args = ap.parse_args()

  target = Path(args.path) if args.path else select_target()
  if target is None or not target.exists():
    say("No folder or file selected, exit.")
    return
  files = targets_of(target)
  if not files:
    say(f"No PDF worth OCR in: {target}")
    return
  say(f"{len(files)} PDF(s) under {target}")

  pending = []
  for src in files:
    # The result replaces the source, so "already done" is decided by the text
    # layer itself: an untouched scan has none, a processed one carries ours.
    if not (args.force or args.ocr_anyway) and text_layer_present(src):
      say(f"skip {src.name}: already has a text layer")
      continue
    out = Path(args.out_dir) / src.name if args.out_dir else src
    out.parent.mkdir(parents=True, exist_ok=True)
    pending.append((src, out))

  if not pending:
    say("Everything is already done.")
    return

  outs = dict(pending)
  tag = re.sub(r"[^A-Za-z0-9_.-]+", "_", target.name)[:24] or "run"
  if str(target) != str(target.resolve()) or len(tag) < 3:
    tag = f"{tag}_{hashlib.sha1(str(target).encode()).hexdigest()[:6]}"
  state = {"done": 0, "total": 0, "start": time.time(), "file": "", "tag": tag,
           "lock": threading.Lock(), "stop": threading.Event()}
  try:
    plan_cache = load_plan_cache()
    plans = order_targets([src for src, _ in pending], args.order, plan_cache)
    save_plan_cache(plan_cache)
    if args.min_pages > 1:
      plans = [p for p in plans if p["pages"] >= args.min_pages]
    total_pages = sum(p["pages"] for p in plans)
    state["total"] = total_pages
    say(f"{len(plans)} PDF(s) to do, {total_pages} pages, order: {args.order}")
    for i, plan in enumerate(plans, 1):
      name = plan["path"].name if target.is_file() else str(plan["path"])
      say(f"  {i:2d}. {plan['pages']:4d}p  ink {plan['ink']:.2f}  "
          f"score {plan['score']:6.1f}  {name}")
    if args.plan_only:
      return
    threading.Thread(target=watch, args=(state,), daemon=True).start()
    for plan in plans:
      src = plan["path"]
      state["file"] = src.name
      build_one(src, outs[src], args, state)
  except KeyboardInterrupt:
    state["stop"].set()
    stop_engines()
    say("\ninterrupted: engines stopped, finished chunks stay cached, "
        "rerun the same command to resume.")
    os._exit(130)


if __name__ == "__main__":
  main()
