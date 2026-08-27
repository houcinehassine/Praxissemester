# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt6 import *

body = seiten_kopf(7, "Variante A &ndash; kompletter Neubau (SW-001)",
    "Ein vollständig neuer Wagen mit eigenem Gerätefach, bemaßter Zeichnung und einem "
    "Belegungsplan über 16 Positionen &ndash; und dem Maßkonflikt, der zum Konzeptwechsel "
    "führte.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>💡 Idee &amp; Zweck</h2>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>🚚 Mobile Ebene</h4><p>Maschine, Gas und die wichtigsten Werkzeuge fahren zum Werkstück &ndash; nicht umgekehrt.</p></div>
        <div class="mini-karte"><h4>⏱️ Spart Wege</h4><p>Hält den Platz flexibel, reduziert Laufwege zwischen Werkstück und Gerät.</p></div>
        <div class="mini-karte"><h4>📦 5S am Wagen</h4><p>Alles griffbereit &ndash; Schubladen bringen die 5S-Ordnung direkt an den Einsatzort.</p></div>
      </div>
    </section>

    <section>
      <h2>🗺️ Belegungsplan &ndash; 16 Positionen</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Pos.</th><th>Element</th><th>Zuordnung</th></tr></thead>
          <tbody>
            <tr><td>1</td><td>Klappbare Stahl-Ablage</td><td>Oberseite &ndash; Arbeitsfläche</td></tr>
            <tr><td>2</td><td>Brenner</td><td>Werkzeugwand</td></tr>
            <tr><td>3</td><td>Masse / Masseklemme</td><td>Werkzeugwand</td></tr>
            <tr><td>4</td><td>Bürste</td><td>Werkzeugwand</td></tr>
            <tr><td>5</td><td>Hammer</td><td>Werkzeugwand</td></tr>
            <tr><td>6</td><td>Zwingen / Winkel</td><td>Werkzeugwand</td></tr>
            <tr><td>7</td><td>Schublade 1 &ndash; Draht / Düsen / Ersatzteile</td><td>Schubladenblock</td></tr>
            <tr><td>8</td><td>Schublade 2 &ndash; PSA-Kleinteile / Trennspray</td><td>Schubladenblock</td></tr>
            <tr><td>9</td><td>Schublade 3 &ndash; Trenn-/Schleifscheiben</td><td>Schubladenblock</td></tr>
            <tr><td>10</td><td>Vorhandene MIG-Maschine</td><td>Gerätefach unten</td></tr>
            <tr><td>11</td><td>Gasflasche &ndash; hinten, gekettet</td><td>Rückseite</td></tr>
            <tr><td>12</td><td>Kabel-/Schlauchhaspel</td><td>Seitlich</td></tr>
            <tr><td>13</td><td>Schleifer</td><td>Seitliche Ablage</td></tr>
            <tr><td>14</td><td>Feuerlöscher</td><td>Seitlich, gut erreichbar</td></tr>
            <tr><td>15</td><td>Helm-Haken</td><td>Seitlich oben</td></tr>
            <tr><td>16</td><td>Handschuhe</td><td>Seitlich</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>📐 Technische Zeichnung SW-001</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <tbody>
            <tr><td>Benennung</td><td>Mobiler Schweißwagen</td></tr>
            <tr><td>Zeichnungs-Nr.</td><td>SW-001 &middot; Blatt 1/1</td></tr>
            <tr><td>Werkstoff</td><td>A: item-Aluprofil / B: Stahl</td></tr>
            <tr><td>Maßstab</td><td>1:10 &middot; Einheit mm</td></tr>
            <tr><td>Allg.-Toleranz</td><td>ISO 2768-m</td></tr>
            <tr><td>Datum</td><td>06.08.2026 &middot; Praxissemester</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Wichtig für die Aufgabenstellung:</strong> Das Schriftfeld nennt bereits zwei
        Werkstoffvarianten (A: item-Aluprofil / B: Stahl). Damit ist die Anforderung
        „2 Varianten: Item-Profile und normale Werkbank“ konstruktiv angelegt &ndash; die
        technisch-wirtschaftliche Gegenüberstellung kann darauf aufbauen.
      </div>
    </section>

    <section>
      <h2>📊 Hauptmaße</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Maß</th><th>Wert</th><th>Bemerkung</th></tr></thead>
          <tbody>
            <tr><td>Grundfläche</td><td>800 × 500 mm</td><td>kompakt, fahrbar</td></tr>
            <tr><td>Höhe</td><td>1320 mm (mit Flasche ~1350)</td><td>inkl. Lochraster-Panel</td></tr>
            <tr><td>Arbeitshöhe</td><td>920 mm</td><td>bis Korpusoberkante</td></tr>
            <tr><td>Gerätefach Höhe</td><td>430 mm</td><td>für die vorhandene MIG-Maschine</td></tr>
            <tr><td>Lochraster-Panel</td><td>600 mm breit</td><td>Werkzeugwand</td></tr>
            <tr><td>Gasflasche</td><td>Ø200 × ~1150 mm</td><td>stehend, hinten, angekettet</td></tr>
            <tr><td>Rollen</td><td>Ø125 mm</td><td>4×, 2 mit Feststellbremse</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>🚨 Der kritische Maßkonflikt</h2>
      <div class="warn-box">
        <strong>Gerätefach vs. Maschine &ndash; die Maschine passt nicht:</strong>
        Gerätefach in SW-001 hat 430 mm Höhe, die gemessene MIG-Maschine ist 520 mm hoch
        &rarr; 90 mm zu wenig. Ebenso: Korpustiefe 500 mm gegen Maschinentiefe 610 mm
        &rarr; 110 mm zu wenig. Das ist der Befund, der zum Konzeptwechsel auf Seite 8 führte.
      </div>
      <h3 style="margin-top:1rem">Maßabgleich über alle Dokumente</h3>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Maß</th><th>Aufmaß vor Ort</th><th>Maße &amp; Ergonomie</th><th>SW-001</th><th>Bewertung</th></tr></thead>
          <tbody>
            <tr><td>Grundfläche</td><td>410 × 300 (Altwagen)</td><td>750 × 1000</td><td>800 × 500</td><td>Tiefe: 1000 vs. 500 mm &ndash; Faktor 2</td></tr>
            <tr><td>Arbeitshöhe</td><td>&mdash;</td><td>900</td><td>920</td><td><span class="st-ok">✅ konsistent</span></td></tr>
            <tr><td>Gerätefach Höhe</td><td>&mdash;</td><td>850</td><td>430</td><td><span class="st-no">⚠️ &minus;420 mm</span></td></tr>
            <tr><td>MIG-Maschine H</td><td>520</td><td>800</td><td>&mdash;</td><td><span class="st-no">passt nicht in 430er Fach</span></td></tr>
            <tr><td>Gasflasche Ø</td><td>220</td><td>230</td><td>200</td><td>3 Werte &ndash; größten wählen</td></tr>
            <tr><td>Gasflasche H</td><td>1640</td><td>1500</td><td>~1150</td><td><span class="st-warn">⚠️ Spanne 490 mm</span></td></tr>
            <tr><td>Rollen Ø</td><td>&mdash;</td><td>160</td><td>125</td><td>Ø125 rollt schlechter über Kabel/Schwellen</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Hinweis zum Auszugskonzept:</strong> In „Maße &amp; Ergonomie“ ist ein
        Schwerlast-Vollauszug festgelegt. In der Zeichnung SW-001 ist dieser Auszug nicht
        dargestellt &ndash; das Gerätefach wirkt als offenes Fach. Zu klären, ob der Auszug
        entfällt oder noch zu ergänzen ist.
      </div>
    </section>

    <section>
      <h2>🔩 Teileliste &amp; Rahmenmaterial</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Position</th><th>Funktion</th><th>Menge</th></tr></thead>
          <tbody>
            <tr><td>Stahl-Kantrohr 40×40×2</td><td>Wagen-Rahmen (geschweißt)</td><td>~14 m</td></tr>
            <tr><td>Bleche / Verstrebungen (Stahl)</td><td>Rahmen aussteifen</td><td>Set</td></tr>
            <tr><td>Lenkrollen Ø125 (2 mit Bremse)</td><td>fahrbar</td><td>4×</td></tr>
            <tr><td>Gasflaschenhalter + Kette/Gurt</td><td>Flasche hinten sichern</td><td>1×</td></tr>
            <tr><td>Schlauchpaket</td><td>Flasche &rarr; Maschine</td><td>1×</td></tr>
            <tr><td>Kabel-/Schlauchhaspel</td><td>Ordnung, kein Schleifen am Boden</td><td>1×</td></tr>
            <tr><td>Bodenplatte + Schubladenblock</td><td>Maschine + Kleinteile</td><td>1×</td></tr>
            <tr><td>Werkzeughalter, Haken, klappbare Ablage</td><td>Brenner, Kabel, Werkzeuge</td><td>Set</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">
        Rechnerisches Rahmengewicht: Kantrohr 40×40×2 wiegt ca. 2,31 kg/m &rarr; 14 m ≈ 32 kg
        (ohne Bleche und Verstrebungen). Das bestätigt die Größenordnung der Gewichtsabschätzung
        von Seite 6.
      </p>
    </section>

    <section>
      <h2>✅ Erfüllungsgrad gegenüber der Anforderungsliste</h2>
      <div class="kennzahlen-grid">
        <div class="kennzahl"><strong>12</strong><span>erfüllt</span></div>
        <div class="kennzahl"><strong>1</strong><span>teilweise (A-11 Kippsicherheit)</span></div>
        <div class="kennzahl"><strong>1</strong><span>Konflikt (A-01 Gerätefach)</span></div>
      </div>
      <p style="margin-top:0.75rem">
        Bis auf den Maßkonflikt beim Gerätefach und den fehlenden Standsicherheitsnachweis erfüllt
        SW-001 die Anforderungen vollständig &ndash; inklusive Gasflaschensicherung, Haspel,
        klappbarer Ablage, Feuerlöscher und aller PSA-Halterungen.
      </p>
    </section>

{projekt_nav("06-masse-ergonomie.html", "Maße & Ergonomie", "08-variante-b-zusatzwagen.html", "Variante B: Zusatzwagen")}
  </main>
"""

write_page("07-variante-a-neubau.html", "Projekt 6: Variante A – Neubau SW-001", body)
