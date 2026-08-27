# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt5 import *

body = seiten_kopf(5, "Lochplatte auswählen &amp; zeichnen",
    "Die Arbeitsfläche ist das Herz des Tischs: die passende Lochplatte wurde am Markt gesucht, "
    "verglichen und im CAD nachgebaut. 9. April 2026.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>Ergebnis &ndash; Gewählte Platte</h2>
      <div class="kennzahlen-grid">
        <div class="kennzahl"><strong>800×500×12</strong><span>mm &middot; 000-005-013-2</span></div>
        <div class="kennzahl"><strong>D16</strong><span>System 16, Raster 100×100 mm</span></div>
        <div class="kennzahl"><strong>3</strong><span>Stück nebeneinander (Ausgangsplanung)</span></div>
      </div>
      <p style="margin-top:0.75rem">Produkt: Lochplatte D16 | 12 mm &ndash; flexible Spannbasis für modulare Schweißtische im System 16 mit 100×100 Raster.</p>
    </section>

    <section>
      <h2>Marktrecherche &ndash; Lochplatte suchen</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Variante</th><th>Loch-Ø</th><th>Raster</th><th>Dicke</th><th>Maße</th><th>Preis / Info</th></tr></thead>
          <tbody>
            <tr><td>Schweißtisch24 &ndash; Bausatz mobil</td><td>D16</td><td>50 × 50</td><td>6 mm</td><td>800 × 400 × 50</td><td>Bausatz für unterwegs</td></tr>
            <tr><td>WELDINGER (hausundwerkstatt24)</td><td>D16</td><td>50 × 50</td><td>6 mm</td><td>800 × 400 × 50</td><td>199,99 € &middot; Stahl S355 &middot; 23 kg</td></tr>
            <tr><td>hot-tabledance &ndash; Lochplatte D16</td><td>D16</td><td>50 × 50</td><td>8 mm</td><td>&ndash;</td><td>kostenloser Versand</td></tr>
            <tr><td><strong>✅ hot-tabledance &ndash; System 16</strong></td><td>D16</td><td>100 × 100</td><td>12 mm</td><td>800 × 500</td><td><strong>GEWÄHLT</strong> &middot; modulares Spannsystem</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        Auswahlkriterium: 12 mm Plattenstärke = höhere Steifigkeit &amp; Verzugsfestigkeit beim
        Schweißen. 100 × 100 Raster = weniger Bohrungen, stabilere Platte, Standard im
        modularen System 16.
      </div>
    </section>

    <section>
      <h2>Auf dem Tisch ansehen</h2>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Drei Lochplatten auf dem Schweißtisch-Rahmen</span>
          <img src="img/lochplatten-auf-rahmen.png" alt="CAD-Ansicht von drei D16-Lochplatten 800×500×12mm nebeneinander auf dem Schweißtisch-Rahmen, isometrisch und in Draufsicht mit Lochraster" />
          <p class="bildtext">Isometrie, Draufsicht und Seitenansichten der modellierten Lochplatte 800 × 500 × 12 mm, platziert auf dem Tisch.</p>
        </div>
      </div>
    </section>

    <section>
      <h2>Anordnung der Arbeitsplatten &ndash; 2 Varianten</h2>
      <p class="section-intro">Drei Platten werden nebeneinander platziert. Dabei gibt es zwei Konfigurationen:</p>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>🅰️ Variante A &ndash; mit Zwischenabstand</h4><p>✔ Maximale Vergrößerung der Gesamtarbeitsfläche. ✘ Erhöhte Verschmutzung &ndash; Schweißreste fallen auf den Boden.</p></div>
        <div class="mini-karte"><h4>🅱️ Variante B &ndash; auf Stoß (lückenlos)</h4><p>✔ Sauberer Arbeitsbereich &ndash; Schweißreste bleiben auf den Platten. ✘ Geringere nutzbare Gesamtlänge der Arbeitsfläche.</p></div>
      </div>
    </section>

    <section>
      <h2>Erkanntes Problem &ndash; Verschraubung</h2>
      <div class="warn-box">
        <strong>Nachteil der Schrauben:</strong> Die Schraubenköpfe stehen über und stören die
        Arbeitsfläche &rarr; Werkstücke liegen nicht plan auf.
      </div>
      <p style="margin-top:0.75rem">
        <strong>Lösungsansatz:</strong> Senkschrauben / versenkte Befestigung oder Verschraubung
        von unten prüfen. Drei konkrete Lösungsmethoden werden auf der nächsten Seite
        durchgespielt.
      </p>
    </section>

{projekt_nav("04-erste-zeichnungen.html", "Erste Zeichnungen", "06-oberteil-unterteil.html", "Oberteil & Unterteil")}
  </main>
"""

write_page("05-lochplatte.html", "Projekt 5: Lochplatte auswählen", body)
