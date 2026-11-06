import argparse
import io
import json
import re
import sys
from collections import Counter
from pathlib import Path
from tkinter import Tk,filedialog

# Remove every whitespace character inside math spans, so "$a b$" becomes "$ab$".
#
# A space right after a control word is the *terminator* of that word, so
# "\partial u" must never become "\partialu" (an undefined command that kills the
# formula). The following letter is wrapped in braces instead:
#   "\partial u" -> "\partial{u}"
#   "\sqrt g"    -> "\sqrt{g}"
#   "\mathrm d"  -> "\mathrm{d}"
# Braces around a single token are semantically neutral for a command that takes
# no argument (a transparent group) and exactly right for one that does. The only
# measurable side effect is a lost italic correction on the wrapped letter
# (<=0.04em, about 0.4px at 12px), which is uniform across the whole file.
# Only *letters* are wrapped: after "(" or ">" or "+" the control word already
# ends by itself, so "\big (" just becomes "\big(" without any braces.
#
# "\ " (backslash-space, e.g. "\delta^{\alpha}_{\ \gamma}") becomes "\," so the
# shifted-index look survives without a real space character.
#
# Deliberately kept, never rewritten: "\quad", "\quad" (side-by-side layout),
# "\!" (the overlap in "R[\![t]\!]"), and "\," wherever it still carries meaning:
# before a differential or unit, between two factors, before a condition.
#
# "\," next to \text{...} becomes "\;" instead, so the gap between a formula and
# an annotation has the width of an interword space in the surrounding text
# (0.2778em, against 0.1667em for "\,"). ", \," is dropped outright: the comma
# already ends the list item with its own punctuation space.
#
# Protected regions are never touched: fenced code blocks, inline code, TeX
# comments. Math is recognised in $...$, $$...$$, \[...\], \(...\) and, in .tex
# files, the numbered/display environments listed in TEX_ENVS.
#
# Self-check before writing: no whitespace left, no new control word, and the
# token stream unchanged once braces, "\," and "~" are ignored. A file failing
# the check is reported and left untouched.
SPACE=" \t\u00a0\u3000"
CTRL_SPACE=re.compile(r"(\\+)([ \t])")
CTRL_GLUE=re.compile(r"\\([A-Za-z]+)([ \t]+)([A-Za-z])")
# "\partial{}u" left behind by an earlier pass, or written by hand to end a
# command: normalise to the single canonical "\partial{u}" form.
EMPTY_GLUE=re.compile(r"\\([A-Za-z]+)\{\}([A-Za-z])")
CTRL_TRAIL=re.compile(r"\\([A-Za-z]+)([ \t]+)")
ANGLE_GLUE=re.compile(r"([<>])([ \t]+)([A-Za-z])")
CTRL_WORD=re.compile(r"\\[A-Za-z]+")
TEXT_MODE=re.compile(r"\\(?:text|mbox|textrm|textnormal|intertext|hbox)\s*\{")
FENCE=re.compile(r"([ \t]{0,3})(`{3,}|~{3,})")
TEX_ENVS=("equation","equation*","align","align*","alignat","alignat*","gather",
          "gather*","multline","multline*","eqnarray","eqnarray*","displaymath",
          "math","flalign","flalign*")


# ---------------------------------------------------------------- protected regions
def fenced_ranges(text:str)->"list[tuple[int,int]]":
  """Ranges covered by ``` / ~~~ fenced code blocks, delimiter lines included."""
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
  """Ranges of `code` spans whose backtick runs pair up; positions already masked are skipped."""
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
  """% to end of line, unless escaped by an odd number of backslashes."""
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


# ---------------------------------------------------------------- math spans
def _env_span(text:str,i:int,name:str,mask:bytearray):
  """End offset of \\begin{name} ... \\end{name}, or None (depth counted)."""
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
  """(start, end, open_len, close_len) for every math span, scanning left to right."""
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
  """End offset of the {...} group opening at i (i points at '{'), or None."""
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
  """Inside \\text{...} a space means a real word gap, so it becomes '~' instead."""
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
  """s[i] starts a TeX argument: a {...} group, a control word, or one char."""
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
  """`^{A}_{\\,B}` -> `^{A}{}_{B}`.

  A thin space at the head of the subscript only shifts the glyph inside a
  subscript box that still hangs directly under the superscript, so the two
  indices stay stacked. Attaching the subscript to an empty base after the
  superscript is the construction that really offsets it.
  """
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
  """Give the gap between a formula and \\text{...} the width of body text.

  "\\," is 0.1667em, a third of an interword space; "\\;" is 0.2778em and reads
  as the same gap the Chinese prose around the formula uses. A gap already
  carrying a comma or semicolon is dropped instead -- that punctuation is its
  own separation and stacking both looks loose.
  """
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
  """",\\," -> ",": the comma already supplies the punctuation space."""
  def _drop(m):
    count[0]+=1
    return m.group(1)
  return PUNCT_THIN.sub(_drop,span)


def convert_span(span:str,pairs:Counter,stagger=None,counts=None)->str:
  if stagger is None:
    stagger=[0]
  if counts is None:
    counts={"text_gap":[0],"punct_thin":[0]}
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
  # ">x" / "<x" is what space_gt.py just fixed; keep it fixed without a space.
  span=ANGLE_GLUE.sub(r"\1{}\3",span)
  span=fix_stagger(span,stagger)
  span=retune_text_gaps(span,counts["text_gap"])
  span=drop_redundant_thin(span,counts["punct_thin"])
  return "".join(ch for ch in span if ch not in SPACE)


def canonical(span:str)->str:
  """Form that ignores everything the rewrite may legally add or drop.

  A space right after a control word disappears, and "\\ " becomes "\\,": both
  are already expressed above by dropping "\\," and by trimming one backslash
  when an odd run of them is followed by a space. Line breaks are then folded
  ("\\\\" -> one marker) so that "\\\\ \\widetilde" and "\\\\\\widetilde" -- the
  same thing before and after the rewrite -- compare equal.
  """
  s=span
  for tok in ("\\quad","\\quad","\\;","\\,","\\:","\\!"):
    s=s.replace(tok,"")
  s=re.sub(r"(\\+)[ \t]",lambda m: m.group(1) if len(m.group(1))%2==0 else m.group(1)[:-1],s)
  while "\\\\" in s:
    s=s.replace("\\\\","\x00")
  return "".join(ch for ch in s if ch not in "{}~" and ch not in SPACE)


def check_span(old:str,new:str)->"str|None":
  """Reason string when the rewrite may have broken the formula, else None."""
  left=[ch for ch in new if ch in SPACE]
  if left:
    return f"whitespace left: {left[:3]!r}"
  a=canonical(old)
  b=canonical(new)
  # a mashed command ("\\partialu") is invisible to the token comparison, so
  # control words are compared on the folded form as well
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
    counts={"text_gap":[0],"punct_thin":[0]}
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
    # "$ $" would collapse to "$$" and silently turn the rest of the paragraph
    # into display math; keep the gap as "\," instead.
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
  counts={"text_gap":[0],"punct_thin":[0]}
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
          "skipped_encoding":0,"stagger":0,"text_gap":0,"punct_thin":0,"pairs":Counter()}


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
  pairs=stats["pairs"]
  print(f"distinct control-word/next-letter pairs: {len(pairs)}")
  risky=[(f"\\{k[0]} {k[1]}",v) for k,v in pairs.items()
         if k[0] in ("big","Big","bigg","Bigg","bigl","bigr","Bigl","Bigr","bigg l","left","right")]
  if risky:
    print("  delimiter-like commands seen:", sorted(risky,key=lambda x:-x[1])[:10])


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
