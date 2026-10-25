import re
import sys
from pathlib import Path
from tkinter import Tk,filedialog
BR_PLACEHOLDER="\x00__BR__\x00"
ANGLE_AFTER=re.compile(r"(>|<)(?! )")
def convert(text:str)->"tuple[str,int]":
  text=text.replace("<br>",BR_PLACEHOLDER)
  text,n=ANGLE_AFTER.subn(r"\1 ",text)
  text=text.replace(BR_PLACEHOLDER,"<br>")
  return text,n
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
