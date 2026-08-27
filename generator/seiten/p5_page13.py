# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt5 import *

body = seiten_kopf(13, "Endstand &amp; Technische Daten",
    "Die korrigierte Stückliste, Materialverteilung und die Auslegung der Lenkrollen für das "
    "reale Gewicht des fertigen Schweißtischs.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>🏆 Das fertige Produkt in Zahlen</h2>
      <div class="kennzahlen-grid">
        <div class="kennzahl"><strong>1600×1000</strong><span>mm Arbeitsfläche &middot; 4 Lochplatten 2×2</span></div>
        <div class="kennzahl"><strong>~900</strong><span>mm Arbeitshöhe</span></div>
        <div class="kennzahl"><strong>~3,1</strong><span>m beidseitig ausziehbar</span></div>
        <div class="kennzahl"><strong>~320</strong><span>kg real (289 kg dokumentiert)</span></div>
      </div>
    </section>

    <section>
      <h2>✅ Korrigierte Hauptstückliste</h2>
      <p class="section-intro">Zusammenführung aller Erkenntnisse der Prüfung &ndash; drei Korrekturen markiert mit ✎.</p>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Pos.</th><th>Menge</th><th>Teilenummer</th><th>Benennung</th><th>Quelle</th><th>Gewicht ges.</th></tr></thead>
          <tbody>
            <tr><td>1</td><td>4</td><td>000-005-010-1</td><td>Lochplatte D16 &ndash; 800×500×12</td><td>Gekauft</td><td>145,88 kg</td></tr>
            <tr><td>2</td><td>2</td><td>000-005-002-2</td><td>Rohr 80×80×3 &ndash; 1580 &ndash; 6×10</td><td>Hergestellt</td><td>22,90 kg</td></tr>
            <tr><td>3</td><td>2</td><td>000-005-004-2</td><td>Rohr 80×80×3 &ndash; 820 &ndash; 2×10</td><td>Hergestellt</td><td>11,90 kg</td></tr>
            <tr><td>4</td><td>2</td><td>000-005-003-2</td><td>Rohr 80×80×3 &ndash; 1420 &ndash; 4×10</td><td>Hergestellt</td><td>20,60 kg</td></tr>
            <tr><td>5</td><td>3</td><td>000-005-003-1</td><td>Rohr 80×80×3 &ndash; 1420</td><td>Hergestellt</td><td>30,90 kg</td></tr>
            <tr><td>6</td><td>2</td><td>000-005-004-1</td><td>Rohr 80×80×3 &ndash; 820</td><td>Hergestellt</td><td>11,90 kg</td></tr>
            <tr><td>7</td><td>4</td><td>000-005-005-1</td><td>Rohr 80×80×3 &ndash; 660</td><td>Hergestellt</td><td>19,15 kg</td></tr>
            <tr><td>8</td><td>4</td><td>0055761</td><td>Lenkrolle</td><td>Gekauft ✎</td><td>ca. 3,9 kg</td></tr>
            <tr><td>9</td><td>4</td><td>000-005-011-1</td><td>Blech 145 × 117,5 × 5</td><td>Hergestellt</td><td>2,60 kg</td></tr>
            <tr><td>10</td><td>4</td><td>000-005-008-1</td><td>Rohr 40×40×3 &ndash; 980 ✎ &ndash; 3×12</td><td>Hergestellt</td><td>13,66 kg</td></tr>
            <tr><td>11</td><td>6</td><td>000-005-006-1</td><td>Rohr 40×40×3 &ndash; 750 ✎</td><td>Hergestellt</td><td>15,68 kg</td></tr>
            <tr><td>12</td><td>3</td><td>000-005-009-1</td><td>Rohr 50×50×3 &ndash; 1580 &ndash; 2×12</td><td>Hergestellt</td><td>20,99 kg</td></tr>
            <tr class="total-row"><td colspan="5">Summe &middot; 40 Teile</td><td>ca. 320 kg</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        Drei Korrekturen: Pos. 8 Quelle &rarr; Gekauft &middot; Pos. 10 Länge &rarr; 980 mm &middot;
        Pos. 11 Länge ergänzt &rarr; 750 mm. Korrigiertes Gesamtgewicht: ca. 320 kg statt der
        ausgewiesenen 289,11 kg &ndash; die Differenz stammt aus den drei Streben Pos. 5 (Fund 4).
      </div>
    </section>

    <section>
      <h2>🏭 Make-or-Buy nach Korrektur</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Kategorie</th><th>Teile</th><th>Gewicht</th><th>Anteil</th></tr></thead>
          <tbody>
            <tr><td>Zukauf (4 Platten + 4 Rollen)</td><td>8</td><td>ca. 150 kg</td><td>47 %</td></tr>
            <tr><td>Eigenfertigung (Rohre + Bleche)</td><td>32</td><td>ca. 170 kg</td><td>53 %</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">
        Für die wirtschaftliche Bewertung: Zwar sind nur 8 von 40 Teilen Zukauf, diese machen aber
        fast die Hälfte des Gewichts und mit hoher Wahrscheinlichkeit den größten Kostenanteil aus
        (Lochplatten S355MC mit Lochbild + Schwerlastrollen). Die 32 Eigenfertigungsteile sind
        einfache Ablängteile mit Bohrungen aus nur 3 Profilgrößen &ndash; fertigungstechnisch
        unkritisch.
      </p>
    </section>

    <section>
      <h2>⚠️ Auslegung der Lenkrollen</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <tbody>
            <tr><td>Gesamtgewicht Tisch (korrigiert)</td><td>~320 kg</td></tr>
            <tr><td>Anzahl Rollen</td><td>4</td></tr>
            <tr><td>Last je Rolle (statisch, leer)</td><td>~80 kg</td></tr>
            <tr><td>Last je Rolle bei 200 kg Zuladung</td><td>~130 kg</td></tr>
            <tr><td>Empfehlung je Rolle</td><td>mind. 150&ndash;200 kg Tragkraft, Sicherheitsfaktor 2</td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        Auf einem Schweißtisch liegen regelmäßig schwere Werkstücke. Rollen mit 150&ndash;200 kg
        Tragkraft je Stück sind daher sinnvoll bis notwendig. Außerdem sollten mindestens 2
        Rollen feststellbar sein &ndash; sonst wandert der Tisch beim Arbeiten.
      </div>
    </section>

    <section>
      <h2>Prüfstand aller 7 Baugruppen des Endstands</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Baugruppe</th><th>Blatt</th><th>Angabe</th><th>Nachrechnung</th><th>Status</th></tr></thead>
          <tbody>
            <tr><td>Oberteil-BG</td><td>3/15</td><td>0,00 kg</td><td>201,28 kg</td><td><span class="st-no">✘ Fund 3</span></td></tr>
            <tr><td>Plattenpaket</td><td>4/15</td><td>145,88 kg</td><td>145,88 kg</td><td><span class="st-ok">✔</span></td></tr>
            <tr><td>Oberer Rahmen</td><td>5/15</td><td>55,40 kg</td><td>55,40 kg</td><td><span class="st-ok">✔</span></td></tr>
            <tr><td>Untergestell</td><td>6/15</td><td>37,51 kg</td><td>ca. 68 kg</td><td><span class="st-no">✘ Fund 4</span></td></tr>
            <tr><td>Erweiterungssystem</td><td>7/15</td><td>50,32 kg</td><td>50,32 kg</td><td><span class="st-ok">✔</span></td></tr>
            <tr><td>Auszug-BG</td><td>8/15</td><td>14,66 kg</td><td>14,67 kg</td><td><span class="st-ok">✔</span></td></tr>
            <tr><td>Führungsrohre</td><td>9/15</td><td>21,00 kg</td><td>20,99 kg</td><td><span class="st-ok">✔</span></td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        Endbilanz: 5 von 7 Baugruppen korrekt. Die beiden fehlerhaften (Oberteil-BG und
        Untergestell) sind identifiziert, die Ursache ist bekannt und die korrekten Werte sind
        berechnet.
      </div>
    </section>

{projekt_nav("12-pruefung-weitere-funde.html", "Prüfung: weitere Funde", "14-fazit-ausblick.html", "Fazit & Ausblick")}
  </main>
"""

write_page("13-endstand-technische-daten.html", "Projekt 5: Endstand & Technische Daten", body)
