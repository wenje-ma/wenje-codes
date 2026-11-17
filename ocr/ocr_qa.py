"""Dump a rebuilt page's text next to its image so a human can judge the layer."""
from pathlib import Path
import argparse
import unicodedata

import pymupdf


def main() -> None:
  ap = argparse.ArgumentParser()
  ap.add_argument("pdf")
  ap.add_argument("page", type=int)
  ap.add_argument("--png", default="")
  ap.add_argument("--chars", type=int, default=1500)
  args = ap.parse_args()

  doc = pymupdf.open(args.pdf)
  page = doc[args.page]
  text = unicodedata.normalize("NFKC", page.get_text("text"))
  flat = "".join(text.split())
  print(f"page {args.page}: {len(page.get_text())} chars, {len(page.get_text('dict')['blocks'])} blocks")
  print(flat[:args.chars])
  png = Path(args.png) if args.png else Path(args.pdf).with_name(f"{Path(args.pdf).stem}_p{args.page}.png")
  page.get_pixmap(dpi=200).save(str(png))
  print(f"image {png}")


if __name__ == "__main__":
  main()
