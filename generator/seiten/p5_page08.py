# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt5 import *

body = seiten_kopf(8, "Zeichnungssatz 10.04.2026",
    "Zum Entwurfsstand vom 10.04.2026 entstehen vollständige Zeichnungssätze mit Stücklisten für "
    "jede Baugruppe &ndash; je Baugruppe ein Zeichnungsblatt und ein Stücklistenblatt.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>Stückliste 000-005-104-1 &ndash; Oberteil Basic</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Pos.</th><th>Menge</th><th>Teilenummer / Benennung</th><th>Quelle</th></tr></thead>
          <tbody>
            <tr><td>1</td><td>2</td><td>000-005-005-4 &middot; 4-Kantrohr 80×80×3 &ndash; 1500 gebohrt</td><td>Hergestellt</td></tr>
            <tr><td>2</td><td>2</td><td>000-005-004-2 &middot; 4-Kantrohr 80×80×3 &ndash; 500 gebohrt</td><td>Hergestellt</td></tr>
            <tr><td>3</td><td>1</td><td>000-005-005-3 &middot; 4-Kantrohr 80×80×3 &ndash; 1330 gebohrt</td><td>Hergestellt</td></tr>
            <tr><td>&ndash;</td><td>3</td><td>000-005-101-2 &middot; Lochplatte + Schrauben</td><td>Hergestellt (Baugruppe)</td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Auffälligkeit:</strong> Die Baugruppe heißt „Lochplatte + Schrauben“, enthält in
        der Stückliste aber nur die Platte &ndash; die Schrauben fehlen. Das passt zum offenen
        Punkt der Vorseite: die Verschraubungsmethode war zu diesem Zeitpunkt noch nicht
        entschieden (3 Varianten in Prüfung).
      </div>
    </section>

    <section>
      <h2>Stückliste 000-005-105-1 &ndash; Unterteil Basic</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Pos.</th><th>Menge</th><th>Teilenummer / Benennung</th><th>Quelle</th></tr></thead>
          <tbody>
            <tr><td>1</td><td>2</td><td>000-005-005-1 &middot; 4-Kantrohr 80×80×3 &ndash; 1328</td><td>Gekauft</td></tr>
            <tr><td>2</td><td>4</td><td>000-005-006-1 &middot; 4-Kantrohr 80×80×3 &ndash; 750</td><td>Gekauft</td></tr>
            <tr><td>3</td><td>2</td><td>000-005-004-1 &middot; 4-Kantrohr 80×80×3 &ndash; 500</td><td>Gekauft</td></tr>
            <tr><td>4</td><td>4</td><td>000-005-012-2 &middot; Platte 120×120×10 gebohrt</td><td>Hergestellt</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Beschaffungslogik:</strong> Beim Unterteil sind die Rohre reine Ablängteile
        (Zukauf); nur Teile mit Bohrungen oder Sonderform werden intern gefertigt.
      </div>
    </section>

    <section>
      <h2>Stückliste 000-005-103-3 &ndash; Erweiterungssystem</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Pos.</th><th>Menge</th><th>Teilenummer / Benennung</th><th>Quelle</th></tr></thead>
          <tbody>
            <tr><td>&ndash;</td><td>2</td><td>000-005-102-1 &middot; Erweiterungssystem &ndash; Mobile Teil</td><td>Gekauft (Baugruppe)</td></tr>
            <tr><td>1</td><td>2</td><td>000-005-003-1 &middot; 4-Kantrohr 50×50×2 &ndash; 1500</td><td>Gekauft</td></tr>
            <tr><td>2</td><td>4</td><td>DIN EN ISO Sechskantschraube M16×30</td><td>Gekauft</td></tr>
            <tr><td>3</td><td>4</td><td>DIN EN ISO 4032 Sechskantmutter M16</td><td><span class="st-warn">Unbekannt</span></td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box">
        <strong>Offener Punkt:</strong> Bei Position 3 (M16-Mutter) ist die Quelle „Unbekannt“
        hinterlegt &ndash; vor der Beschaffung sollte hier „Gekauft“ mit Lieferant ergänzt werden.
      </div>
      <h3 style="margin-top:1rem">Stückliste 000-005-102-1 &ndash; Mobile Teil (Unterbaugruppe)</h3>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Pos.</th><th>Menge</th><th>Teilenummer / Benennung</th><th>Quelle</th></tr></thead>
          <tbody>
            <tr><td>4</td><td>2</td><td>000-005-002-1 &middot; 4-Kantrohr 40×40×2 &ndash; 750</td><td>Gekauft</td></tr>
            <tr><td>5</td><td>2</td><td>000-005-002-2 &middot; 4-Kantrohr 40×40×2 &ndash; 750 + gebohrt</td><td>Hergestellt</td></tr>
            <tr><td>6</td><td>5</td><td>DIN EN ISO 4032 Sechskantmutter M20</td><td>Gekauft</td></tr>
            <tr><td>7</td><td>2</td><td>DIN EN ISO 4762 Zylinderschraube ISK M20×200</td><td>Gekauft</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">Zwei Schraubengrößen, zwei Funktionen: M20×200 (lang, Innensechskant) = Höhenverstellung &middot; M16×30 (kurz, Sechskant) = Klemmung der Längenfixierung.</p>
    </section>

    <section>
      <h2>🔍 Wichtige Abweichung zur Konzeptbeschreibung</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Angabe</th><th>Konzepttext</th><th>Stückliste</th></tr></thead>
          <tbody>
            <tr><td>Führungsrohr</td><td>50 × 50 × 4 mm</td><td>50 × 50 × 2 mm &ndash; Länge 1500</td></tr>
            <tr><td>Auszugsrohr</td><td>40 × 40 × 2 mm</td><td>40 × 40 × 2 mm &ndash; Länge 750 ✔</td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Konsequenz für die Passung:</strong> Bei Wandstärke 2 mm beträgt das Innenmaß des
        Führungsrohrs 50 &minus; 2×2 = 46 mm. Das Auszugsrohr misst außen 40 mm &rarr; 6 mm Spiel
        statt der bei 4 mm Wand errechneten ~2 mm &ndash; für ein reibungsloses Gleiten viel Spiel.
        Diese Frage wird im Endstand (Seite 13) endgültig geklärt.
      </div>
    </section>

{projekt_nav("07-erweiterung-gesamtzusammenbau.html", "Erweiterung & Gesamtzusammenbau", "09-gesamtzusammenbau-stueckliste.html", "Gesamtzusammenbau & Stückliste")}
  </main>
"""

write_page("08-zeichnungssatz-10-april.html", "Projekt 5: Zeichnungssatz 10.04.", body)
