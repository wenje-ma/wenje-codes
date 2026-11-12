"""Stamp an invisible LaTeX text layer onto PDF pages.

The page's own text layer is discarded: the visual content is re-rendered as a
bitmap (or copied as vector content), and the hand-written LaTeX source is
written on top with zero opacity, so selecting the page yields compilable
LaTeX instead of the broken glyph codes the source file carries.
"""
from pathlib import Path
import argparse
import sys
import pymupdf

PAGE_BREAK=r"\newpage"
CJK_FONT="china-s"


def read_tex_lines(tex_path:Path)->list[list[str]]:
  """Split the LaTeX source into per-page, non-comment, non-empty lines."""
  pages:list[list[str]]=[[]]
  for raw in tex_path.read_text(encoding="utf-8").splitlines():
    line=raw.strip()
    if not line or line.startswith("%"):
      continue
    if line==PAGE_BREAK:
      pages.append([])
      continue
    pages[-1].append(line)
  return pages


def source_slots(page)->list[pymupdf.Rect]:
  """Line boxes of the source page, used as anchors for the invisible lines.

  Only the geometry is reused; whatever text the source stores in those boxes
  is irrelevant (it is about to be thrown away)."""
  boxes=[]
  for block in page.get_text("dict")["blocks"]:
    if block["type"]!=0:
      continue
    for line in block["lines"]:
      box=pymupdf.Rect(line["bbox"])
      if box.width>2 and box.height>2:
        boxes.append(box)
  return boxes


def synthetic_slots(page,fontsize=10)->list[pymupdf.Rect]:
  """Fallback ladder for pages that carry no text at all (pure scans)."""
  rect=page.rect
  left=rect.x0+72
  width=rect.width-144
  lead=fontsize*1.6
  boxes=[]
  y=rect.y0+90
  while y+fontsize<rect.y1-72:
    boxes.append(pymupdf.Rect(left,y,left+width,y+fontsize*1.2))
    y+=lead
  return boxes


def inject(page,lines,font):
  """Write the lines at zero opacity, so they paint nothing but stay selectable.

  TextWriter embeds the CJK font it uses; insert_text with the reserved name
  "china-s" leaves it unembedded and silently dropped two long lines in testing,
  hence this route."""
  boxes=source_slots(page) or synthetic_slots(page)
  count=len(boxes)
  writer=pymupdf.TextWriter(page.rect)
  for i,line in enumerate(lines):
    box=boxes[i] if i<count else boxes[i%count]
    unit=font.text_length(line,fontsize=1) or 1
    size=min(0.78*box.height,box.width/unit,30)
    size=max(size,0.8)
    writer.append(pymupdf.Point(box.x0,box.y1-0.18*box.height),line,font=font,fontsize=size)
  writer.write_text(page,opacity=0)


def build(src_path:Path,tex_path:Path,out_path:Path,dpi:int,vector:bool):
  tex_pages=read_tex_lines(tex_path)
  src=pymupdf.open(str(src_path))
  out=pymupdf.open()
  font=pymupdf.Font(CJK_FONT)
  zoom=dpi/72
  for index,src_page in enumerate(src):
    page=out.new_page(width=src_page.rect.width,height=src_page.rect.height)
    if vector:
      page.show_pdf_page(page.rect,src,index)
    else:
      pixmap=src_page.get_pixmap(matrix=pymupdf.Matrix(zoom,zoom),alpha=False)
      page.insert_image(page.rect,stream=pixmap.tobytes("png"))
    lines=tex_pages[index] if index<len(tex_pages) else []
    if lines:
      inject(page,lines,font)
    print(f"  page {index+1}: {len(lines)} LaTeX lines injected")
  out.save(str(out_path),garbage=3,deflate=True)
  out.close()
  src.close()
  return tex_pages


def verify(out_path:Path,tex_pages:list[list[str]]):
  """Read the written file back and demand every injected line to be there."""
  doc=pymupdf.open(str(out_path))
  flat="".join("".join(page.get_text().split()) for page in doc)
  doc.close()
  missing=[]
  for lines in tex_pages:
    for line in lines:
      if "".join(line.split()) not in flat:
        missing.append(line)
  return missing


def main():
  parser=argparse.ArgumentParser(description="Stamp an invisible LaTeX text layer onto a PDF")
  parser.add_argument("pdf",help="source PDF")
  parser.add_argument("--tex",required=True,help="hand-written LaTeX source; \\newpage starts a new page")
  parser.add_argument("--out",help="output PDF (default: <stem>_ocr.pdf next to the source)")
  parser.add_argument("--dpi",type=int,default=600,help="rasterisation dpi of the background (default 600)")
  parser.add_argument("--vector",action="store_true",help="keep the vector content instead of rasterising (the stale text layer survives)")
  parser.add_argument("--force",action="store_true",help="overwrite an existing output file")
  args=parser.parse_args()

  src_path=Path(args.pdf)
  tex_path=Path(args.tex)
  if not src_path.exists():
    sys.exit(f"missing source: {src_path}")
  if not tex_path.exists():
    sys.exit(f"missing tex: {tex_path}")
  out_path=Path(args.out) if args.out else src_path.with_name(src_path.stem+"_ocr.pdf")
  if out_path.exists() and not args.force and out_path.resolve()!=tex_path.resolve():
    sys.exit(f"output exists, pass --force to overwrite: {out_path}")

  print(f"stamping {tex_path.name} onto {src_path.name} ({args.dpi} dpi, {'vector' if args.vector else 'raster'})")
  tex_pages=build(src_path,tex_path,out_path,args.dpi,args.vector)
  missing=verify(out_path,tex_pages)
  total=sum(len(lines) for lines in tex_pages)
  if missing:
    print(f"verify: {len(missing)}/{total} lines NOT found after re-reading")
    for line in missing[:5]:
      print(f"  missing: {line[:60]}")
    sys.exit(1)
  print(f"verify: {total}/{total} lines readable back")
  print(f"written: {out_path} ({out_path.stat().st_size/1e6:.1f} MB)")
  return str(out_path)


if __name__=="__main__":
  main()
