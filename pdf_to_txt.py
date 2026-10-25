from pathlib import Path
from tkinter import Tk,filedialog,messagebox
from pypdf import PdfReader
def pdf_to_txt(pdf_path:str,txt_path:str|None=None):
  pdf_file=Path(pdf_path)
  if not pdf_file.exists():
    raise FileNotFoundError(f"File not found: {pdf_file}")
  if txt_path is None:
    txt_file=pdf_file.with_suffix(".txt")
  else:
    txt_file=Path(txt_path)
  reader=PdfReader(str(pdf_file))
  pages_text=[]
  for i,page in enumerate(reader.pages,start=1):
    text=page.extract_text() or ""
    pages_text.append(f"--- Page {i} ---\n{text}\n")
  txt_file.write_text("\n".join(pages_text),encoding="utf-8")
  print(f"Generated: {txt_file}")
  return str(txt_file)
def select_and_convert_pdfs():
  root=Tk()
  root.withdraw()
  targets:list[Path]=[]
  seen:set[str]=set()
  while True:
    selected_files=filedialog.askopenfilenames(title='Select PDF files to convert (multi-select; reselect for cross-folder, cancel to stop)',filetypes=[('PDF files','*.pdf'),('All Files','*.*')])
    if selected_files:
      for f in selected_files:
        p=Path(f)
        if p.suffix.lower()!='.pdf':
          continue
        key=str(p.resolve())
        if key not in seen:
          seen.add(key)
          targets.append(p)
      if not messagebox.askyesno(
        title='Continue selecting',
        message=f'Selected {len(targets)} PDF files.\n\nYes -> continue selecting\nNo -> start converting'):
        break
    else:
      break
  if not targets:
    print('No file selected, exit.')
    return []
  converted=[]
  for pdf_path in targets:
    output=pdf_to_txt(str(pdf_path))
    converted.append(output)
  print(f'Done, processed {len(converted)} files.')
  return converted
if __name__=="__main__":
  select_and_convert_pdfs()
