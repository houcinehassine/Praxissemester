# -*- coding: utf-8 -*-
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDIR = os.path.join(ROOT, "projekte", "projekt-1")
TDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tabellen")

def T(i):
    with open(os.path.join(TDIR, f"t{i}.html"), encoding="utf-8") as f:
        return f.read().strip()

PAGES = [
    ("index.html", "Überblick"),
    ("02-aufgabenstellung.html", "Aufgabenstellung"),
    ("03-bestandsaufnahme.html", "Bestandsaufnahme"),
    ("04-bestandsanalyse.html", "Bestandsanalyse"),
    ("05-zylinderkopf.html", "Zylinderkopf"),
    ("06-sechskant.html", "Sechskant"),
    ("07-holzschrauben.html", "Holzschrauben"),
    ("08-schlossschrauben.html", "Schloßschrauben"),
    ("09-zusammenfuehrung.html", "Zusammenführung"),
    ("10-boxen-regal-layout.html", "Boxen & Regal"),
    ("11-cad-konstruktion.html", "CAD-Konstruktion"),
    ("12-kapazitaetsnachweis.html", "Kapazitätsnachweis"),
    ("13-bewertung-ausblick.html", "Bewertung & Ausblick"),
]

def head(title):
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | Mein Praxissemester</title>
  <link rel="icon" type="image/svg+xml" href="../../favicon.svg" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../css/style.css" />
</head>
<body>

  <header class="site-header">
    <div class="inner">
      <a href="../../index.html" class="logo">Mein <span>Praxissemester</span></a>
      <nav>
        <a href="../../index.html">Start</a>
        <a href="../../index.html#projekte">Projekte</a>
      </nav>
    </div>
  </header>
"""

def subnav(active_file):
    aktiv_index = next(i for i, (fname, _) in enumerate(PAGES, start=1) if fname == active_file)
    prozent = round(aktiv_index / len(PAGES) * 100)

    tab_links = []
    menu_links = []
    for i, (fname, label) in enumerate(PAGES, start=1):
        ist_aktiv = fname == active_file
        cls = "aktiv" if ist_aktiv else ""
        tab_links.append(f'<a href="{fname}" class="{cls}"><span class="nr">{i}</span>{label}</a>')
        menu_links.append(f'<a href="{fname}" class="{cls}"><span class="nr">{i}</span>{label}</a>')

    return f"""  <nav class="projekt-subnav">
    <div class="fortschritt">
      <span>{aktiv_index}/{len(PAGES)}</span>
      <span class="balken"><span style="width:{prozent}%"></span></span>
    </div>
    <div class="scroll-bereich">
      <div class="inner">
        {''.join(tab_links)}
      </div>
    </div>
    <details class="seiten-menu">
      <summary><span class="icon">&#9776;</span><span class="text">Alle Seiten</span><span class="chevron">&#9662;</span></summary>
      <div class="seiten-menu-liste">
        {''.join(menu_links)}
      </div>
    </details>
  </nav>
"""

def seiten_kopf(nr, titel, intro):
    return f"""  <header class="seiten-kopf">
    <div class="inner">
      <div class="breadcrumb"><a href="../../index.html">Start</a> &rsaquo; <a href="index.html">Projekt 1</a> &rsaquo; Seite {nr} von 13</div>
      <h1>{titel}</h1>
      <p class="intro">{intro}</p>
    </div>
  </header>
"""

def footer_scripts():
    return """  <footer class="site-footer">
    Praxissemester-Dokumentation
  </footer>

  <script src="../../js/main.js"></script>
</body>
</html>
"""

def projekt_nav(prev_href, prev_label, next_href, next_label):
    return f"""    <nav class="projekt-nav">
      <a href="{prev_href}">
        <span class="richtung">&larr; Zurück</span>
        {prev_label}
      </a>
      <a class="naechste" href="{next_href}">
        <span class="richtung">Weiter &rarr;</span>
        {next_label}
      </a>
    </nav>
"""

def write_page(fname, title, body):
    path = os.path.join(PDIR, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(head(title))
        f.write(subnav(fname))
        f.write(body)
        f.write(footer_scripts())
    print("wrote", fname, len(body))

os.makedirs(PDIR, exist_ok=True)
print("Setup ok, pages:", len(PAGES))
