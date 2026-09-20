"""Build the user manual without importing the CAD runtime."""

import os
from pathlib import Path
import sys
import tomllib

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))  # The doctest builder exercises this checkout.
metadata = tomllib.loads((ROOT / "pyproject.toml").read_text())["project"]

project = "Machinome Mechanics"
author = "Luis Henrique Cassis Fagundes"
copyright = "2023–2026, Luis Henrique Cassis Fagundes"
release = metadata["version"]
version = release
extensions = ["sphinx.ext.doctest"]
doctest_global_setup = f"import sys; sys.path.insert(0, {str(ROOT / 'docs' / 'examples')!r})"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
nitpicky = True
highlight_language = "python"

html_theme = "sphinx_rtd_theme"
html_title = f"{project} — Mechanics helpers for Machinome"
html_static_path = ["_static"]
html_css_files = ["mechanics.css"]
html_theme_options = {
    "navigation_depth": 2,
    "collapse_navigation": False,
    "style_external_links": True,
}
html_context = {
    "display_github": True,
    "github_user": "machinome",
    "github_repo": "machinome-mechanics",
    "github_version": "main",
    "conf_py_path": "/docs/",
}
html_baseurl = os.environ.get(
    "READTHEDOCS_CANONICAL_URL",
    "https://machinome-mechanics.readthedocs.io/en/latest/",
)
