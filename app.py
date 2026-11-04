"""MyCV: my CV / resume web app.

Run: flask --app app run --debug
"""

from flask import Flask, Response, abort, render_template

from cv_data import CV
from resume_pdf import build_resume_pdf, paper_size


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def index():
        return render_template("index.html", cv=CV)

    @app.get("/resume")
    def resume():
        return render_template("resume.html", cv=CV)

    # The size is in the path (resume-a4.pdf), not a query, so a static host can serve it as a plain file.
    @app.get("/resume-<size>.pdf")
    def resume_pdf(size):
        if paper_size(size) is None:
            abort(404)
        pdf = build_resume_pdf(CV, size)
        # inline: the browser shows it first and the person can save it from there.
        return Response(pdf, mimetype="application/pdf", headers={
            "Content-Disposition": f'inline; filename="errolito-lopez-cv-{size}.pdf"'})

    return app


app = create_app()
