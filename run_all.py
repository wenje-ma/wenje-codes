import importlib.util
import io
import sys
from contextlib import redirect_stdout
from pathlib import Path
from tkinter import Tk,filedialog

# Runs the three Markdown/LaTeX passes in the only order that makes sense:
#
#   1. leftright.py         wrap bare delimiters as \left...\right...
#   2. space_gt.py          insert a space after every '>' / '<' glued to a
#                           following character, so a renderer (WeChat editor and
#                           the like) never reads ">x" as the start of an HTML tag.
#                           It works inside math too, which is where the next
#                           pass has to clean up again.
#   3. math_space_strip.py  delete every whitespace character inside math spans.
#                           The space pass 2 put between ">" and a letter is turned
#                           into "{}" there, so pass 2 keeps doing its job without
#                           leaving a space character inside the formula.
#
# Each pass is a full sweep over the folder; the audit at the end only reports.
# Usage: python run_all.py [folder-or-file]   (a native folder dialog opens when
# no argument is given)
HERE=Path(__file__).resolve().parent
STAGES=("leftright","space_gt","math_space_strip")
EXTS=(".md",".qmd",".tex")
MAX_LINES=40


def load(name:str):
  """Import a sibling script by path, so this works from any working directory."""
  path=HERE/(name+".py")
  if not path.is_file():
    raise FileNotFoundError(f"missing sibling script: {path}")
  spec=importlib.util.spec_from_file_location(name,path)
  mod=importlib.util.module_from_spec(spec)
  spec.loader.exec_module(mod)
  return mod


def targets_of(path:Path):
  if path.is_file():
    return [path] if path.suffix.lower() in EXTS else []
  files=[p for p in path.rglob("*") if p.is_file() and p.suffix.lower() in EXTS]
  files.sort(key=lambda p: str(p).lower())
  return files


def run_stage(mod, files, label:str) -> "tuple[int,int,int]":
  changed=skipped=warned=0
  lines=[]
  for f in files:
    buf=io.StringIO()
    with redirect_stdout(buf):
      mod.process_file(f)
    for line in buf.getvalue().splitlines():
      line=line.strip()
      if not line or line.startswith("No change"):
        continue
      if line.startswith("Converted"):
        changed+=1
      elif line.startswith("Skipped"):
        skipped+=1
      elif line.startswith("Warning"):
        warned+=1
      lines.append(line)
  print(f"  {label}: changed {changed}, skipped {skipped}, warnings {warned}")
  shown=0
  for line in lines:
    if shown>=MAX_LINES:
      print(f"    ... {len(lines)-shown} more lines suppressed")
      break
    print(f"    {line}")
    shown+=1
  return changed,skipped,warned


def audit(strip_mod, files)->None:
  """Report any file that still has whitespace inside a math span."""
  bad=[]
  total_spans=0
  for f in files:
    try:
      text=f.read_bytes().decode("utf-8-sig")
    except UnicodeDecodeError:
      continue
    spans=strip_mod.math_spans(text,f.suffix.lower())
    total_spans+=len(spans)
    if any(ch in strip_mod.SPACE for a,b,ol,cl in spans for ch in text[a:b]):
      bad.append(f)
  print(f"  audit: {len(files)} files, {total_spans} math spans, "
        f"{len(bad)} file(s) still hold whitespace inside math")
  for f in bad[:MAX_LINES]:
    print(f"    {f}")


def run(path:Path)->None:
  files=targets_of(path)
  if not files:
    print(f"No .md/.qmd/.tex files under: {path}")
    return
  print(f"Chain over {len(files)} file(s) under {path}")
  mods=[]
  for i,name in enumerate(STAGES,1):
    print(f"[{i}/{len(STAGES)}] {name}")
    mod=load(name)
    mods.append(mod)
    run_stage(mod, files, name)
  print(f"[audit]")
  audit(mods[-1], files)


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
  run(target)
