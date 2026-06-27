# personaltrainerindelft.nl

Statische site, gegenereerd met een Python-script. Geen frameworks, geen build-tools nodig.

## Bouwen
    python3 build.py
De gegenereerde site komt in `site/`.

## Deployen (Cloudflare Pages)
- Build command: `python3 build.py`
- Output directory: `site`
Of upload de inhoud van `site/` rechtstreeks via een directe upload.

## Structuur
- Eigen huisstijl: Delfts Blauw met goud, serif-display (Fraunces) en Instrument Sans.
- Pagina's: home, buiten trainen, per wijk, trainer kiezen, tarieven, drie aanbiederspagina's, contact, privacy, cookies, 404.
- Video: zelf gehoste sfeerimpressie, opgebouwd uit de aangeleverde trainingsfoto's (`assets/video/sfeer-delft.mp4`), met posterframe.

## Aandachtspunten
- De aanbieders-URL's volgen het patroon `/personal-trainer-delft/` per merk. Controleer of die landingspagina's bestaan en pas ze zo nodig aan in `PROVIDERS` in `build.py`.
- Het telefoonnummer is gelijk aan dat van de Amstelveen-opzet (zelfde aanbieders). Aanpassen kan via `PHONE`/`TEL`.
- Wil je een betaalde plaatsing markeren, voeg dan `rel="sponsored"` toe aan de uitgaande links in `provider_card` en `provider_page`.
- CSS, video en poster hebben een versie-stempel (`?v=hash`) voor cache-busting; bij een wijziging vernieuwt dat vanzelf.
