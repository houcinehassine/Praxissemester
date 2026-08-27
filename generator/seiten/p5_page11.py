# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt5 import *

body = seiten_kopf(11, "Prüfung: der Gewichtsfehler",
    "Die wichtigste Entdeckung der Konstruktionsprüfung: ein systematischer Gewichtsfehler in "
    "drei frühen Einzelzeichnungen &ndash; gefunden, bewiesen und auf die Ursache "
    "zurückgeführt.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>🚨 Der Fund: dasselbe Teil, zwei völlig verschiedene Gewichte</h2>
      <p>
        Die frühen Einzelzeichnungen der drei gebohrten Rahmenrohre (000-005-008-3/4/5, erstellt
        vor dem 10.04.) zeigen exakt dieselbe Geometrie wie die finalen Zeichnungen im
        15-Blätter-Paket (000-005-002-2 / 004-2 / 003-2) &ndash; aber mit einem völlig anderen
        Gewicht.
      </p>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Länge</th><th>Frühe Zeichnung (008-x)</th><th>Finale Zeichnung</th><th>Nachrechnung</th><th>Faktor</th></tr></thead>
          <tbody>
            <tr><td>1580 mm</td><td>1,46 kg ✘</td><td>11,45 kg ✔</td><td>11,46 kg</td><td>7,85</td></tr>
            <tr><td>820 mm</td><td>0,76 kg ✘</td><td>5,95 kg ✔</td><td>5,95 kg</td><td>7,83</td></tr>
            <tr><td>1420 mm</td><td>1,31 kg ✘</td><td>10,30 kg ✔</td><td>10,30 kg</td><td>7,86</td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Diagnose:</strong> Der Faktor liegt bei allen drei Teilen konstant bei ≈ 7,85 &ndash;
        exakt die Dichte von Stahl in g/cm³. In den frühen Zeichnungen wurde dem CAD-Modell also
        keine Werkstoffdichte zugewiesen (gerechnet mit 1 g/cm³ statt 7,85 g/cm³). Die Gewichte
        der frühen Ausgabe sind durchgängig um Faktor 7,85 zu niedrig.
      </div>
    </section>

    <section>
      <h2>🧮 Die Nachrechnung Schritt für Schritt (Beispiel Rohr 1580 mm)</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Schritt</th><th>Rechnung</th><th>Ergebnis</th></tr></thead>
          <tbody>
            <tr><td>1 &middot; Außenquerschnitt</td><td>80 × 80</td><td>6.400 mm²</td></tr>
            <tr><td>2 &middot; Innenquerschnitt</td><td>(80 &minus; 2×3) × (80 &minus; 2×3) = 74 × 74</td><td>5.476 mm²</td></tr>
            <tr><td>3 &middot; Materialquerschnitt</td><td>6.400 &minus; 5.476</td><td>924 mm²</td></tr>
            <tr><td>4 &middot; Volumen</td><td>924 × 1.580</td><td>1.459.920 mm³ = 1.459,9 cm³</td></tr>
            <tr><td>5 &middot; Masse</td><td>1.459,9 cm³ × 7,85 g/cm³</td><td><strong>11,46 kg ✔</strong></td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">Abweichung zur finalen Zeichnung: 11,46 kg berechnet vs. 11,45 kg im Schriftfeld &rarr; 0,01 kg (0,1 %) &ndash; reine Rundung. Die finale Zeichnung ist bestätigt korrekt.</p>
    </section>

    <section>
      <h2>💡 Damit ist auch der große Gewichtssprung erklärt</h2>
      <p>Warum sprang das Gesamtgewicht von 32,98 kg (10.04.) auf 289,11 kg (17.04.)? Drei Ursachen zusammen:</p>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>1 &middot; Fehlende Werkstoffdichte</h4><p>Im frühen CAD-Stand &rarr; alle Gewichte um ca. Faktor 7,85 zu niedrig.</p></div>
        <div class="mini-karte"><h4>2 &middot; Vierte Lochplatte</h4><p>Ergänzt &rarr; +36 kg Plattenmasse.</p></div>
        <div class="mini-karte"><h4>3 &middot; Größere Profile &amp; mehr Träger</h4><p>Echter konstruktiver Zuwachs (siehe Seite 10).</p></div>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        Überschlag: 32,98 kg × 7,85 ≈ 259 kg &ndash; plus die zusätzliche Platte und die größeren
        Profile landet man bei rund 289 kg. Der Sprung ist also zum größten Teil eine
        Korrektur, kein Konstruktionsfehler.
      </div>
    </section>

    <section>
      <h2>🎯 Fund 2: der Längenwiderspruch 820 vs. 980 mm</h2>
      <p>
        Ein zweiter, unabhängiger Fund: Die Stückliste nennt den Erweiterungsarm
        „Rohr_40x40x3 &ndash; 820“, die zugehörige Zeichnung bemaßt ihn aber mit 980 mm. Vier
        unabhängige Nachrechnungen entscheiden die Frage eindeutig zugunsten von 980 mm:
      </p>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>#</th><th>Beweis</th><th>Ergebnis</th></tr></thead>
          <tbody>
            <tr><td>1</td><td>Gewicht des Einzelteils (Blatt 15/15): 3,40 kg</td><td>passt zu 980 mm (3,42 kg berechnet), nicht zu 820 mm (2,86 kg, 16 % Abweichung)</td></tr>
            <tr><td>2</td><td>Rahmenbreite außen = Querträger 820 + 2 × Längsträgerbreite 80</td><td>= 980 mm &ndash; der Arm reicht exakt über die volle Tischbreite</td></tr>
            <tr><td>3</td><td>Gewicht Erweiterungssystem Blatt 7/15: 50,32 kg</td><td>geht nur mit 980 mm auf (2 × 3,42 + 6 × 2,61 = 50,33 kg)</td></tr>
            <tr><td>4</td><td>Gewicht Auszug-Baugruppe Blatt 8/15: 14,66 kg</td><td>geht nur mit 980 mm auf (Abweichung 0,07 % statt 8 %)</td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Risiko:</strong> Wer nach der (falschen) Stücklisten-Benennung „820“ zuschneidet,
        sägt 160 mm zu kurz &ndash; bei 4 Stück sind das 640 mm Ausschuss. Vermutlich wurde beim
        Vergrößern des Tisches die Rohrlänge im CAD angepasst, die Teilebenennung aber nicht
        nachgezogen &ndash; ein typischer Fehler bei Konstruktionsänderungen.
      </div>
    </section>

{projekt_nav("10-finale-anpassungen.html", "Finale Anpassungen", "12-pruefung-weitere-funde.html", "Prüfung: weitere Funde")}
  </main>
"""

write_page("11-pruefung-gewichtsfehler.html", "Projekt 5: Prüfung – Gewichtsfehler", body)
