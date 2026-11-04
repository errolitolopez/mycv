# MyCV

My CV as a small website: a modern one-page portfolio and a one page CV that downloads as a real PDF
(A4 or short bond / Letter).

**Live site:** https://errolitolopez.github.io/mycv/

## Stack

Flask + vanilla JavaScript + Bootstrap. The PDFs are made with [WeasyPrint](https://weasyprint.org).
GitHub Pages hosts a static copy built from the Flask app.

## Where things are

| File | Job |
|------|-----|
| `cv_data.py` | All the CV content (summary, skills, experience, education). Edit this to change the site |
| `app.py` | Flask routes: home, `/resume`, `/resume-a4.pdf`, `/resume-letter.pdf` |
| `resume_pdf.py` | Builds the PDF from `templates/resume_print.html` |
| `static/img/profile.webp` | Portrait with the background removed |
| `tools/build_static.py` | Writes the plain-files site into `site/` for GitHub Pages |

## Run

```
python3 -m venv .venv && .venv/bin/pip install -r requirements-dev.txt
.venv/bin/flask --app app run --debug
.venv/bin/pytest -q
```

WeasyPrint needs Pango (`libpango-1.0-0` on Ubuntu/Debian).

## Deploy

Every push to `main` runs `.github/workflows/pages.yml`, which builds the static site
(`python tools/build_static.py /mycv`) and publishes it to GitHub Pages.
