# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt6 import *

body = seiten_kopf(11, "Prüfung des Zeichnungssatzes &ndash; Funde",
    "Systematische Durchsicht aller 21 Blätter: Gewichtsangaben nachgerechnet, Schriftfelder und "
    "Stücklisten kontrolliert &ndash; mit mehreren belegten Befunden.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>🧮 Gewichtsangaben stichprobenartig nachgerechnet</h2>
      <p>
        Rohr 40×40×3 hat einen Materialquerschnitt von 444 mm² und wiegt rechnerisch
        <strong>3,49 kg/m</strong>. Damit lassen sich die Blattangaben direkt prüfen:
      </p>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Blatt</th><th>Länge</th><th>Rechnerisch</th><th>Zeichnung</th><th>Status</th></tr></thead>
          <tbody>
            <tr><td>6/21</td><td>510 mm</td><td>1,78 kg</td><td>1,78 kg</td><td><span class="st-ok">✅ korrekt</span></td></tr>
            <tr><td>8/21</td><td>550 mm</td><td>1,92 kg</td><td>1,92 kg</td><td><span class="st-ok">✅ korrekt</span></td></tr>
            <tr><td>9/21</td><td>650 mm</td><td>2,27 kg</td><td>2,27 kg</td><td><span class="st-ok">✅ korrekt</span></td></tr>
            <tr><td>1/21</td><td>200 mm</td><td>0,70 kg</td><td>0,09 kg</td><td><span class="st-no">⚠️ Fehler</span></td></tr>
            <tr><td>7/21</td><td>550 mm (mit Bohrungen)</td><td>~1,92 kg</td><td>0,24 kg</td><td><span class="st-no">⚠️ Fehler</span></td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Befund:</strong> Drei von fünf Stichproben stimmen exakt. Blatt 1 und Blatt 7
        weichen dagegen erheblich ab &ndash; Blatt 7 nennt bei derselben Länge wie Blatt 8
        (550 mm) nur 0,24 kg statt 1,92 kg. Beide Werte sind vor der Abgabe zu korrigieren.
      </div>
    </section>

    <section>
      <h2>📝 Weitere Befunde</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>#</th><th>Befund</th><th>Hintergrund / Risiko</th></tr></thead>
          <tbody>
            <tr><td>1</td><td><strong>Schriftfeld „Schweißtisch“</strong></td><td>Alle 21 Blätter tragen im Feld „Project“ die Bezeichnung „Schweißtisch“ &ndash; dargestellt ist jedoch der Schweißwagen. Ohne Korrektur passt die Zeichnungsdokumentation nicht zum Bauteil.</td></tr>
            <tr><td>2</td><td><strong>Gasflaschenaufnahme fehlt</strong></td><td>Anforderung A-02 (hinten fixiert und angekettet) ist im Zeichnungssatz nicht umgesetzt &ndash; keine Flaschenaufnahme in der Stückliste. Das ist die wichtigste offene Sicherheitslücke.</td></tr>
            <tr><td>3</td><td><strong>Position 7 Quelle „Unbekannt“</strong></td><td>Die 6× M20-Schrauben (ISO 4018) sind ohne Bezugsquelle geführt. Für eine vollständige Fertigungsdokumentation muss die Quelle auf „Gekauft“ gesetzt und eine Bestellbezeichnung hinterlegt werden.</td></tr>
            <tr><td>4</td><td><strong>Verschraubung M20 überdimensioniert?</strong></td><td>M20 ist für einen Werkstattwagen dieser Größe sehr kräftig. Bei Profil 40×40 mm nimmt eine Ø20-Bohrung die halbe Profilbreite ein und schwächt den Querschnitt deutlich. Prüfen, ob M10 oder M12 ausreichen &ndash; das spart Material, Bearbeitungszeit und erhält mehr Restquerschnitt.</td></tr>
            <tr><td>5</td><td><strong>Baugruppen mit 0,00 kg</strong></td><td>Blatt 11/21 und 20/21 weisen 0,00 kg aus, obwohl sie 4 bzw. 17 Teile enthalten &ndash; typisches Anzeichen fehlender Werkstoffzuweisung im CAD.</td></tr>
            <tr><td>6</td><td><strong>Datumsdifferenz</strong></td><td>Der Zeichnungssatz ist auf 17.04.2026 datiert, die Konzeptdokumente auf 25.08.2026. Die Zeichnungen sind also älter als die zuletzt dokumentierten Konzeptstände &ndash; zu prüfen, ob sie den aktuellen Stand abbilden.</td></tr>
            <tr><td>7</td><td><strong>Flaschenhöhe uneinheitlich</strong></td><td>Vier Werte in vier Dokumenten: &gt;1800 / 1640 / 1500 / 1150 mm. Vor der Fertigung ist die maßgebende Flaschengröße festzulegen.</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>⚖️ Abgleich mit der früheren Gewichtsabschätzung</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Position</th><th>Frühere Schätzung</th><th>Zeichnungssatz</th><th>Bewertung</th></tr></thead>
          <tbody>
            <tr><td>Rahmen/Konstruktion</td><td>40&ndash;60 kg</td><td>91,05 kg</td><td>deutlich schwerer als geschätzt</td></tr>
            <tr><td>MIG-Maschine</td><td>80&ndash;100 kg</td><td>&mdash;</td><td>kommt hinzu</td></tr>
            <tr><td>Gasflasche 50 L (voll)</td><td>60&ndash;75 kg</td><td>&mdash;</td><td>kommt hinzu</td></tr>
            <tr><td>Werkzeug &amp; Verbrauchsmaterial</td><td>35&ndash;55 kg</td><td>&mdash;</td><td>kommt hinzu</td></tr>
            <tr class="total-row"><td>Gesamt beladen</td><td>≈ 215&ndash;290 kg</td><td>≈ 265&ndash;320 kg</td><td>&rarr; Rollenauswahl anpassen</td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Konsequenz für die Rollen:</strong> Bei bis zu 320 kg Gesamtmasse und 4 Rollen
        ergeben sich rechnerisch 80 kg je Rolle. Da sich die Last beim Fahren und Beladen
        ungleich verteilt, sollten Rollen mit mindestens 150 kg Tragkraft je Stück gewählt
        werden. Die Rolle ist als Zukaufteil 0055761 geführt &ndash; Datenblatt prüfen.
      </div>
    </section>

    <section>
      <h2>❗ Offene Punkte &ndash; Gesamtübersicht</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Prio</th><th>Offener Punkt</th><th>Hintergrund</th></tr></thead>
          <tbody>
            <tr><td><span class="prio prio--hoch">hoch</span></td><td>Gasflaschenaufnahme fehlt</td><td>A-02 nicht umgesetzt &ndash; wichtigste Sicherheitslücke</td></tr>
            <tr><td><span class="prio prio--hoch">hoch</span></td><td>Schriftfeld „Schweißtisch“</td><td>Alle 21 Blätter tragen die falsche Projektbezeichnung</td></tr>
            <tr><td><span class="prio prio--hoch">hoch</span></td><td>Gewichtsangaben Blatt 1 und 7</td><td>0,09 kg statt 0,70 kg bzw. 0,24 kg statt 1,92 kg</td></tr>
            <tr><td><span class="prio prio--mittel">mittel</span></td><td>Flaschenhöhe uneinheitlich</td><td>Vier Werte in vier Dokumenten</td></tr>
            <tr><td><span class="prio prio--mittel">mittel</span></td><td>Position 7 Quelle „Unbekannt“</td><td>M20-Schrauben ohne Bezugsquelle</td></tr>
            <tr><td><span class="prio prio--mittel">mittel</span></td><td>Rollen-Tragkraft</td><td>Beladen ≈265&ndash;320 kg &rarr; ≥150 kg je Rolle erforderlich</td></tr>
            <tr><td><span class="prio prio--mittel">mittel</span></td><td>Verschraubung M20</td><td>Bei Profil 40×40 sehr groß &ndash; M10/M12 prüfen</td></tr>
            <tr><td><span class="prio prio--mittel">mittel</span></td><td>Standsicherheitsnachweis</td><td>Gewicht jetzt bekannt &ndash; Rechnung steht noch aus</td></tr>
            <tr><td><span class="prio prio--mittel">mittel</span></td><td>Anbauteile fehlen</td><td>Haspel, Feuerlöscherhalter, Helm-Haken, klappbare Ablage</td></tr>
            <tr><td><span class="prio prio--niedrig">niedrig</span></td><td>Belegungsplan Lochwand</td><td>Welches Werkzeug an welche Position (5S-Schattenbrett)</td></tr>
            <tr><td><span class="prio prio--niedrig">niedrig</span></td><td>Kostenkalkulation</td><td>Für die technisch-wirtschaftliche Gegenüberstellung</td></tr>
            <tr><td><span class="prio prio--niedrig">niedrig</span></td><td>Datumsdifferenz</td><td>Zeichnungen 17.04.2026, Konzepte 25.08.2026</td></tr>
          </tbody>
        </table>
      </div>
    </section>

{projekt_nav("10-zeichnungssatz.html", "Zeichnungssatz (21 Blätter)", "12-fazit.html", "Fazit & Ausblick")}
  </main>
"""

write_page("11-pruefung-funde.html", "Projekt 6: Prüfung & Funde", body)
