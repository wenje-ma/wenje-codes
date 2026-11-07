import re
import sys
from pathlib import Path
from tkinter import Tk,filedialog

ANGLE_AFTER=re.compile(r"(>|<)(?![ \t\r\n\f\v]|$)")
WHITESPACE=" \t\r\n\f\v"

HTML_TAGS=frozenset("""
a abbr address area article aside audio b base bdi bdo big blockquote body br button
canvas caption center cite code col colgroup data dd del details dfn dialog div dl dt
em embed fieldset figcaption figure font footer form h1 h2 h3 h4 h5 h6 head header hr
html i iframe img input ins kbd label legend li link main map mark menu meta meter nav
noscript object ol optgroup option output p param picture pre progress q rp rt ruby s
samp section select slot small source span strong style sub summary sup table tbody td
template textarea tfoot th thead time title tr track tt u ul var video wbr
circle defs ellipse g line marker path polygon polyline rect tspan
math mrow mi mo mn ms mtext mspace mfrac msqrt mroot mtable mtr mtd msub msup
msubsup munder mover munderover semantics annotation
""".split())

FRONT_MATTER_OPEN=re.compile(r"---[ \t]*\r?\n")
FRONT_MATTER_CLOSE=re.compile(r"\r?\n(?:---|\.\.\.)[ \t\r]*(?=\r?\n|$)")
TAG_OPEN=re.compile(r"<(/?)([A-Za-z][A-Za-z0-9._:-]*)(?=[ \t\r\n/>])")
ATTR_NAME=re.compile(r"[A-Za-z_:][-A-Za-z0-9._:]*")
ATTR_UNQUOTED=re.compile(r"[^ \t\r\n<>`\"'=]+")
AUTOLINK=re.compile(r"<[A-Za-z][A-Za-z0-9+.\-]*:[^<>\s]*>")
EMAIL_LINK=re.compile(r"<[^<>\s@]+@[^<>\s@]+>")
BLANK_LINE=re.compile(r"\n[ \t\r]*\n")

def _line_prefix_blank(text:str,i:int)->bool:
  j=i
  while j>0 and text[j-1] in " \t":
    j-=1
  return j==0 or text[j-1]=="\n"

def _fence_end(text:str,i:int)->"int|None":
  c=text[i]
  j=i
  while j<len(text) and text[j]==c: j+=1
  run=j-i
  if run<3:
    return None
  eol=text.find("\n",j)
  if eol<0:
    return None
  info=text[j:eol].rstrip("\r")
  if c in info:
    return None
  closer=re.compile(r"^[ \t]*"+re.escape(c)+"{"+str(run)+r",}[ \t\r]*(?=\r?\n|$)",re.M)
  m=closer.search(text,eol+1)
  return None if m is None else m.end()

def _code_span_end(text:str,i:int)->"int|None":
  j=i
  while j<len(text) and text[j]=="`": j+=1
  run=j-i
  closer=re.compile(r"`{"+str(run)+r"}(?!`)")
  m=closer.search(text,j)
  if m is None:
    return None
  if BLANK_LINE.search(text,j,m.start()):
    return None
  return m.end()

def _tag_end(text:str,i:int)->"int|None":
  if text.startswith("<!--",i):
    k=text.find("-->",i+4)
    return None if k<0 else k+3
  m=TAG_OPEN.match(text,i)
  if m is None:
    return None
  closing=m.group(1)=="/"
  known=m.group(2).lower() in HTML_TAGS
  j=m.end()
  has_attr=False
  n=len(text)
  while j<n:
    c=text[j]
    if c==">":
      return j+1 if(known or closing or has_attr) else None
    if c=="/" and text.startswith("/>",j):
      return j+2 if(known or closing or has_attr) else None
    if c in WHITESPACE:
      j+=1
      continue
    am=ATTR_NAME.match(text,j)
    if am is None:
      return None
    j=am.end()
    has_attr=True
    if j<n and text[j]=="=":
      j+=1
      if j<n and text[j] in "\"'":
        q=text[j]
        k=text.find(q,j+1)
        if k<0:
          return None
        j=k+1
      else:
        vm=ATTR_UNQUOTED.match(text,j)
        if vm is None:
          return None
        j=vm.end()
  return None

def _angle_end(text:str,i:int)->"int|None":
  for pat in(AUTOLINK,EMAIL_LINK):
    m=pat.match(text,i)
    if m is not None:
      return m.end()
  return _tag_end(text,i)

def _front_matter_end(text:str)->int:
  m=FRONT_MATTER_OPEN.match(text)
  if m is None:
    return 0
  k=FRONT_MATTER_CLOSE.search(text,m.end()-1)
  return 0 if k is None else k.end()

def protected_spans(text:str)->"list":
  spans=[]
  start=_front_matter_end(text)
  if start:
    spans.append((0,start))
  n=len(text)
  i=start
  while i<n:
    c=text[i]
    if c=="`" or c=="~":
      if _line_prefix_blank(text,i):
        e=_fence_end(text,i)
        if e is not None:
          spans.append((i,e))
          i=e
          continue
      if c=="`":
        e=_code_span_end(text,i)
        if e is not None:
          spans.append((i,e))
          i=e
          continue
    elif c=="<":
      e=_angle_end(text,i)
      if e is not None:
        spans.append((i,e))
        i=e
        continue
    i+=1
  return spans

def convert(text:str)->"tuple[str,int]":
  spans=protected_spans(text)
  parts=[]
  total=0
  pos=0
  for start,end in spans:
    seg=text[pos:start]
    seg,k=ANGLE_AFTER.subn(r"\1 ",seg)
    total+=k
    parts.append(seg)
    parts.append(text[start:end])
    pos=end
  seg=text[pos:]
  seg,k=ANGLE_AFTER.subn(r"\1 ",seg)
  total+=k
  parts.append(seg)
  return "".join(parts),total

def process_file(path:Path)->None:
  raw=path.read_bytes()
  bom=raw.startswith(b"\xef\xbb\xbf")
  data=raw[3:] if bom else raw
  try:
    text=data.decode("utf-8")
  except UnicodeDecodeError:
    print(f"Skipped (non-UTF-8): {path}")
    return
  new,n=convert(text)
  if new==text:
    print(f"No change: {path}")
    return
  path.write_bytes((("\ufeff" if bom else "")+new).encode("utf-8"))
  print(f"Converted: {path}  (+space x{n})")

def process_folder(folder:str)->None:
  folder_path=Path(folder)
  if not folder_path.is_dir():
    print(f"Path is not a valid folder: {folder_path}")
    return
  exts=(".md",".qmd",".tex")
  targets=[p for p in folder_path.rglob("*") if p.is_file() and p.suffix.lower() in exts]
  targets.sort(key=lambda p: str(p).lower())
  if not targets:
    print(f"No .md/.qmd/.tex files in folder: {folder_path}")
    return
  print(f"Found {len(targets)} target files, converting...")
  for md_path in targets:
    process_file(md_path)
  print(f"Done, processed {len(targets)} files.")

def select_folder_and_convert()->None:
  root=Tk()
  root.withdraw()
  folder=filedialog.askdirectory(title="Select folder (recursively processes .md/.qmd/.tex)")
  if not folder:
    print("No folder selected, exit.")
    return
  process_folder(folder)

if __name__=="__main__":
  if len(sys.argv)>1:
    process_folder(sys.argv[1])
  else:
    select_folder_and_convert()