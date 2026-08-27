# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt5 import *

body = seiten_kopf(9, "Gesamtzusammenbau &amp; Stückliste (000-005-200-2)",
    "52 Teile, 32,98 kg, 21 m Rohrbedarf &ndash; der erste vollständige Entwurf des Schweißtischs, "
    "rechnerisch bis ins letzte Teil bestätigt.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>✅ Rechnerische Bestätigung des Gewichts</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Baugruppe</th><th>Zeichnung</th><th>Gewicht</th></tr></thead>
          <tbody>
            <tr><td>Oberteil &ndash; Basis</td><td>000-005-104-1</td><td>18,63 kg</td></tr>
            <tr><td>Unterteil &ndash; Basis</td><td>000-005-105-1</td><td>7,60 kg</td></tr>
            <tr><td>Erweiterungssystem</td><td>000-005-103-3</td><td>6,75 kg</td></tr>
            <tr class="total-row"><td>Summe</td><td>&ndash;</td><td>32,98 kg</td></tr>
            <tr><td>Angabe im Schriftfeld</td><td>000-005-200-2</td><td>32,98 kg ✔</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        Die Summe der drei Einzelbaugruppen stimmt exakt mit dem Gesamtgewicht überein &ndash; das
        bestätigt eine sauber aufgebaute Baugruppenstruktur im CAD, ohne doppelt gezählte oder
        vergessene Teile.
      </div>
    </section>

    <section>
      <h2>Baugruppen-Struktur (5 Ebenen)</h2>
      <p>
        📦 000-005-200-2 · Gesamtzusammenbau (32,98 kg) gliedert sich in
        🔝 Oberteil (18,63 kg, 2× Rohr 1500 + 2× Rohr 500 + 1× Rohr 1330 gebohrt, 3× Lochplatte
        + Schrauben), 🔽 Unterteil (7,60 kg, 2× Rohr 1328 + 4× Rohr 750 Beine + 2× Rohr 500 +
        4× Platte 120×120×10) und ↔️ Erweiterungssystem (6,75 kg, 2× Rohr 50×50×2 &ndash; 1500 +
        4× Schraube M16×30 + 4× Mutter M16, darin 2× Mobile Teil mit je 2× Rohr 40×40×2 &ndash;
        750 + 2× Rohr 750 gebohrt + 5× Mutter M20 + 2× Schraube M20×200).
      </p>
    </section>

    <section>
      <h2>🧮 Summenstückliste &ndash; 52 Teile, 15 verschiedene</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Menge</th><th>Teilenummer / Benennung</th><th>Kategorie</th></tr></thead>
          <tbody>
            <tr><td>2</td><td>000-005-005-4 &middot; Rohr 80×80×3 &ndash; 1500 gebohrt</td><td>Rohr Oberteil</td></tr>
            <tr><td>2</td><td>000-005-004-2 &middot; Rohr 80×80×3 &ndash; 500 gebohrt</td><td>Rohr Oberteil</td></tr>
            <tr><td>1</td><td>000-005-005-3 &middot; Rohr 80×80×3 &ndash; 1330 gebohrt</td><td>Rohr Oberteil</td></tr>
            <tr><td>3</td><td>000-005-013-2 &middot; Lochplatte D16 &ndash; 800×500×12</td><td>Arbeitsfläche</td></tr>
            <tr><td>2</td><td>000-005-005-1 &middot; Rohr 80×80×3 &ndash; 1328</td><td>Rohr Unterteil</td></tr>
            <tr><td>4</td><td>000-005-006-1 &middot; Rohr 80×80×3 &ndash; 750</td><td>Beine</td></tr>
            <tr><td>2</td><td>000-005-004-1 &middot; Rohr 80×80×3 &ndash; 500</td><td>Rohr Unterteil</td></tr>
            <tr><td>4</td><td>000-005-012-2 &middot; Platte 120×120×10 gebohrt</td><td>Fußplatten</td></tr>
            <tr><td>4</td><td>000-005-002-1 &middot; Rohr 40×40×2 &ndash; 750</td><td>Rohr Erweiterung</td></tr>
            <tr><td>4</td><td>000-005-002-2 &middot; Rohr 40×40×2 &ndash; 750 gebohrt</td><td>Rohr Erweiterung</td></tr>
            <tr><td>2</td><td>000-005-003-1 &middot; Rohr 50×50×2 &ndash; 1500</td><td>Führungsrohr</td></tr>
            <tr><td>10</td><td>DIN EN ISO 4032 &middot; Sechskantmutter M20</td><td>Normteil</td></tr>
            <tr><td>4</td><td>DIN EN ISO 4762 &middot; Zylinderschraube ISK M20×200</td><td>Normteil</td></tr>
            <tr><td>4</td><td>DIN EN ISO &middot; Sechskantschraube M16×30</td><td>Normteil</td></tr>
            <tr><td>4</td><td>DIN EN ISO 4032 &middot; Sechskantmutter M16</td><td>Normteil</td></tr>
            <tr class="total-row"><td>52</td><td>SUMME</td><td>15 verschiedene Teile</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">Kontrollrechnung: 2+2+1+3+2+4+2+4+4+4+10+4+2+4+4 = 52 ✔ &ndash; stimmt mit der Angabe im Kopf überein.</div>
    </section>

    <section>
      <h2>📏 Abgeleiteter Materialbedarf &ndash; Rohre</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Profil</th><th>Gesamtlänge</th><th>Stangen à 6 m</th></tr></thead>
          <tbody>
            <tr><td>80 × 80 × 3</td><td>≈ 12,0 m</td><td>2 Stangen</td></tr>
            <tr><td>40 × 40 × 2</td><td>6,0 m</td><td>1 Stange</td></tr>
            <tr><td>50 × 50 × 2</td><td>3,0 m</td><td>1 Stange</td></tr>
            <tr class="total-row"><td>Summe</td><td>≈ 21,0 m</td><td>4 Stangen</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">
        Beim Profil 80×80×3 bleibt aus 2 × 6 m ein Verschnitt von nur 14 mm &ndash; die Längen
        passen fast perfekt zusammen. Beim 50×50×2 bleiben dagegen 3 m Rest &rarr; passt zur
        Praktikumsaufgabe „Restverwertung“.
      </p>
    </section>

    <section>
      <h2>🏭 Make-or-Buy-Auswertung</h2>
      <div class="kennzahlen-grid">
        <div class="kennzahl"><strong>21</strong><span>Teile gekauft (Zukauf)</span></div>
        <div class="kennzahl"><strong>11</strong><span>Teile hergestellt (intern)</span></div>
        <div class="kennzahl"><strong>4</strong><span>Teile Quelle unbekannt</span></div>
      </div>
    </section>

    <section>
      <h2>📌 Offene Punkte aus dem Gesamtdokument (Stand 10.04.)</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>#</th><th>Punkt</th><th>Risiko</th><th>To-do</th></tr></thead>
          <tbody>
            <tr><td>1</td><td>Quelle „Unbekannt“ bei 4 × Mutter M16</td><td>Teil fehlt in der Bestellung &rarr; Montage stockt</td><td>Quelle auf „Gekauft“ setzen, Lieferant hinterlegen</td></tr>
            <tr><td>2</td><td>„Lochplatte + Schrauben“ ohne Schrauben</td><td>Verschraubungsmethode noch nicht entschieden</td><td>Nach Entscheidung Senkschraube / Innengewinde / Gewindeblech ergänzen</td></tr>
            <tr><td>3</td><td>Wandstärke Führungsrohr widersprüchlich</td><td>Spiel 6 mm statt ~2 mm &rarr; Teleskop läuft zu locker</td><td>Wandstärke festlegen oder Gleitstücke vorsehen</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>🛤️ Der Weg zum Endstand</h2>
      <div class="stepper">
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">1</span>
            <span class="schritt-titel">10.04.2026 &ndash; Entwurfsstand 000-005-200-2 (32,98 kg)</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>3 Lochplatten in Reihe, Fußplatten fest, 52 Teile.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">2</span>
            <span class="schritt-titel">Überarbeitung in einer Woche</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Querträger 500 &rarr; 820 mm (Platz für 2. Plattenreihe) &middot; Platten 3 &rarr; 4 Stück, Anordnung 2×2 &middot; Fußplatten &rarr; 4 Lenkrollen (fahrbar) &middot; Beine 750 &rarr; 660 mm (Rollen gleichen aus) &middot; Werkstoffe im CAD korrekt zugewiesen.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">3</span>
            <span class="schritt-titel">17.04.2026 &ndash; Endstand 000-005-200-1 (289,11 kg)</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>4 Lochplatten 2×2, 4 Lenkrollen, 40 Teile, 15 Zeichnungsblätter, geprüft von MW Schmidt.</p></div>
        </div>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        Für den Tätigkeitsbericht: Dieser Vergleich zeigt eine vollständige
        Konstruktions-Iteration &ndash; vom ersten vollständigen Entwurf über die Prüfung bis zur
        überarbeiteten, fertigungsreifen Version mit 15 Zeichnungsblättern.
      </div>
    </section>

{projekt_nav("08-zeichnungssatz-10-april.html", "Zeichnungssatz 10.04.", "10-finale-anpassungen.html", "Finale Anpassungen")}
  </main>
"""

write_page("09-gesamtzusammenbau-stueckliste.html", "Projekt 5: Gesamtzusammenbau & Stückliste", body)
