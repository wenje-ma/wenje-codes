import importlib.util
import io
import sys
from contextlib import redirect_stdout
from pathlib import Path
from tkinter import Tk,filedialog
HERE=Path(__file__).resolve().parent
STAGES=("leftright","space_gt","math_space_strip")
EXTS=(".md",".qmd",".tex")
MAX_LINES=40
ENC_SKIP="non-UTF-8"

def load(name:str):
  path=HERE/(name+".py")
  if not path.is_file():
    raise FileNotFoundError(f"missing sibling script: {path}")
  spec=importlib.util.spec_from_file_location(name,path)
  mod=importlib.util.module_from_spec(spec)
  spec.loader.exec_module(mod)
  return mod

def targets_of(path:Path):
  if path.is_file():
    return[path] if path.suffix.lower() in EXTS else[]
  files=[p for p in path.rglob("*") if p.is_file() and p.suffix.lower() in EXTS]
  files.sort(key=lambda p: str(p).lower())
  return files

def show(lines)->None:
  for k,line in enumerate(lines):
    if k>=MAX_LINES:
      print(f"    ... {len(lines)-MAX_LINES} more lines suppressed")
      break
    print(f"    {line}")

def run_stage(mod,files,label,state)->"tuple[int,int,int,int]":
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
  print(f"  {label}: changed {changed}, skipped {skipped}, warnings {warned}, errors {errors}")
  show(lines)
  return changed,skipped,warned,errors

def restore(f:Path,state)->bool:
  try:
    f.write_bytes(state[f]["orig"])
    return True
  except OSError as e:
    print(f"    restore failed: {f} ({e})")
    return False

def settle(files,state)->"tuple[int,int,int,int,int]":
  changed=unchanged=rejected=encoding=errors=0
  for f in files:
    st=state[f]
    if st["error"]:
      restore(f,state)
      errors+=1
      print(f"    error, chain undone: {f}  {st['error']}")
      continue
    if st["reject"]:
      if ENC_SKIP in st["reject"]:
        encoding+=1
        print(f"    not UTF-8, left alone: {f}")
      elif restore(f,state):
        rejected+=1
        print(f"    self-check failed, chain undone: {f}  {st['reject']}")
      else:
        errors+=1
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
  return changed,unchanged,rejected,encoding,errors

def audit(strip_mod,files)->int:
  bad=[]
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
    if any(ch in strip_mod.SPACE for a,b,ol,cl in spans for ch in text[a:b]):
      bad.append(f)
  print(f"  audit: {len(files)} files, {total_spans} math spans, "
        f"{len(bad)} file(s) still hold whitespace inside math, {unreadable} unreadable")
  for f in bad[:MAX_LINES]:
    print(f"    {f}")
  if len(bad)>MAX_LINES:
    print(f"    ... {len(bad)-MAX_LINES} more lines suppressed")
  return len(bad)

def run(path:Path)->int:
  files=targets_of(path)
  if not files:
    print(f"No .md/.qmd/.tex files in: {path}")
    return 0
  print(f"Chain over {len(files)} file(s) in {path}")
  state={}
  order=[]
  for f in files:
    try:
      state[f]={"orig":f.read_bytes(),"reject":"","error":""}
      order.append(f)
    except OSError as e:
      print(f"  unreadable, left alone: {f} ({e})")
  mods=[]
  for i,name in enumerate(STAGES,1):
    print(f"[{i}/{len(STAGES)}] {name}")
    try:
      mod=load(name)
    except Exception as e:
      print(f"  cannot load {name}: {e}")
      return 1
    mods.append(mod)
    run_stage(mod,order,name,state)
  print("[net]")
  changed,unchanged,rejected,encoding,errors=settle(order,state)
  print("[audit]")
  bad=audit(mods[-1],order)
  return 1 if bad or rejected or errors else 0

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