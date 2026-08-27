# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt7 import *

TOC = [
    ("02-aufgabe-rahmen.html", "Aufgabe & Rahmen", "Die Aufgabe in einem Satz, die fünf bewerteten Teilaufgaben A bis E und die Rahmenbedingungen der Werkstatt."),
    ("03-werkzeugbedarf.html", "Werkzeugbedarf", "Der vollständige Werkzeugbedarf in sechs Gruppen: Drehen, Fräsen, Spannen, Messen, Nacharbeit und Hilfsmittel."),
    ("04-kostenliste.html", "Bepreiste Werkzeugliste", "35 Positionen mit Menge und Richtpreis – 4.825 € netto, 5.742 € brutto, aufgeschlüsselt nach Kategorien."),
    ("05-5s-ordnung.html", "5S-Ordnung & Zonen", "Die fünf S konkret am Platz und die Zuordnung jedes Werkzeugs zu Zone A, B oder C nach Nutzungshäufigkeit."),
    ("06-werkbank-masse.html", "Werkbank: Maße & Ergonomie", "Grundmaße der Werkbank mit Begründung und der Normbezug nach DIN EN ISO 14738 und DIN 33402-2."),
    ("07-varianten.html", "4 Bauvarianten", "item-Profil, Stahl-Standard, Systemmodule und Eigenbau – jede in 3D dargestellt und mit Vor- und Nachteilen."),
    ("08-layout-konzepte.html", "4 Layout-Konzepte", "Vier Anordnungen der Werkbank im Raum, das gewählte Konzept 2 in 3D und der maßstäbliche Werkstatt-Grundriss."),
    ("09-nutzwertanalyse.html", "Nutzwertanalyse & Empfehlung", "Sieben gewichtete Kriterien, alle vier Varianten bewertet – mit nachvollziehbarer Rechnung und Empfehlung."),
    ("10-wirtschaftlichkeit.html", "Wirtschaftlichkeit & Amortisation", "Was die Ordnung an Suchzeit spart, gegen die Investition gerechnet – Amortisation je Variante."),
    ("11-arbeitssicherheit.html", "Arbeitssicherheit", "Gefährdungsbeurteilung nach § 5 ArbSchG: zehn Gefährdungen, Maßnahmen nach STOP-Prinzip, Restrisiko."),
    ("12-umsetzung-audit.html", "Umsetzung, Zeitplan & Audit", "Sieben Projektphasen mit Meilensteinen, die 5S-Audit-Checkliste mit 20 Punkten und das Entscheidungsblatt."),
    ("13-fazit-quellen.html", "Fazit, Quellen & Normen", "Was das Konzept leistet, was offen bleibt – und die vollständige Normübersicht mit Kernaussagen."),
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
      <span class="tag tag--zerspan">Zerspanung</span>
      <h1>Projekt 7: Zerspanarbeitsplatz nach 5S</h1>
      <p class="intro">
        Ein kompletter Arbeitsplatz zum konventionellen Drehen und Fräsen &ndash; geplant von der
        Werkzeugaufnahme über vier Bauvarianten und vier Layout-Konzepte bis zur
        Gefährdungsbeurteilung. Die Besonderheit dieses Projekts: Jede Entscheidung ist mit Zahlen
        hinterlegt &ndash; bepreiste Werkzeugliste, gewichtete Nutzwertanalyse und eine
        Amortisationsrechnung, die die eingesparte Suchzeit gegen die Investition stellt.
      </p>
      <div class="meta">
        <span>Houcine Hassine &middot; 08.06. &ndash; 11.09.2026</span>
        <span>Mechanische Werkstätte Schmidt e.K., Essing</span>
        <span>Urlaub: 23.07. &ndash; 21.08.2026</span>
      </div>
      <div class="kennzahlen-grid">
        <div class="kennzahl"><strong>35</strong><span>Werkzeugpositionen</span></div>
        <div class="kennzahl"><strong>5.742</strong><span>€ brutto Werkzeugkosten</span></div>
        <div class="kennzahl"><strong>4</strong><span>Bauvarianten bewertet</span></div>
        <div class="kennzahl"><strong>4</strong><span>Layout-Konzepte</span></div>
        <div class="kennzahl"><strong>10</strong><span>Gefährdungen beurteilt</span></div>
        <div class="kennzahl"><strong>26,5</strong><span>Monate Amortisation</span></div>
      </div>
    </div>
    </header>

    <section>
      <div class="info-box">
        <strong>Ausgangslage:</strong> Drehen und Fräsen konventionell, drei Personen pro Schicht,
        eine Schicht pro Tag, kein festes Budget. Daraus folgt unmittelbar: Handwerkzeug und
        Messmittel teils dreifach beschaffen, die Werkbank aber zentral für alle drei Personen
        auslegen.
      </div>
    </section>

    <section>
      <h2>Vorgehen in 8 Kapiteln</h2>
      <div class="stepper">
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">1</span>
            <span class="schritt-titel">Einführung &ndash; Aufgabe klären</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Die Aufgabe wird in fünf prüfbare Teilaufgaben A bis E zerlegt: Werkzeuge aufnehmen, Werkbank planen, 5S anwenden, Varianten entwerfen, technisch-wirtschaftlich gegenüberstellen. <em>Seite 2.</em></p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">2</span>
            <span class="schritt-titel">Analyse &ndash; Werkzeuge &amp; Kosten</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Vollständiger Werkzeugbedarf in sechs Gruppen, anschließend bepreist: 35 Positionen, 4.825 € netto. <em>Seiten 3&ndash;4.</em></p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">3</span>
            <span class="schritt-titel">5S-Ordnung &amp; Zonen</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Die fünf S konkret angewandt und jedes Werkzeug nach Nutzungshäufigkeit in Zone A (Lochwand, täglich), B (Schubladen, wöchentlich) oder C (Schrank, selten) einsortiert. <em>Seite 5.</em></p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">4</span>
            <span class="schritt-titel">Planung &ndash; Maße, Varianten, Layout</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Grundmaße mit Normbezug, vier Bauvarianten (item-Profil, Stahl, Systemmodule, Eigenbau) und vier Layout-Konzepte &ndash; jeweils in 3D visualisiert. <em>Seiten 6&ndash;8.</em></p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">5</span>
            <span class="schritt-titel">Bewertung &ndash; Nutzwertanalyse</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Sieben gewichtete Kriterien, jede Variante mit 1&ndash;5 Punkten bewertet. Ergebnis: item-Profil 4,15 vor Systemmodule 3,95. <em>Seite 9.</em></p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">6</span>
            <span class="schritt-titel">Wirtschaftlichkeit &ndash; Amortisation</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>10 Minuten gesparte Suchzeit je Person und Tag ergeben 110 Stunden im Jahr. Gegen 9.700 € Investition gerechnet: Amortisation nach 26,5 Monaten. <em>Seite 10.</em></p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">7</span>
            <span class="schritt-titel">Arbeitssicherheit</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Gefährdungsbeurteilung nach § 5 ArbSchG: zehn Gefährdungen, Maßnahmen nach dem STOP-Prinzip, Restrisiko bewertet. <em>Seite 11.</em></p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">8</span>
            <span class="schritt-titel">Umsetzung &amp; Abgabe</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Sieben Projektphasen mit Meilensteinen, 5S-Audit-Checkliste mit 20 erreichbaren Punkten und das finale Entscheidungsblatt. <em>Seiten 12&ndash;13.</em></p></div>
        </div>
      </div>
    </section>

    <section>
      <h2>🎓 Bezug zur Aufgabenstellung der Hochschule</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Teilaufgabe</th><th>Status</th><th>Nachweis</th></tr></thead>
          <tbody>
            <tr><td>A &ndash; Alle Werkzeuge für Zerspanen und Nacharbeit aufnehmen</td><td><span class="st-ok">✅ erfüllt</span></td><td>6 Gruppen, 35 bepreiste Positionen (Seiten 3&ndash;4)</td></tr>
            <tr><td>B &ndash; Werkbank planen (Aufbau, Maße, Schubladen, Lochwand)</td><td><span class="st-ok">✅ erfüllt</span></td><td>Grundmaße mit Normbezug, Konzept 2 in 3D (Seiten 6, 8)</td></tr>
            <tr><td>C &ndash; 5S anwenden (feste Plätze, Shadow-Board, Standards)</td><td><span class="st-ok">✅ erfüllt</span></td><td>5 Schritte + Zonen A/B/C + Audit-Checkliste (Seiten 5, 12)</td></tr>
            <tr><td>D &ndash; Varianten (item-Profil, Stahl, System, Eigenbau)</td><td><span class="st-ok">✅ erfüllt</span></td><td>4 Varianten je in 3D mit Vor-/Nachteilen (Seite 7)</td></tr>
            <tr><td>E &ndash; Technisch-wirtschaftliche Gegenüberstellung + Empfehlung</td><td><span class="st-ok">✅ erfüllt</span></td><td>Nutzwertanalyse + Kostenschätzung + Amortisation (Seiten 9&ndash;10)</td></tr>
            <tr><td>Zusatz &ndash; Gefährdungsbeurteilung</td><td><span class="st-ok">✅ erfüllt</span></td><td>10 Gefährdungen nach STOP-Prinzip (Seite 11)</td></tr>
            <tr><td>Zusatz &ndash; Beschaffung mit realen Angeboten</td><td><span class="st-no">❌ offen</span></td><td>Preise sind Netto-Richtwerte aus Marktrecherche, keine Angebote</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Ehrlich eingeordnet:</strong> Alle fünf gestellten Teilaufgaben sind bearbeitet.
        Was fehlt, ist der Schritt in die Realität &ndash; echte Lieferantenangebote statt
        recherchierter Richtpreise und die tatsächlichen Raummaße statt der im Grundriss
        angenommenen Beispielwerte.
      </div>
    </section>

    <section>
      <h2>Alle Seiten dieses Projekts</h2>
      <div class="toc-grid">
{toc_html}      </div>
    </section>

{projekt_nav("../projekt-6/12-fazit.html", "Projekt 6: Schweißwagen", "02-aufgabe-rahmen.html", "Aufgabe & Rahmen")}
  </main>
"""

write_page("index.html", "Projekt 7: Zerspanarbeitsplatz – Überblick", body)
