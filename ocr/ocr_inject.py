"""Give a scanned PDF a real text layer without touching its appearance.

The page keeps its bitmap; invisible glyphs are written on top, positioned on
the lines they came from. Copying text out of the result then yields characters
in reading order, which is what a TeX-compiled PDF gives.
"""
from pathlib import Path
import unicodedata

import pymupdf

LATIN_TTF = Path(r"D:\wenje-ma\wenje-codes\.venv-ocr\Lib\site-packages\matplotlib\mpl-data\fonts\ttf\DejaVuSans.ttf")
CJK_TTF = Path(r"C:\Windows\Fonts\simhei.ttf")
ASCENT_TRIM = 0.25


class Painter:
  """Chooses a font per character so every glyph has a home.

  TextWriter cannot map supplementary-plane codepoints back to Unicode (a
  written U+1D466 reads back as U+1D55), so math italics are folded to their
  ASCII twins first; symbols such as ∈, ≤, ‖ live in the BMP and survive.
  """

  def __init__(self) -> None:
    self.fonts = []
    for path in (LATIN_TTF, CJK_TTF):
      if path.exists():
        self.fonts.append(pymupdf.Font(fontfile=str(path)))

  def runs(self, text: str) -> list[tuple[object, str]]:
    out: list[tuple[object, str]] = []
    for raw in text:
      for ch in unicodedata.normalize("NFKC", raw):
        slot = None
        for f in self.fonts:
          if f.has_glyph(ord(ch)):
            slot = f
            break
        if slot is None:
          continue
        if out and out[-1][0] is slot:
          out[-1] = (slot, out[-1][1] + ch)
        else:
          out.append((slot, ch))
    return out

  def size_for(self, text: str, rect: pymupdf.Rect) -> float:
    size = rect.height * 0.78
    probe = self.fonts[0]
    width = probe.text_length(text, fontsize=size) if text else 0
    if width > rect.width > 0:
      size *= rect.width / width
    return max(size, 0.8)


def place_line(writer: pymupdf.TextWriter, painter: Painter, text: str, rect: pymupdf.Rect) -> None:
  if not text.strip():
    return
  size = painter.size_for(text, rect)
  x = rect.x0
  for font, chunk in painter.runs(text):
    width = font.text_length(chunk, fontsize=size)
    slot = pymupdf.Rect(x, rect.y0, x + width * 1.6 + 40, rect.y1)
    writer.fill_textbox(slot, chunk, font=font, fontsize=size, lineheight=1.0)
    x += width


def clear_text_layer(doc: pymupdf.Document, page: pymupdf.Page) -> None:
  """Blank a page's content streams, keeping its full-page bitmap."""
  images = page.get_images(full=True)
  if len(images) != 1:
    return
  xref = images[0][0]
  rect = page.rect
  for stream_xref in page.get_contents():
    doc.update_stream(stream_xref, b"")
  page.insert_image(rect, xref=xref)


def inject_page(doc: pymupdf.Document, pno: int, blocks: list[dict], painter: Painter) -> int:
  page = doc.load_page(pno)
  if len(pymupdf.utils.get_text(page, "text").strip()) > 0:
    clear_text_layer(doc, page)
  writer = pymupdf.TextWriter(page.rect)
  drawn = 0
  for block in blocks:
    bbox = block.get("bbox") or block.get("rect")
    text = block.get("text") or block.get("latex") or ""
    rect = pymupdf.Rect(bbox)
    if rect.is_empty or rect.width <= 0:
      continue
    place_line(writer, painter, text, rect)
    drawn += 1
  writer.write_text(page, opacity=0)
  return drawn


def inject(src: Path, out: Path, blocks_by_page: dict[int, list[dict]]) -> dict[int, int]:
  doc = pymupdf.open(str(src))
  painter = Painter()
  stats = {}
  for pno, blocks in blocks_by_page.items():
    if 0 <= pno < len(doc):
      stats[pno] = inject_page(doc, pno, blocks, painter)
  doc.save(str(out), garbage=3, deflate=True)
  doc.close()
  return stats
