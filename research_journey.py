"""Concise six-stage research narrative."""

STAGES = [
('interpretation','2010–2014','University of Dundee','Studying language comprehension',
['At the University of Dundee, I studied Computing and Cognitive Science and used eye tracking to investigate language comprehension in a psychology lab. I examined how mismatches between a sentence and an accompanying image affected gaze. My bachelor’s project then introduced me to medical imaging: comparing automated retinal-vessel measurements with expert assessments, leading to my first publication in 2014.'],
'How do language and visual context shape where people look?',
[('https://scholar.google.com/citations?user=-hXV9EsAAAAJ&amp;hl=en','Research publications')]),
('clinical-learning','2014–2020','Toshiba / Canon Medical Research Europe','Learning from clinical expertise',
['During my industrial Engineering Doctorate with Heriot-Watt and subsequent research at Canon, I developed methods for learning from limited medical data. Clinical knowledge shaped how we built and evaluated models.',
'I went on to lead active- and continual-learning projects and supervise master’s researchers. This work connected efficient annotation and model adaptation with the practical constraints of clinical research, contributing to publications and patents.'],
'How can AI learn efficiently while making effective use of clinical expertise?',
[('https://research.vu.nl/en/publications/comparison-of-active-learning-strategies-applied-to-lung-nodule-s/','Active learning · 2019'),('https://arxiv.org/abs/2008.05557','Continual learning · 2020')]),
('personalised-support','2020–2024','Poznań University of Technology & Sano','Supporting decisions over time',
['I shifted towards personalised digital health, developing coaching and decision support for cancer patients in CAPABLE. Reinforcement learning brought a new focus: choosing support in response to a person’s changing context.',
'At Sano, I developed a digital-health research agenda and led projects on mobile-health engagement. This sharpened an important distinction: engagement, adherence, and health outcomes measure different things. Their relationship needs testing.'],
'Are we optimising what is easy to record, or the outcome we value?',
[('https://doi.org/10.1016/j.jbi.2022.104276','SATO intervention-design workflow'),('https://ceur-ws.org/Vol-3060/paper-2.pdf','RL for timely prompts · Feasibility study')]),
('bridge-role','Since 2024','Vrije Universiteit Amsterdam & Amsterdam UMC','Connecting AI and clinical needs',
['My current position bridges VU Computer Science and Cancer Center Amsterdam. I develop joint research questions, build projects, and supervise work across disciplines. Patient-facing reinforcement learning remains central, while clinical collaborations have brought me back to imaging.',
'The overarching goal is to maximise survival and quality of life. I frame AI across the patient journey as a sequential-decision problem: estimate patient state, predict transitions given actions, and evaluate longer-term consequences. A collaboration on pancreatic cancer connected this vision to survival and quality-of-life trajectories despite incomplete follow-up.'],
'What could AI change along the patient journey, and how would we know it helped?',
[('projects.html#carepath','CAREPATH · RL component lead')]),
('uncertain-state','Current research','CLARITY','Learning from uncertain evidence',
['Clinical discussions made one challenge especially clear: patient state is inferred from evidence that can vary between measurements and readers. This led to CLARITY, for which I led the application and now lead joint work across AI, radiology, radiotherapy, and surgery.',
'We investigate whether tumour volume and boundary uncertainty over time provide information about treatment response. Associations with reader variability, pathological response, and outcomes are being tested. Uncertainty is a candidate source of information; its value as a biomarker remains a research hypothesis.'],
'Could variability in an assessment itself carry clinically meaningful information?',
[('projects.html#clarity','CLARITY · Project and research question')]),
('return-to-gaze','Future direction','Proposed studies','Returning to human interpretation',
['My proposed studies return to eye tracking in a new setting: AI-assisted clinical decisions. I want to investigate how radiologists interpret AI advice, recognise errors, and decide when evidence is uncertain.',
'Agreement with gaze, clinical meaning, and faithfulness to model behaviour are distinct properties. The aim is to test their relationship to diagnostic decisions, reading time, and burden. These studies are proposed and depend on funding and study setup.'],
'When AI is wrong, what helps a clinician notice?',
[('research.html#agenda','Future research agenda')]),
]

def render_stage(index,stage):
    anchor,date,place,title,paragraphs,question,links=stage
    body=''.join(f'<p>{paragraph}</p>' for paragraph in paragraphs)
    evidence=' '.join(f'<a href="{url}">{label} ↗</a>' for url,label in links)
    return f'<li id="{anchor}"><div class="chapter-margin"><span class="chapter-number">{index:02}</span><p>{date}</p></div><article><p class="eyebrow">{place}</p><h2>{title}</h2>{body}<p class="journey-question">{question}</p><div class="journey-evidence">{evidence}</div></article></li>'

STORY='''<section class="journey-opening concise-opening"><p>My research began with language comprehension and eye tracking, then moved into medical imaging, learning from clinical expertise, and personalised decisions over time. These experiences now inform my work on AI across the patient journey, with survival and quality of life as the long-term objectives.</p></section><ol class="narrative-journey concise-journey">'''
STORY+=''.join(render_stage(index,stage) for index,stage in enumerate(STAGES,1))
STORY+='''</ol><section class="journey-contact"><p class="eyebrow">Looking ahead</p><h2>Human expertise.<br><em>Decisions that matter to patients.</em></h2><p>The journey brings eye tracking into a new context: understanding how clinicians use AI advice. I welcome collaborations connecting AI methods, clinical expertise, and patient-centred research.</p><div class="hero-actions"><a class="button" href="mailto:a.j.lisowska@vu.nl?subject=Research%20collaboration">Discuss a research question ↗</a><a class="text-link" href="cv.html">Academic CV ↗</a></div></section>'''
