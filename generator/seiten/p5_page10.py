# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt5 import *

body = seiten_kopf(10, "Finale Anpassungen &amp; finale Zeichnungen",
    "Der finale, geprüfte Stand vom 17.04.2026: vier Lochplatten in 2×2-Anordnung, fahrbares "
    "Untergestell, 15 Zeichnungsblätter &ndash; und eine systematische Prüfung aller Angaben.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>Oberteil 000-005-106-2 &ndash; finale Version</h2>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Gesamtzusammenbau, Blatt 1/15 &middot; Endstand</span>
          <img src="img/endstand-blatt1-15-17april.jpg" alt="Finale technische Zeichnung des Schweißtischs 000-005-200-1 vom 17.04.2026 mit vier Lenkrollen, vier Lochplatten in 2x2-Anordnung, Schriftfeld mit Gewicht 289,11 kg, geprüft von MW Schmidt" />
          <p class="bildtext">Blatt 1/15, Maßstab 1:15, Werkstoff S235JRH, Gewicht laut Schriftfeld 289,11 kg. Designed by Houcine Hassine, Checked by MW Schmidt, 17.04.2026.</p>
        </div>
      </div>
      <p>
        Deutlicher Unterschied zur Vorversion: Die Platten liegen jetzt in einer 2 × 2 Anordnung
        (statt 3 nebeneinander) &rarr; die Arbeitsfläche wird breiter statt nur länger. Zwei
        innenliegende Längsträger stützen die Plattenstöße in der Mitte.
      </p>
    </section>

    <section>
      <h2>🔄 Der Entwicklungssprung im Oberteil</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Merkmal</th><th>000-005-104-1 (10.04.)</th><th>000-005-106-2 (17.04.)</th><th>Δ</th></tr></thead>
          <tbody>
            <tr><td>Lochplatten</td><td>3</td><td>4</td><td>+1</td></tr>
            <tr><td>Plattenanordnung</td><td>3 in Reihe</td><td>2 × 2</td><td>umgestellt</td></tr>
            <tr><td>Längsträger außen</td><td>2 × 1500</td><td>2 × 1580</td><td>+80 mm</td></tr>
            <tr><td>Querträger</td><td>2 × 500</td><td>2 × 820</td><td>+320 mm</td></tr>
            <tr><td>Längsträger innen</td><td>1 × 1330</td><td>2 × 1420</td><td>+1 Stück</td></tr>
            <tr><td>Gewicht Rahmen</td><td>18,63 kg</td><td>25,61 kg</td><td>+37 %</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        Zusammengefasst: Der Querträger wuchs um 320 mm &ndash; genau der Betrag, der eine zweite
        Plattenreihe ermöglicht. Der Rahmen wurde dafür 37 % schwerer, die nutzbare
        Arbeitsfläche stieg aber von 3 auf 4 Platten (+33 %).
      </div>
    </section>

    <section>
      <h2>📐 Das Zeichnungspaket 000-005-200-1</h2>
      <div class="kennzahlen-grid">
        <div class="kennzahl"><strong>289,11</strong><span>kg Gesamtgewicht (Schriftfeld)</span></div>
        <div class="kennzahl"><strong>40</strong><span>Teile, 12 verschiedene</span></div>
        <div class="kennzahl"><strong>15</strong><span>Blätter, Format A3</span></div>
      </div>
      <p style="margin-top:0.75rem">Werkstoffe: S235JRH (Rohre) &middot; S355MC (Lochplatten). Toleranzen: DIN ISO 2768-mK, Kanten DIN ISO 13715, Oberfläche Rz 6,3.</p>
    </section>

    <section>
      <h2>⚖️ Gewichtsverteilung der Baugruppen</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <tbody>
            <tr><td>Plattenpaket (4× Lochplatte)</td><td>145,88 kg</td></tr>
            <tr><td>Oberer Rahmen</td><td>55,40 kg</td></tr>
            <tr><td>Erweiterungssystem</td><td>50,32 kg</td></tr>
            <tr><td>Untergestell + Rollen</td><td>37,51 kg</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">Die Lochplatten machen rund die Hälfte des Gesamtgewichts aus &ndash; deshalb sind Rollen und ein steifer Rahmen entscheidend.</p>
    </section>

    <section>
      <h2>🗂️ Alle 15 Zeichnungsblätter im Überblick</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Blatt</th><th>Bezeichnung</th><th>Kerninhalt</th></tr></thead>
          <tbody>
            <tr><td>1/15</td><td>Gesamtzusammenbau</td><td>Isometrische Ansichten 1:15 &middot; Positionen 1&ndash;12 &middot; 289,11 kg</td></tr>
            <tr><td>2/15</td><td>Hauptstückliste</td><td>12 verschiedene Teile &middot; 40 Teile gesamt</td></tr>
            <tr><td>3/15</td><td>Oberteil-Baugruppe</td><td>4 Lochplatten + Rahmen 80×80×3 &middot; 10 Teile</td></tr>
            <tr><td>4/15</td><td>Plattenpaket</td><td>4× Lochplatte D16 800×500×12 &middot; S355MC &middot; 145,88 kg</td></tr>
            <tr><td>5/15</td><td>Oberer Rahmen</td><td>Rohre 1580 / 820 / 1420 &middot; Abstand 320 mm &middot; 55,40 kg</td></tr>
            <tr><td>6/15</td><td>Untergestell</td><td>Beine 660 &middot; 4 Rollen &middot; Bleche 145×117 &middot; 37,51 kg</td></tr>
            <tr><td>7/15</td><td>Erweiterungssystem</td><td>Rohre 40×40×3 und 50×50×3 &middot; 13 Teile &middot; 50,32 kg</td></tr>
            <tr><td>8/15</td><td>Auszug-Baugruppe</td><td>Rohr 40×40×3 &middot; Abstände 350 / 80 mm &middot; 14,66 kg</td></tr>
            <tr><td>9/15</td><td>Führungsrohre</td><td>3× Rohr 50×50×3 &ndash; 1580 &middot; Abstand 340 mm &middot; 21,00 kg</td></tr>
            <tr><td>10/15</td><td>Rohr 80×80×3 &ndash; 1580</td><td>6 Bohrungen &middot; Teilung 740/390/40 &middot; 11,45 kg</td></tr>
            <tr><td>11/15</td><td>Rohr 80×80×3 &ndash; 820</td><td>2 Bohrungen &middot; Abstand 360 mm &middot; 5,95 kg</td></tr>
            <tr><td>12/15</td><td>Rohr 80×80×3 &ndash; 1420</td><td>4 Bohrungen &middot; 660/310 mm &middot; 10,30 kg</td></tr>
            <tr><td>13/15</td><td>Rollenblech 145×117×5</td><td>4× Ø11 &middot; Raster 105 × 77,5 mm &middot; 0,65 kg</td></tr>
            <tr><td>14/15</td><td>Rohr 50×50×3 &ndash; 1580</td><td>2 Bohrungen &middot; Abstand 100 mm &middot; 7,00 kg</td></tr>
            <tr><td>15/15</td><td>Rohr 40×40×3 &ndash; 980</td><td>3× Ø12 &middot; Abstand 80 mm &middot; 3,40 kg</td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        Wichtige Änderung gegenüber den früheren Entwürfen: jetzt 4 Lochplatten (statt 3),
        Rohrprofile durchgängig ×3 mm Wandstärke, Beine nur noch 660 mm (Rollen bringen die
        Höhe), Fußblech 145 × 117 × 5 mm. Auf den nächsten beiden Seiten folgt die vollständige
        Prüfung dieser 15 Blätter.
      </div>
    </section>

{projekt_nav("09-gesamtzusammenbau-stueckliste.html", "Gesamtzusammenbau & Stückliste", "11-pruefung-gewichtsfehler.html", "Prüfung: Gewichtsfehler")}
  </main>
"""

write_page("10-finale-anpassungen.html", "Projekt 5: Finale Anpassungen", body)
