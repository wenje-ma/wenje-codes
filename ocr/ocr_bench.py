"""Benchmark text-layer engines against a PDF that already carries a real text layer.

Selected pages are rendered to bitmaps, rebuilt as one image-only PDF, and parsed
once. Each page's parse is then compared character by character with the page's
own text layer, so the number is a genuine error rate.
"""
from pathlib import Path
import argparse
import json
import os
import subprocess
import sys
import tempfile
import unicodedata
import difflib
import time

import pymupdf

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from ocr.latex2glyph import flatten


FOLD = {"−": "-", "⋯": "...", "···": "...", "·": ".", "‘": "'", "’": "'", "“": '"', "”": '"'}


def norm(s: str) -> str:
  s = unicodedata.normalize("NFKC", s)
  for k, v in FOLD.items():
    s = s.replace(k, v)
  return "".join(s.split())


def cer(gt: str, hyp: str) -> float:
  if not gt:
    return 0.0
  return 1.0 - difflib.SequenceMatcher(None, gt, hyp, autojunk=False).ratio()


def build_scan(src: pymupdf.Document, pages: list[int], dpi: int, out: Path) -> None:
  doc = pymupdf.open()
  for i in pages:
    page = src[i]
    pix = page.get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY)
    p = doc.new_page(width=page.rect.width, height=page.rect.height)
    p.insert_image(p.rect, stream=pix.tobytes("png"))
  doc.save(str(out), garbage=3, deflate=True)
  doc.close()


def run_mineru(pdf: Path, out_root: Path, backend: str, timeout: int) -> Path | None:
  cmd = [sys.executable, "-m", "mineru.cli.client", "-p", str(pdf), "-o", str(out_root),
         "-b", backend, "-m", "ocr", "-l", "ch", "-d", "cpu"]
  env = dict(os.environ, MINERU_MODEL_SOURCE="local")
  proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, env=env)
  if proc.returncode != 0:
    print(proc.stderr[-3000:], file=sys.stderr)
    return None
  hits = sorted(out_root.rglob("*_middle.json"))
  return hits[0] if hits else None


def page_text(middle: dict, pno: int) -> str:
  for page in middle["pdf_info"]:
    if page.get("page_idx") != pno:
      continue
    chunks = []
    for block in page.get("para_blocks", []) + page.get("discarded_blocks", []):
      for line in block.get("lines", []):
        for span in line.get("spans", []):
          content = span.get("content", "")
          if span.get("type") in ("inline_equation", "interline_equation"):
            chunks.append(flatten(content.strip("$ ")))
          else:
            chunks.append(content)
    return "".join(chunks)
  return ""


def main() -> None:
  ap = argparse.ArgumentParser()
  ap.add_argument("pdf")
  ap.add_argument("--pages", default="34-46")
  ap.add_argument("--dpi", type=int, default=300)
  ap.add_argument("--backend", default="pipeline")
  ap.add_argument("--timeout", type=int, default=1800)
  ap.add_argument("--work", default=str(Path(tempfile.gettempdir()) / "ocr_bench"))
  args = ap.parse_args()

  lo, hi = (int(x) for x in args.pages.split("-"))
  src = pymupdf.open(args.pdf)
  pages = list(range(lo, min(hi + 1, len(src))))
  work = Path(args.work)
  work.mkdir(parents=True, exist_ok=True)
  scan = work / "scan.pdf"
  build_scan(src, pages, args.dpi, scan)

  out_root = work / "out"
  t0 = time.time()
  middle_path = run_mineru(scan, out_root, args.backend, args.timeout)
  elapse = time.time() - t0
  if middle_path is None:
    print("engine failed")
    return
  middle = json.loads(middle_path.read_text(encoding="utf-8"))

  rows = []
  for k, pno in enumerate(pages):
    gt = norm(src[pno].get_text("text"))
    hyp = norm(page_text(middle, k))
    e = cer(gt, hyp)
    rows.append((pno, len(gt), len(hyp), e))
    print(f"p{pno:3d} gt={len(gt):5d} hyp={len(hyp):5d} CER={e*100:6.2f}%")
  total = sum(r[1] for r in rows)
  weighted = sum(r[3] * r[1] for r in rows) / total if total else 0
  print(f"weighted CER = {weighted*100:.2f}% over {len(rows)} pages, {elapse:.0f}s total, {elapse/len(rows):.1f}s/page")


if __name__ == "__main__":
  main()
