#!/usr/bin/env python3
# Generator voor personaltrainerindelft.nl - eigen content, structuur en huisstijl.
import os, json, html, hashlib

def _ver(relpath):
    try: return hashlib.md5(open(os.path.join(os.path.dirname(__file__),relpath),'rb').read()).hexdigest()[:8]
    except Exception: return "1"

BASE = "https://personaltrainerindelft.nl"
SITE = "Personal Trainer in Delft"
EMAIL = "info@personaltrainerindelft.nl"
PHONE = "06 21264241"; TEL = "+31621264241"
OUT = os.path.join(os.path.dirname(__file__), "site")
SRC = os.path.dirname(__file__)
CSS_VER = _ver("assets/css/style.css")
VID_VER = _ver("assets/video/sfeer-delft.mp4")
POS_VER = _ver("assets/img/sfeer-delft-poster.jpg")

def esc(s): return html.escape(str(s), quote=True)

IC = {
 "check":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
 "arrow":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
 "phone":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
 "mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
 "pin":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 "users":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
 "target":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
 "leaf":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10z"/><path d="M2 21c0-3 1.85-5.36 5.08-6"/></svg>',
 "home":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9.5 12 3l9 6.5"/><path d="M5 10v10h14V10"/></svg>',
 "clock":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><polyline points="12 7 12 12 15 14"/></svg>',
 "euro":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 21a8 8 0 1 1 0-16"/><path d="M4 9h11"/><path d="M4 13h9"/></svg>',
 "heart":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.29 1.51 4.04 3 5.5l7 7Z"/></svg>',
 "shield":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
 "play":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>',
 "tower":'<svg viewBox="0 0 24 24" fill="currentColor"><polygon points="8,9 16,9 12,3"/><rect x="8.5" y="9" width="7" height="12"/></svg>',
 "menu":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="17" x2="20" y2="17"/></svg>',
}

NAV = [("Home","/"),("Buiten trainen","/buiten-trainen-in-delft/"),("Per wijk","/personal-trainer-per-wijk/"),("Tarieven","/tarieven/"),("Contact","/contact/")]

def head(title, desc, path, ld=None):
    can = BASE + path
    j = ""
    if ld:
        for block in ld:
            j += '<script type="application/ld+json">'+json.dumps(block, ensure_ascii=False)+'</script>'
    nav = "".join(f'<a class="navlink" href="{href}">{esc(label)}</a>' for label,href in NAV)
    return f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{can}">
<meta property="og:type" content="website">
<meta property="og:locale" content="nl_NL">
<meta property="og:site_name" content="{esc(SITE)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{can}">
<meta property="og:image" content="{BASE}/assets/img/foto/d-hero.jpg">
<meta name="theme-color" content="#16335F">
<link rel="icon" href="/assets/icons/logo-mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css?v={CSS_VER}">
{j}
</head>
<body>
<header class="site-head">
  <nav class="nav" id="nav">
    <a class="brand" href="/"><img class="mark" src="/assets/icons/logo-mark.svg" alt=""><span><b>Personal Trainer</b><span>in Delft</span></span></a>
    {nav}
    <a class="btn btn-primary" href="/#trainers">Aanbevolen trainers</a>
    <button class="menu-toggle" aria-label="Menu" onclick="document.getElementById('nav').classList.toggle('open')">{IC['menu']}</button>
  </nav>
</header>
"""

def footer():
    return f"""<footer class="foot">
  <div class="wrap">
    <div class="cols">
      <div>
        <a class="brand" href="/" style="color:#fff"><img class="mark" src="/assets/icons/logo-mark.svg" alt=""><span><b>Personal Trainer</b><span style="color:#90A0BC">in Delft</span></span></a>
        <p style="margin-top:14px;max-width:32em;color:#AEBBD0">Onafhankelijk overzicht dat helpt bij het vinden van een passende personal trainer in Delft en omgeving, voor training aan huis en in de buitenlucht.</p>
        <span class="tower">{IC['tower']} Lokaal in de Prinsenstad</span>
      </div>
      <div>
        <h4>Op de site</h4>
        <a href="/buiten-trainen-in-delft/">Buiten trainen in Delft</a>
        <a href="/personal-trainer-per-wijk/">Personal trainer per wijk</a>
        <a href="/trainer-kiezen/">Een trainer kiezen</a>
        <a href="/tarieven/">Tarieven en proefles</a>
      </div>
      <div>
        <h4>Meer</h4>
        <a href="/#trainers">Aanbevolen trainers</a>
        <a href="/contact/">Contact</a>
        <a href="/privacybeleid/">Privacybeleid</a>
        <a href="/cookiebeleid/">Cookiebeleid</a>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; 2026 {esc(SITE)}</span>
      <span><a href="/contact/">Contact</a> &middot; <a href="/privacybeleid/">Privacy</a> &middot; <a href="/cookiebeleid/">Cookies</a></span>
    </div>
  </div>
</footer>
<script>
(function(){{
  var hv=document.querySelector('.sfeer-video video');
  if(hv&&window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches){{hv.removeAttribute('autoplay');try{{hv.pause();}}catch(e){{}}}}
}})();
</script>
</body>
</html>"""

def breadcrumb(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":BASE+u} for i,(n,u) in enumerate(items)]}

def crumbs_html(items):
    out=[f'<a href="{u}">{esc(n)}</a>' for n,u in items[:-1]]
    out.append(f'<span>{esc(items[-1][0])}</span>')
    return '<div class="wrap"><nav class="crumbs">'+' / '.join(out)+'</nav></div>'

def write(path, content):
    full = os.path.join(OUT, "index.html") if path=="/" else os.path.join(OUT, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full,"w",encoding="utf-8").write(content)

PROVIDERS = [
 {"slug":"yourhealth-personal-training","name":"YourHealth Personal Training","cc":"var(--c1)","ct":"#C8431F","tc":"#fff","badge":"Grootste netwerk","badge_ic":"users",
  "tagline":"Brede keuze aan trainers, actief in heel Nederland sinds 2007.","url":"https://www.yourhealthpt.nl/personal-trainer-delft/","home":"https://www.yourhealthpt.nl/","domain":"yourhealthpt.nl","anchor":"YourHealth in Delft","banner":"d-prov-yh.jpg",
  "lead":"YourHealth werkt met een groot netwerk van trainers, zodat er in Delft bijna altijd iemand beschikbaar is die past bij het doel en de agenda.",
  "usps":["Een van de grootste aanbieders voor training aan huis, met een ruim trainersbestand.","Veel specialisaties naast elkaar, van afvallen en conditie tot kracht en herstel.","Trainen op een vaste of wisselende plek, thuis, op het werk of buiten in Delft.","Werkt met strippenkaarten, dus zonder vast abonnement, en een partner traint kosteloos mee."],
  "for":"Wie wil kiezen uit veel trainers en specialisaties en flexibel wil trainen zonder vaste verplichting."},
 {"slug":"lets-do-it-personal-training","name":"LET'S DO IT Personal Training","cc":"var(--c2)","ct":"#9A6F0C","tc":"#14264B","badge":"Voor vrouwen, door vrouwen","badge_ic":"heart",
  "tagline":"Personal training speciaal voor vrouwen, met vrouwelijke trainers.","url":"https://www.letsdoitpt.nl/personal-trainer-delft/","home":"https://www.letsdoitpt.nl/","domain":"letsdoitpt.nl","anchor":"LET'S DO IT in Delft","banner":"d-prov-ldi.jpg",
  "lead":"LET'S DO IT richt zich volledig op vrouwen en koppelt elke deelnemer aan een vrouwelijke trainer, met aandacht voor de verschillende levensfasen.",
  "usps":["Volledig gericht op vrouwen, met uitsluitend vrouwelijke trainers.","Kennis van de invloed van de cyclus, een zwangerschap en de overgang op de training.","Begeleiding voor vrouwen na een bevalling en voor vrouwen boven de veertig.","Trainen aan huis of buiten in de eigen Delftse buurt, in een vertrouwde omgeving."],
  "for":"Vrouwen die het prettig vinden om met een vrouwelijke trainer te werken en aandacht voor de levensfase belangrijk vinden."},
 {"slug":"jouw-personal-trainer-aan-huis","name":"Jouw Personal Trainer aan Huis","cc":"var(--c3)","ct":"#157A6E","tc":"#fff","badge":"Sterk in 40-plus","badge_ic":"home",
  "tagline":"Training aan huis met aandacht voor fit blijven na het veertigste.","url":"https://www.jouwpersonaltraineraanhuis.nl/personal-trainer-delft/","home":"https://www.jouwpersonaltraineraanhuis.nl/","domain":"jouwpersonaltraineraanhuis.nl","anchor":"Jouw Personal Trainer aan Huis in Delft","banner":"d-prov-jptah.jpg",
  "lead":"Jouw Personal Trainer aan Huis legt de nadruk op een geleidelijke opbouw, met veel ervaring onder veertig- en vijftigplussers.",
  "usps":["Veel ervaring met veertig- en vijftigplussers die fit willen blijven.","Aandacht voor kracht, balans en soepel bewegen, met een geleidelijke opbouw.","Geschikt bij stijfheid, klachten of een herstart na een periode van weinig beweging.","Trainen aan huis of buiten in de buurt, zonder langdurig abonnement, met een partner die kosteloos meetraint."],
  "for":"Veertig- en vijftigplussers die geleidelijk willen opbouwen en willen werken aan kracht, balans en energie."},
]

def usp_list(p): return "".join(f'<li>{IC["check"]}<span>{esc(u)}</span></li>' for u in p["usps"])

def provider_card(p):
    return f"""<article class="provider" style="--cc:{p['cc']}">
    <div class="pmain">
      <span class="badge" style="--cc:{p['cc']};color:{p['tc']}">{IC[p['badge_ic']]}{esc(p['badge'])}</span>
      <p class="logo-slot">{esc(p['name'])}</p>
      <p class="tagline">{esc(p['tagline'])}</p>
      <ul class="usp" style="--cc:{p['ct']}">{usp_list(p)}</ul>
    </div>
    <div class="pside">
      <span class="for-who">Past goed bij</span>
      <p class="for-text">{esc(p['for'])}</p>
      <div class="links">
        <a class="btn btn-primary" style="background:{p['cc']};border-color:{p['cc']};color:{p['tc']}" href="{p['url']}" target="_blank" rel="noopener">{esc(p['anchor'])} {IC['arrow']}</a>
        <a class="more" style="color:{p['ct']}" href="/aanbieders/{p['slug']}/">Meer over {esc(p['name'])}</a>
      </div>
    </div>
  </article>"""

LOCATIES = [
 ("Delftse Hout","Het grootste groen- en recreatiegebied van de stad, met een meer, brede paden en volop ruimte voor bootcamp, hardlopen en oefeningen met het eigen lichaamsgewicht."),
 ("Abtswoudse Bos en Abtswoudsepark","Aan de zuidkant van Delft, met lange paden en open plekken die zich lenen voor intervaltraining en duurloopjes."),
 ("Agnetapark","Een historisch parkje met paden en bankjes, prima voor een korte krachtsessie dicht bij de binnenstad."),
 ("Nieuwe Plantage en Kalverbos","Groen aan de rand van het centrum, geschikt voor een training tussendoor zonder ver te reizen."),
 ("Langs de Schie en de vesten","De kades en het water bieden een vlak parcours voor hardlopen, fietsintervallen en oefeningen op een bankje."),
 ("Sportpark Brasserskade en Tanthof","Velden en groen aan de buitenrand, met ruimte voor duotraining en circuits in de openlucht."),
]
WIJKEN = [
 ("Binnenstad en Centrum","Trainen tussen de grachten, of aan huis in een appartement in het oude centrum."),
 ("Hof van Delft","Een woonwijk net buiten het centrum, met groen en kalme straten voor een training aan huis of buiten."),
 ("Vrijenban","Aan de noordkant, dicht bij de Delftse Hout, ideaal als de training graag buiten plaatsvindt."),
 ("Voordijkshoorn en Buitenhof","Ruime wijken met veel groen en parkeergelegenheid, handig voor een trainer die aan huis komt."),
 ("Tanthof","Een groene wijk in het zuiden met water en paden, geschikt voor buitentraining vlak bij de voordeur."),
 ("Voorhof","Centraal gelegen met sportvoorzieningen in de buurt, ook geschikt voor training thuis."),
 ("Wippolder en de TU-wijk","Rond de Technische Universiteit, met studenten en medewerkers die vaak buiten of thuis trainen."),
 ("Den Hoorn, Schipluiden en Delfgauw","De dorpen en buurten rond Delft, waar trainers aan huis eveneens langskomen."),
]

def page_home():
    path="/"; crumbs=[("Home","/")]
    ld=[
      {"@context":"https://schema.org","@type":"WebSite","@id":BASE+"/#website","url":BASE+"/","name":SITE,"inLanguage":"nl-NL","description":"Onafhankelijk overzicht van personal training in Delft, voor training aan huis en in de buitenlucht."},
      {"@context":"https://schema.org","@type":"Organization","@id":BASE+"/#org","name":SITE,"url":BASE+"/","email":EMAIL,"areaServed":"Delft","logo":BASE+"/assets/icons/logo-mark.svg"},
      {"@context":"https://schema.org","@type":"ItemList","name":"Aanbevolen personal trainers in Delft","itemListElement":[{"@type":"ListItem","position":i+1,"name":p["name"],"url":BASE+f"/aanbieders/{p['slug']}/"} for i,p in enumerate(PROVIDERS)]},
      {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":"Komt een personal trainer in Delft aan huis?","acceptedAnswer":{"@type":"Answer","text":"Ja. De aanbevolen aanbieders komen aan huis in alle Delftse wijken en in de dorpen eromheen, of trainen buiten op een plek in de buurt."}},
        {"@type":"Question","name":"Kan er buiten getraind worden in Delft?","acceptedAnswer":{"@type":"Answer","text":"Zeker. De Delftse Hout, het Abtswoudse Bos en de kades langs de Schie zijn geliefde plekken voor buitentraining, dicht bij huis."}},
        {"@type":"Question","name":"Is een abonnement nodig?","acceptedAnswer":{"@type":"Answer","text":"Niet altijd. Twee van de drie aanbieders werken met strippenkaarten, dus zonder vaste maandverplichting. De voorwaarden staan op de eigen websites."}},
      ]},
      breadcrumb(crumbs),
    ]
    crit=[("target","Een doel dat past","Een goede trainer begint met de vraag waar iemand naartoe werkt en stemt het programma daarop af, in plaats van een standaardschema af te draaien."),
          ("shield","Onderbouwd en veilig","Aandacht voor techniek en opbouw voorkomt blessures. Een ervaren trainer kijkt naar houding, belastbaarheid en herstel."),
          ("clock","Vol te houden","Het beste plan is het plan dat in de week past. Een trainer die meedenkt over tijd en plek houdt de motivatie op peil."),
          ("heart","Een klik die werkt","Vertrouwen en sfeer bepalen of iemand blijft komen. Een proefles laat snel merken of de samenwerking klikt.")]
    crit_html="".join(f'<div class="card"><div class="ic">{IC[i]}</div><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for i,t,d in crit)
    gal_html="".join(f'<img src="/assets/img/foto/{g}.jpg" alt="Personal training buiten in Delft" loading="lazy">' for g in ["d-gal-1","d-gal-2","d-gal-3","d-gal-4","d-gal-5","d-gal-6"])
    prov_html="".join(provider_card(p) for p in PROVIDERS)
    loc_html="".join(f'<div class="tile"><h3>{esc(n)}</h3><p>{esc(d)}</p></div>' for n,d in LOCATIES[:4])
    h=head("Personal Trainer in Delft | training aan huis en in de buitenlucht",
      "Een passende personal trainer vinden in Delft. Onafhankelijk overzicht van drie aanbevolen aanbieders voor training aan huis en buiten in de Prinsenstad.",path,ld)
    h+=f"""<section class="hero">
  <div class="wrap hero-inner">
    <div>
      <span class="eyebrow">{IC['pin']}Delft en omgeving</span>
      <h1>Een personal trainer in <em>Delft</em> die echt past</h1>
      <p class="lead">Fit worden in de Prinsenstad gaat het makkelijkst met begeleiding op maat. Dit overzicht legt uit waar een goede trainer aan voldoet en licht drie aanbevolen aanbieders uit, voor training aan huis en in de buitenlucht.</p>
      <div class="hero-actions">
        <a class="btn btn-gold" href="#trainers">Bekijk de aanbevolen trainers {IC['arrow']}</a>
        <a class="btn btn-ghost-light" href="/trainer-kiezen/">Hoe kies ik een trainer</a>
      </div>
      <div class="hero-meta">
        <span>{IC['check']}Aan huis en buiten</span>
        <span>{IC['check']}Proefles mogelijk</span>
        <span>{IC['check']}Vaak zonder abonnement</span>
      </div>
    </div>
    <div class="hero-media">
      <img src="/assets/img/foto/d-hero.jpg" alt="Personal training langs het water in Delft" width="800" height="520">
    </div>
  </div>
</section>

<section class="section tight">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow" style="justify-content:center">{IC['play']}In beeld</span>
      <h2>Personal training in Delft</h2>
      <p class="lead">Een korte impressie van trainen aan huis en in de buitenlucht, van de Delftse Hout tot de eigen wijk.</p>
    </div>
    <div class="sfeer-video">
      <video autoplay muted loop playsinline preload="metadata" poster="/assets/img/sfeer-delft-poster.jpg?v={POS_VER}" aria-label="Impressie van personal training in Delft">
        <source src="/assets/video/sfeer-delft.mp4?v={VID_VER}" type="video/mp4">
      </video>
    </div>
  </div>
</section>

<section class="section panel">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{IC['target']}Waar op te letten</span>
      <h2>Wat een goede personal trainer onderscheidt</h2>
      <p class="lead">Niet elke trainer past bij elk doel. Vier punten helpen om de juiste keuze te maken.</p>
    </div>
    <div class="grid cols-2">{crit_html}</div>
  </div>
</section>

<section class="section" id="trainers">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{IC['users']}Aanbevolen in Delft</span>
      <h2>Drie aanbieders, elk met een eigen kracht</h2>
      <p class="lead">Drie partijen die personal training aan huis en buiten verzorgen in Delft. De keuze hangt af van het doel en de voorkeur.</p>
    </div>
    <div class="providers">{prov_html}</div>
  </div>
</section>

<section class="section panel">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{IC['leaf']}Buitenlucht</span>
      <h2>Buiten trainen in Delft</h2>
      <p class="lead">De stad heeft volop groen en water binnen handbereik. Een greep uit de plekken waar buiten getraind wordt.</p>
    </div>
    <div class="tiles">{loc_html}</div>
    <p style="margin-top:22px"><a class="btn btn-ghost" href="/buiten-trainen-in-delft/">Alle locaties bekijken {IC['arrow']}</a></p>
    <div class="gallery" style="margin-top:30px">{gal_html}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow" style="justify-content:center">{IC['home']}Dichtbij</span>
      <h2>In elke wijk van Delft</h2>
      <p class="lead">Van de binnenstad tot Tanthof: een trainer aan huis of buiten in de eigen buurt scheelt reistijd en houdt de drempel laag.</p>
    </div>
    <p style="text-align:center"><a class="btn btn-primary" href="/personal-trainer-per-wijk/">Personal trainer per wijk {IC['arrow']}</a></p>
  </div>
</section>

<section class="section panel">
  <div class="wrap">
    <div class="cta-band">
      <h2>Klaar om te beginnen in Delft?</h2>
      <p>Vraag een intake met proefles aan bij een van de aanbevolen trainers en ervaar of de aanpak en de trainer passen.</p>
      <a class="btn btn-gold" href="/#trainers">Naar de aanbevolen trainers {IC['arrow']}</a>
    </div>
  </div>
</section>"""
    h+=footer(); write(path,h)

def page_buiten():
    path="/buiten-trainen-in-delft/"; crumbs=[("Home","/"),("Buiten trainen in Delft",path)]
    ld=[{"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":"Buiten trainen in Delft","inLanguage":"nl-NL"},
        {"@context":"https://schema.org","@type":"ItemList","name":"Locaties voor buitentraining in Delft","itemListElement":[{"@type":"ListItem","position":i+1,"name":n} for i,(n,d) in enumerate(LOCATIES)]},
        breadcrumb(crumbs)]
    tiles="".join(f'<div class="tile {"gold" if i%2 else ""}"><h3>{esc(n)}</h3><p>{esc(d)}</p></div>' for i,(n,d) in enumerate(LOCATIES))
    gal_html="".join(f'<img src="/assets/img/foto/{g}.jpg" alt="Buitentraining in Delft" loading="lazy">' for g in ["d-gal-2","d-gal-6","d-gal-1","d-gal-4"])
    h=head("Buiten trainen in Delft | Delftse Hout, Abtswoudse Bos en meer | "+SITE,
      "De mooiste plekken voor buitentraining in Delft, van de Delftse Hout en het Abtswoudse Bos tot de kades langs de Schie. Trainen in de buitenlucht, dicht bij huis.",path,ld)
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{IC['leaf']}In de buitenlucht</span>
      <h1>Buiten trainen in Delft</h1>
      <p class="lead">Delft is compact en groen tegelijk. Binnen een paar minuten staat iemand in een park, langs het water of in het bos. Dat maakt buitentraining hier laagdrempelig, het hele jaar door.</p>
    </div>
    <div class="tiles">{tiles}</div>
    <div class="gallery" style="margin-top:34px">{gal_html}</div>
  </div>
</section>

<section class="section panel">
  <div class="wrap">
    <div class="grid cols-2">
      <div class="card"><div class="ic">{IC['leaf']}</div><h3>Waarom buiten</h3><p>Frisse lucht, wisselend terrein en daglicht maken een training afwisselender dan een zaal. Het kost bovendien geen lidmaatschap van een sportschool.</p></div>
      <div class="card"><div class="ic">{IC['clock']}</div><h3>Het hele jaar</h3><p>Met de juiste kleding gaat buitentraining ook in de winter door. Een trainer past de oefeningen aan op het weer en de ondergrond.</p></div>
      <div class="card"><div class="ic">{IC['home']}</div><h3>Of toch thuis</h3><p>Bij slecht weer of een drukke dag verschuift een sessie naar binnen. De meeste aanbieders combineren binnen en buiten moeiteloos.</p></div>
      <div class="card"><div class="ic">{IC['target']}</div><h3>Voor elk niveau</h3><p>Van een eerste herstart tot een gevorderde krachtopbouw: buiten trainen schaalt mee met het doel en de belastbaarheid.</p></div>
    </div>
    <p style="margin-top:26px"><a class="btn btn-primary" href="/#trainers">Bekijk de aanbevolen trainers {IC['arrow']}</a></p>
  </div>
</section>"""
    h+=footer(); write(path,h)

def page_wijken():
    path="/personal-trainer-per-wijk/"; crumbs=[("Home","/"),("Personal trainer per wijk",path)]
    ld=[{"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":"Personal trainer per wijk in Delft","inLanguage":"nl-NL"},
        {"@context":"https://schema.org","@type":"ItemList","name":"Delftse wijken","itemListElement":[{"@type":"ListItem","position":i+1,"name":n} for i,(n,d) in enumerate(WIJKEN)]},
        breadcrumb(crumbs)]
    tiles="".join(f'<div class="tile"><h3>{esc(n)}</h3><p>{esc(d)}</p></div>' for n,d in WIJKEN)
    h=head("Personal trainer per wijk in Delft | aan huis in de hele stad | "+SITE,
      "Een personal trainer aan huis in elke Delftse wijk, van de binnenstad en Hof van Delft tot Tanthof, Voorhof en de TU-wijk, en in de dorpen eromheen.",path,ld)
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{IC['home']}Dicht bij huis</span>
      <h1>Personal trainer per wijk in Delft</h1>
      <p class="lead">Een trainer die aan huis komt of buiten in de eigen buurt traint, scheelt reistijd en maakt het makkelijker om vol te houden. De aanbevolen aanbieders komen in de hele stad en in de dorpen eromheen.</p>
    </div>
    <div class="tiles">{tiles}</div>
  </div>
</section>

<section class="section panel">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow" style="justify-content:center">{IC['pin']}Ook buiten de stad</span>
      <h2>Rond Delft</h2>
      <p class="lead">Den Hoorn, Schipluiden, Delfgauw en Pijnacker-Nootdorp liggen op een steenworp afstand. Ook daar komen trainers aan huis of trainen ze in het groen van Midden-Delfland.</p>
    </div>
    <p style="text-align:center"><a class="btn btn-primary" href="/#trainers">Naar de aanbevolen trainers {IC['arrow']}</a></p>
  </div>
</section>"""
    h+=footer(); write(path,h)

def page_kiezen():
    path="/trainer-kiezen/"; crumbs=[("Home","/"),("Een trainer kiezen",path)]
    steps=[("Bepaal het doel","Afvallen, sterker worden, herstellen na een blessure of fitter de trap op. Een helder doel maakt het makkelijker om de juiste trainer te vinden."),
           ("Kies binnen of buiten","Thuis, in een park of een combinatie. Wie graag buiten is, kiest een trainer die gewend is aan de Delftse Hout en de parken."),
           ("Vraag een proefles aan","Een eerste sessie laat merken of de aanpak en de klik kloppen. Pas daarna volgt een keuze voor een traject."),
           ("Let op de voorwaarden","Strippenkaart of abonnement, de duur van een sessie en of een partner mee mag trainen. Dit verschilt per aanbieder.")]
    steps_html="".join(f'<div class="step"><div class="n">{i+1}</div><div><h3>{esc(t)}</h3><p>{esc(d)}</p></div></div>' for i,(t,d) in enumerate(steps))
    ld=[{"@context":"https://schema.org","@type":"Article","@id":BASE+path,"headline":"Een personal trainer kiezen in Delft","inLanguage":"nl-NL","author":{"@type":"Organization","name":SITE},"publisher":{"@type":"Organization","name":SITE}},breadcrumb(crumbs)]
    h=head("Een personal trainer kiezen in Delft | stappenplan | "+SITE,
      "In vier stappen een passende personal trainer kiezen in Delft: bepaal het doel, kies binnen of buiten, vraag een proefles aan en let op de voorwaarden.",path,ld)
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap prose">
    <span class="eyebrow">{IC['target']}Stappenplan</span>
    <h1>Een personal trainer kiezen in Delft</h1>
    <p class="lead">Een trainer kiezen hoeft niet ingewikkeld te zijn. Met een helder doel en een proefles is de juiste keuze vaak snel gemaakt.</p>
    <div class="steps" style="margin:28px 0">{steps_html}</div>
    <div class="callout"><p><strong>Tip.</strong> Een proefles kost weinig tijd en zegt veel. De klik met de trainer weegt minstens zo zwaar als het programma zelf.</p></div>
    <h2>Binnen of buiten in Delft</h2>
    <p>Wie de buitenlucht opzoekt, heeft in Delft veel te kiezen, van de Delftse Hout tot het Abtswoudse Bos. Wie liever thuis traint, hoeft de deur niet uit en bespaart reistijd. De meeste trainers schakelen moeiteloos tussen beide.</p>
    <h2>Wat het kost</h2>
    <p>Tarieven verschillen per aanbieder en hangen af van het aantal sessies en de duur. Twee van de drie aanbevolen partijen werken met strippenkaarten, dus zonder vaste maandverplichting. Meer hierover staat op de pagina over tarieven.</p>
    <p style="margin-top:18px"><a class="btn btn-primary" href="/#trainers">Bekijk de aanbevolen trainers {IC['arrow']}</a> <a class="btn btn-ghost" href="/tarieven/">Naar de tarieven</a></p>
  </div>
</section>"""
    h+=footer(); write(path,h)

def page_tarieven():
    path="/tarieven/"; crumbs=[("Home","/"),("Tarieven en proefles",path)]
    ld=[{"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":"Tarieven personal training Delft","inLanguage":"nl-NL"},breadcrumb(crumbs)]
    h=head("Tarieven personal training Delft | strippenkaart, abonnement en proefles | "+SITE,
      "Hoe werkt de prijs van een personal trainer in Delft? Uitleg over strippenkaarten, abonnementen, de duur van een sessie en de proefles. De exacte tarieven staan bij de aanbieders.",path,ld)
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap prose">
    <span class="eyebrow">{IC['euro']}Wat kost het</span>
    <h1>Tarieven en proefles</h1>
    <p class="lead">Dit is een onafhankelijk overzicht, geen aanbieder. De exacte tarieven staan op de websites van de drie trainers. Wel valt in het algemeen iets te zeggen over hoe de prijs is opgebouwd.</p>
    <h2>Strippenkaart of abonnement</h2>
    <p>Twee van de drie aanbevolen aanbieders werken met strippenkaarten. Daarbij wordt een aantal sessies vooraf afgenomen, zonder vaste maandverplichting. Dat geeft vrijheid om het tempo zelf te bepalen. Een abonnement is er ook, vaak iets voordeliger per sessie, maar met een langere binding.</p>
    <h2>Wat de prijs bepaalt</h2>
    <ul>
      <li>Het aantal sessies per week en de totale omvang van een traject.</li>
      <li>De duur van een sessie, meestal zestig minuten.</li>
      <li>Training aan huis, op locatie of buiten in de buurt.</li>
      <li>Of een partner kosteloos meetraint, wat bij twee aanbieders mogelijk is.</li>
    </ul>
    <div class="callout"><p><strong>Proefles.</strong> Alle drie de aanbieders bieden de mogelijkheid om eerst kennis te maken. Dat is het moment om te merken of de aanpak en de trainer passen, voordat er iets wordt afgesproken.</p></div>
    <h2>Aan huis in Delft</h2>
    <p>Omdat de trainer naar de deelnemer toe komt, vervallen reistijd en de kosten van een sportschool. Voor veel mensen in Delft weegt dat op tegen het uurtarief, zeker bij een drukke agenda.</p>
    <p style="margin-top:18px"><a class="btn btn-primary" href="/#trainers">Bekijk de aanbevolen trainers {IC['arrow']}</a></p>
  </div>
</section>"""
    h+=footer(); write(path,h)

PBODY = {
 "yourhealth-personal-training":[
   ("Waarom YourHealth","De kracht van YourHealth zit in de schaal. Door het grote aantal aangesloten trainers is er voor vrijwel elk doel en elke agenda een match te vinden, van krachtopbouw tot afvallen of herstel na een blessure."),
   ("In Delft","In Delft betekent dat een trainer die aan huis komt of buiten afspreekt, bijvoorbeeld in de Delftse Hout. Het werken met strippenkaarten houdt de stap klein, en een partner mag kosteloos meetrainen."),
 ],
 "lets-do-it-personal-training":[
   ("Waarom LET'S DO IT","LET'S DO IT richt zich uitsluitend op vrouwen en koppelt elke deelnemer aan een vrouwelijke trainer. Veel vrouwen ervaren dat als prettiger en veiliger, zeker rond gevoelige onderwerpen als de cyclus, een zwangerschap of de overgang."),
   ("In Delft","De training vindt plaats aan huis of buiten in de eigen Delftse buurt, in een vertrouwde omgeving. Dat verlaagt de drempel om te beginnen en maakt het makkelijker om het vol te houden."),
 ],
 "jouw-personal-trainer-aan-huis":[
   ("Waarom Jouw Personal Trainer aan Huis","Deze aanbieder is sterk in een geleidelijke, verantwoorde opbouw en heeft veel ervaring met veertig- en vijftigplussers. De aandacht gaat naar kracht, balans en soepel blijven bewegen, ook bij stijfheid of klachten."),
   ("In Delft","De trainer komt aan huis in heel Delft, of spreekt buiten af in een park of langs het water. Zonder langdurig abonnement, en met een partner die kosteloos meetraint."),
 ],
}

def provider_page(p):
    path=f"/aanbieders/{p['slug']}/"; crumbs=[("Home","/"),("Aanbieders","/#trainers"),(p["name"],path)]
    ld=[{"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":p["name"]+" in Delft","inLanguage":"nl-NL"},breadcrumb(crumbs)]
    usp="".join(f'<li>{IC["check"]}<span>{esc(u)}</span></li>' for u in p["usps"])
    secs="".join(f'<h2>{esc(t)}</h2><p>{esc(d)}</p>' for t,d in PBODY[p["slug"]])
    h=head(f"{p['name']} in Delft | {SITE}",
      f"{p['name']} voor personal training in Delft. {p['tagline']} Lees waar deze aanbieder sterk in is en plan een proefles.",path,ld)
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap prose">
    <span class="eyebrow" style="color:{p['ct']}">{IC[p['badge_ic']]}{esc(p['badge'])}</span>
    <h1>{esc(p['name'])} in Delft</h1>
    <p class="lead">{esc(p['lead'])}</p>
    <div style="border-radius:14px;overflow:hidden;margin:24px 0;border:1px solid var(--line)"><img src="/assets/img/foto/{p['banner']}" alt="Personal training in Delft" loading="lazy"></div>
    <ul class="ticks" style="--cc:{p['ct']};margin:6px 0 8px">{usp}</ul>
    {secs}
    <div class="callout">
      <p><strong>Past dit bij het doel?</strong> Bekijk het aanbod en de tarieven rechtstreeks bij <a href="{p['url']}" target="_blank" rel="noopener" style="color:{p['ct']}">{esc(p['anchor'])}</a>.</p>
      <p style="margin-bottom:0">Direct contact: <a href="tel:{TEL}">{PHONE}</a>.</p>
    </div>
    <p><a href="/#trainers">Terug naar alle aanbevolen trainers</a></p>
  </div>
</section>

<section class="section tight">
  <div class="wrap">
    <div class="cta-band">
      <h2>{esc(p['name'])} in Delft</h2>
      <p>Vraag een intake met proefles aan en ervaar of de werkwijze en de trainer passen.</p>
      <a class="btn btn-gold" href="{p['url']}" target="_blank" rel="noopener">Naar {esc(p['domain'])} {IC['arrow']}</a>
    </div>
  </div>
</section>"""
    h+=footer(); write(path,h)

def contact():
    path="/contact/"; crumbs=[("Home","/"),("Contact",path)]
    ld=[breadcrumb(crumbs),{"@context":"https://schema.org","@type":"ContactPage","@id":BASE+path,"url":BASE+path,"name":"Contact","inLanguage":"nl-NL"}]
    cards=""
    for p in PROVIDERS:
        cards+=f"""<div class="ccard" style="--cc:{p['cc']};--ct:{p['ct']}">
        <span class="tag">{esc(p['badge'])}</span>
        <h3>{esc(p['name'])}</h3>
        <a class="row" href="tel:{TEL}">{IC['phone']}{PHONE}</a>
        <div class="ext"><a href="{p['url']}" target="_blank" rel="noopener">{esc(p['anchor'])} {IC['arrow']}</a></div>
      </div>"""
    h=head("Contact | "+SITE,"Een afspraak of vraag over personal training in Delft? Neem rechtstreeks contact op met een van de drie aanbevolen aanbieders.",path,ld)
    h+=crumbs_html(crumbs)
    h+=f"""<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{IC['mail']}Contact</span>
      <h1>Contact opnemen</h1>
      <p class="lead">Voor een afspraak, een proefles of een vraag over personal training is het het handigst om rechtstreeks contact op te nemen met een van de drie aanbevolen aanbieders in Delft.</p>
    </div>
    <div class="ccards">{cards}</div>
  </div>
</section>"""
    h+=footer(); write(path,h)

def legal_page(path, title, blocks):
    crumbs=[("Home","/"),(title,path)]
    ld=[breadcrumb(crumbs),{"@context":"https://schema.org","@type":"WebPage","@id":BASE+path,"url":BASE+path,"name":title,"inLanguage":"nl-NL"}]
    body="".join(blocks)
    h=head(f"{title} | {SITE}", f"{title} van {SITE}.", path, ld)
    h+=crumbs_html(crumbs)
    h+=f'<section class="section"><div class="wrap prose"><h1>{esc(title)}</h1>{body}</div></section>'
    h+=footer(); write(path,h)

def privacy():
    legal_page("/privacybeleid/","Privacybeleid",[
      "<p>Deze website is een onafhankelijk, informatief overzicht van personal training in Delft. De site verwerkt zo min mogelijk persoonsgegevens.</p>",
      "<h2>Welke gegevens</h2><p>Er is geen contactformulier. Wie via een telefoonnummer of een link contact opneemt met een aanbieder, deelt gegevens rechtstreeks met die aanbieder, niet met deze site.</p>",
      "<h2>Statistieken</h2><p>Indien bezoekstatistieken worden bijgehouden, gebeurt dat zo privacyvriendelijk mogelijk en zonder gegevens te verkopen.</p>",
      "<h2>Vragen</h2><p>Vragen over privacy kunnen per e-mail gesteld worden via "+EMAIL+".</p>",
    ])

def cookies():
    legal_page("/cookiebeleid/","Cookiebeleid",[
      "<p>Deze site gebruikt zo min mogelijk cookies en plaatst geen advertentiecookies.</p>",
      "<h2>Functioneel</h2><p>Functionele cookies zorgen dat de site goed werkt. Die zijn noodzakelijk en worden altijd geplaatst.</p>",
      "<h2>Video</h2><p>De video in de sfeerimpressie wordt rechtstreeks vanaf deze site geladen, zonder externe videodienst en zonder bijbehorende cookies.</p>",
      "<h2>Vragen</h2><p>Vragen over cookies kunnen per e-mail gesteld worden via "+EMAIL+".</p>",
    ])

def not_found():
    h=head("Pagina niet gevonden | "+SITE,"De opgevraagde pagina bestaat niet.","/404.html",None)
    h+=f"""<section class="section"><div class="wrap prose" style="text-align:center">
      <span class="eyebrow" style="justify-content:center">{IC['pin']}404</span>
      <h1>Deze pagina bestaat niet</h1>
      <p class="lead">Mogelijk is de link verouderd. Terug naar de startpagina of bekijk de aanbevolen trainers.</p>
      <p><a class="btn btn-primary" href="/">Naar de homepage {IC['arrow']}</a> <a class="btn btn-ghost" href="/#trainers">Aanbevolen trainers</a></p>
    </div></section>"""
    h+=footer()
    open(os.path.join(OUT,"404.html"),"w",encoding="utf-8").write(h)

def extras():
    urls=["/","/buiten-trainen-in-delft/","/personal-trainer-per-wijk/","/trainer-kiezen/","/tarieven/","/contact/","/privacybeleid/","/cookiebeleid/"]+[f"/aanbieders/{p['slug']}/" for p in PROVIDERS]
    sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls: sm+=f"  <url><loc>{BASE}{u}</loc></url>\n"
    sm+="</urlset>\n"
    open(os.path.join(OUT,"sitemap.xml"),"w").write(sm)
    open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    open(os.path.join(OUT,"_headers"),"w").write("/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n")
    open(os.path.join(OUT,"_redirects"),"w").write("https://www.personaltrainerindelft.nl/* https://personaltrainerindelft.nl/:splat 301!\n")

def copy_assets():
    import shutil
    dst=os.path.join(OUT,"assets")
    if os.path.exists(dst): shutil.rmtree(dst)
    shutil.copytree(os.path.join(SRC,"assets"), dst)

def main():
    import shutil
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT, exist_ok=True)
    copy_assets()
    page_home(); page_buiten(); page_wijken(); page_kiezen(); page_tarieven()
    for p in PROVIDERS: provider_page(p)
    contact(); privacy(); cookies(); not_found(); extras()
    print("Build klaar in", OUT)

if __name__=="__main__":
    main()
