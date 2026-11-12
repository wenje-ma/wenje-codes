# codes — Desktop Utilities for Markdown & PDF

> A small toolbox of Python 3 utilities for batch-processing Markdown and PDF files, all driven by native `tkinter` file dialogs: pick files from multiple folders, then process them in one go.

Conventions for the corpus itself — math spacing, symbol choice, writing rules — live in [`STYLE.md`](STYLE.md).

## Requirements

- Python 3.8+ with Tkinter (standard on Windows builds);
- Per-script extras, installed as needed:
  ```sh
  pip install PyMuPDF rapidocr-onnxruntime pypdf
  ```
- `pdf_to_svg.py` additionally requires the external command-line tool [`pdf2svg`](https://github.com/dawbarton/pdf2svg) (looked up by default under `C:\rtools45\mingw64\bin\`).

## The scripts

| Script | What it does | Extra dependency |
|--------|--------------|------------------|
| `leftright.py` | Adds `\left` / `\right` to bare brackets, braces and vertical bars inside Markdown math environments | — |
| `math_space_strip.py` | Removes every whitespace character inside math spans, rewriting `\partial u` as `\partial{u}` and `\sqrt g` as `\sqrt{g}` so the formula still compiles; `\ ` becomes `\,`; moves a subscript parked behind a thin space onto an empty base (`^{\beta}_{\,B}` → `^{\beta}{}_{B}`); gives the gap beside `\text{…}` the width of body text (`\,` → `\;`, and a `\,` already carrying a comma is dropped); drops `,\,` after a comma as redundant; shields `<` from a letter that directly follows it (`<x` → `<{}x`, the only angle-bracket form a renderer reads as the start of an HTML tag — `<\alpha` needs no shield); leaves `\quad` and `\!` untouched (the corpus standardises on `\quad`, so `\qquad` must never be reintroduced); leaves fenced code, inline code and TeX comments alone; understands `$…$`, `$$…$$`, `\[…\]`, `\(…\)` and the usual `equation`/`align`/`gather` environments | — |
| `auto_typesetting.py` | Runs `leftright.py` → `math_space_strip.py` over one file or folder in that order, then audits for leftover math whitespace and for a `<` still glued to a letter; a file whose stage raises or fails its self-check is restored from its pre-run bytes | — |
| `cn_punct.py` | Turns every full-width and CJK punctuation mark outside code into its half-width ASCII form, spaced like English text (`，`→`,`, `（`→` (`, `）`→`) `, `《》`→`"`, `…`→`...`, `　`→ a plain space); also halves full-width letters, digits and operators left by OCR; keeps the em dash `—` and the interpunct `·`; downgrades quotes inside YAML front matter to `'` so the block still parses; never adds a space inside a math span | — |
| `md_merge.py` | Merges the selected Markdown files into a single `document.md` | — |
| `pdf_OCR.py` | OCRs scanned PDFs and writes a searchable-text copy `_ocr.pdf` | PyMuPDF, rapidocr-onnxruntime |
| `pdf_split.py` | Splits large PDFs into parts under 95 MB (staying below GitHub's 100 MB limit); override with `--limit` | PyMuPDF |
| `pdf_to_txt.py` | Extracts each PDF page's text into a same-named `.txt` | pypdf |
| `md_to_pdf.exe` | Prebuilt executable that converts Markdown to PDF | — |

## Usage

Run any script with `python <script>.py`. A native file dialog opens:

1. Select one or more files, click **Yes** to add files from another folder (repeat as needed);
2. Click **No** to start processing the accumulated list;
3. **Cancel** exits. Duplicate selections are removed automatically.

Output files are written next to their inputs (e.g. `foo.pdf` → `foo_ocr.pdf`, `foo.txt`, or part files `foo_part1.pdf`,...).

The folder-based scripts (`auto_typesetting.py`, `math_space_strip.py`) also accept a folder — or a single file — as the first argument, which skips the dialog:

```sh
python auto_typesetting.py D:\wenje-ma
python math_space_strip.py D:\wenje-ma --dry-run      # report only, writes nothing
python math_space_strip.py D:\wenje-ma --pairs out.jsonl   # dump rewritten formulas for render checking
python cn_punct.py D:\wenje-ma --dry-run               # count what the punctuation pass would change
```

## Related repositories

More tools, notes and research on the [profile page](https://github.com/wenje-ma).
