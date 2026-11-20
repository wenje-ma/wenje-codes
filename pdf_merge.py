import re,sys
from pathlib import Path
from tkinter import Tk,filedialog,messagebox
import fitz
def _common_stem(paths:list[Path])->str:
  stems=[re.sub(r"_part\d+$","",p.stem) for p in paths]
  if len(set(stems))==1:
    return stems[0]
  return paths[0].stem+"_merged"
def merge_pdfs(pdf_paths:list[str],out_dir:Path|None=None,out_name:str|None=None)->str:
  files=[Path(p) for p in pdf_paths]
  if not files:
    raise ValueError("No input PDFs")
  for f in files:
    if not f.exists():
      raise FileNotFoundError(f"File not found: {f}")
    if f.suffix.lower()!=".pdf":
      raise ValueError(f"Not a PDF: {f}")
  if out_dir is None:
    out_dir=files[0].parent
  out_dir.mkdir(exist_ok=True)
  name=out_name or _common_stem(files)
  out_path=out_dir/f"{name}.pdf"
  if out_path.resolve() in {f.resolve() for f in files}:
    out_path=out_dir/f"{name}_merged.pdf"
  doc=fitz.open()
  total=0
  try:
    for f in files:
      src=fitz.open(str(f))
      pages=src.page_count
      print(f"  Adding {f.name} ({pages} pages, {f.stat().st_size/1048576:.1f}MB)...",flush=True)
      doc.insert_pdf(src)
      src.close()
      total+=pages
    doc.set_metadata({})
    doc.save(str(out_path),garbage=3,deflate=True)
  finally:
    doc.close()
  print(f"Generated: {out_path.name} ({total} pages, {out_path.stat().st_size/1048576:.1f}MB)",flush=True)
  return str(out_path)
def parse_args(argv:list[str]):
  out_name=None
  files=[]
  i=1
  while i<len(argv):
    a=argv[i]
    if a=="--out" and i+1<len(argv):
      out_name=argv[i+1]
      i+=2
    else:
      files.append(a)
      i+=1
  return out_name,files
def select_pdfs()->list[Path]:
  root=Tk()
  root.withdraw()
  targets:list[Path]=[]
  seen:set[str]=set()
  while True:
    selected_files=filedialog.askopenfilenames(title="Select PDF files to merge (multi-select, in add order; reselect for cross-folder, cancel to stop)",filetypes=[("PDF files","*.pdf"),("All Files","*.*")])
    if selected_files:
      for f in selected_files:
        p=Path(f)
        if p.suffix.lower()!=".pdf":
          continue
        key=str(p.resolve())
        if key not in seen:
          seen.add(key)
          targets.append(p)
      if not messagebox.askyesno(
        title="Continue selecting",
        message=f"Selected {len(targets)} PDF files.\n\nYes -> continue selecting\nNo -> start merging (order = selection order)"):
        break
    else:
      break
  return targets
def main():
  out_name,files=parse_args(sys.argv)
  if files:
    selected=[Path(a) for a in files]
  else:
    selected=select_pdfs()
  if not selected:
    print("No file selected, exit.",flush=True)
    return
  if len(selected)<2:
    print("Need at least 2 PDFs to merge, exit.",flush=True)
    return
  print(f"\nProcessing: {len(selected)} files -> 1",flush=True)
  for f in selected:
    print(f"  {f.name} ({f.stat().st_size/1048576:.1f}MB)",flush=True)
  try:
    merge_pdfs([str(p) for p in selected],out_name=out_name)
  except Exception as e:
    print(f"Failed: {str(e)}",flush=True)
def _run():
  try:
    main()
  finally:
    print("Done.",flush=True)
if __name__=="__main__":
  try:
    _run()
  except Exception as e:
    print(f"Failed: {str(e)}",flush=True)
  try:
    sys.stdout.flush()
    input("Press Enter to exit...")
  except(EOFError,KeyboardInterrupt):
    pass
