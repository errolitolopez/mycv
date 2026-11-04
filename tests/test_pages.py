"""The home page and the printable resume page are served."""

from app import create_app


def test_index_and_resume():
    client = create_app().test_client()
    page = client.get("/")
    assert page.status_code == 200
    assert b"MyCV" in page.data
    assert client.get("/static/js/index.js").status_code == 200
    assert client.get("/static/js/theme.js").status_code == 200
    resume = client.get("/resume")
    assert resume.status_code == 200
    assert b'data-size="a4"' in resume.data
    assert b'data-size="letter"' in resume.data
    assert client.get("/static/js/resume.js").status_code == 200


def test_resume_pdf_sizes():
    client = create_app().test_client()
    for size in ("a4", "letter"):
        response = client.get(f"/resume-{size}.pdf")
        assert response.status_code == 200
        assert response.mimetype == "application/pdf"
        assert response.data.startswith(b"%PDF")
    assert client.get("/resume-legal.pdf").status_code == 404
