# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt6 import *

body = seiten_kopf(3, "Anforderungen (Lastenheft)",
    "Bevor konstruiert wird: was muss der Wagen tragen und was muss er können? 14 nummerierte "
    "Anforderungen A-01 bis A-14 als verbindliche Grundlage.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>1️⃣ Was muss der Wagen tragen?</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Komponente</th><th>Anforderung</th><th>Konstruktive Folge</th></tr></thead>
          <tbody>
            <tr><td>Vorhandene MIG-Maschine</td><td>Maße vom Typenschild zu besorgen</td><td>Bestimmt Ablagefläche &amp; lichte Höhe</td></tr>
            <tr><td>Gasflasche</td><td>&gt; 1,8 m Höhe &ndash; hinten fixiert und angekettet</td><td>Halterung + Kette, Position über Hinterachse</td></tr>
            <tr><td>Schweißbrenner</td><td>inkl. Schlauchpaket, Massekabel/-klemme</td><td>Haspel bzw. Haken erforderlich</td></tr>
          </tbody>
        </table>
      </div>
      <div class="karten-grid-4" style="margin-top:0.75rem">
        <div class="mini-karte"><h4>📦 Schubladeninhalt</h4><p>Draht / Düsen &middot; PSA-Kleinteile &middot; Trenn-/Schleifscheiben.</p></div>
        <div class="mini-karte"><h4>🔨 Handwerkzeuge</h4><p>Drahtbürste, Schlackenhammer, Zange, Anschlagwinkel.</p></div>
        <div class="mini-karte"><h4>🌀 Kabelführung &amp; Fläche</h4><p>Kabel-/Schlauchhaspel, klappbare Stahl-Ablage.</p></div>
        <div class="mini-karte"><h4>🦺 Sicherheit &amp; PSA</h4><p>Helm-Haken, Handschuh-Ablage, Feuerlöscher-Halterung.</p></div>
      </div>
    </section>

    <section>
      <h2>2️⃣ Was muss der Wagen können?</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Fähigkeit</th><th>Anforderung</th><th>Konstruktive Umsetzung</th></tr></thead>
          <tbody>
            <tr><td>🛞 Fahrbar</td><td>4 Lenkrollen, davon 2 mit Feststellbremse</td><td>Rollenaufnahmen im Bodenrahmen, Tragfähigkeit je Rolle prüfen</td></tr>
            <tr><td>⚖️ Kippsicher</td><td>Gasflasche über der Hinterachse, tiefer Schwerpunkt</td><td>Schwere Bauteile unten, Flaschenaufnahme hinten positionieren</td></tr>
            <tr><td>↩️ Wendig &amp; kompakt</td><td>Enge Ecken befahrbar, teils von 2 Personen bewegt</td><td>Grundfläche begrenzen, Griffe an zwei Seiten</td></tr>
            <tr><td>⚡ Sichere Masse/Erdung</td><td>Definierte Masseanbindung, saubere Schlauchführung</td><td>Massekabelhalter + Haspel</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>3️⃣ Getroffene Entscheidungen</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Thema</th><th>Entscheidung</th><th>Begründung / Auswirkung</th></tr></thead>
          <tbody>
            <tr><td>Schubladen</td><td>Fertiger Schubladenblock als Zukaufteil</td><td>Kein Eigenbau nötig &ndash; spart Fertigungszeit; Einbaumaß des Blocks wird zur Rahmenvorgabe</td></tr>
            <tr><td>Schweißverfahren</td><td>Nur MIG/MAG &ndash; kein E-Hand</td><td>Kein Elektrodenhalter/-köcher nötig &rarr; Wagen wird kompakter</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Zwischenstand nach dem Aufmaß:</strong> Die zunächst offenen Maße wurden durch das
        Aufmaß vor Ort (Seite 2) weitgehend geschlossen &ndash; MIG-Maschine 430 × 610 × 520 mm
        gemessen, Gasflasche Ø 220 mm. Offen bleiben das Maschinengewicht (Typenschild) und die
        maßgebende Flaschengröße.
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Wichtiger Klärungspunkt:</strong> Die Anforderung fordert eine Gasflasche &gt; 1,8 m,
        gemessen wurden jedoch 1640 mm. Für die Auslegung der Halterung sollte die größte im
        Betrieb vorkommende Flasche maßgebend sein &ndash; zu klären, ob 50-l-Flaschen
        (ca. 1650&ndash;1800 mm) im Einsatz sind.
      </div>
    </section>

    <section>
      <h2>📋 Anforderungsliste A-01 bis A-14</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Nr.</th><th>Anforderung</th><th>Kategorie</th><th>Status</th></tr></thead>
          <tbody>
            <tr><td>A-01</td><td>Aufnahme einer MIG/MAG-Maschine (430 × 610 × 520 mm)</td><td>Muss</td><td><span class="st-ok">✅ definiert</span></td></tr>
            <tr><td>A-02</td><td>Gasflaschenaufnahme, hinten fixiert und angekettet</td><td>Muss</td><td><span class="st-ok">✅ definiert</span></td></tr>
            <tr><td>A-03</td><td>Aufnahme Schweißbrenner, Schlauchpaket, Massekabel</td><td>Muss</td><td><span class="st-ok">✅ definiert</span></td></tr>
            <tr><td>A-04</td><td>Schubladenblock (Zukauf) für Draht, Düsen, PSA, Scheiben</td><td>Muss</td><td><span class="st-warn">⚠️ Einbaumaß offen</span></td></tr>
            <tr><td>A-05</td><td>Halterung für Bürste, Hammer, Zange, Winkel</td><td>Muss</td><td><span class="st-ok">✅ definiert</span></td></tr>
            <tr><td>A-06</td><td>Kabel-/Schlauchhaspel</td><td>Soll</td><td><span class="st-ok">✅ definiert</span></td></tr>
            <tr><td>A-07</td><td>Klappbare Stahl-Ablage</td><td>Soll</td><td><span class="st-warn">⚠️ Größe offen</span></td></tr>
            <tr><td>A-08</td><td>Helm-Haken, Handschuhablage</td><td>Soll</td><td><span class="st-ok">✅ definiert</span></td></tr>
            <tr><td>A-09</td><td>Feuerlöscher-Halterung</td><td>Muss</td><td><span class="st-warn">⚠️ Löschertyp offen</span></td></tr>
            <tr><td>A-10</td><td>4 Lenkrollen, 2 mit Feststellbremse</td><td>Muss</td><td><span class="st-warn">⚠️ Tragfähigkeit offen</span></td></tr>
            <tr><td>A-11</td><td>Kippsicherheit: tiefer Schwerpunkt, Flasche über Hinterachse</td><td>Muss</td><td><span class="st-ok">✅ definiert</span></td></tr>
            <tr><td>A-12</td><td>Kompakte Bauform für enge Werkstattbereiche</td><td>Muss</td><td><span class="st-warn">⚠️ Maximalmaß offen</span></td></tr>
            <tr><td>A-13</td><td>Sichere Masse/Erdung</td><td>Muss</td><td><span class="st-ok">✅ definiert</span></td></tr>
            <tr><td>A-14</td><td>5S-gerechte Werkzeugordnung (fester Platz je Werkzeug)</td><td>Muss</td><td><span class="st-ok">✅ aus Aufgabenstellung</span></td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Gemeinsame Lücke beider Erstentwürfe:</strong> Die Rollen (A-10) sind in keinem der
        frühen CAD-Modelle konstruiert &ndash; erst der Zusatzwagen (Seite 8) setzt sie erstmals
        konstruktiv um.
      </div>
    </section>

{projekt_nav("02-ist-aufnahme.html", "IST-Aufnahme", "04-ideensammlung.html", "Ideensammlung")}
  </main>
"""

write_page("03-anforderungen.html", "Projekt 6: Anforderungen (Lastenheft)", body)
