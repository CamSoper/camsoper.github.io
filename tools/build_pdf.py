#!/usr/bin/env python3
"""
build_pdf.py — render the already-built résumé page to PDF with WeasyPrint.

Runs AFTER `jekyll build`, so it reads the real HTML from _site/ and produces
a PDF that looks like the website but with real, selectable, ATS-parseable
text. Output:

    dist/cam_soper_resume.pdf       styled (dark name band)

Usage:
    pip install weasyprint
    python tools/build_pdf.py
"""

import os
from weasyprint import HTML, CSS

SITE = "_site"
RESUME_HTML = os.path.join(SITE, "resume", "index.html")  # permalink: pretty
OUT_DIR = "dist"

os.makedirs(OUT_DIR, exist_ok=True)

base = HTML(filename=RESUME_HTML, base_url=SITE)

# Styled PDF — matches the website
base.write_pdf(
    os.path.join(OUT_DIR, "cam_soper_resume.pdf"),
    stylesheets=[CSS(filename="assets/css/print.css")],
)
print("wrote dist/cam_soper_resume.pdf")
