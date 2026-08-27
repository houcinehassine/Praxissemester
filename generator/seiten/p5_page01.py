# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt5 import *

TOC = [
    ("02-ideen-sammeln.html", "Ideen sammeln", "Marktrecherche und Inspirationsquellen für Schweißtische, Werkzeugwissen zu Klemmenarten – der Startpunkt am 18.–19. März 2026."),
    ("03-grundkonzept-gewaehlt.html", "Grundkonzept gewählt", "Entscheidung für das Grundkonzept: 1500 × 700 mm mit Lochplatten und seitlichen Auslegern für überlange Werkstücke."),
    ("04-erste-zeichnungen.html", "Erste Zeichnungen", "Vier erste CAD-Zeichnungen: Teilen-Nummern, Lochplatte, Tisch-Obere-Teile, Tisch-Unten-Teile."),
    ("05-lochplatte.html", "Lochplatte auswählen", "Vergleich von vier Marktvarianten, Auswahl D16 · 800 × 500 × 12 mm, und das erkannte Schraubenproblem."),
    ("06-oberteil-unterteil.html", "Oberteil & Unterteil", "Aus dem Grundkonzept werden konkrete Baugruppen: Rahmen 80×80×3, Beine, Adapterplatten – und drei Lösungsmethoden für die Verschraubung."),
    ("07-erweiterung-gesamtzusammenbau.html", "Erweiterung & Gesamtzusammenbau", "Das Teleskop-Erweiterungssystem und wie alle drei Baugruppen zum Gesamtkonzept zusammenfinden."),
    ("08-zeichnungssatz-10-april.html", "Zeichnungssatz 10.04.", "Vollständige Zeichnungssätze mit Stücklisten für jede Baugruppe – der Entwurfsstand vom 10. April."),
    ("09-gesamtzusammenbau-stueckliste.html", "Gesamtzusammenbau & Stückliste", "52 Teile, 32,98 kg, 21 m Rohrbedarf – die komplette Summenstückliste des ersten fertigen Entwurfs."),
    ("10-finale-anpassungen.html", "Finale Anpassungen", "Der Sprung zum Endstand: 4 statt 3 Lochplatten, fahrbares Untergestell, 15 Zeichnungsblätter."),
    ("11-pruefung-gewichtsfehler.html", "Prüfung: Gewichtsfehler", "Wie ein systematischer Gewichtsfehler (Faktor 7,85) in drei Einzelzeichnungen aufgedeckt und bewiesen wurde."),
    ("12-pruefung-weitere-funde.html", "Prüfung: weitere Funde", "Fünf weitere Befunde – von der falsch deklarierten Lenkrolle bis zur veralteten Teilebenennung."),
    ("13-endstand-technische-daten.html", "Endstand & Technische Daten", "Die korrigierte Stückliste, Materialverteilung und die Auslegung der Lenkrollen für das reale Gewicht."),
    ("14-fazit-ausblick.html", "Fazit & Ausblick", "Was diese Konstruktionsprüfung für den Bericht bedeutet – und die Verbindung zu Projekt 4 und 6."),
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
      <h1>Projekt 5: Schweißtisch-Konstruktion</h1>
      <p class="intro">
        Konstruktion eines modularen Schweißarbeitsplatzes: von der ersten Idee im März 2026
        über einen ersten vollständigen Entwurf (52 Teile, 32,98 kg) bis zum geprüften Endstand
        im April (40 Teile, 289 kg dokumentiert / ca. 320 kg real) &ndash; inklusive einer
        vollständigen, selbst durchgeführten Plausibilitätsprüfung aller Zeichnungen und
        Stücklisten.
      </p>
      <div class="meta">
        <span>Houcine Hassine &middot; März &ndash; April 2026</span>
        <span>Bereich: Schweißarbeitsplatz</span>
        <span>Geprüft von: MW Schmidt</span>
      </div>
      <div class="kennzahlen-grid">
        <div class="kennzahl"><strong>1600×1000</strong><span>mm Arbeitsfläche</span></div>
        <div class="kennzahl"><strong>3,1</strong><span>m beidseitig ausziehbar</span></div>
        <div class="kennzahl"><strong>4</strong><span>Lenkrollen, ca. 900 mm Arbeitshöhe</span></div>
        <div class="kennzahl"><strong>~320</strong><span>kg real (40 Teile, 12 verschiedene)</span></div>
        <div class="kennzahl"><strong>5</strong><span>belegte Fehler in der Prüfung gefunden</span></div>
        <div class="kennzahl"><strong>15</strong><span>Zeichnungsblätter im finalen Paket</span></div>
      </div>
    </div>
    </header>

    <section>
      <h2>Die fünf Projektteile</h2>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>💡 1 &middot; Ideen &amp; Grundkonzept</h4><p>Recherche von Vorbildern, Auswahl des Grundkonzepts und erste CAD-Zeichnungen der Tischstruktur.</p></div>
        <div class="mini-karte"><h4>🕳️ 2 &middot; Lochplatte</h4><p>Vergleich von vier Marktvarianten, Auswahl D16 · 800×500×12 mm, CAD-Nachbau und das erkannte Schraubenproblem.</p></div>
        <div class="mini-karte"><h4>🔧 3 &middot; Erste Anpassungen</h4><p>Oberteil, Unterteil und Erweiterungssystem werden erstmals durchkonstruiert.</p></div>
        <div class="mini-karte"><h4>📐 4 &middot; Vollständige Zeichnungen</h4><p>Zum Stand 10.04.2026: vollständige Zeichnungssätze mit Stücklisten &ndash; 52 Teile, 32,98 kg.</p></div>
        <div class="mini-karte"><h4>🏁 5 &middot; Finale Anpassungen</h4><p>Der geprüfte Endstand vom 17.04.2026: 4 Platten, fahrbares Untergestell, 15 Zeichnungsblätter &ndash; und eine systematische Prüfung aller Angaben.</p></div>
      </div>
    </section>

    <section>
      <h2>Der Projektverlauf</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Datum</th><th>Meilenstein</th><th>Inhalt</th></tr></thead>
          <tbody>
            <tr><td>18.&ndash;19. März 2026</td><td>Ideen sammeln &amp; Grundkonzept</td><td>Recherche von Vorbildern, Entscheidung für Lochplatten-Konzept mit Erweiterung</td></tr>
            <tr><td>9. April 2026</td><td>Lochplatte auswählen</td><td>Marktvergleich, Auswahl D16 800×500×12, CAD-Nachbau</td></tr>
            <tr><td>10. April 2026</td><td>Baugruppen konstruieren</td><td>Oberteil, Unterteil und Erweiterungssystem werden durchkonstruiert</td></tr>
            <tr><td>10. April 2026</td><td>Zeichnungssätze erstellen</td><td>Vollständige Zeichnungen und Stücklisten &middot; 52 Teile &middot; 32,98 kg</td></tr>
            <tr><td>17. April 2026</td><td>Überarbeitung &amp; finale Zeichnungen</td><td>4 Platten, Lenkrollen, 15 Blätter &middot; geprüft von MW Schmidt</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>Ergebnis der Konstruktionsprüfung</h2>
      <div class="kennzahlen-grid">
        <div class="kennzahl"><strong>5</strong><span>Belegte Fehler</span></div>
        <div class="kennzahl"><strong>5</strong><span>Dokumentationsmängel</span></div>
        <div class="kennzahl"><strong>1</strong><span>Offene Frage</span></div>
        <div class="kennzahl"><strong>15</strong><span>Geprüfte Blätter</span></div>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        Alle Fehler haben zwei Ursachen: fehlende Werkstoffzuweisung im CAD und nicht
        nachgeführte Teilebenennung nach einer Maßänderung. Details in den Seiten 11&ndash;13.
      </div>
    </section>

    <section>
      <h2>Alle Seiten dieses Projekts</h2>
      <div class="toc-grid">
{toc_html}      </div>
    </section>

{projekt_nav("../projekt-4/13-fazit-quellen.html", "Projekt 4: Fazit", "02-ideen-sammeln.html", "Ideen sammeln")}
  </main>
"""

write_page("index.html", "Projekt 5: Schweißtisch – Überblick", body)
