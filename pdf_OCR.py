from pathlib import Path
from tkinter import Tk,filedialog,messagebox
import fitz
from rapidocr_onnxruntime import RapidOCR
def ocr_pdf(pdf_path:str,output_pdf:str|None=None):
  pdf_file=Path(pdf_path)
  if not pdf_file.exists():
    raise FileNotFoundError(f"File not found: {pdf_file}")
  if output_pdf is None:
    out_file=pdf_file.with_name(pdf_file.stem+"_ocr.pdf")
  else:
    out_file=Path(output_pdf)
  doc=fitz.open(str(pdf_file))
  engine=RapidOCR()
  for i,page in enumerate(doc,start=1):
    _add_ocr_text_layer(page,engine)
    print(f"  Page {i}: OCR done, text layer written")
  doc.save(str(out_file),garbage=3,deflate=True)
  doc.close()
  print(f"Generated: {out_file}")
  return str(out_file)
def _add_ocr_text_layer(page,engine,dpi:int=200):
  zoom=dpi/72
  pix=page.get_pixmap(matrix=fitz.Matrix(zoom,zoom),alpha=False)
  result,_=engine(pix.tobytes("png"))
  if not result:
    return
  font=fitz.Font("china-s")
  tw=fitz.TextWriter(page.rect)
  for box,text,_conf in result:
    text=text.strip()
    if not text:
      continue
    xs=[p[0]/zoom for p in box]
    ys=[p[1]/zoom for p in box]
    x0,y_top=min(xs),min(ys)
    y_bot=max(ys)
    box_h=y_bot-y_top
    fontsize=box_h*0.85
    if fontsize<3:
      continue
    baseline=y_bot-box_h*0.12
    tw.append((x0,baseline),text,font=font,fontsize=fontsize)
  tw.write_text(page,opacity=0)
def select_and_convert_pdfs():
  root=Tk()
  root.withdraw()
  targets:list[Path]=[]
  seen:set[str]=set()
  while True:
    selected=filedialog.askopenfilenames(
      title='Select PDF files (multi-select; reselect for cross-folder, cancel to stop)',
      filetypes=[('PDF files','*.pdf'),('All Files','*.*')]
    )
    if selected:
      for f in selected:
        p=Path(f)
        if p.suffix.lower()!='.pdf':
          continue
        key=str(p.resolve())
        if key not in seen:
          seen.add(key)
          targets.append(p)
      if not messagebox.askyesno(
        title='Continue selecting',
        message=f'Selected {len(targets)} PDF files.\n\nYes -> continue selecting\nNo -> start OCR'):
        break
    else:
      break
  if not targets:
    print('No PDF file selected, exit.')
    return []
  converted=[]
  for pdf_path in targets:
    output=ocr_pdf(str(pdf_path))
    converted.append(output)
  print(f'Done, processed {len(converted)} files.')
  return converted
if __name__=="__main__":
  select_and_convert_pdfs()
