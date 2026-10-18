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
    print(f"警告: 数学片段内 | 数量为奇数（无法可靠配对，整段跳过）: {span[:60]!r}")
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
    print(f"跳过（非 UTF-8）: {path}")
    return
  new=convert(text)
  if new==text:
    print(f"无需修改: {path}")
    return
  path.write_bytes((("\ufeff" if bom else "")+new).encode("utf-8"))
  n1=new.count("\\left(")-text.count("\\left(")
  n2=new.count("\\left[")-text.count("\\left[")
  n3=new.count("\\left\\{")-text.count("\\left\\{")
  n4=new.count("\\left|")-text.count("\\left|")
  n5=new.count("\\left\\|")-text.count("\\left\\|")
  n6=new.count("\\left\\langle")-text.count("\\left\\langle")
  n7=new.count("\\right\\rangle")-text.count("\\right\\rangle")
  print(f"已转换: {path}  (+\\left( ×{n1}, +\\left[ ×{n2}, +\\left\\{{ ×{n3}, +\\left| ×{n4}, +\\left\\| ×{n5}, +\\left\\langle ×{n6}, +\\right\\rangle ×{n7})")
def select_folder_and_convert_mds():
  root=Tk()
  root.withdraw()
  folder=filedialog.askdirectory(title="请选择要处理的文件夹（将递归处理其中所有 .md/.qmd/.tex 文件）")
  if not folder:
    print("未选择文件夹，退出。")
    return []
  folder_path=Path(folder)
  exts=(".md",".qmd",".tex")
  targets=[p for p in folder_path.rglob("*") if p.is_file() and p.suffix.lower() in exts]
  targets.sort(key=lambda p: str(p).lower())
  if not targets:
    print(f"所选文件夹中没有 .md/.qmd/.tex 文件: {folder_path}")
    return []
  print(f"共找到 {len(targets)} 个目标文件，开始转换…")
  for md_path in targets:
    process_file(md_path)
  print(f"转换完成，共处理 {len(targets)} 个文件。")
if __name__=="__main__":
  select_folder_and_convert_mds()
