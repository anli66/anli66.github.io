from pathlib import Path
from html import escape

ROOT = Path(__file__).parent
NAV = [('index.html','Home'), ('research-journey.html','Research journey'), ('projects.html','Current projects'), ('students.html','Students'), ('collaborators.html','Collaborators'), ('teaching.html','Teaching')]

def write_page(filename, title, eyebrow, intro, body):
    nav = ''.join(f'<a href="{url}"'+(' aria-current="page"' if url == filename else '')+f'>{label}</a>' for url,label in NAV)
    content = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Aneta Lisowska</title><meta name="description" content="{escape(intro, quote=True)}">
<meta name="theme-color" content="#163f38"><link rel="stylesheet" href="style.css"></head>
<body><a class="skip" href="#main">Skip to content</a>
<header><div class="header-inner"><a class="brand" href="index.html">Aneta Lisowska<span>AI &amp; Health</span></a>
<nav aria-label="Main navigation">{nav}</nav></div></header>
<main id="main"><section class="page-heading"><p class="eyebrow">{eyebrow}</p><h1>{title}</h1><p class="intro">{intro}</p></section>{body}</main>
<footer><div><strong>Aneta Lisowska</strong><p>Artificial intelligence for better cancer care.</p></div><div class="footer-links"><a href="https://www.linkedin.com/in/anetajl/">LinkedIn ↗</a><a href="https://scholar.google.com/citations?user=-hXV9EsAAAAJ&amp;hl=en">Google Scholar ↗</a></div></footer>
</body></html>'''
    (ROOT / filename).write_text(content, encoding='utf-8')

def card(label, title, text, extra=''):
    return f'<article class="card"><p class="eyebrow">{label}</p><h2>{title}</h2><p>{text}</p>{extra}</article>'

write_page('index.html', 'AI that makes a difference in cancer care.', 'Aneta Lisowska · Assistant Professor in AI and Health',
    'Connecting artificial intelligence, clinical practice, and the everyday lives of patients.', '''
<section class="home-profile" aria-label="About Aneta"><div class="portrait"><img src="https://anli66.github.io/profile.jpg" alt="Aneta Lisowska" width="420" height="480"><span>Research with people at its heart</span></div>
<div class="profile-copy"><p class="eyebrow">Vrije Universiteit Amsterdam · Cancer Center Amsterdam UMC</p><h2>From data to decisions.<br>From decisions to better care.</h2>
<p>My research investigates how artificial intelligence can improve decision-making in cancer care.</p>
<p>I build and test AI tools with a dual focus: supporting clinicians with treatment planning and shared decision-making, and helping patients with treatment adherence. My goal is to understand how these tools influence choices and to work towards measurable improvements in survival and quality of life.</p>
<a class="button" href="research-journey.html">Explore my research journey <span aria-hidden="true">↗</span></a></div></section>
<section class="section"><div class="section-title"><p class="eyebrow">Research directions</p><h2>Better decisions, together.</h2></div><div class="grid three">'''+
    card('01 · Clinical decisions', 'Learning from medical data', 'Medical imaging, treatment-response biomarkers, and methods that address the challenges of limited or incomplete data.')+
    card('02 · Patient support', 'Personalized digital health', 'Mobile and wearable interventions that support well-being, engagement, and medication adherence.')+
    card('03 · Clinical translation', 'AI people can use', 'Connecting AI research with clinical questions, including explainability and treatment monitoring.')+'''
</div></section><section class="feature-strip"><div><p class="eyebrow">Work in progress</p><h2>Explore the current projects.</h2><p>CAREPATH, CLARITY, and PULSE-ONC connect methods research with questions in oncology and patient support.</p></div><a class="button light" href="projects.html">View projects ↗</a></section>''')

journey = [
('Apr 2024 — present','Academic appointment','Assistant Professor in AI and Health','Vrije Universiteit Amsterdam & Cancer Center Amsterdam UMC · Netherlands','Developing collaborations between VU AI research groups and Amsterdam UMC to translate AI research into clinical practice. Supervising PhD and master’s research, teaching, and leading work on personalized interventions and imaging biomarkers.'),
('Dec 2020 — Jan 2024','Research','Post-doctoral Researcher','Poznan University of Technology · Poland','Within the Horizon 2020 CAPABLE project, developed personalized coaching and decision support to help cancer patients with mental well-being, combining wearable and mobile data, machine learning, and behavioral models.'),
('Oct 2021 — Dec 2022','Research · concurrent appointment','Senior Post-doctoral Researcher','Sano Centre for Computational Medicine · Cracow, Poland','Created a digital health intervention research agenda and led two projects exploring machine learning to improve engagement with mHealth applications. Outputs included mobile and wearable applications, real-life participant studies, and a publicly released dataset.'),
('Dec 2020 — Dec 2022','Education','Master of Business Administration','Edinburgh Business School · United Kingdom','Studies included project management, strategic planning, leadership, entrepreneurship, accounting, and marketing.'),
('Jun 2018 — Nov 2020','Industry research','AI Scientist','Canon Medical Research Europe · Edinburgh, United Kingdom','Proposed and led computer vision projects on incremental deep learning and efficient annotation for medical image segmentation and classification. Contributed to clinical text research, including ICD-9 code prediction and label extraction from radiology reports.'),
('Sep 2014 — Jun 2018','Industry research','Research Engineer','Canon Medical Research Europe / formerly Toshiba Medical Visualisation Systems Europe · United Kingdom','Developed machine learning applications for similar-patient retrieval, stroke-sign detection in non-contrast CT, and fall detection from accelerometer data.'),
('Sep 2014 — Jun 2018','Education','Engineering Doctorate · Machine Learning from Medical Data','Heriot-Watt University · Edinburgh, United Kingdom','Thesis: Learning from limited data: Three case studies in healthcare. EPSRC Centre for Doctoral Training in Applied Photonics.'),
('Jun 2014 — Sep 2014','Industry research','Image Analysis Research Intern','Toshiba Medical Visualisation Systems Europe · Edinburgh, United Kingdom','Brain gyrus segmentation from MRI using Random Forest.'),
('Jun 2013 — Jul 2013','Education','Exchange Student','Wuhan University · China','Studies in business, conversational Chinese, Chinese history, and philosophy.'),
('Sep 2011 — Aug 2013','Research','Research Apprentice','Communication and Eye-Tracking Lab, University of Dundee · United Kingdom','Ran eye-tracking experiments investigating language comprehension.'),
('Sep 2010 — Jun 2014','Education','BSc Honours · Computing and Cognitive Science','University of Dundee · United Kingdom','First Class Honours. Honours project: analysis of retinal vessel tortuosity for VAMPIRE (Vessel Assessment and Measurement Platform for Images of the Retina).')]
months = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
journey.sort(key=lambda entry: (int(entry[0].split()[1]), months[entry[0].split()[0]]), reverse=True)
timeline = '<ol class="timeline">' + ''.join(f'<li><div class="timeline-date">{date}</div><article><p class="eyebrow">{kind}</p><h2>{title}</h2><p class="institution">{place}</p><p>{text}</p></article></li>' for date,kind,title,place,text in journey) + '</ol>'
write_page('research-journey.html','My research journey','Experience & education','From computing and cognitive science to medical imaging, digital health, and AI for cancer care. Appointments and education overlap where they ran concurrently.',timeline+'''
<section class="section"><p class="eyebrow">Beyond the lab</p><h2>Scientific community & engagement</h2><div class="grid two">'''+
card('Service','Research community','Editorial Board, Journal of Biomedical Informatics (2024–2028). Program committees: KR4HC 2023 and AIME 2025. Co-organizer of the AI for Affordable Healthcare workshop at ICLR 2020.')+
card('Outreach','Sharing research','Speaker and mentor at the Perspektywy Women in Tech Summit (2022), and project contributor and student mentor at brainhack-krakow (2022).')+'</div></section>')

write_page('projects.html','Current projects','Research in practice','Personalized support, imaging biomarkers, and explainable models for oncology.', '<div class="project-list">'+
card('EU IHI · Personalized interventions','CAREPATH','Developing reinforcement learning methods to personalize mobile interventions and improve medication adherence.','<p class="role"><strong>My role:</strong> Lead the reinforcement learning component focused on personalized mobile interventions.</p><div class="tags"><span>Reinforcement learning</span><span>Medication adherence</span><span>Mobile health</span></div>')+
card('Cancer Center Amsterdam · Imaging biomarkers','CLARITY','Discovering imaging biomarkers of treatment response in solid tumors, with case studies in colorectal liver metastases and pancreatic cancer.','<p class="role"><strong>My role:</strong> Project lead.</p><div class="tags"><span>Medical imaging</span><span>Treatment response</span><span>Oncology</span></div>')+
card('VU–UT · Treatment monitoring','PULSE-ONC','A collaborative project exploring explainability methods and foundation models for sequential data captured during oncology treatment monitoring.','<div class="tags"><span>Explainable AI</span><span>Foundation models</span><span>Sequential data</span></div>')+'</div>')

write_page('students.html','Students & supervision','Learning through research','Supervising PhD, master’s, and bachelor’s research at the intersection of artificial intelligence and health.', '<section aria-labelledby="phd-students"><div class="section-title"><p class="eyebrow">Current students</p><h2 id="phd-students">PhD researchers</h2></div><div class="grid two">'+
card('Current PhD student','Rutger van der Linden','Reinforcement learning for mobile health (mHealth).')+
card('Current PhD student','Shahab Ud Din','Explainable artificial intelligence (XAI).')+
card('Current PhD student','Yue Su','Gaze language models.')+
card('Current PhD student','Kieran Keesmaat','Reinforcement learning for personalized medication adherence.')+'''
</div></section><section class="section reading" aria-labelledby="student-projects"><p class="eyebrow">Past & current student research</p><h2 id="student-projects">Master’s & bachelor’s students</h2>
<ol class="timeline student-timeline">
<li><div class="timeline-date">2026</div><article><h2>Student projects</h2><p>Student details to be added.</p></article></li>
<li><div class="timeline-date">2025</div><article><h2>Student projects</h2><p>Student details to be added.</p></article></li>
<li><div class="timeline-date">2024</div><article><h2>Student projects</h2><p>Student details to be added.</p></article></li>
<li><div class="timeline-date">2022</div><article><p class="eyebrow">Bachelor’s students</p><h2>Paulina Adamczyk, Maciej Kus,<br>Sylwia Marek &amp; Ryszard Pręcikowski</h2></article></li>
<li><div class="timeline-date">2020</div><article><h2>Abdelrahman Elskhawy</h2><p>Continual learning for medical image segmentation.</p><a class="text-link" href="https://arxiv.org/abs/2008.05557">Continual Class Incremental Learning for CT Thoracic Segmentation ↗</a></article></li>
<li><div class="timeline-date">2019</div><article><h2>Daria Zotova</h2></article></li>
</ol></section><section class="section reading"><p class="eyebrow">Selected research outputs</p><h2>Research connected to supervision</h2>
<ul class="publication-list"><li><strong>Forecasting stress transitions using ecological momentary assessment data and machine learning.</strong><span>Internet Interventions · 2026</span></li><li><strong>Which explainable AI methods in medical imaging are clinically impactful? A systematic literature review addressing the clinician’s perspective.</strong><span>Frontiers in Artificial Intelligence · 2026</span></li><li><strong>Detecting silent failures in rare tumor segmentation: The impact of distributional shift on uncertainty-aware quality assessment.</strong><span>International Conference on Artificial Intelligence in Medicine · 2026</span></li></ul>
<a class="text-link" href="https://scholar.google.com/citations?user=-hXV9EsAAAAJ&amp;hl=en">Find publications on Google Scholar ↗</a></section>''')

write_page('collaborators.html','Collaborators','Across disciplines','Connecting AI researchers and clinical partners around questions that matter for cancer care.', '''
<section class="reading section first"><h2>Bridging AI research and clinical practice</h2><p>At Vrije Universiteit Amsterdam and Cancer Center Amsterdam UMC, I facilitate collaborative projects between AI research groups and clinical researchers.</p><p>These collaborations connect methods in machine learning with treatment planning, response assessment, patient support, and oncology monitoring.</p></section><div class="grid two">'''+
card('Current research environment','Vrije Universiteit Amsterdam','AI research and teaching, including collaborative projects with Amsterdam UMC.')+
card('Clinical research environment','Cancer Center Amsterdam UMC','Collaboration on AI for cancer care and imaging biomarkers of treatment response.')+'''
</div><section class="section"><p class="eyebrow">Collaborative projects</p><h2>Working across research communities</h2><div class="grid two">'''+
card('Current','PULSE-ONC · VU–UT','Collaborative research on explainability and foundation models for sequential oncology monitoring data.')+
card('Previous','CAPABLE','At Poznan University of Technology, contributed to the Horizon 2020 Cancer Patient Better Life Experience project, developing personalized coaching and decision support for patients.')+'</div></section>')

write_page('teaching.html','Teaching','AI & healthcare education','Connecting machine learning methods with the questions and constraints of healthcare research.', '<div class="grid two">'+
card('Master’s · Course coordinator','Machine Learning and Reasoning for Healthcare','Coordinator of this AI master’s course at Vrije Universiteit Amsterdam.')+
card('Postgraduate · Lecturer','Introduction to AI for Medical Researchers','Lecturer in the postgraduate course offered through the Department of Epidemiology.')+'''
</div><section class="feature-strip"><div><p class="eyebrow">Research education</p><h2>Learning through real research questions.</h2><p>I also supervise PhD and master’s students working on AI and health.</p></div><a class="button light" href="students.html">Explore supervision ↗</a></section>''')

print('Generated six pages.')
