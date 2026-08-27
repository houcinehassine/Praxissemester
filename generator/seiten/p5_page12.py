# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt5 import *

body = seiten_kopf(12, "Prüfung: weitere Funde",
    "Fünf weitere Befunde &ndash; von Baugruppen ohne Gewichtsangabe über eine falsch deklarierte "
    "Lenkrolle bis zu Dokumentationslücken. Die Gesamtbilanz der Prüfung.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>Fund 3: Oberteil-Baugruppe mit 0,00 kg</h2>
      <p>Im Schriftfeld von Blatt 3/15 (000-005-103-1, Oberteil-Baugruppe) steht „WEIGHT (kg) = 0,00“ &ndash; obwohl die Baugruppe aus 4 Lochplatten und 6 Rahmenrohren besteht.</p>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Bestandteil</th><th>Menge</th><th>Einzelgewicht</th><th>Gesamt</th></tr></thead>
          <tbody>
            <tr><td>Lochplatte D16 &ndash; 800×500×12</td><td>4</td><td>36,47 kg</td><td>145,88 kg</td></tr>
            <tr><td>Rohr 80×80×3 &ndash; 1580</td><td>2</td><td>11,45 kg</td><td>22,90 kg</td></tr>
            <tr><td>Rohr 80×80×3 &ndash; 820</td><td>2</td><td>5,95 kg</td><td>11,90 kg</td></tr>
            <tr><td>Rohr 80×80×3 &ndash; 1420</td><td>2</td><td>10,30 kg</td><td>20,60 kg</td></tr>
            <tr class="total-row"><td colspan="3">Tatsächliches Gewicht der Baugruppe</td><td>201,28 kg</td></tr>
            <tr><td colspan="3">Angabe im Schriftfeld</td><td>0,00 kg ✘</td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        Gleiche Ursache wie bei Fund 1 (fehlende Werkstoffzuweisung) &ndash; hier führt sie nicht zu
        einem falschen, sondern zu gar keinem Wert. Risiko: Für Transport- und
        Hebezeugplanung wäre „gewichtslos“ gefährlich &ndash; 201 kg hebt man nicht von Hand.
      </div>
    </section>

    <section>
      <h2>Fund 4: Untergestell-Gewicht zu niedrig</h2>
      <p>Die Stückliste von Blatt 6/15 (Untergestell) ist vollständig &ndash; damit lässt sich das Gewicht exakt nachrechnen:</p>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Bauteil</th><th>Menge</th><th>Gesamt</th></tr></thead>
          <tbody>
            <tr><td>Rohr 80×80×3 &ndash; 1420 (3 Streben)</td><td>3</td><td>30,90 kg</td></tr>
            <tr><td>Rohr 80×80×3 &ndash; 820</td><td>2</td><td>11,90 kg</td></tr>
            <tr><td>Rohr 80×80×3 &ndash; 660</td><td>4</td><td>19,15 kg</td></tr>
            <tr><td>Blech 145 × 117,5 × 5</td><td>4</td><td>2,60 kg</td></tr>
            <tr class="total-row"><td colspan="2">Summe nur Stahlteile (ohne Rollen)</td><td>64,55 kg</td></tr>
            <tr><td colspan="2">Angabe im Schriftfeld</td><td>37,51 kg ✘</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">
        Rechnet man ohne die drei 1420-mm-Streben, ergeben sich exakt die 37,51 kg des
        Schriftfelds (33,64 kg Rohre/Bleche + 3,87 kg für 4 Rollen). Sehr wahrscheinliche
        Ursache: Den drei Streben fehlt die Werkstoffzuweisung &ndash; wie bei Fund 1 und 3.
        <strong>Das tatsächliche Untergestell wiegt rund 68 kg, nicht 37,51 kg.</strong>
      </p>
      <div class="info-box" style="margin-top:0.75rem">
        Gegenprobe: Das Erweiterungssystem (Blatt 7/15) ist korrekt berechnet (50,33 vs. 50,32 kg
        Blattangabe) &ndash; der Fehler betrifft also nur einzelne Baugruppen, nicht alle.
      </div>
    </section>

    <section>
      <h2>Fund 5 &amp; 6: Beschaffungsrelevante Fehler auf der Hauptstückliste</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>#</th><th>Befund</th><th>Risiko</th></tr></thead>
          <tbody>
            <tr><td>5</td><td>Lenkrolle (Pos. 8, Teil 0055761) als „Hergestellt“ eingetragen &ndash; auf Blatt 6/15 dasselbe Teil als „Gekauft“</td><td>Bei Auswertung nach „Quelle“ landen 4 Rollen in der Fertigungsliste statt in der Bestellung &rarr; sie fehlen bei der Montage</td></tr>
            <tr><td>6</td><td>Pos. 11 („Rohr_40x40x3“) ohne Längenangabe &ndash; andere Blätter nennen „&ndash; 750“</td><td>Ohne Länge ist das Teil nicht bestellbar und nicht zuschneidbar</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">Eine 7-stellige Sachnummer ohne Projektpräfix (0055761) ist typisch für ein Katalogteil &ndash; ein Zusatzargument, dass „Hergestellt“ hier falsch ist.</p>
    </section>

    <section>
      <h2>Weitere Dokumentationsmängel</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <tbody>
            <tr><td>Material „XXX“ auf 6 Baugruppenblättern</td><td>statt eines Werkstoffs oder „siehe Einzelteile“</td></tr>
            <tr><td>Maßstab „1&gt;10“ statt „1:10“ (Blatt 7/15)</td><td>Tippfehler im Schriftfeld, in der Ansichtsbeschriftung korrekt</td></tr>
            <tr><td>Quelle „Unbekannt“ bei 4 × Mutter M16</td><td>Bestelllücke, siehe Seite 8</td></tr>
            <tr><td>„Lochplatte + Schrauben“ ohne Schrauben</td><td>Datenlücke, siehe Seite 8</td></tr>
            <tr><td>Bohrungszahl Lochplatte unklar (40 vs. 64)</td><td>rechnerischer Rückschluss aus dem Gewicht ergibt ca. 64 Bohrungen statt der im 100×100-Raster erwarteten 40 &ndash; zu prüfen am CAD-Modell</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>✅ Ein geklärter Punkt: die Wandstärke des Führungsrohrs</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Quelle</th><th>Profil</th><th>Spiel zum 40er-Rohr</th></tr></thead>
          <tbody>
            <tr><td>Konzepttext</td><td>50 × 50 × 4</td><td>2 mm</td></tr>
            <tr><td>Stückliste 10.04.</td><td>50 × 50 × 2</td><td>6 mm &ndash; zu viel</td></tr>
            <tr><td><strong>Endstand 17.04.</strong></td><td><strong>50 × 50 × 3</strong></td><td><strong>4 mm gesamt, 2 mm je Seite</strong></td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">Der Endstand vereinheitlicht die Wandstärke auf 3 mm für alle Rohre &ndash; ein brauchbares, leichtgängiges Gleitspiel und ein Beschaffungs-/Lagervorteil.</p>
    </section>

    <section>
      <h2>📊 Gesamtbilanz der Konstruktionsprüfung</h2>
      <div class="kennzahlen-grid">
        <div class="kennzahl"><strong>5</strong><span>Belegte Fehler</span></div>
        <div class="kennzahl"><strong>5</strong><span>Dokumentationsmängel</span></div>
        <div class="kennzahl"><strong>1</strong><span>Offene Frage</span></div>
        <div class="kennzahl"><strong>1</strong><span>Geklärter Punkt</span></div>
      </div>
      <p style="margin-top:0.75rem">Alle fünf Fehler lassen sich auf zwei Ursachen zurückführen: fehlende Werkstoffzuweisung im CAD (Funde 1, 3, 4) und nicht nachgeführte Teilebenennung nach einer Maßänderung (Fund 2) sowie unsaubere Quellen-Deklaration (Fund 5).</p>
    </section>

    <section>
      <h2>✅ Empfehlungen</h2>
      <div class="fazit-grid">
        <div class="karte">
          <span class="label">1</span>
          <h4>Werkstoffzuweisung als Pflichtschritt</h4>
          <p>Verhindert Fehler 1, 3 und 4 vollständig. Vor Zeichnungsausgabe prüfen, ob jedes Teil Werkstoff und Dichte hat &ndash; Gewicht 0,00 kg ist immer ein Warnsignal.</p>
        </div>
        <div class="karte">
          <span class="label">2</span>
          <h4>Teilebenennung nach Maßänderung nachziehen</h4>
          <p>Bei Fund 2 drohten 4 × 160 mm Fehlschnitt. Die Länge steht im Teilenamen &rarr; bei jeder Maßänderung mit ändern.</p>
        </div>
        <div class="karte">
          <span class="label">3</span>
          <h4>Lenkrollen nach korrigiertem Gewicht auslegen</h4>
          <p>Real ca. 320 kg statt 289 kg + Werkstückgewicht. 150&ndash;200 kg Tragkraft je Rolle, mindestens 2 feststellbar.</p>
        </div>
      </div>
    </section>

{projekt_nav("11-pruefung-gewichtsfehler.html", "Prüfung: Gewichtsfehler", "13-endstand-technische-daten.html", "Endstand & Technische Daten")}
  </main>
"""

write_page("12-pruefung-weitere-funde.html", "Projekt 5: Prüfung – weitere Funde", body)
