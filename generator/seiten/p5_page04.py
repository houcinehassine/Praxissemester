# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt5 import *

body = seiten_kopf(4, "Erste technische Zeichnungen",
    "Vier CAD-Zeichnungen setzen das Grundkonzept in konkrete Maße um: die Gesamtbaugruppe, "
    "die Lochplatte, sowie die oberen und unteren Rahmenteile.") + f"""
  <main class="projekt-detail">

    <section>
      <div class="info-box">
        Inhalt 4 CAD-Zeichnungen &middot; Bauteil-Material Vierkantrohr + Stahlplatten &middot; Typ Konstruktionsunterlagen
      </div>
    </section>

    <section>
      <h2>1 &middot; Teilen-Nummern &ndash; Gesamtbaugruppe</h2>
      <p class="section-intro">Isometrische Ansicht, Maßstab 1:8 | Detail A 1:10 | Übersicht 1:15 &middot; Positionsnummern 1&ndash;14.</p>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Isometrische Gesamtansicht mit Positionsnummern 1–14</span>
          <img src="img/teilennummern-isometrie.png" alt="Isometrische CAD-Zeichnung des Schweißtischs mit 14 nummerierten Positionen: Rahmen, Tischplatten, Auslegerarme, Fußplatten und Detailansicht der Verschraubung" />
          <p class="bildtext">Aufbauprinzip: Geschweißter Grundrahmen aus Vierkantrohr &rarr; darauf 4 verschraubte Lochplatten &rarr; seitlich Auslegerarme für Werkzeug/Klemmen.</p>
        </div>
      </div>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <tbody>
            <tr><td>1</td><td>Verschraubung Unterseite (Detail A)</td></tr>
            <tr><td>2</td><td>Längsträger Rahmen oben</td></tr>
            <tr><td>3</td><td>Eckverbinder / Knotenblech</td></tr>
            <tr><td>4</td><td>Tischplatte (rechts)</td></tr>
            <tr><td>5</td><td>Tischplatte (links / außen)</td></tr>
            <tr><td>6</td><td>Seitliche Aufnahme / Konsole</td></tr>
            <tr><td>7</td><td>Auslegerarm oben (Anbau rechts)</td></tr>
            <tr><td>8</td><td>Untere Längsstrebe (Rahmen unten)</td></tr>
            <tr><td>9</td><td>Tischbein vorne links</td></tr>
            <tr><td>10</td><td>Untere Querstrebe</td></tr>
            <tr><td>11</td><td>Fußplatte 160 × 160 × 10 mm</td></tr>
            <tr><td>12</td><td>Querträger Anbauseite</td></tr>
            <tr><td>13</td><td>Ablage-/Klemmenleiste rechts</td></tr>
            <tr><td>14</td><td>Ablage-/Klemmenleiste links</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>2 &middot; Platte &ndash; Tischplatte mit Lochraster</h2>
      <p class="section-intro">Vorderansicht 1:4 | Schnittansicht F&ndash;F 1:4.</p>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Merkmal</th><th>Wert</th><th>Anmerkung</th></tr></thead>
          <tbody>
            <tr><td>Länge</td><td>750 mm</td><td>Außenmaß</td></tr>
            <tr><td>Breite</td><td>300 mm</td><td>Außenmaß</td></tr>
            <tr><td>Dicke</td><td>30 mm</td><td>Schnitt F&ndash;F</td></tr>
            <tr><td>Lochraster</td><td>80 mm</td><td>gleichmäßig in Länge &amp; Breite</td></tr>
            <tr><td>Randabstand</td><td>55 mm</td><td>oben &amp; unten</td></tr>
            <tr><td>Nutzbereich</td><td>640 × 250 mm</td><td>Lochfeld</td></tr>
            <tr><td>Bohrung Ø</td><td>Ø20 mm</td><td>Systemlöcher für Spannmittel</td></tr>
            <tr><td>Senkung</td><td>20 / 22 mm</td><td>an Befestigungspunkten</td></tr>
            <tr><td>Lochabstand quer</td><td>75 mm</td><td>vom Mittelloch aus</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        Funktion: Das Ø20-Raster ist der Standard für Schweißtisch-Spannsysteme &rarr; Bolzen,
        Prismen und Spanner sind frei positionierbar.
      </div>
    </section>

    <section>
      <h2>3 &middot; Tisch-Obere-Teile &ndash; Träger &amp; Profile</h2>
      <p class="section-intro">Vorderansichten &amp; Schnitte G&ndash;G, H&ndash;H, I&ndash;I, J&ndash;J &middot; Maßstab 1:5.</p>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Teil</th><th>Länge</th><th>Profil</th><th>Bohrungen</th></tr></thead>
          <tbody>
            <tr><td>Längsträger A (Schnitt G&ndash;G)</td><td>1500 mm</td><td>80 × 80 (Wand ~3 mm, außen 86)</td><td>Ø20 &middot; Teilung 250 / 150 &middot; Randabstand 25</td></tr>
            <tr><td>Längsträger B (Schnitt I&ndash;I)</td><td>1330 mm</td><td>80 × 80</td><td>Ø20 &middot; erste Bohrung 190 &middot; Teilung 250 / 150</td></tr>
            <tr><td>Querträger (Schnitt H&ndash;H)</td><td>500 mm</td><td>80 × 80</td><td>1 × Ø20 bei 250 mm (mittig)</td></tr>
            <tr><td>Leiste / Ausleger (Schnitt J&ndash;J)</td><td>1500 mm</td><td>40 × 40 (außen 44)</td><td>ohne Bohrbild in dieser Ansicht</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">Merke: Zwei Profilgrößen &rarr; 80×80 für die tragende Struktur, 40×40 für die leichten Anbau-/Ablageleisten.</p>
    </section>

    <section>
      <h2>4 &middot; Tisch-Unten-Teile &ndash; Beine, Streben &amp; Fußplatte</h2>
      <p class="section-intro">Vorderansichten &amp; Schnitte B&ndash;B, C&ndash;C, D&ndash;D, E&ndash;E &middot; Maßstab 1:4.</p>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Teil</th><th>Maß</th><th>Profil / Schnitt</th><th>Funktion</th></tr></thead>
          <tbody>
            <tr><td>Längsstrebe unten</td><td>1328 mm</td><td>80 × 80 (B&ndash;B)</td><td>Rahmen unten, Längsrichtung</td></tr>
            <tr><td>Tischbein</td><td>750 mm</td><td>80 × 80 (C&ndash;C)</td><td>Standhöhe der Konstruktion</td></tr>
            <tr><td>Querstrebe unten</td><td>500 mm</td><td>80 × 80 (D&ndash;D)</td><td>Rahmen unten, Querrichtung</td></tr>
            <tr><td>Fußplatte</td><td>160 × 160 × 10 mm</td><td>Blech (E&ndash;E)</td><td>4 Bohrungen &rarr; Bodenverankerung</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">Hinweis: Alle Vierkantrohre einheitlich 80 × 80 mm &rarr; ein Materialtyp, wenig Verschnitt, einfache Beschaffung.</p>
    </section>

    <section>
      <h2>Zusammenfassung der Konstruktion</h2>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>📏 Grundfläche</h4><p>Rahmen ca. 1500 × 500 mm, Plattenfeld 4 × (750 × 300).</p></div>
        <div class="mini-karte"><h4>📐 Höhe</h4><p>Beine 750 + Rahmen 80 + Platte 30 &rarr; ca. 860 mm Arbeitshöhe.</p></div>
        <div class="mini-karte"><h4>🔩 Verbindung</h4><p>Rahmen geschweißt, Platten verschraubt, Fußplatten gedübelt.</p></div>
        <div class="mini-karte"><h4>🧰 Erweiterung</h4><p>Seitliche Ausleger (40×40) &rarr; Ablage für Klemmen &amp; Werkzeug.</p></div>
      </div>
    </section>

{projekt_nav("03-grundkonzept-gewaehlt.html", "Grundkonzept gewählt", "05-lochplatte.html", "Lochplatte auswählen")}
  </main>
"""

write_page("04-erste-zeichnungen.html", "Projekt 5: Erste Zeichnungen", body)
