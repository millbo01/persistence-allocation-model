"""Build the SSRN PDF: the paper with the supplement appended (James, 7 October 2026).

Usage: python scripts/build_pdf.py
Output: papers/pam-model/From cells to councils.pdf (and the intermediate .html beside it)

Markdown is converted with markdown-it-py (CommonMark, with tables). LaTeX ($...$ and $$...$$) is protected from the
Markdown converter and typeset in the browser by KaTeX. Chrome (headless) prints the page to PDF.
Working-status lines (draft notes) are dropped; nothing else in the text is changed.
"""
import html
import os
import re
import subprocess
import sys

from markdown_it import MarkdownIt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPER = os.path.join(ROOT, "papers", "pam-model", "08 Paper draft 3.md")
SUPP = os.path.join(ROOT, "papers", "pam-model", "03 Supplement draft 1.md")
OUT_HTML = os.path.join(ROOT, "papers", "pam-model", "From cells to councils.html")
OUT_PDF = os.path.join(ROOT, "papers", "pam-model", "From cells to councils.pdf")
CHROME = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
          r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"]

AUTHOR = "James Miller"
AFFIL = "Independent researcher"
DATE = "October 2026"
ORCID = "ORCID: 0009-0009-6595-647X"
EMAIL = "contact@n-ought.com"
RECORD = "Record: https://doi.org/10.5281/zenodo.23222615"


def strip_status(md):
    """Drop the title line and italic working-status lines directly under it."""
    lines = md.split("\n")
    out, skipping = [], True
    for i, ln in enumerate(lines):
        if i == 0 and ln.startswith("# "):
            continue
        if skipping and (ln.strip() == "" or (ln.startswith("*") and ln.rstrip().endswith("*")) or ln.strip() == "---"):
            continue
        skipping = False
        out.append(ln)
    return "\n".join(out)


def protect_math(md):
    store = []

    def keep(m):
        store.append(m.group(0))
        return f"MATHPLACEHOLDER{len(store) - 1}X"
    md = re.sub(r"\$\$.+?\$\$", keep, md, flags=re.S)
    md = re.sub(r"(?<![\\$])\$(?!\s)([^$\n]+?)(?<!\s)\$(?!\d)", keep, md)
    return md, store


def restore_math(h, store):
    def back(m):
        return html.escape(store[int(m.group(1))], quote=False)
    return re.sub(r"MATHPLACEHOLDER(\d+)X", back, h)


def link_dois(h):
    """Render every DOI as a clickable https://doi.org/ link (James, 7 October 2026)."""
    def a(doi):
        core = doi.rstrip(".,;)")
        tail = doi[len(core):]
        return f'<a href="https://doi.org/{core}">https://doi.org/{core}</a>{tail}'
    h = re.sub(r"https://doi\.org/(10\.[^\s<\"]+?)(?=[.,;)]?(?:\s|<|$))", lambda m: a(m.group(1)), h)
    h = re.sub(r"(?<![/\w])doi:\s?(10\.[^\s<\"]+?)(?=[.,;)]?(?:\s|<|$))", lambda m: a(m.group(1)), h)
    return h


def to_html(md):
    md, store = protect_math(md)
    h = MarkdownIt("commonmark", {"html": False}).enable("table").render(md)
    return link_dois(restore_math(h, store))


def main():
    paper = open(PAPER, encoding="utf-8").read()
    title = paper.split("\n", 1)[0].lstrip("# ").strip()
    supp = open(SUPP, encoding="utf-8").read()
    supp_body = strip_status(supp)
    body_paper = to_html(strip_status(paper))
    body_supp = to_html(supp_body)
    css = """
    @page { size: A4; margin: 22mm 20mm 22mm 20mm; }
    body { font-family: 'Georgia', 'Times New Roman', serif; font-size: 10.5pt; line-height: 1.45; color: #111; }
    h1 { font-size: 19pt; line-height: 1.25; margin: 0 0 10pt 0; }
    h2 { font-size: 13.5pt; margin: 18pt 0 6pt 0; page-break-after: avoid; }
    h3 { font-size: 11.5pt; margin: 14pt 0 4pt 0; page-break-after: avoid; }
    p { margin: 0 0 7pt 0; text-align: left; }
    ul, ol { margin: 0 0 7pt 0; padding-left: 18pt; }
    li { margin: 0 0 2pt 0; }
    blockquote { margin: 6pt 14pt; padding-left: 10pt; border-left: 2px solid #999; color: #222; }
    table { border-collapse: collapse; width: 100%; margin: 6pt 0 10pt 0; font-size: 8.3pt; line-height: 1.3; page-break-inside: auto; }
    th, td { border: 0.5pt solid #888; padding: 2.5pt 4pt; vertical-align: top; text-align: left; }
    th { background: #eee; }
    tr { page-break-inside: avoid; }
    code { font-family: Consolas, monospace; font-size: 8.8pt; }
    a { color: #1a4f8a; text-decoration: none; word-break: break-all; }
    .titlepage { margin-top: 30mm; }
    .titlepage .meta { font-size: 11.5pt; margin-top: 14pt; line-height: 1.6; }
    .supplement { page-break-before: always; }
    .supplement-title { font-size: 17pt; margin-bottom: 12pt; }
    .katex { font-size: 1.02em; }
    .katex-display { margin: 6pt 0; overflow: hidden; }
    """
    page = f"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
 onload="renderMathInElement(document.body,{{delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'$',right:'$',display:false}}],throwOnError:false}});document.body.setAttribute('data-math','done');"></script>
<style>{css}</style></head><body>
<div class="titlepage"><h1>{html.escape(title)}</h1>
<div class="meta">{AUTHOR}<br>{AFFIL}<br>{EMAIL}<br>{ORCID}<br>{DATE}<br>{link_dois(RECORD)}</div></div>
{body_paper}
<div class="supplement"><h1 class="supplement-title">Supplementary material</h1>
{body_supp}</div>
</body></html>"""
    open(OUT_HTML, "w", encoding="utf-8").write(page)
    chrome = next((c for c in CHROME if os.path.exists(c)), None)
    if not chrome:
        sys.exit("No Chrome or Edge found")
    url = "file:///" + OUT_HTML.replace("\\", "/")
    cmd = [chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
           "--virtual-time-budget=20000", "--run-all-compositor-stages-before-draw",
           f"--print-to-pdf={OUT_PDF}", url]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    print(r.stderr[-500:] if r.returncode else "", end="")
    number_pages(OUT_PDF)
    print("PDF:", OUT_PDF, os.path.getsize(OUT_PDF) if os.path.exists(OUT_PDF) else "missing")


def number_pages(path):
    """Stamp 'n of N' centred in the footer of every page (James, 7 October 2026)."""
    import io
    from pypdf import PdfReader, PdfWriter
    from reportlab.pdfgen import canvas
    reader = PdfReader(path)
    n = len(reader.pages)
    writer = PdfWriter()
    for i, page in enumerate(reader.pages):
        w, hgt = float(page.mediabox.width), float(page.mediabox.height)
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=(w, hgt))
        c.setFont("Times-Roman", 9)
        c.setFillGray(0.3)
        c.drawCentredString(w / 2, 28, f"{i + 1} of {n}")
        c.save()
        buf.seek(0)
        page.merge_page(PdfReader(buf).pages[0])
        writer.add_page(page)
    with open(path, "wb") as f:
        writer.write(f)


if __name__ == "__main__":
    main()
