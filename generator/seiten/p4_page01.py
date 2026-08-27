# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt4 import *

TOC = [
    ("02-grundlagen.html", "Grundlagen", "Schweißverfahren MAG/MIG vs. E-Hand, die 5S-Methode und Item-Profil vs. Stahl-Werkbank – von Grund auf erklärt."),
    ("03-rahmenbedingungen.html", "Rahmenbedingungen", "Der reale Platz in der Halle (5900 × 4000 mm Ecke), die vorhandene Schweißmaschine, Budget und die Grundsatzentscheidung für ein Zwei-Ebenen-Konzept."),
    ("04-werkzeugliste.html", "Werkzeugliste", "Die vollständige, kategorisierte Liste aller Werkzeuge – plus eine bepreiste Kostenschätzung."),
    ("05-konzeptphase-bewertung.html", "Konzeptphase & Bewertung", "Die frühe, formale Nutzwertanalyse mit vier abstrakten Varianten – bevor die konkrete CAD-Lösung feststand."),
    ("06-gesamtplan-layout.html", "Gesamtplan & Layout", "Wie alle Bauteile in der Ecke zusammen angeordnet sind, Ergonomie-Grundmaße und die Arbeitszonen nach 5S."),
    ("07-feste-station-idee-aufbau.html", "Station: Idee & Aufbau", "Warum eine feste Station neben dem mobilen Wagen, und wie sie an den zwei realen Hallenwänden aufgebaut ist."),
    ("08-feste-station-lochwaende-schubladen.html", "Station: Lochwände & Schubladen", "Drei Lochwände und zwei Schubladenschränke im Detail – Inhalt, Platzbedarf, gewählte Produkte."),
    ("09-feste-station-reinigung-psa.html", "Station: Reinigung & PSA", "Die Reinigungsecke und der PSA-Schrank für drei Mitarbeiter."),
    ("10-feste-station-material-zusammenbau.html", "Station: Material & Zusammenbau", "Das Materialregal sowie der finale Zusammenbau mit kompletter Einkaufsliste."),
    ("11-sicherheit.html", "Sicherheit", "Gefährdungsbeurteilung, STOP-Prinzip und die einschlägigen Normen (TRGS 528, DGUV) für den Schweißplatz."),
    ("12-wirtschaftlichkeit-bezugsquellen.html", "Wirtschaftlichkeit & Einkauf", "Amortisationsrechnung und die konkreten Bezugsquellen je Kaufteil in drei Preisstufen."),
    ("13-fazit-quellen.html", "Fazit & Quellen", "Zeitplan, 5S-Audit-Checkliste, Entscheidungsblatt und alle verwendeten Normen."),
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
      <span class="tag tag--schweiss">Schweißarbeitsplatz</span>
      <h1>Projekt 4: Schweißarbeitsplatz nach 5S</h1>
      <p class="intro">
        Einen Schweißarbeitsplatz von Grund auf durchdenken und planen: welche
        Werkzeuge ein Schweißer wirklich braucht, wie der Arbeitsplatz aufgebaut
        ist, und das Ganze ordentlich und effizient nach der 5S-Methode. Diese
        Seite ist die Klammer um das gesamte Vorhaben – die konkrete
        CAD-Konstruktion des Schweißtisches und des Maschinenwagens sind als
        eigene Projekte (5 und 6) ausgearbeitet.
      </p>
      <div class="meta">
        <span>Verfahren: E-Hand &amp; MAG/MIG</span>
        <span>Bereich: Schweißarbeitsplatz</span>
        <span>Methode: 5S · Nutzwertanalyse</span>
      </div>
      <div class="kennzahlen-grid">
        <div class="kennzahl"><strong>3</strong><span>Mitarbeiter am Platz</span></div>
        <div class="kennzahl"><strong>2</strong><span>Ebenen: feste Station + Wagen</span></div>
        <div class="kennzahl"><strong>29</strong><span>m² verfügbare Fläche</span></div>
        <div class="kennzahl"><strong>9</strong><span>Werkzeug-Kategorien A&ndash;I</span></div>
        <div class="kennzahl"><strong>3</strong><span>Layout-Konzepte geprüft</span></div>
        <div class="kennzahl"><strong>13</strong><span>Seiten dieser Dokumentation</span></div>
      </div>
    </div>
    </header>

    <section>
      <h2>Das Projekt in einem Satz</h2>
      <div class="zitat-box">
        Du sollst einen Arbeitsplatz zum Schweißen von Grund auf durchdenken
        und planen: welche Werkzeuge ein Schweißer dort braucht, wie der
        Tisch (die Werkbank) aussieht, und das Ganze ordentlich und effizient
        (nach der 5S-Methode).
        <span class="quelle">Ohne Fachchinesisch erklärt &ndash; Auftrag des Arbeitgebers</span>
      </div>
    </section>

    <section>
      <h2>Die Aufgabe entschlüsselt</h2>
      <p class="section-intro">Links steht, was der Arbeitgeber geschrieben hat &ndash; rechts, was das konkret bedeutet.</p>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Auftrag</th><th>Bedeutung</th></tr></thead>
          <tbody>
            <tr><td>Konzept &amp; Planung von Schweißarbeitsplätzen</td><td>Überlege dir den kompletten Arbeitsplatz und halte ihn planbar fest &ndash; die Oberaufgabe, alles andere zahlt darauf ein.</td></tr>
            <tr><td>Aufnahme aller nötigen Werkzeuge</td><td>Liste jedes Werkzeug/Gerät auf, das man zum Schweißen wirklich braucht &ndash; vom Schweißgerät bis zur Drahtbürste.</td></tr>
            <tr><td>Planung einer Werkbank</td><td>Entwirf den Arbeitstisch: Maße, Aufbau, wo was liegt &ndash; das Herzstück des Arbeitsplatzes.</td></tr>
            <tr><td>Augenmerk auf 5S-Methode</td><td>Alles hat einen festen, sauberen, sinnvollen Platz &ndash; das Ordnungssystem aus der Lean-Produktion.</td></tr>
            <tr><td>Werkzeuge für Schweiß- &amp; Nachbearbeitungsaufgaben</td><td>Nicht nur schweißen &ndash; auch schleifen, bürsten, prüfen, reinigen. Der ganze Arbeitsablauf muss abgedeckt sein.</td></tr>
            <tr><td>2 Varianten: Item-Profil &amp; normale Werkbank</td><td>Ursprünglich gefordert. Umgesetzt wurde eine Kaufteil-/Stahl-Lösung &ndash; Item wurde nach Abstimmung mit dem Arbeitgeber nicht gebaut.</td></tr>
            <tr><td>Technisch-wirtschaftliche Gegenüberstellung</td><td>Was kann jede Variante, was kostet sie, welche ist wann besser &ndash; mit Empfehlung am Schluss.</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>Der Fahrplan &ndash; 8 Schritte</h2>
      <p class="section-intro">Aus der ursprünglichen Planung; in dieser Dokumentation auf 13 Seiten plus die zwei Detailprojekte 5 und 6 ausgearbeitet.</p>
      <div class="stepper">
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">1</span>
            <span class="schritt-titel">Überblick &amp; Fahrplan</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Verstehen, was verlangt wird, und die Reihenfolge festlegen.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">2</span>
            <span class="schritt-titel">Grundlagen verstehen</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Schweißverfahren (E-Hand, MAG/MIG), 5S-Methode und das Item-Profil-System &ndash; von Grund auf.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">3</span>
            <span class="schritt-titel">Werkzeuge erfassen</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Komplette Liste: Schweißen, Nachbearbeitung, Schutz/Sicherheit, Hilfsmittel.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">4</span>
            <span class="schritt-titel">Werkbank planen</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Maße, Arbeitszonen, Anordnung nach 5S &ndash; das Grundlayout des Tisches.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">5</span>
            <span class="schritt-titel">Schweißtisch (Detail)</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Die CAD-Konstruktion: Maße, Platte, Rollen, Stückliste &ndash; ausgearbeitet in <a href="../projekt-5/index.html">Projekt 5</a>.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">6</span>
            <span class="schritt-titel">Feste Station (Detail)</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Lochwände + Schränke (Kaufteile), 5S-Verteilung &ndash; Seiten 7&ndash;10 dieser Dokumentation.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">7</span>
            <span class="schritt-titel">Wagen (Detail)</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Stahl-Wagen: Maschine, Gas, Werkzeuge, fahrbar &ndash; ausgearbeitet in <a href="../projekt-6/index.html">Projekt 6</a>.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">8</span>
            <span class="schritt-titel">Bericht &amp; Zeichnung</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Alles zur Abgabe zusammenstellen: Dokument + Skizze/Plan &ndash; Sicherheit, Wirtschaftlichkeit und Quellen auf den Seiten 11&ndash;13.</p></div>
        </div>
      </div>
    </section>

    <section>
      <h2>Zwei Planungsebenen in dieser Dokumentation</h2>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>Konzeptphase (Seite 5)</h4><p>Eine frühe, formale Nutzwertanalyse mit vier abstrakten Varianten (A&ndash;D) und drei Layout-Konzepten &ndash; die methodische Bewertungsgrundlage.</p></div>
        <div class="mini-karte"><h4>Reale Umsetzung (ab Seite 6)</h4><p>Die konkrete, mit echten Hallenmaßen und Fotos abgestimmte Lösung: Stahltisch (Projekt 5) + Kaufteile-Station + Stahlwagen (Projekt 6).</p></div>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Warum beide Ebenen gezeigt werden:</strong> Die formale Bewertung (Seite 5) war der erste,
        noch allgemeine Schritt der Planung. Die tatsächliche Entscheidung fiel danach auf Basis der
        echten Rahmenbedingungen (Seite 3) &ndash; teils anders, als die abstrakte Nutzwertanalyse es
        nahelegte. Beide Stufen gehören zum echten Planungsprozess und werden deshalb nicht
        „glattgezogen&ldquo;, sondern nachvollziehbar nacheinander dokumentiert.
      </div>
    </section>

    <section>
      <h2>Alle Seiten dieses Projekts</h2>
      <div class="toc-grid">
{toc_html}      </div>
    </section>

{projekt_nav("../../index.html", "Übersicht", "02-grundlagen.html", "Grundlagen")}
  </main>
"""

write_page("index.html", "Projekt 4: Schweißarbeitsplatz nach 5S – Überblick", body)
