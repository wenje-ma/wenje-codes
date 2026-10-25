from pathlib import Path
from tkinter import Tk,filedialog,messagebox
import re
def merge_markdown_files(selected_md_paths:list[str],output_md_path:str|None=None):
  if len(selected_md_paths)==0:
    raise ValueError("No Markdown files provided")
  first_file=Path(selected_md_paths[0])
  if output_md_path is None:
    out_file=first_file.parent/"document.md"
  else:
    out_file=Path(output_md_path)
  source_comment_pat=re.compile(r"\s*<!-- source file: .*? -->\r?\n?")
  with open(out_file,"w",encoding="utf-8") as out_f:
    for md_path_str in selected_md_paths:
      p=Path(md_path_str)
      print(f"Merging: {p.name}")
      if not p.exists():
        print(f"Skipping missing file: {p.name}")
        continue
      try:
        content=p.read_text(encoding="utf-8")
        content=source_comment_pat.sub("",content)
        out_f.write("\n\n")
        out_f.write(content)
      except Exception as e:
        print(f"Read failed, skipped {p.name}: {str(e)}")
  print(f"\nDone, output file: {out_file.resolve()}")
  return str(out_file)
def select_and_merge_md():
  root=Tk()
  root.withdraw()
  targets:list[Path]=[]
  seen:set[str]=set()
  while True:
    selected_files=filedialog.askopenfilenames(title="Select Markdown files to merge (Ctrl multi-select, order is merge order; reselect for cross-folder, cancel to stop)",filetypes=[("Markdown files","*.md"),("All Files","*.*")])
    if selected_files:
      for f in selected_files:
        p=Path(f)
        if p.suffix.lower()!=".md":
          continue
        key=str(p.resolve())
        if key not in seen:
          seen.add(key)
          targets.append(p)
      if not messagebox.askyesno(
        title="Continue selecting",
        message=f"Selected {len(targets)} Markdown files.\n\nYes -> continue selecting from other folders\nNo -> start merging"):
        break
    else:
      break
  if not targets:
    print("No Markdown file selected, exit.")
    return []
  merged_output=merge_markdown_files([str(p) for p in targets])
  return [merged_output]
if __name__=="__main__":
  select_and_merge_md()
