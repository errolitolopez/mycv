"""Builds the one page CV as a real PDF file with WeasyPrint."""

from flask import render_template
from weasyprint import HTML

# Paper sizes the CV can be made for. "letter" is the short bond paper.
PAPER_SIZES = {"a4": "A4", "letter": "letter"}
DEFAULT_SIZE = "a4"


def paper_size(name):
    """The CSS page size for a size name, or None if the name is unknown."""
    return PAPER_SIZES.get(name)


def build_resume_pdf(cv, size):
    """PDF bytes of the CV for a known size name (a4 or letter)."""
    html = render_template("resume_print.html", cv=cv, page_size=PAPER_SIZES[size])
    return HTML(string=html).write_pdf()
