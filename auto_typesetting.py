"""Run the math-rewrite chain over one file or folder.

Chain: leftright.py (bare brackets -> \\left/\\right) then math_space_strip.py
(strip whitespace inside math, shield "<" from a following letter). Both stages
are idempotent; a file whose stage raises is restored from its pre-run bytes, and
a file flagged by either stage's self-check is rolled back to its pre-chain state.
Only "<" glued to a letter is a renderer hazard (a bare "<" before a command such
as "\\alpha" is not a tag opener and needs no shield), so no standalone
angle-bracket pass exists any more.
"""
import importlib.util
import io
import re
import sys
from contextlib import redirect_stdout
from pathlib import Path
from tkinter import Tk,filedialog
HERE=Path(__file__).resolve().parent
STAGES=("leftright","math_space_strip")
EXTS=(".md",".qmd",".tex")
MAX_LINES=40
ENC_SKIP="non-UTF-8"
ANGLE_LETTER=re.compile(r"<[A-Za-z]")

def load(name:str):
  """Load a sibling script as a module."""
  path=HERE/(name+".py")
  if not path.is_file():
    raise FileNotFoundError(f"missing sibling script: {path}")
  spec=importlib.util.spec_from_file_location(name,path)
  if spec is None or spec.loader is None:
    raise ImportError(f"cannot build a module spec for: {path}")
  mod=importlib.util.module_from_spec(spec)
  spec.loader.exec_module(mod)
  return mod

def targets_of(path:Path)->"list[Path]":
  if path.is_file():
    return[path] if path.suffix.lower() in EXTS else[]
  files=[p for p in path.rglob("*") if p.is_file() and p.suffix.lower() in EXTS]
  files.sort(key=lambda p: str(p).lower())
  return files

def show(lines:"list[str]")->None:
  for k,line in enumerate(lines):
    if k>=MAX_LINES:
      print(f"    ... {len(lines)-MAX_LINES} more lines suppressed")
      break
    print(f"    {line}")

def run_stage(mod,stage:str,files:"list[Path]",state)->"tuple[int,int,int,int]":
  changed=skipped=warned=errors=0
  lines=[]
  for f in files:
    buf=io.StringIO()
    try:
      with redirect_stdout(buf):
        mod.process_file(f)
      out=buf.getvalue()
    except Exception as e:
      state[f]["error"]=f"{type(e).__name__}: {e}"
      errors+=1
      lines.append(f"Error: {f}  {state[f]['error']}")
      continue
    for line in out.splitlines():
      line=line.strip()
      if not line or line.startswith("No change") or line.startswith("Would convert"):
        continue
      if line.startswith("Converted"):
        changed+=1
      elif line.startswith("Skipped"):
        skipped+=1
        if not state[f]["reject"]:
          state[f]["reject"]=line
      elif line.startswith("Warning"):
        warned+=1
      lines.append(line)
  print(f"  {stage}: changed {changed}, skipped {skipped}, warnings {warned}, errors {errors}")
  show(lines)
  return changed,skipped,warned,errors

def restore(f:Path,state)->bool:
  try:
    f.write_bytes(state[f]["orig"])
    return True
  except OSError as e:
    print(f"    restore failed: {f} ({e})")
    return False

def settle(files,state)->"tuple[int,int,int,int,int,list]":
  changed=unchanged=rejected=encoding=errors=0
  left=[]   # files the chain gave up on; their residue is not an invariant break
  for f in files:
    st=state[f]
    if st["error"]:
      restore(f,state)
      errors+=1
      left.append(f)
      print(f"    error, chain undone: {f}  {st['error']}")
      continue
    if st["reject"]:
      if ENC_SKIP in st["reject"]:
        encoding+=1
        left.append(f)
        print(f"    not UTF-8, left alone: {f}")
      elif restore(f,state):
        rejected+=1
        left.append(f)
        print(f"    self-check failed, chain undone: {f}  {st['reject']}")
      else:
        errors+=1
        left.append(f)
      continue
    try:
      now=f.read_bytes()
    except OSError as e:
      errors+=1
      print(f"    unreadable after the run: {f} ({e})")
      continue
    if now==st["orig"]:
      unchanged+=1
    else:
      changed+=1
  print(f"  net: changed {changed}, unchanged {unchanged}, restored {rejected}, "
        f"non-UTF-8 {encoding}, errors {errors}")
  return changed,unchanged,rejected,encoding,errors,left

def audit(strip_mod,files)->"tuple[int,int]":
  """Check the chain's own invariants on the files it wrote: no whitespace and
  no "<" glued to a letter left inside a math span."""
  space_files=[]
  angle_files=[]
  total_spans=0
  unreadable=0
  for f in files:
    try:
      text=f.read_bytes().decode("utf-8-sig")
    except UnicodeDecodeError:
      unreadable+=1
      continue
    spans=strip_mod.math_spans(text,f.suffix.lower())
    total_spans+=len(spans)
    if any(ch in strip_mod.SPACE for a,b,_,_ in spans for ch in text[a:b]):
      space_files.append(f)
    for a,b,ol,cl in spans:
      body=text[a+ol:b-cl]
      if ANGLE_LETTER.search(body):
        angle_files.append(f)
        break
  print(f"  audit: {len(files)} files, {total_spans} math spans, "
        f"{len(space_files)} with whitespace left in math, "
        f"{len(angle_files)} with '<'+letter left in math, {unreadable} unreadable")
  for f in space_files[:MAX_LINES]:
    print(f"    whitespace: {f}")
  for f in angle_files[:MAX_LINES]:
    print(f"    angle: {f}")
  return len(space_files),len(angle_files)

def run(path:Path)->int:
  files=targets_of(path)
  if not files:
    print(f"No .md/.qmd/.tex files in: {path}")
    return 0
  print(f"Chain {' -> '.join(STAGES)} over {len(files)} file(s) in {path}")
  mods={}
  for name in STAGES:
    try:
      mods[name]=load(name)
    except Exception as e:
      print(f"cannot load {name}: {e}")
      return 1
  state={}
  order=[]
  for f in files:
    try:
      state[f]={"orig":f.read_bytes(),"reject":"","error":""}
      order.append(f)
    except OSError as e:
      print(f"  unreadable, left alone: {f} ({e})")
  for i,name in enumerate(STAGES,1):
    print(f"[{i}/{len(STAGES)}] {name}")
    run_stage(mods[name],name,order,state)
  print("[net]")
  changed,unchanged,rejected,encoding,errors,left=settle(order,state)
  print("[audit]")
  clean=[f for f in order if f not in left]
  if left:
    print(f"  {len(left)} file(s) left as they were, not audited")
  bad_space,bad_angle=audit(mods["math_space_strip"],clean)
  return 1 if bad_space or bad_angle or errors else 0

def select_path()->"Path|None":
  root=Tk()
  root.withdraw()
  folder=filedialog.askdirectory(title="Select folder (recursively processes .md/.qmd/.tex)")
  return Path(folder) if folder else None

if __name__=="__main__":
  if len(sys.argv)>1:
    target=Path(sys.argv[1])
  else:
    target=select_path()
    if target is None:
      print("No folder selected, exit.")
      sys.exit(0)
  if not target.exists():
    print(f"Path does not exist: {target}")
    sys.exit(1)
  sys.exit(run(target))
