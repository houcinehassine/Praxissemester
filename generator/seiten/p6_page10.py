# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt6 import *

body = seiten_kopf(10, "Technischer Zeichnungssatz &ndash; 21 Blätter",
    "Meilenstein erreicht: Der vollständige Zeichnungssatz liegt vor &ndash; 21 A3-Blätter mit "
    "Einzelteilen, Teilbaugruppen und Gesamtbaugruppe. Erstmals sind alle Maße, Gewichte und "
    "Stücklisten verbindlich festgelegt. 17.04.2026, geprüft von MW Schmidt.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>📊 Kennzahlen der Baugruppe</h2>
      <div class="kennzahlen-grid">
        <div class="kennzahl"><strong>91,05</strong><span>kg Gesamtgewicht</span></div>
        <div class="kennzahl"><strong>58</strong><span>Teile gesamt</span></div>
        <div class="kennzahl"><strong>15</strong><span>verschiedene Teile</span></div>
        <div class="kennzahl"><strong>21</strong><span>Zeichnungsblätter</span></div>
      </div>
      <div class="bild-vergleich" style="margin-top:1rem">
        <div class="bild-box">
          <span class="label">Blatt 21/21 &middot; Gesamtbaugruppe 000-006-200-1</span>
          <img src="img/zeichnung-blatt21-gesamtbaugruppe.jpg" alt="Technische Zeichnung Blatt 21 von 21: isometrische Ansicht des Schweißwagens mit nummerierten Positionen 1-15, vollständiger Stückliste und Schriftfeld mit 91,05 kg, S235JRH, MW Schmidt" />
          <p class="bildtext">Isometrische Ansicht mit Positionsnummern, vollständiger Stückliste und Schriftfeld: Maßstab 1:10, Gewicht 91,05 kg, Werkstoff S235JRH, geprüft von MW Schmidt.</p>
        </div>
      </div>
    </section>

    <section>
      <h2>📏 Zeichnungsnormen &amp; Vorgaben</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Angabe</th><th>Wert</th><th>Bedeutung</th></tr></thead>
          <tbody>
            <tr><td>Werkstoff</td><td>S235JRH</td><td>Baustahl für Hohlprofile &ndash; nicht Aluminium!</td></tr>
            <tr><td>Hauptprofil</td><td>Rohr 40×40×3</td><td>Quadratrohr, Wandstärke 3 mm</td></tr>
            <tr><td>Allgemeintoleranz</td><td>DIN ISO 2768-mK</td><td>mittel (m) für Längen, grob (K) für Form/Lage</td></tr>
            <tr><td>Oberflächen</td><td>DIN EN ISO 1302, Rz 6,3</td><td>Gemittelte Rautiefe 6,3 µm</td></tr>
            <tr><td>Kanten</td><td>DIN ISO 13715, &minus;0,3 / +0,3</td><td>Kantenzustand Außen-/Innenkanten</td></tr>
            <tr><td>Fasen</td><td>Alle unbemaßten Fasen 1×45°</td><td>Standardfase</td></tr>
            <tr><td>Blattformat</td><td>A3</td><td>Einheitlich über alle 21 Blätter</td></tr>
            <tr><td>Projektion</td><td>1. Winkel (ISO-E)</td><td>Europäische Projektionsmethode</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>🔍 Zwei zentrale Erkenntnisse</h2>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>1 &middot; Werkstoff ist Stahl, nicht Aluminium</h4><p>Alle Blätter nennen S235JRH und Rohr 40×40×3. Die CAD-Modelle wirkten wie Nutprofil (Item-Alu) &ndash; tatsächlich ausgeführt ist Variante B: Stahl. Der Erdungsvorteil (keine isolierende Eloxalschicht) spricht klar für diese Wahl.</p></div>
        <div class="mini-karte"><h4>2 &middot; Verschraubt statt geschweißt</h4><p>Die Stücklisten führen 6× ISO 4018 Schraube M20×60 und 6× Sechskantmutter M20. Der Rahmen wird also verschraubt &ndash; das kombiniert die Demontierbarkeit des Profilsystems mit der Robustheit von Stahl.</p></div>
      </div>
    </section>

    <section>
      <h2>📋 Gesamtstückliste (Blatt 21/21 &middot; 000-006-200-1)</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Pos.</th><th>Menge</th><th>Teilenummer</th><th>Nomenklatur</th><th>Quelle</th></tr></thead>
          <tbody>
            <tr><td>1</td><td>2</td><td>000-006-002-1</td><td>Lochblech (Werkzeugwand)</td><td>Gekauft</td></tr>
            <tr><td>2</td><td>2</td><td>000-006-006-3</td><td>Rohr 40×40×3</td><td>Hergestellt</td></tr>
            <tr><td>3</td><td>4</td><td>000-005-006-1</td><td>Rohr 40×40×3</td><td>Hergestellt</td></tr>
            <tr><td>4</td><td>7</td><td>000-006-006-1</td><td>Rohr 40×40×3</td><td>Hergestellt</td></tr>
            <tr><td>5</td><td>2</td><td>000-006-006-2</td><td>Rohr 40×40×3</td><td>Hergestellt</td></tr>
            <tr><td>6</td><td>3</td><td>000-006-005-1</td><td>Flacheisen 40×630×5</td><td>Hergestellt</td></tr>
            <tr><td>7</td><td>6</td><td>ISO 4018</td><td>Sechskantschraube M20×60, Steel Grade C</td><td><span class="st-warn">Unbekannt</span></td></tr>
            <tr><td>8</td><td>6</td><td>DIN EN ISO 4032</td><td>Sechskantmutter M20</td><td>Gekauft</td></tr>
            <tr><td>9</td><td>8</td><td>000-006-001-1</td><td>Rohr 40×40×3</td><td>Hergestellt</td></tr>
            <tr><td>10</td><td>4</td><td>000-006-007-2</td><td>Rohr 40×40×3</td><td>Hergestellt</td></tr>
            <tr><td>11</td><td>2</td><td>000-006-004-1</td><td>SchubladeBox</td><td>Hergestellt</td></tr>
            <tr><td>12</td><td>2</td><td>000-006-004-1</td><td>Schubladenschiene</td><td>Hergestellt</td></tr>
            <tr><td>13</td><td>2</td><td>Symmetry of 000-006-004-1</td><td>Schubladenschiene (gespiegelt)</td><td>Hergestellt</td></tr>
            <tr><td>14</td><td>4</td><td>0055761</td><td>Rolle</td><td>Gekauft</td></tr>
            <tr><td>15</td><td>4</td><td>000-005-011-1</td><td>Blech 145×117 (Rollenplatte)</td><td>Hergestellt</td></tr>
          </tbody>
        </table>
      </div>
      <div class="kennzahlen-grid" style="margin-top:0.75rem">
        <div class="kennzahl"><strong>42</strong><span>Teile hergestellt</span></div>
        <div class="kennzahl"><strong>12</strong><span>Teile gekauft</span></div>
        <div class="kennzahl"><strong>6</strong><span>Quelle „Unbekannt“</span></div>
      </div>
    </section>

    <section>
      <h2>🌳 Baugruppenstruktur</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Ebene</th><th>Zeichnungs-Nr.</th><th>Bezeichnung</th><th>Teile</th><th>Gewicht</th></tr></thead>
          <tbody>
            <tr><td>0</td><td>000-006-200-1</td><td>Gesamtbaugruppe Wagen</td><td>58</td><td>91,05 kg</td></tr>
            <tr><td>1</td><td>000-006-102-1</td><td>Untergestell</td><td>22</td><td>13,97 kg</td></tr>
            <tr><td>1</td><td>000-006-103-1</td><td>Bodenrahmen</td><td>8</td><td>8,45 kg</td></tr>
            <tr><td>1</td><td>000-006-104-1</td><td>Schubladenetage</td><td>11</td><td>27,04 kg</td></tr>
            <tr><td>1</td><td>000-006-105-1</td><td>Schubladenetage (Variante)</td><td>7</td><td>26,69 kg</td></tr>
            <tr><td>1</td><td>000-006-108-1</td><td>Seitenwand</td><td>17</td><td>&mdash;</td></tr>
            <tr><td>1</td><td>000-006-106-1</td><td>Rolle (4×)</td><td>2</td><td>0,65 kg</td></tr>
            <tr><td>2</td><td>000-006-107-1</td><td>Schublade komplett</td><td>3</td><td>18,62 kg</td></tr>
            <tr><td>2</td><td>000-006-101-1/2/3</td><td>Rahmen-Teilbaugruppen</td><td>3&ndash;4</td><td>0&ndash;8,10 kg</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>🗂️ Alle 21 Zeichnungsblätter</h2>
      <p class="section-intro">Einzelteile (Blatt 1&ndash;10), Teilbaugruppen (Blatt 11&ndash;20), Gesamtbaugruppe (Blatt 21).</p>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Blatt</th><th>Zeichnungs-Nr.</th><th>Benennung</th><th>Maßstab</th><th>Gewicht</th></tr></thead>
          <tbody>
            <tr><td>1/21</td><td>000-006-001-1</td><td>Rohr 40×40×3, L=200 &ndash; Stütze/Distanzstück</td><td>1:1</td><td><span class="st-warn">0,09 kg</span></td></tr>
            <tr><td>2/21</td><td>000-006-002-1</td><td>Lochblech 650×520 &ndash; Werkzeugwand</td><td>1:4</td><td>6,14 kg</td></tr>
            <tr><td>3/21</td><td>000-006-004-1</td><td>Schubladenschiene, L=550 &middot; Profil 60×40, 4 Bohrungen</td><td>1:3</td><td>6,03 kg</td></tr>
            <tr><td>4/21</td><td>000-006-004-1</td><td>SchubladeBox 490×410 &middot; Höhe 30, Rand 20</td><td>1:4</td><td>11,83 kg</td></tr>
            <tr><td>5/21</td><td>000-006-005-1</td><td>Flacheisen 40×630×5 &middot; Querriegel, 2× Ø20</td><td>1:2</td><td>0,90 kg</td></tr>
            <tr><td>6/21</td><td>000-006-006-1</td><td>Rohr 40×40×3, L=510 &ndash; Rahmenprofil</td><td>1:2</td><td>1,78 kg</td></tr>
            <tr><td>7/21</td><td>000-006-006-2</td><td>Rohr 40×40×3, L=550 &middot; Ständer mit 3× Ø20</td><td>1:2</td><td><span class="st-warn">0,24 kg</span></td></tr>
            <tr><td>8/21</td><td>000-006-006-3</td><td>Rohr 40×40×3, L=550 &ndash; ohne Bohrung</td><td>1:2</td><td>1,92 kg</td></tr>
            <tr><td>9/21</td><td>000-005-006-1</td><td>Rohr 40×40×3, L=650 &ndash; langes Rahmenprofil</td><td>1:3</td><td>2,27 kg</td></tr>
            <tr><td>10/21</td><td>000-006-007-2</td><td>Rohr 40×40×3, L=650 &middot; Ständer mit 4× Ø10</td><td>1:3</td><td>2,25 kg</td></tr>
            <tr><td>11/21</td><td>000-006-101-1</td><td>Teilbaugruppe Rahmen &ndash; 4 Teile</td><td>1:4</td><td><span class="st-warn">0,00 kg</span></td></tr>
            <tr><td>12/21</td><td>000-006-101-2</td><td>Teilbaugruppe Winkel &ndash; 3 Teile, L-förmig</td><td>1:4</td><td>6,32 kg</td></tr>
            <tr><td>13/21</td><td>000-006-101-3</td><td>Teilbaugruppe Rahmen umlaufend &ndash; 4 Teile</td><td>1:4</td><td>8,10 kg</td></tr>
            <tr><td>14/21</td><td>000-006-102-1</td><td>Baugruppe Untergestell &ndash; 22 Teile</td><td>1:6</td><td>13,97 kg</td></tr>
            <tr><td>15/21</td><td>000-006-103-1</td><td>Baugruppe Bodenrahmen &ndash; 8 Teile</td><td>1:4</td><td>8,45 kg</td></tr>
            <tr><td>16/21</td><td>000-006-104-1</td><td>Baugruppe Schubladenetage &ndash; 11 Teile</td><td>1:6</td><td>27,04 kg</td></tr>
            <tr><td>17/21</td><td>000-006-105-1</td><td>Baugruppe Schubladenetage (Var.) &ndash; 7 Teile</td><td>1:6</td><td>26,69 kg</td></tr>
            <tr><td>18/21</td><td>000-006-106-1</td><td>Baugruppe Rolle &ndash; Rolle 0055761 + Blech</td><td>1:2</td><td>0,65 kg</td></tr>
            <tr><td>19/21</td><td>000-006-107-1</td><td>Baugruppe Schublade komplett &ndash; Box + 2 Schienen</td><td>1:4</td><td>18,62 kg</td></tr>
            <tr><td>20/21</td><td>000-006-108-1</td><td>Baugruppe Seitenwand &ndash; 17 Teile</td><td>1:4</td><td><span class="st-warn">0,00 kg</span></td></tr>
            <tr><td>21/21</td><td>000-006-200-1</td><td><strong>GESAMTBAUGRUPPE Wagen &ndash; 58 Teile</strong></td><td>1:10</td><td><strong>91,05 kg</strong></td></tr>
          </tbody>
        </table>
      </div>
    </section>

{projekt_nav("09-gewaehltes-konzept.html", "Gewähltes Konzept", "11-pruefung-funde.html", "Prüfung & Funde")}
  </main>
"""

write_page("10-zeichnungssatz.html", "Projekt 6: Zeichnungssatz (21 Blätter)", body)
