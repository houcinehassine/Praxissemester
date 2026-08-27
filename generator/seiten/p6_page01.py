# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt6 import *

TOC = [
    ("02-ist-aufnahme.html", "IST-Aufnahme", "Der vorhandene Wagen im Betrieb: Fotos, Aufmaß vor Ort (Gerät 610×430×520, Flasche Ø220×1640) und CAD-Vereinfachung als Bauraum-Platzhalter."),
    ("03-anforderungen.html", "Anforderungen (Lastenheft)", "14 nummerierte Anforderungen A-01 bis A-14: was der Wagen tragen und was er können muss."),
    ("04-ideensammlung.html", "Ideensammlung", "Vier Referenzprojekte und fünf Designrichtungen als Ausgangspunkt der Lösungssuche."),
    ("05-grundkonzept.html", "Grundkonzept: Idee 1 & 2", "Zwei erste CAD-Entwürfe im direkten Vergleich – Kompaktrahmen gegen Werkstattwagen mit Lochblech."),
    ("06-masse-ergonomie.html", "Maße & Ergonomie", "Startwerte für Grundfläche und Höhen, das Auszugskonzept – und der aufgedeckte Maßwiderspruch zum realen Aufmaß."),
    ("07-variante-a-neubau.html", "Variante A: Neubau SW-001", "Der komplette Neubau mit bemaßter Zeichnung, Belegungsplan mit 16 Positionen – und dem entscheidenden Maßkonflikt beim Gerätefach."),
    ("08-variante-b-zusatzwagen.html", "Variante B: Zusatzwagen", "Der Konzeptwechsel: ein Portalgestell über den Bestandswagen, in zwei Versionen entwickelt."),
    ("09-gewaehltes-konzept.html", "Gewähltes Konzept", "Die Vorzugsvariante: modularer 4-Etagen-Aufbau mit Wiederholteilen und parametrischer Lochwand."),
    ("10-zeichnungssatz.html", "Zeichnungssatz (21 Blätter)", "Fertigungsreif dokumentiert: 58 Teile, 91,05 kg, Werkstoff S235JRH – mit vollständiger Stückliste und Baugruppenstruktur."),
    ("11-pruefung-funde.html", "Prüfung & Funde", "Systematische Durchsicht des Zeichnungssatzes: Gewichtsfehler, falsches Schriftfeld, fehlende Gasflaschenaufnahme und weitere offene Punkte."),
    ("12-fazit.html", "Fazit & Ausblick", "Erfüllungsgrad gegenüber Lastenheft und Hochschul-Aufgabenstellung, offene Punkte und nächste Schritte."),
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
      <h1>Projekt 6: Schweißmaschinenwagen</h1>
      <p class="intro">
        Ein mobiler Wagen, der Maschine, Gas und die wichtigsten Werkzeuge zum Werkstück bringt.
        Diese Dokumentation folgt dem <strong>logischen Konstruktionsablauf</strong> &ndash; nicht
        der Dateireihenfolge: Aufgabe klären &rarr; Konzipieren &rarr; Entwerfen &rarr;
        Konzeptentscheidung &rarr; Ausarbeiten. Vom Aufmaß des Bestandswagens über sechs
        Entwicklungsstufen bis zum fertigungsreifen Zeichnungssatz mit 21 Blättern.
      </p>
      <div class="meta">
        <span>Houcine Hassine &middot; 02.03. &ndash; 31.07.2026</span>
        <span>Mechanische Werkstätte Schmidt e.K., Essing</span>
        <span>Geprüft: MW Schmidt</span>
      </div>
      <div class="kennzahlen-grid">
        <div class="kennzahl"><strong>91,05</strong><span>kg Gesamtgewicht</span></div>
        <div class="kennzahl"><strong>58</strong><span>Teile, 15 verschiedene</span></div>
        <div class="kennzahl"><strong>21</strong><span>Zeichnungsblätter A3</span></div>
        <div class="kennzahl"><strong>14</strong><span>Anforderungen A-01 bis A-14</span></div>
        <div class="kennzahl"><strong>6</strong><span>Entwicklungsstufen</span></div>
        <div class="kennzahl"><strong>4</strong><span>Etagen im Endkonzept</span></div>
      </div>
    </div>
    </header>

    <section>
      <div class="info-box">
        Zu dieser Fassung: Die Dokumentation ist nach dem logischen Konstruktionsablauf geordnet
        &ndash; nicht nach Dateinamen, Nummerierung oder Eingangsdatum. Die Gliederung folgt dem
        methodischen Vorgehen der Produktentwicklung.
      </div>
    </section>

    <section>
      <h2>Arbeitsablauf in 5 Phasen</h2>
      <div class="stepper">
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">1</span>
            <span class="schritt-titel">Aufgabe klären</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Was ist vorhanden? Was wird gebraucht? &ndash; IST-Aufnahme des vorhandenen Wagens (Fotos, Aufmaß, CAD-Vereinfachung) und das Lastenheft mit 14 nummerierten Anforderungen. <em>Seiten 2&ndash;3.</em></p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">2</span>
            <span class="schritt-titel">Konzipieren</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Lösungssuche &ndash; Recherche (4 Referenzprojekte, 5 Designrichtungen), erste Entwürfe Idee 1 und Idee 2, Original-CAD mit Bemaßung 700 / 1100 / 1500 / 1450 mm. <em>Seiten 4&ndash;5.</em></p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">3</span>
            <span class="schritt-titel">Entwerfen</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Gestaltung &ndash; Maße &amp; Ergonomie festlegen, dann zwei konkurrierende Varianten durchkonstruieren: Variante A (kompletter Neubau SW-001) und Variante B (Zusatzwagen als Portalgestell). <em>Seiten 6&ndash;8.</em></p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">4</span>
            <span class="schritt-titel">Konzeptentscheidung</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Festlegung der Vorzugsvariante und ihres modularen Aufbaus: 4-Etagen-Konzept &ndash; Etage 1 Maschine, Etage 2+3 Schubladen, Etage 4 Deckel + Lochwand. <em>Seite 9.</em></p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">5</span>
            <span class="schritt-titel">Ausarbeiten</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Fertigungsunterlagen &ndash; Einzelteile, Baugruppen, Stücklisten: 21 Blätter A3, 58 Teile, 91,05 kg, Werkstoff S235JRH. <em>Seiten 10&ndash;11.</em></p></div>
        </div>
      </div>
    </section>

    <section>
      <h2>📈 Entwicklung der Lösung</h2>
      <p class="section-intro">Sechs Stufen &ndash; jede mit einem konkreten Grund für die Weiterentwicklung.</p>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Stufe</th><th>Ansatz</th><th>Warum weiterentwickelt?</th></tr></thead>
          <tbody>
            <tr><td>Idee 1</td><td>Schlanker Kompaktrahmen mit Lamellenwand</td><td>Kippgefährdet, nur 1 Flasche, zu wenig Ablagefläche</td></tr>
            <tr><td>Idee 2</td><td>Werkstattwagen mit Lochblech, 3 Ebenen</td><td>Grundrichtung gut &ndash; Länge 1450 mm zu groß</td></tr>
            <tr><td>SW-001</td><td>Kompletter Neubau mit Gerätefach</td><td>Gerätefach 430 mm zu niedrig für 520 mm hohe Maschine</td></tr>
            <tr><td>Zusatzwagen V1</td><td>Portal über den Bestandswagen</td><td>Maßkonflikt gelöst &ndash; Flasche stand außerhalb</td></tr>
            <tr><td>Zusatzwagen V2</td><td>Kompakteres Portal</td><td>Flasche innerhalb der Aufstandsfläche</td></tr>
            <tr><td><strong>4-Etagen-Konzept</strong></td><td><strong>Gewählte Lösung</strong></td><td>Modular, Wiederholteile, parametrische Lochwand</td></tr>
            <tr><td>Zeichnungssatz</td><td>Fertigungsreif</td><td>Stahl S235JRH, verschraubt, 91,05 kg</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>🎓 Bezug zur Aufgabenstellung der Hochschule</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Vorgabe aus der Aufgabenstellung</th><th>Status</th><th>Nachweis</th></tr></thead>
          <tbody>
            <tr><td>Aufnahme aller nötigen Werkzeuge für einen Schweißarbeitsplatz</td><td><span class="st-ok">✅ erfüllt</span></td><td>Belegungsplan mit 16 Positionen (Seite 7)</td></tr>
            <tr><td>Planung einer Werkbank</td><td><span class="st-ok">✅ erfüllt</span></td><td>Zeichnungssatz 21 Blätter (Seite 10)</td></tr>
            <tr><td>Augenmerk auf 5S-Methode</td><td><span class="st-ok">✅ erfüllt</span></td><td>Fester Platz je Werkzeug, Lochwand, Schubladen</td></tr>
            <tr><td>Werkzeuge für Schweiß- und Nachbearbeitungsaufgaben</td><td><span class="st-warn">⚠️ teilweise</span></td><td>Schleifer und Bürste vorgesehen, Halterungen fehlen</td></tr>
            <tr><td>2 Varianten: Item-Profile und normale Werkbank</td><td><span class="st-warn">⚠️ teilweise</span></td><td>Beide konstruiert &ndash; Stahl ausgeführt, Alu-Variante nicht bemaßt</td></tr>
            <tr><td>Technisch-wirtschaftliche Gegenüberstellung</td><td><span class="st-no">❌ offen</span></td><td>Technischer Vergleich liegt vor, Kosten fehlen</td></tr>
            <tr><td>Erstellen von Arbeitsanweisungen</td><td><span class="st-no">❌ offen</span></td><td>Noch nicht dokumentiert</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        Für die verbleibende Zeit: Die beiden wichtigsten Lücken gegenüber der Aufgabenstellung
        sind die Kostenkalkulation (für die geforderte Gegenüberstellung) und die
        Arbeitsanweisung. Beides lässt sich mit den vorhandenen Unterlagen gut erstellen &ndash;
        Stückliste und Fotos sind bereits da.
      </div>
    </section>

    <section>
      <h2>Alle Seiten dieses Projekts</h2>
      <div class="toc-grid">
{toc_html}      </div>
    </section>

{projekt_nav("../projekt-5/14-fazit-ausblick.html", "Projekt 5: Schweißtisch", "02-ist-aufnahme.html", "IST-Aufnahme")}
  </main>
"""

write_page("index.html", "Projekt 6: Schweißmaschinenwagen – Überblick", body)
