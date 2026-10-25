import sys
from pathlib import Path
from tkinter import Tk,filedialog,messagebox
import fitz
DEFAULT_LIMIT_BYTES=95*1024*1024
def _measure(doc,start:int,end:int,tmp:Path)->int:
  print(f"  Measuring pages {start+1}-{end+1}...",flush=True)
  out=fitz.open()
  out.insert_pdf(doc,from_page=start,to_page=end)
  out.save(str(tmp),garbage=3,deflate=True)
  out.close()
  size=tmp.stat().st_size
  print(f"    -> {size/1048576:.1f}MB",flush=True)
  return size
def _find_end(doc,start:int,n:int,limit_bytes:int,tmp:Path)->int:
  first=_measure(doc,start,start,tmp)
  est=max(1,int(limit_bytes*0.9/max(first,1)))
  guess=min(start+est-1,n-1)
  if guess>start:
    if _measure(doc,start,guess,tmp)<limit_bytes:
      lo,hi=guess,n-1
    else:
      lo,hi=start,guess
  else:
    lo,hi=start,start
  best=start
  while lo<=hi:
    mid=(lo+hi)//2
    if _measure(doc,start,mid,tmp)<limit_bytes:
      best=mid
      lo=mid+1
    else:
      hi=mid-1
  return best
def split_pdf(pdf_path:str,limit_bytes:int=DEFAULT_LIMIT_BYTES,out_dir:Path|None=None)->list[str]:
  pdf_file=Path(pdf_path)
  if not pdf_file.exists():
    raise FileNotFoundError(f"File not found: {pdf_file}")
  if pdf_file.stat().st_size<limit_bytes:
    print(f"No split needed: {pdf_file.name} ({pdf_file.stat().st_size/1048576:.1f}MB < limit {limit_bytes/1048576:.0f}MB)",flush=True)
    return [str(pdf_file)]
  if out_dir is None:
    out_dir=pdf_file.parent
  out_dir.mkdir(exist_ok=True)
  src=fitz.open(str(pdf_file))
  n=src.page_count
  if n==0:
    src.close()
    raise ValueError(f"Empty PDF: {pdf_file.name}")
  tmp=out_dir/f".tmp_{pdf_file.stem}_split.pdf"
  parts=[]
  try:
    start,index=0,1
    while start<n:
      print(f"  Determining pages of part {index} (remaining pages {start+1}-{n})...",flush=True)
      end=_find_end(src,start,n,limit_bytes,tmp)
      part=out_dir/f"{pdf_file.stem}_part{index}.pdf"
      out=fitz.open()
      out.insert_pdf(src,from_page=start,to_page=end)
      out.save(str(part),garbage=3,deflate=True)
      out.close()
      size=part.stat().st_size
      flag=" (single page over limit, cannot split further)" if size>=limit_bytes else ""
      print(f"Generated: {part.name} (pages {start+1}-{end+1}, {end-start+1} pages, {size/1048576:.1f}MB){flag}",flush=True)
      parts.append(str(part))
      start=end+1
      index+=1
  finally:
    src.close()
    if tmp.exists():
      tmp.unlink()
  return parts
def parse_args(argv:list[str]):
  limit=DEFAULT_LIMIT_BYTES
  files=[]
  i=1
  while i<len(argv):
    a=argv[i]
    if a=="--limit" and i+1<len(argv):
      limit=int(float(argv[i+1])*1024*1024)
      i+=2
    else:
      files.append(a)
      i+=1
  return limit,files
def select_pdfs()->list[Path]:
  root=Tk()
  root.withdraw()
  targets:list[Path]=[]
  seen:set[str]=set()
  while True:
    selected_files=filedialog.askopenfilenames(title="Select PDF files to split (multi-select; reselect for cross-folder, cancel to stop)",filetypes=[("PDF files","*.pdf"),("All Files","*.*")])
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
        message=f"Selected {len(targets)} PDF files.\n\nYes -> continue selecting\nNo -> start splitting (each under 95MB default, --limit overrides)"):
        break
    else:
      break
  return targets
def main():
  limit,files=parse_args(sys.argv)
  if files:
    selected=[Path(a) for a in files]
  else:
    selected=select_pdfs()
  if not selected:
    print("No file selected, exit.",flush=True)
    return
  done=0
  total=0
  for pdf in selected:
    if not pdf.is_file() or pdf.suffix.lower()!=".pdf":
      print(f"Skipped (not PDF or missing): {pdf}",flush=True)
      continue
    print(f"\nProcessing: {pdf.name} ({pdf.stat().st_size/1048576:.1f}MB)",flush=True)
    try:
      parts=split_pdf(str(pdf),limit)
      total+=len(parts)
      done+=1
    except Exception as e:
      print(f"Failed: {pdf.name}  {str(e)}",flush=True)
  print(f"\nAll done: split {done} files, generated {total} parts.",flush=True)
if __name__=="__main__":
  try:
    main()
  finally:
    try:
      sys.stdout.flush()
      input("Press Enter to exit...")
    except(EOFError,KeyboardInterrupt):
      pass
