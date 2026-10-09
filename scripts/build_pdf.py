"""Build the paper PDF: the paper with the supplement appended (James, 7 October 2026; figures from 8 October).

Usage: python scripts/build_pdf.py          (SSRN: paper with the supplement appended, From cells to councils.pdf)
       python scripts/build_pdf.py ijgs     (IJGS: "- IJGS submission.pdf" and "- IJGS supplement.pdf")
The intermediate .html is written beside each PDF.

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
PAPER = os.path.join(ROOT, "papers", "pam-model", "From cells to councils.md")
SUPP = os.path.join(ROOT, "papers", "pam-model", "From cells to councils - supplement.md")
OUT_HTML = os.path.join(ROOT, "papers", "pam-model", "From cells to councils.html")
OUT_PDF = os.path.join(ROOT, "papers", "pam-model", "From cells to councils.pdf")
IJGS = os.path.join(ROOT, "papers", "pam-model", "From cells to councils - IJGS submission.md")
OUT_IJGS_HTML = os.path.join(ROOT, "papers", "pam-model", "From cells to councils - IJGS submission.html")
OUT_IJGS_PDF = os.path.join(ROOT, "papers", "pam-model", "From cells to councils - IJGS submission.pdf")
OUT_SUPP_HTML = os.path.join(ROOT, "papers", "pam-model", "From cells to councils - IJGS supplement.html")
OUT_SUPP_PDF = os.path.join(ROOT, "papers", "pam-model", "From cells to councils - IJGS supplement.pdf")
CHROME = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
          r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"]

AUTHOR = "James Miller"
AFFIL = "Independent researcher"
DATE = "Version 2, October 2026"
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


# Printed width of each figure as a share of the text width (tall figures narrower, to limit blank page ends).
FIG_WIDTH = {"fig2_law": "80%", "fig3_silence_and_break": "78%", "fig4_rate_decides_harm": "90%",
             "fig5_pt1_order_of_loss": "88%"}


def figures(h):
    """Wrap each image and the 'Figure n.' caption paragraph after it in one figure, kept on one page."""
    def wrap(m):
        img, cap = m.group(1), m.group(2)
        name = re.search(r'src="figures/([^".]+)\.', img)
        w = FIG_WIDTH.get(name.group(1) if name else "", "100%")
        img = img.replace("<img ", f'<img style="width:{w}" ', 1)
        return f"<figure>{img}<figcaption>{cap}</figcaption></figure>"
    return re.sub(r"<p>(<img [^>]*>)</p>\s*<p>(<strong>Figure S?\d+\..*?)</p>", wrap, h, flags=re.S)


def to_html(md):
    md, store = protect_math(md)
    h = MarkdownIt("commonmark", {"html": False}).enable("table").render(md)
    return link_dois(restore_math(figures(h), store))


def main(variant="ssrn"):
    """ssrn: the paper with the supplement appended, one PDF.
    ijgs: the IJGS manuscript and the supplement as two PDFs (supplemental online material)."""
    paper = open(IJGS if variant == "ijgs" else PAPER, encoding="utf-8").read()
    title = paper.split("\n", 1)[0].lstrip("# ").strip()
    supp = open(SUPP, encoding="utf-8").read()
    body_paper = to_html(strip_status(paper))
    body_supp = to_html(strip_status(supp))
    meta = f'<div class="meta">{AUTHOR}<br>{AFFIL}<br>{EMAIL}<br>{ORCID}<br>{DATE}<br>{link_dois(RECORD)}</div>'
    if variant == "ijgs":
        render(title, f'<div class="titlepage"><h1>{html.escape(title)}</h1>\n{meta}</div>\n{body_paper}',
               OUT_IJGS_HTML, OUT_IJGS_PDF)
        render("Supplementary material", '<div class="titlepage"><h1>Supplementary material</h1>\n'
               f'<p class="subtitle">for &ldquo;{html.escape(title)}&rdquo;</p>\n{meta}</div>\n{body_supp}',
               OUT_SUPP_HTML, OUT_SUPP_PDF)
    else:
        render(title, f'<div class="titlepage"><h1>{html.escape(title)}</h1>\n{meta}</div>\n{body_paper}\n'
               f'<div class="supplement"><h1 class="supplement-title">Supplementary material</h1>\n{body_supp}</div>',
               OUT_HTML, OUT_PDF)


def render(title, body, out_html, out_pdf):
    css = """
    @page { size: A4; margin: 22mm 20mm 22mm 20mm; }
    body { font-family: 'Georgia', 'Times New Roman', serif; font-size: 10.5pt; line-height: 1.45; color: #111; }
    h1 { font-size: 19pt; line-height: 1.25; margin: 0 0 10pt 0; }
    h2 { font-size: 13.5pt; margin: 18pt 0 6pt 0; page-break-after: avoid; }
    h3 { font-size: 11.5pt; margin: 14pt 0 4pt 0; page-break-after: avoid; }
    p { margin: 0 0 7pt 0; text-align: left; }
    ul, ol { margin: 0 0 7pt 0; padding-left: 18pt; }
    li { margin: 0 0 2pt 0; page-break-inside: avoid; break-inside: avoid; }
    blockquote { margin: 6pt 14pt; padding-left: 10pt; border-left: 2px solid #999; color: #222; }
    table { border-collapse: collapse; width: 100%; margin: 6pt 0 10pt 0; font-size: 8.3pt; line-height: 1.3; page-break-inside: auto; }
    th, td { border: 0.5pt solid #888; padding: 2.5pt 4pt; vertical-align: top; text-align: left; }
    th { background: #eee; }
    tr { page-break-inside: avoid; }
    code { font-family: Consolas, monospace; font-size: 8.8pt; overflow-wrap: anywhere; word-break: break-word; }
    a { color: #1a4f8a; text-decoration: none; word-break: break-all; }
    .titlepage { margin-top: 30mm; }
    .titlepage .meta { font-size: 11.5pt; margin-top: 14pt; line-height: 1.6; }
    .supplement { page-break-before: always; }
    .supplement-title { font-size: 17pt; margin-bottom: 12pt; }
    .titlepage .subtitle { font-size: 13pt; font-style: italic; margin: 0 0 6pt 0; }
    figure { margin: 10pt 0 12pt 0; page-break-inside: avoid; break-inside: avoid; }
    figure img { display: block; width: 100%; height: auto; margin: 0 auto 6pt auto; }
    img { max-width: 100%; height: auto; }
    p:has(+ table), p:has(+ figure), p:has(+ ul), p:has(+ ol) { page-break-after: avoid; break-after: avoid; }
    figcaption { font-size: 8.8pt; line-height: 1.38; color: #222; }
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
{body}
</body></html>"""
    open(out_html, "w", encoding="utf-8").write(page)
    chrome = next((c for c in CHROME if os.path.exists(c)), None)
    if not chrome:
        sys.exit("No Chrome or Edge found")
    url = "file:///" + out_html.replace("\\", "/")
    cmd = [chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
           "--virtual-time-budget=20000", "--run-all-compositor-stages-before-draw",
           f"--print-to-pdf={out_pdf}", url]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    print(r.stderr[-500:] if r.returncode else "", end="")
    number_pages(out_pdf)
    print("PDF:", out_pdf, os.path.getsize(out_pdf) if os.path.exists(out_pdf) else "missing")


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
    main(sys.argv[1] if len(sys.argv) > 1 else "ssrn")
