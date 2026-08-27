# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt3 import *

TOC = [
    ("02-original-system.html", "Das Original-System verstehen", "Tablet- und Entwickler-Modus, die sechs Tabellenblätter, die vier UserForms und die 24 VBA-Module A–H – die Grundlage, die vor jeder Neuentwicklung komplett durchgearbeitet wurde."),
    ("03-schwachstellen.html", "Erkannte Schwachstellen", "Kein Mehrbenutzerbetrieb, doppelte Mac/Windows-Codepfade, eine nie fertig unterstützte Gmail-Anbindung und mehr – die konkreten Gründe für die Neuentwicklung."),
    ("04-architektur.html", "Architekturentscheidung", "Warum die Wahl auf Python, Streamlit und SQLite fiel und wie die Anwendung in drei Schichten (app.py, logic.py, db.py) aufgeteilt wurde."),
    ("05-vba-python-portierung.html", "VBA → Python", "Wie zentrale VBA-Funktionen wie ProzessMaterialEntnahme 1:1 nach Python übertragen wurden – inklusive Mehrbenutzerbetrieb mit WAL-Modus und Lasttest."),
    ("06-datenmodell.html", "Datenmodell & Import", "Das Datenbankschema, bewusst nah an den alten Excel-Tabellen gehalten, sowie die kontrollierte Digitalisierung von 86 echten Artikel-Datensätzen aus handschriftlichen Listen."),
    ("07-oberflaeche.html", "Iterative Oberfläche", "PDF-Export, modale Dialoge statt Seitenwechsel, automatische Voll/Rest-Erkennung und eine einstellbare Schrott-Grenze – Schritt für Schritt im Browser getestet."),
    ("08-papierkorb.html", "Papierkorb & Löschsicherheit", "Wie aus einem endgültigen Löschvorgang eine zweistufig abgesicherte, wiederherstellbare Aktion wurde."),
    ("09-produktionsreife.html", "Produktionsreife", "Automatisches Backup, Hintergrunddienst, der Umzug aus iCloud Drive und ein fertiges Windows-Setup-Paket für den Firmenrechner."),
    ("10-cloud-migration.html", "Cloud-Migration", "Die Entscheidung für GitHub, Neon und Streamlit Community Cloud – und die vier subtilen Postgres-Fallstricke, die dabei auftraten."),
    ("11-go-live.html", "Go-Live & Fehlerbehebung", "Die eigentliche Veröffentlichung sowie zwei Fehler, die kurz danach gemeldet und grundlegend behoben wurden."),
    ("12-code-vertiefung.html", "Code-Vertiefung", "Ein genauerer Blick in den echten Quellcode: die _Zeile-Klasse, die Materialentnahme-Logik in Python und das Migrationsskript."),
    ("13-fazit.html", "Fazit & Ausblick", "Was heute funktioniert, was noch offen ist und was die Cloud-Version leistet, was die Excel-Datei nie konnte."),
]

toc_html = ""
for i, (href, titel, text) in enumerate(TOC, start=2):
    toc_html += f"""      <a class="toc-karte" href="{href}">
        <span class="toc-nr">{i}</span>
        <h3>{titel}</h3>
        <p>{text}</p>
      </a>
"""

body = f"""  <main class="projekt-detail">
    <header class="projekt-kopf">
    <div class="kopf-inner">
      <a class="zurueck-link" href="../../index.html">&larr; Zurück zur Übersicht</a>
      <span class="tag tag--lager">Lager &amp; Organisation</span>
      <h1>Projekt 3: Vom Excel-Lagersystem zur Cloud-Anwendung</h1>
      <p class="intro">
        Das Lagerbestand-System aus Projekt 2 lief zuverlässig, war aber an
        eine Excel-Datei auf einem einzelnen Rechner gebunden. In diesem
        Projekt wurde es komplett neu aufgebaut: als eigenständige
        Python/Streamlit-Webanwendung mit Datenbank im Hintergrund – vom
        lokalen Einzelplatzbetrieb bis zu einer privat erreichbaren
        Cloud-Version, die unabhängig von jedem einzelnen Gerät oder jeder
        einzelnen Person läuft.
      </p>
      <div class="meta">
        <span>Stand: 16.08.2026</span>
        <span>Bereich: Lager</span>
        <span>Werkzeug: Python · Streamlit · SQLite/Postgres</span>
      </div>
      <div class="kennzahlen-grid">
        <div class="kennzahl"><strong>3</strong><span>Code-Schichten (app/logic/db)</span></div>
        <div class="kennzahl"><strong>86</strong><span>echte Artikel-Datensätze übernommen</span></div>
        <div class="kennzahl"><strong>50</strong><span>Artikelgruppen</span></div>
        <div class="kennzahl"><strong>4</strong><span>Postgres-Fallstricke gelöst</span></div>
        <div class="kennzahl"><strong>100</strong><span>gleichzeitige Schreibzugriffe im Lasttest</span></div>
        <div class="kennzahl"><strong>13</strong><span>Seiten dieser Dokumentation</span></div>
      </div>
    </div>
    </header>

    <section>
      <h2>Die Ausgangslage in einem Satz</h2>
      <div class="zitat-box">
        Ein System, das an den privaten Rechner einer einzelnen Person
        gebunden ist, ist nicht betriebsfähig, sobald diese Person das
        Unternehmen verlässt.
        <span class="quelle">Kernproblem, das die Cloud-Entscheidung ausgelöst hat – Details auf Seite 10</span>
      </div>
    </section>

    <section>
      <h2>Warum diese Seite nötig war</h2>
      <p>
        Punkt 3 der ursprünglichen Aufgabenliste lautete: das Excel-Lagersystem
        „in eine Webseite umwandeln“. Am Ende wurde daraus mehr als eine reine
        Webseite – eine vollwertige, mehrbenutzerfähige Anwendung mit
        eigener Datenbank, automatischem Backup, Papierkorb-Funktion und
        einer öffentlich (im privaten, eingeladenen Sinn) erreichbaren
        Cloud-Version. Diese Dokumentation zeigt den kompletten Weg dorthin –
        inklusive der Stellen, an denen es nicht auf Anhieb funktioniert hat.
      </p>
    </section>

    <section>
      <h2>Eingesetzte Methoden &amp; Werkzeuge</h2>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>Python + Streamlit</h4><p>Komplette Web-Oberfläche aus reinem Python-Code, ohne separates Frontend-Framework.</p></div>
        <div class="mini-karte"><h4>SQLite (lokal) / Postgres (Cloud)</h4><p>Eine Datenzugriffsschicht, die automatisch zwischen beiden Datenbanktypen wechselt.</p></div>
        <div class="mini-karte"><h4>Drei-Schichten-Architektur</h4><p>Oberfläche, Geschäftslogik und Datenzugriff strikt getrennt – austauschbar und einzeln testbar.</p></div>
        <div class="mini-karte"><h4>Mehrbenutzerbetrieb</h4><p>WAL-Modus plus anwendungsinterner Lock, mit einem echten Lasttest verifiziert.</p></div>
        <div class="mini-karte"><h4>Papierkorb-Prinzip</h4><p>Löschen wird zweistufig abgesichert und ist wiederherstellbar statt endgültig.</p></div>
        <div class="mini-karte"><h4>Cloud-Deployment</h4><p>GitHub, Neon-Postgres und Streamlit Community Cloud – alle drei kostenlos, aber mit privatem Zugriff.</p></div>
      </div>
    </section>

    <section>
      <h2>Ergebnisse auf einen Blick</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>Vollständige Portierung</strong>jede Funktion des Original-Excel-Systems (Barcode-Vergabe, Materialentnahme, Suche, Export) existiert 1:1 in der neuen Anwendung wieder.</span></li>
        <li><span><strong>Keine Plattformweichen mehr</strong>die durchgängigen Mac/Windows-Verzweigungen des VBA-Codes sind komplett entfallen.</span></li>
        <li><span><strong>Echter Mehrbenutzerbetrieb</strong>WAL-Modus plus Lock, verifiziert mit 100 gleichzeitigen Schreibzugriffen ohne einen einzigen Konflikt.</span></li>
        <li><span><strong>Datensicherheit durch Papierkorb</strong>ein direkter, bewusster Gegenentwurf zum sofortigen, endgültigen Löschen im Original.</span></li>
        <li><span><strong>Von einem Rechner unabhängig</strong>eine privat erreichbare Cloud-Version läuft parallel zum weiterhin aktiven lokalen Mac-Betrieb.</span></li>
        <li><span><strong>86 reale Datensätze</strong>sorgfältig aus handschriftlichen Listen digitalisiert und vom Auftraggeber vor der Übernahme bestätigt.</span></li>
      </ul>
    </section>

    <section>
      <h2>Alle Seiten dieses Projekts</h2>
      <p class="section-intro">Vom Original-System über die Neuentwicklung bis in die Cloud – jede Seite ist auch einzeln über die Leiste oben erreichbar.</p>
      <div class="toc-grid">
{toc_html}      </div>
    </section>

{projekt_nav("../../index.html", "Übersicht", "02-original-system.html", "Das Original-System")}
  </main>
"""

write_page("index.html", "Projekt 3: Cloud-Lagersystem – Überblick", body)
