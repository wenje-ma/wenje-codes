"""Replace full-width and CJK punctuation with half-width ASCII, spaced like English text.

CJK blocks (U+3000-U+303F), full-width forms (U+FF01-U+FF5E) and the curly quotes
become their ASCII counterparts. The em dash (U+2014) and the interpunct (U+00B7)
stay: both already are the English glyphs.

Spacing follows the convention the corpus already uses outside code: one space
after a terminator, one before an opening bracket, one after a closing bracket
before Chinese text. Fenced code, inline code and TeX comments are untouched,
and nothing inside a math span gains a space.
"""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

import math_space_strip as m

SPACE = m.SPACE

PUNCT = {
  "，": ",", "、": ",", "。": ".", "：": ":", "；": ";", "？": "?", "！": "!",
  "（": "(", "）": ")", "【": "[", "】": "]", "〔": "(", "〕": ")",
  "「": '"', "」": '"', "『": '"', "』": '"',
  "“": '"', "”": '"', "‘": "'", "’": "'", "《": '"', "》": '"',
  "…": "...", "　": " ",
}

OPENERS = set("《「『“")
CLOSERS = set("》」』”")
TERM = set(",.;:?!")
TEXTY = set("$\\*")


def _trim(out):
  """No space before a comma, period, colon or closing bracket."""
  while out and out[-1] == " " and len(out) > 1 and out[-2] not in "\r\n":
    out.pop()


def _is_text(ch):
  """Character that reads as prose and therefore wants a space next to a mark."""
  if ch is None or ch in SPACE or ch in "\r\n":
    return False
  code = ord(ch)
  return (0x4E00 <= code <= 0x9FFF) or ch.isalnum() or ch in TEXTY


def _front_matter_ranges(text):
  """YAML block at the head of the file, where a raw double quote would break it."""
  if not text.startswith("---"):
    return []
  lines = text.splitlines(keepends=True)
  end = 0
  for i, line in enumerate(lines[1:], 1):
    if line.rstrip() in ("---", "..."):
      end = sum(len(l) for l in lines[:i + 1])
      return [(0, end)]
  return []


def _map(ch, suffix, in_yaml):
  """Replacement for one character, or None when it is to be left alone."""
  if ch in PUNCT:
    r = PUNCT[ch]
    if in_yaml and r == '"':
      return "'"
    return r
  code = ord(ch)
  if 0xFF01 <= code <= 0xFF5E:
    if ch == "％" and suffix == ".tex":
      return None
    return chr(code - 0xFEE0)
  return None


def convert_text(text, suffix, counters):
  mask = m.skip_mask(text, suffix)
  spans = m.math_spans(text, suffix)
  in_math = []
  for a, b, _, _ in spans:
    in_math.append((a, b))
  yaml_ranges = _front_matter_ranges(text)
  math_at = {i for a, b in in_math for i in range(a, b)}
  out = []
  i = 0
  n = len(text)
  yaml_mark = 0
  while i < n:
    if mask[i]:
      out.append(text[i])
      i += 1
      continue
    ch = text[i]
    while yaml_mark < len(yaml_ranges) and i >= yaml_ranges[yaml_mark][1]:
      yaml_mark += 1
    in_yaml = yaml_mark < len(yaml_ranges)
    chunk = ch
    if ch == "…" and i + 1 < n and text[i + 1] == "…":
      chunk = "……"
      i += 2
    else:
      i += 1
    rep = _map(ch, suffix, in_yaml)
    if rep is None:
      out.append(chunk)
      continue
    counters[ch] += 1
    at_math = (i - 1) in math_at
    prev = out[-1] if out else "\n"
    nxt = text[i] if i < n else None
    if at_math:
      out.append(rep)
      continue
    if rep == " ":
      if prev not in SPACE and prev not in "\r\n":
        out.append(" ")
      continue
    if rep == "(":
      if prev not in SPACE and prev not in "\r\n" and (prev.isalnum() or prev in "$)*"):
        out.append(" ")
      out.append("(")
      continue
    if rep == ")":
      _trim(out)
      out.append(")")
      if _is_text(nxt):
        out.append(" ")
      continue
    if ch in OPENERS:
      if prev not in SPACE and prev not in "\r\n" and prev not in "([{":
        out.append(" ")
      out.append(rep)
      continue
    if ch in CLOSERS:
      _trim(out)
      out.append(rep)
      if _is_text(nxt):
        out.append(" ")
      continue
    if rep in TERM:
      _trim(out)
      out.append(rep)
      if _is_text(nxt):
        out.append(" ")
      continue
    if rep == "...":
      _trim(out)
      out.append("...")
      if _is_text(nxt):
        out.append(" ")
      continue
    out.append(rep)
  s = "".join(out)
  counters["double-space"] += len(re.findall(r"[ \t]{2,}", s))
  return s


def process_file(path, stats, dry_run):
  raw = path.read_bytes()
  bom = raw.startswith(b"\xef\xbb\xbf")
  data = raw[3:] if bom else raw
  try:
    text = data.decode("utf-8")
  except UnicodeDecodeError:
    print(f"Skipped (non-UTF-8): {path}")
    stats["skipped_encoding"] += 1
    return
  counters = Counter()
  new = convert_text(text, path.suffix.lower(), counters)
  if new == text:
    return
  new_mask = m.skip_mask(new, path.suffix.lower())
  left = [ch for i, ch in enumerate(new) if not new_mask[i] and (
    ord(ch) in range(0x3000, 0x3040) or ord(ch) in range(0xFF00, 0xFF5F)
    or ch in "“”‘’…")]
  if left:
    print(f"Skipped (full-width left): {path} {left[:4]!r}")
    stats["rejected"] += 1
    return
  stats["files"] += 1
  stats["chars"].update({k: v for k, v in counters.items() if len(k) == 1})
  if not dry_run:
    path.write_bytes((("\ufeff" if bom else "") + new).encode("utf-8"))
  else:
    print(f"Would convert: {path}  ({sum(v for k, v in counters.items() if len(k) == 1)} marks)")


def main():
  ap = argparse.ArgumentParser(description=__doc__)
  ap.add_argument("path", nargs="?", help="folder or single file")
  ap.add_argument("--dry-run", action="store_true")
  a = ap.parse_args()
  target = Path(a.path) if a.path else Path(".")
  stats = {"files": 0, "rejected": 0, "skipped_encoding": 0, "chars": Counter()}
  files = [target] if target.is_file() else [
    p for p in sorted(target.rglob("*"), key=lambda q: str(q).lower())
    if p.is_file() and p.suffix.lower() in (".md", ".qmd", ".tex")]
  for p in files:
    process_file(p, stats, a.dry_run)
  print("---- summary ----")
  print(f"changed files {stats['files']}, rejected {stats['rejected']}, "
        f"non-UTF-8 {stats['skipped_encoding']}")
  total = sum(stats["chars"].values())
  print(f"marks replaced {total}, distinct {len(stats['chars'])}")
  top = ", ".join(f"{k}{v}" for k, v in stats["chars"].most_common(12))
  print("  " + top)


if __name__ == "__main__":
  sys.exit(main())
