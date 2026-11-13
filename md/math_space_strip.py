import argparse
import io
import json
import re
import sys
from collections import Counter
from pathlib import Path
from tkinter import Tk,filedialog

SPACE=" \t\u00a0\u3000"
CTRL_SPACE=re.compile(r"(\\+)([ \t])")
CTRL_GLUE=re.compile(r"\\([A-Za-z]+)([ \t]+)([A-Za-z])")
EMPTY_GLUE=re.compile(r"\\([A-Za-z]+)\{\}([A-Za-z])")
CTRL_TRAIL=re.compile(r"\\([A-Za-z]+)([ \t]+)")
ANGLE_GLUE=re.compile(r"(<)([ \t]*)([A-Za-z])")
CTRL_WORD=re.compile(r"\\[A-Za-z]+")
TEXT_MODE=re.compile(r"\\(?:text|mbox|textrm|textnormal|intertext|hbox)\s*\{")
FENCE=re.compile(r"([ \t]{0,3})(`{3,}|~{3,})")
TEX_ENVS=("equation","equation*","align","align*","alignat","alignat*","gather",
          "gather*","multline","multline*","eqnarray","eqnarray*","displaymath",
          "math","flalign","flalign*")

def fenced_ranges(text:str)->"list[tuple[int,int]]":
  ranges=[]
  i,n=0,len(text)
  opened=None
  marker=""
  while i<n:
    eol=text.find("\n",i)
    eol=n if eol<0 else eol+1
    m=FENCE.match(text,i)
    if opened is None:
      if m:
        opened=i
        marker=m.group(2)
    elif m and m.group(2)[0]==marker[0] and len(m.group(2))>=len(marker):
      ranges.append((opened,eol))
      opened=None
      marker=""
    i=eol
  if opened is not None:
    ranges.append((opened,n))
  return ranges

def inline_code_ranges(text:str,mask:bytearray)->"list[tuple[int,int]]":
  ranges=[]
  i,n=0,len(text)
  while i<n:
    if text[i]!="`" or mask[i]:
      i+=1
      continue
    k=1
    while i+k<n and text[i+k]=="`":
      k+=1
    j=i+k
    closed=False
    while j<n:
      if text[j]!="`" or mask[j]:
        j+=1
        continue
      run=1
      while j+run<n and text[j+run]=="`":
        run+=1
      if run==k:
        ranges.append((i,j+run))
        i=j+run
        closed=True
        break
      j+=run
    if not closed:
      i+=k
  return ranges

def tex_comment_ranges(text:str)->"list[tuple[int,int]]":
  ranges=[]
  i,n=0,len(text)
  while i<n:
    c=text[i]
    if c=="\\":
      i+=2
      continue
    if c=="%":
      eol=text.find("\n",i)
      ranges.append((i,n if eol<0 else eol))
      i=n if eol<0 else eol
      continue
    i+=1
  return ranges

def skip_mask(text:str,suffix:str)->bytearray:
  mask=bytearray(len(text))
  ranges=fenced_ranges(text)
  if suffix==".tex":
    ranges+=tex_comment_ranges(text)
  for a,b in ranges:
    mask[a:b]=b"\x01"*(b-a)
  for a,b in inline_code_ranges(text,mask):
    mask[a:b]=b"\x01"*(b-a)
  return mask

def _env_span(text:str,i:int,name:str,mask:bytearray):
  begin="\\begin{"+name+"}"
  end="\\end{"+name+"}"
  depth=1
  j=i+len(begin)
  n=len(text)
  while j<n:
    if not mask[j] and text.startswith(begin,j):
      depth+=1
      j+=len(begin)
      continue
    if not mask[j] and text.startswith(end,j):
      depth-=1
      j+=len(end)
      if depth==0:
        return j
      continue
    j+=1
  return None

def math_spans(text:str,suffix:str=".md")->"list[tuple[int,int,int,int]]":
  mask=skip_mask(text,suffix)
  spans=[]
  i,n=0,len(text)
  while i<n:
    if mask[i]:
      i+=1
      continue
    c=text[i]
    if c=="\\":
      if text.startswith("\\[",i):
        j=text.find("\\]",i+2)
        if j>=0:
          spans.append((i,j+2,2,2))
          i=j+2
          continue
        i+=2
        continue
      if text.startswith("\\(",i):
        j=text.find("\\)",i+2)
        if j>=0:
          spans.append((i,j+2,2,2))
          i=j+2
          continue
        i+=2
        continue
      is_begin=False
      for name in TEX_ENVS:
        if text.startswith("\\begin{"+name+"}",i):
          is_begin=True
          j=_env_span(text,i,name,mask)
          if j is not None:
            spans.append((i,j,len("\\begin{"+name+"}"),len("\\end{"+name+"}")))
            i=j
          else:
            i+=1
          break
      if is_begin:
        continue
      i+=2
      continue
    if c=="$":
      if i+1<n and text[i+1]=="$":
        j=text.find("$$",i+2)
        if j<0:
          break
        spans.append((i,j+2,2,2))
        i=j+2
      else:
        j=text.find("$",i+1)
        if j<0:
          break
        spans.append((i,j+1,1,1))
        i=j+1
      continue
    i+=1
  return spans

def _brace_group_end(text:str,i:int):
  depth=0
  n=len(text)
  while i<n:
    c=text[i]
    if c=="\\":
      i+=2
      continue
    if c=="{":
      depth+=1
    elif c=="}":
      depth-=1
      if depth==0:
        return i+1
    i+=1
  return None

def protect_text_mode(span:str)->str:
  parts=[]
  pos=0
  for m in TEXT_MODE.finditer(span):
    if m.start()<pos:
      continue
    end=_brace_group_end(span,m.end()-1)
    if end is None:
      continue
    parts.append(span[pos:m.end()])
    inner=span[m.end():end-1]
    parts.append("".join("~" if ch in SPACE else ch for ch in inner))
    parts.append("}")
    pos=end
  parts.append(span[pos:])
  return "".join(parts)

STAGGER_LEAD=re.compile(r"(?:\\[,;:>]|\\quad|\\quad|\\ |~|\s)+")

TEXT_GAP_LEFT_PUNCT=re.compile(
  r"([,;])\\,(?=\\(?:text|mbox|textrm|textnormal|intertext|hbox)\s*\{)")
TEXT_GAP_LEFT=re.compile(
  r"\\,(?=\\(?:text|mbox|textrm|textnormal|intertext|hbox)\s*\{)")
PUNCT_THIN=re.compile(r"([,;])(?:\\,)+")

def _atom_end(s:str,i:int)->int:
  if i>=len(s):
    return -1
  if s[i]=="{":
    depth=0
    while i<len(s):
      c=s[i]
      if c=="\\":
        i+=2
        continue
      if c=="{":
        depth+=1
      elif c=="}":
        depth-=1
        if depth==0:
          return i+1
      i+=1
    return -1
  if s[i]=="\\":
    j=i+1
    while j<len(s) and s[j].isalpha():
      j+=1
    return j if j>i+1 else min(i+2,len(s))
  return i+1

def fix_stagger(span:str,count:list)->str:
  out=[]
  i,n=0,len(span)
  while i<n:
    c=span[i]
    if c=="\\" and i+1<n:
      out.append(span[i:i+2])
      i+=2
      continue
    if c=="^":
      e=_atom_end(span,i+1)
      if e>0 and e+1<n and span[e]=="_" and span[e+1]=="{":
        f=_atom_end(span,e+1)
        if f>0:
          body=span[e+2:f-1]
          m=STAGGER_LEAD.match(body)
          if m and m.end()<len(body) and _atom_end(body,m.end())>0:
            count[0]+=1
            out.append(span[i:e])
            out.append("{}")
            out.append("_{"+body[m.end():]+"}")
            i=f
            continue
      out.append("^")
      i+=1
      continue
    out.append(c)
    i+=1
  return "".join(out)

def retune_text_gaps(span:str,count:list)->str:
  def _punct(m):
    count[0]+=1
    return m.group(1)
  span=TEXT_GAP_LEFT_PUNCT.sub(_punct,span)
  def _wide(m):
    count[0]+=1
    return "\\;"
  span=TEXT_GAP_LEFT.sub(_wide,span)
  out=[]
  pos=0
  for m in TEXT_MODE.finditer(span):
    if m.start()<pos:
      continue
    end=_brace_group_end(span,m.end()-1)
    if end is None:
      continue
    out.append(span[pos:end])
    pos=end
    if span[end:end+2]=="\\,":
      out.append("\\;")
      pos=end+2
      count[0]+=1
  out.append(span[pos:])
  return "".join(out)

def drop_redundant_thin(span:str,count:list)->str:
  def _drop(m):
    count[0]+=1
    return m.group(1)
  return PUNCT_THIN.sub(_drop,span)

def convert_span(span:str,pairs:Counter,stagger=None,counts=None)->str:
  if stagger is None:
    stagger=[0]
  if counts is None:
    counts={"text_gap":[0],"punct_thin":[0],"angle":[0]}
  span=protect_text_mode(span)
  prev=None
  while prev!=span:
    prev=span
    def _glue(m,pairs=pairs):
      pairs[(m.group(1),m.group(3))]+=1
      return "\\"+m.group(1)+"{"+m.group(3)+"}"
    span=CTRL_GLUE.sub(_glue,span)
  span=CTRL_TRAIL.sub(r"\\\1",span)
  def _empty(m,pairs=pairs):
    pairs[(m.group(1),m.group(2))]+=1
    return "\\"+m.group(1)+"{"+m.group(2)+"}"
  span=EMPTY_GLUE.sub(_empty,span)
  span=CTRL_SPACE.sub(lambda m: m.group(1)+("," if len(m.group(1))%2 else ""),span)
  def _angle(m,counts=counts):
    counts["angle"][0]+=1
    return "<{}"+m.group(3)
  span=ANGLE_GLUE.sub(_angle,span)
  span=fix_stagger(span,stagger)
  span=retune_text_gaps(span,counts["text_gap"])
  span=drop_redundant_thin(span,counts["punct_thin"])
  return "".join(ch for ch in span if ch not in SPACE)

def canonical(span:str)->str:
  s=span
  for tok in("\\quad","\\quad","\\;","\\,","\\:","\\!"):
    s=s.replace(tok,"")
  s=re.sub(r"(\\+)[ \t]",lambda m: m.group(1) if len(m.group(1))%2==0 else m.group(1)[:-1],s)
  while "\\\\" in s:
    s=s.replace("\\\\","\x00")
  return "".join(ch for ch in s if ch not in "{}~" and ch not in SPACE)

WORD_GAP=re.compile(r"[A-Za-z] [A-Za-z]")
CTRL_WORD=re.compile(r"\\[A-Za-z]+[ \t]*")

def span_hazard(span:str)->"str|None":
  """Reject a span that is really prose: a raw backtick means the code-span mask
  drifted, and two Latin words separated by one space means the span runs across
  body text. Both cases would otherwise let the whitespace pass compress prose.
  A space after a control word ("\\mathcal F") is normal LaTeX and is masked out
  before the word test."""
  bare=protect_text_mode(span)
  if "`" in bare:
    return f"backtick inside a math span: {bare[:60]!r}"
  m=WORD_GAP.search(CTRL_WORD.sub("\x00",bare))
  if m is not None:
    return f"prose spaced like text inside a math span: {bare[max(0,m.start()-12):m.end()+12]!r}"
  return None

def check_span(old:str,new:str)->"str|None":
  hazard=span_hazard(old)
  if hazard is not None:
    return hazard
  left=[ch for ch in new if ch in SPACE]
  if left:
    return f"whitespace left: {left[:3]!r}"
  a=canonical(old)
  b=canonical(new)
  new_words=set(re.findall(r"\\([A-Za-z]+)",b))-set(re.findall(r"\\([A-Za-z]+)",a))
  if new_words:
    return f"new control words: {sorted(new_words)[:4]}"
  if a!=b:
    k=0
    while k<min(len(a),len(b)) and a[k]==b[k]:
      k+=1
    return f"token stream changed near ...{a[max(0,k-12):k+12]!r} -> ...{b[max(0,k-12):k+12]!r}"
  return None

def convert(text:str,suffix:str=".md",stagger=None,counts=None)->"tuple[str,int,int,list,Counter,list]":
  if stagger is None:
    stagger=[0]
  if counts is None:
    counts={"text_gap":[0],"punct_thin":[0],"angle":[0]}
  out=[]
  pos=0
  n_space=0
  n_shift=0
  warnings=[]
  pairs=Counter()
  body_pairs=[]
  for a,b,ol,cl in math_spans(text,suffix):
    span=text[a:b]
    new=convert_span(span,pairs,stagger,counts)
    n_space+=sum(1 for ch in span if ch in SPACE)
    n_shift+=len(CTRL_SPACE.findall(span))
    body=span[ol:len(span)-cl]
    if body and body.strip(SPACE)=="":
      new=span[:ol]+"\\,"+span[len(span)-cl:]
    reason=check_span(span,new)
    if reason is not None:
      warnings.append(f"{reason} in {span[:70]!r}")
    else:
      body_pairs.append((body,new[ol:len(new)-cl]))
    out.append(text[pos:a])
    out.append(new)
    pos=b
  out.append(text[pos:])
  return "".join(out),n_space,n_shift,warnings,pairs,body_pairs

def process_file(path:Path,stats=None,dry_run=False,pairs_file=None)->None:
  raw=path.read_bytes()
  bom=raw.startswith(b"\xef\xbb\xbf")
  data=raw[3:] if bom else raw
  try:
    text=data.decode("utf-8")
  except UnicodeDecodeError:
    print(f"Skipped (non-UTF-8): {path}")
    if stats is not None:
      stats["skipped_encoding"]+=1
    return
  st=[0]
  counts={"text_gap":[0],"punct_thin":[0],"angle":[0]}
  new,n_space,n_shift,warnings,pairs,body_pairs=convert(text,path.suffix.lower(),st,counts)
  for w in warnings:
    print(f"Warning: {path.name}: {w}")
  if stats is not None:
    stats["files"]+=1
    stats["pairs"].update(pairs)
    stats["warnings"]+=len(warnings)
    stats["stagger"]+=st[0]
    stats["text_gap"]+=counts["text_gap"][0]
    stats["punct_thin"]+=counts["punct_thin"][0]
    stats["angle"]+=counts["angle"][0]
    if pairs_file is not None:
      for old_body,new_body in body_pairs:
        if old_body!=new_body:
          pairs_file.write(json.dumps({"f":str(path),"o":old_body,"n":new_body},ensure_ascii=False)+"\n")
  if new==text:
    print(f"No change: {path}")
    return
  if warnings:
    print(f"Skipped (self-check failed, file left untouched): {path}")
    if stats is not None:
      stats["rejected"]+=1
    return
  if stats is not None:
    stats["changed"]+=1
    stats["space"]+=n_space
    stats["shift"]+=n_shift
  if not dry_run:
    path.write_bytes((("\ufeff" if bom else "")+new).encode("utf-8"))
    print(f"Converted: {path}  (-space x{n_space}, \\  ->\\, x{n_shift})")
  else:
    print(f"Would convert: {path}  (-space x{n_space}, \\  ->\\, x{n_shift})")

def new_stats()->dict:
  return {"files":0,"changed":0,"space":0,"shift":0,"warnings":0,"rejected":0,
          "skipped_encoding":0,"stagger":0,"text_gap":0,"punct_thin":0,"angle":0,
          "pairs":Counter()}

def report(stats:dict)->None:
  print("---- summary ----")
  print(f"files read {stats['files']}, changed {stats['changed']}, "
        f"self-check rejected {stats['rejected']}, non-UTF-8 {stats['skipped_encoding']}")
  print(f"whitespace characters removed {stats['space']}, \\  ->\\, {stats['shift']}")
  if stats["stagger"]:
    print(f"stacked indices moved onto an empty base (^{{A}}_{{\\,B}} -> ^{{A}}{{}}_{{B}}): {stats['stagger']}")
  if stats["text_gap"]:
    print(f"gap next to \\text{{}} retuned to \\; (or dropped after a comma): {stats['text_gap']}")
  if stats["punct_thin"]:
    print(f"redundant \\, dropped after a comma/semicolon: {stats['punct_thin']}")
  if stats["angle"]:
    print(f"'<' shielded from a following letter (<{{}}x): {stats['angle']}")
  pairs=stats["pairs"]
  print(f"distinct control-word/next-letter pairs: {len(pairs)}")
  risky=[(f"\\{k[0]} {k[1]}",v) for k,v in pairs.items()
        if k[0] in("big","Big","bigg","Bigg","bigl","bigr","Bigl","Bigr","bigg l","left","right")]
  if risky:
    print("  delimiter-like commands seen:",sorted(risky,key=lambda x:-x[1])[:10])

def process_folder(folder:str,dry_run=False,pairs_path=None)->None:
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
  print(f"Found {len(targets)} target files, stripping math spaces...")
  stats=new_stats()
  pf=open(pairs_path,"w",encoding="utf-8") if pairs_path else None
  try:
    for md_path in targets:
      process_file(md_path,stats,dry_run,pf)
  finally:
    if pf is not None:
      pf.close()
  report(stats)
  print(f"Done, processed {len(targets)} files.")

def select_folder_and_convert(**kw)->None:
  root=Tk()
  root.withdraw()
  folder=filedialog.askdirectory(title="Select folder (recursively processes .md/.qmd/.tex)")
  if not folder:
    print("No folder selected, exit.")
    return
  process_folder(folder,**kw)

if __name__=="__main__":
  ap=argparse.ArgumentParser(description="Strip whitespace inside math spans.")
  ap.add_argument("path",nargs="?",help="file or folder; omit to open a folder dialog")
  ap.add_argument("--dry-run",action="store_true",help="report what would change, write nothing")
  ap.add_argument("--pairs",help="dump rewritten math bodies as JSONL for render checking")
  a=ap.parse_args()
  if a.path:
    target=Path(a.path)
    if target.is_dir():
      process_folder(str(target),a.dry_run,a.pairs)
    elif target.is_file():
      stats=new_stats()
      pf=open(a.pairs,"w",encoding="utf-8") if a.pairs else None
      try:
        process_file(target,stats,a.dry_run,pf)
      finally:
        if pf is not None:
          pf.close()
      report(stats)
    else:
      print(f"Path is not a file or folder: {target}")
  else:
    select_folder_and_convert(dry_run=a.dry_run,pairs_path=a.pairs)