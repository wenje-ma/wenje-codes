# codes — Desktop Utilities for Markdown & PDF

> A small toolbox of Python 3 utilities for batch-processing Markdown and PDF files, all driven by native `tkinter` file dialogs: pick files from multiple folders, then process them in one go.

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

Output files are written next to their inputs (e.g. `foo.pdf` → `foo_ocr.pdf`, `foo.txt`, or part files `foo_part1.pdf`, …).

## Related repositories

More tools, notes and research on the [profile page](https://github.com/wenje-ma).
