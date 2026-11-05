# Aneta Lisowska — personal website

A buildless, responsive website for GitHub Pages. All six pages are plain HTML and share `style.css`. No npm packages or server are needed in production.

## Editing

Edit the content in `build_site.py`, then run `python build_site.py` to regenerate the six HTML pages. Styles are edited directly in `style.css`.

Preview with `python -m http.server 8000`, then open http://localhost:8000.

## Content sources and limits

Research, experience, education, teaching, projects and supervision descriptions were transcribed or summarized from the supplied `cv_anli_updated.pdf`. The original homepage supplied the biography and social links. The private CV itself is not included or published.

The Students page lists current PhD students and historical student entries supplied by the site owner, with explicit placeholders for 2024–2026. Abdelrahman Elskhawy’s full name was verified against https://arxiv.org/abs/2008.05557. The Collaborators page includes the people explicitly named in the two oncology overview slides supplied by the site owner. No identity was inferred from an unlabeled portrait. Those slides also inform the homepage clinician/patient support overview and the project descriptions. Slide images are not republished.

The timeline is ordered by start date, newest first; overlapping roles and education are retained. The supplied AIME 2027 reference could not be loaded during implementation, so its layout has not been reproduced.

The portrait uses the existing production `profile.jpg`, which is retained in the GitHub repository. Fonts use Google Fonts with local system fallbacks.

The research introduction reflects the site owner's stated focus on explainability, reinforcement learning / sequential decision-making, uncertainty, and their effects on human decisions. The supplied WAI and Amsterdam presentation decks and the previous Google Sites biography were reviewed for context. The two WebP research illustrations are extracted from the WAI deck, slide 8 (active learning) and slide 14 (wearable/mobile interfaces). The decks themselves are not published. Homepage SVGs are conceptual illustrations, not experimental results.

Student supervision locations follow the owner's clarification. Publication links are matched to the supplied CV, publisher records and author lists. The student paper list includes master's/bachelor's project outputs and verified PhD-student papers/preprints. Kieran has recently started and has no paper link. Names for the 2024–2026 student rosters remain placeholders. Conference-year labels are used for AIME 2026 because the institutional record lists the proceedings publication year as 2027.
