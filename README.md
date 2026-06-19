# camsoper.github.io

Personal résumé and portfolio site. Content is authored in Markdown; a custom
Jekyll theme renders it to HTML, and the résumé is also rendered to PDF.

## How it works

| File | Purpose |
|---|---|
| `index.md` | Home page (`layout: default`) |
| `resume.md` | Résumé — **pure Markdown**, styled by CSS (`layout: resume`). This is the source for the PDF. |
| `portfolio.md` | Portfolio (`layout: default`) |
| `_layouts/`, `_includes/` | Custom theme (replaces the old `jekyll-theme-slate`) |
| `assets/css/style.css` | Site styles (screen) |
| `assets/css/print.css` | PDF overrides (loaded only by WeasyPrint) |
| `assets/css/print-ats.css` | Plain black-on-white variant for maximum ATS compatibility |
| `tools/build_pdf.py` | Renders `_site/resume/index.html` → PDF with real, selectable text |
| `.github/workflows/pages-and-pdf.yml` | Builds site + PDF and deploys to GitHub Pages on every push |

The header (name, tagline, contact links) lives in `_config.yml` under `author`
and `contacts`, so it stays in sync between the web page and the PDF.

## Edit the résumé

Edit `resume.md` in plain Markdown. Section headings (`## Work Experience`),
job titles (`### Senior Content Developer`), and the
`**Company · Location** — *dates*` line are all styled by `assets/css/style.css`
— don't add HTML. On push, GitHub Actions rebuilds the site and regenerates
`dist/cam_soper_resume.pdf` (styled) and `dist/cam_soper_resume_ats.pdf` (plain).

## Run locally

```bash
bundle install
bundle exec jekyll serve          # http://localhost:4000

# build the PDF locally
pip install weasyprint
bundle exec jekyll build
python tools/build_pdf.py         # -> dist/*.pdf
```
