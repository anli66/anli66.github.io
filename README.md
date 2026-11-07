# Aneta Lisowska — personal website

A buildless, responsive website for GitHub Pages. All six pages are plain HTML and share `style.css`. No npm packages or server are needed in production.

## Editing

Edit the shared content in `build_site.py` and the research-journey narrative in `research_journey.py`, then run `python build_site.py` to regenerate the six HTML pages. Styles are edited directly in `style.css`.

Preview with `python -m http.server 8000`, then open http://localhost:8000.

## Content sources and limits

Research, experience, education, teaching, projects and supervision descriptions were transcribed or summarized from the supplied `cv_anli_updated.pdf`. The original homepage supplied the biography and social links. The private CV itself is not included or published.

The Students page lists current PhD students and historical student entries supplied by the site owner, with explicit placeholders for 2024–2026. Abdelrahman Elskhawy’s full name was verified against https://arxiv.org/abs/2008.05557. The Collaborators page has been removed at the owner's request; its previous content is preserved in Git history.

The timeline is ordered by start date, newest first; overlapping roles and education are retained. The supplied AIME 2027 reference could not be loaded during implementation, so its layout has not been reproduced.

The portrait is an optimized WebP copy of the existing `profile.jpg`, which is retained in the GitHub repository. Fonts use Newsreader and DM Sans via Google Fonts with local system fallbacks. The editorial design emphasizes the research focus, selected publications, current projects and direct academic contact for collaboration and joint proposals. No funding or outcome guarantees are implied.

The research introduction reflects the site owner's stated focus on explainability, reinforcement learning / sequential decision-making, uncertainty, and their effects on human decisions. The supplied WAI and Amsterdam presentation decks and the previous Google Sites biography were reviewed for context. The two WebP research illustrations are extracted from the WAI deck, slide 8 (active learning) and slide 14 (wearable/mobile interfaces). The decks themselves are not published. Homepage SVGs are conceptual illustrations, not experimental results.

The Academic Bordeaux revision uses #562435, #762F43, #F6F2EC, #302D30 and #C9A7A1. Dusty rose is decorative; body text uses charcoal or a tested darker muted colour. Main text/button contrast combinations range from 5.85:1 to 12.36:1. The portrait is authentic, unchanged apart from optimization and layout cropping.

The overarching question connects explanations, uncertainty and sequential decisions. The 2027–2031 agenda is framed as future research aims, not awarded funding or completed outcomes. Leadership statements distinguish CLARITY project leadership, CAREPATH component leadership and PULSE-ONC collaboration, following the supplied CV. SATO's individual contributions follow its published CRediT statement: https://pmc.ncbi.nlm.nih.gov/articles/PMC9975785/. The first-author RL feasibility study is explicitly described as synthetic-data research: https://ceur-ws.org/Vol-3060/paper-2.pdf. Other flagship papers are identified as co-authored work.

Student supervision locations follow the owner's clarification. Publication links are matched to the supplied CV, publisher records and author lists. The student paper list includes master's/bachelor's project outputs and verified PhD-student papers/preprints. Kieran has recently started and has no paper link. Names for the 2024–2026 student rosters remain placeholders. Conference-year labels are used for AIME 2026 because the institutional record lists the proceedings publication year as 2027.

The Research Journey narrative is adapted from the SpinozaLecture chat and its recorded-narrative speaker notes, at the site owner’s explicit request. Six chapters explain how the scientific questions developed. Appointments, education and service are available on the separate Academic CV page (cv.html). Ongoing CLARITY work is distinguished from hypotheses and proposed explanation / eye-tracking studies; no reader-study recruitment targets or private proposal files are published.

The homepage also draws on the Spinoza lecture: its central question concerns choosing and explaining the next step from uncertain patient evidence. The framework explicitly separates observations, inferred state, action and feedback. Gaze alignment, clinical meaning and model faithfulness remain distinct, and future diagnostic studies remain in the research agenda. The homepage introduces the programme; Research Journey carries the longer narrative.

The site owner clarified the programme’s measurable overarching objective: maximise survival and quality of life. The homepage now puts those objectives first and connects them to estimating patient state, predicting state transitions conditional on actions, and studying policies over the care journey. Engagement, adherence, response and toxicity are intermediate measures, not replacements for the long-term objectives. Current projects are explicitly parts of a research vision, without claiming a validated end-to-end treatment policy or demonstrated survival benefit.

Following the supplied editorial brief, Research Journey is 666 words (excluding the shared page heading/navigation/footer), down from 1,192 words in the previous narrative, a 44.1% reduction. It preserves six stages with one scientific question each, current leadership evidence and the survival/quality-of-life objective. The chapter jump navigation and large illustrations were removed from this page. Appointments, education and community engagement are now on cv.html, with publication and teaching resource links. Source CV files remain private.

The Dundee wording was checked against the original user recording in the SpinozaLecture chat: the lab work investigated language comprehension using eye tracking, including sentence/image mismatches and their effect on gaze. The later clinical explanation studies revisit eye tracking in a new domain; the early work is not described generically as research on interpreting information.
