"""Builds the plain-files version of MyCV in site/ so GitHub Pages can host it.

Run: python tools/build_static.py [/prefix]
The prefix is the path the site lives under, "/mycv" for https://<user>.github.io/mycv/ (default).
Pass "" when the site is served from a domain root.
"""

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from app import create_app  # noqa: E402  (after the path line above)

# url path -> file written under site/
PAGES = {
    "/": "index.html",
    "/resume": "resume/index.html",
    "/resume-a4.pdf": "resume-a4.pdf",
    "/resume-letter.pdf": "resume-letter.pdf",
}


def build(prefix):
    site = ROOT / "site"
    if site.exists():
        shutil.rmtree(site)
    site.mkdir()

    client = create_app().test_client()
    for url, filename in PAGES.items():
        # A base_url with the prefix makes url_for() write links that start with the prefix.
        response = client.get(url, base_url=f"http://localhost{prefix}")
        assert response.status_code == 200, f"{url} gave {response.status_code}"
        target = site / filename
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(response.data)

    shutil.copytree(ROOT / "static", site / "static")
    (site / ".nojekyll").touch()  # serve every file as it is


if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "/mycv")
    print("Built site/")
