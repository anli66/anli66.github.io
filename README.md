# Aneta Lisowska — personal website

A buildless, responsive website for GitHub Pages. All six pages are plain HTML and share `style.css`. No npm packages or server are needed in production.

## Editing

Edit the content in `build_site.py`, then run `python build_site.py` to regenerate the six HTML pages. Styles are edited directly in `style.css`.

Preview with `python -m http.server 8000`, then open http://localhost:8000.

## Content sources and limits

Research, experience, education, teaching, projects and supervision descriptions were transcribed or summarized from the supplied `cv_anli_updated.pdf`. The original homepage supplied the biography and social links. The private CV itself is not included or published.

The Students page lists current PhD students and historical student entries supplied by the site owner, with explicit placeholders for 2024–2026. Abdelrahman Elskhawy’s full name was verified against https://arxiv.org/abs/2008.05557. The Collaborators page describes documented institutional and project partnerships; individual collaborators can be added when confirmed.

The timeline is ordered by start date, newest first; overlapping roles and education are retained. The supplied AIME 2027 reference could not be loaded during implementation, so its layout has not been reproduced.

The portrait uses the existing production `profile.jpg`, which is retained in the GitHub repository. Fonts use Google Fonts with local system fallbacks.
