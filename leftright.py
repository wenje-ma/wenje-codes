import re
from pathlib import Path
from tkinter import Tk,filedialog,messagebox
MD_LINK=r"!?\[[^\]]*\]\([^)]*\)"
DELIM=r"(?:\(|\)|\[|\]|\\\{|\\\}|\\langle|\\rangle|\||\.)"
WRAPPED=MD_LINK+r"|\\left\s*"+DELIM+r"|\\right\s*"+DELIM+r"|\\[bB]ig(?:g|l|r)?\s*"+DELIM
BARE=r"(?<!\\)(\(|\)|\[|\])|(\\\{|\\\})|(\\langle|\\rangle)"
PAT=re.compile(WRAPPED+"|"+BARE)
BAR=re.compile(r"(?<!\\)((?:\\\\)*\\?)\|")
WRAPPED_PRE=re.compile(r"(?:\\left|\\right|\\[bB]ig(?:g|l|r)?)\s*$")
def math_spans(text:str):
  spans=[]
  i,n=0,len(text)
  while i<n:
    c=text[i]
    if c=="\\":
      i+=2
      continue
    if c=="$":
      if i+1<n and text[i+1]=="$":
        j=text.find("$$",i+2)
        if j<0:
          break
        spans.append((i,j+2))
        i=j+2
      else:
        j=text.find("$",i+1)
        if j<0:
          break
        spans.append((i,j+1))
        i=j+1
    else:
      i+=1
  return spans
def convert_span(span:str)->str:
  bars=[m for m in BAR.finditer(span) if not WRAPPED_PRE.search(m.string,0,m.start())]
  if len(bars)%2:
    print(f"Warning: odd | count in math span (skipped): {span[:60]!r}")
  else:
    for k in range(len(bars)-1,-1,-1):
      m=bars[k]
      tok=m.group(1)+"|"
      lr="\\left" if k%2==0 else "\\right"
      span=span[:m.start()]+lr+tok+span[m.end():]
  def repl(m):
    s=m.group(0)
    if s in("(", "["):
      return "\\left"+s
    if s in(")", "]"):
      return "\\right"+s
    if s=="\\{":
      return "\\left\\{"
    if s=="\\}":
      return "\\right\\}"
    if s=="\\langle":
      return "\\left\\langle"
    if s=="\\rangle":
      return "\\right\\rangle"
    return s
  return PAT.sub(repl,span)
def convert(text:str)->str:
  out=[]
  pos=0
  for a,b in math_spans(text):
    out.append(text[pos:a])
    out.append(convert_span(text[a:b]))
    pos=b
  out.append(text[pos:])
  return "".join(out)
def process_file(path:Path):
  raw=path.read_bytes()
  bom=raw.startswith(b"\xef\xbb\xbf")
  data=raw[3:] if bom else raw
  try:
    text=data.decode("utf-8")
  except UnicodeDecodeError:
    print(f"Skipped (non-UTF-8): {path}")
    return
  new=convert(text)
  if new==text:
    print(f"No change: {path}")
    return
  path.write_bytes((("\ufeff" if bom else "")+new).encode("utf-8"))
  n1=new.count("\\left(")-text.count("\\left(")
  n2=new.count("\\left[")-text.count("\\left[")
  n3=new.count("\\left\\{")-text.count("\\left\\{")
  n4=new.count("\\left|")-text.count("\\left|")
  n5=new.count("\\left\\|")-text.count("\\left\\|")
  n6=new.count("\\left\\langle")-text.count("\\left\\langle")
  n7=new.count("\\right\\rangle")-text.count("\\right\\rangle")
  print(f"Converted: {path}  (+\\left( x{n1}, +\\left[ x{n2}, +\\left\\{{ x{n3}, +\\left| x{n4}, +\\left\\| x{n5}, +\\left\\langle x{n6}, +\\right\\rangle x{n7})")
def select_folder_and_convert_mds():
  root=Tk()
  root.withdraw()
  folder=filedialog.askdirectory(title="Select folder (recursively processes .md/.qmd/.tex)")
  if not folder:
    print("No folder selected, exit.")
    return []
  folder_path=Path(folder)
  exts=(".md",".qmd",".tex")
  targets=[p for p in folder_path.rglob("*") if p.is_file() and p.suffix.lower() in exts]
  targets.sort(key=lambda p: str(p).lower())
  if not targets:
    print(f"No .md/.qmd/.tex files in folder: {folder_path}")
    return []
  print(f"Found {len(targets)} target files, converting...")
  for md_path in targets:
    process_file(md_path)
  print(f"Done, processed {len(targets)} files.")
if __name__=="__main__":
  select_folder_and_convert_mds()
