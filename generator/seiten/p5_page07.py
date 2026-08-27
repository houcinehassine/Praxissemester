# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt5 import *

body = seiten_kopf(7, "Erweiterungssystem &amp; Gesamtzusammenbau",
    "Das Teleskop-Erweiterungssystem für überlange Werkstücke &ndash; und wie Oberteil, Unterteil "
    "und Erweiterung zum Gesamtkonzept zusammenfinden. 10. April 2026.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>↔️ Erweiterungssystem: 000-005-103</h2>
      <div class="kennzahlen-grid">
        <div class="kennzahl"><strong>500</strong><span>mm Ausladung je Seite</span></div>
        <div class="kennzahl"><strong>1000</strong><span>mm Gesamtausladung max.</span></div>
        <div class="kennzahl"><strong>Teleskop</strong><span>stufenlos arretierbar</span></div>
      </div>
    </section>

    <section>
      <h2>Funktion &amp; Zielsetzung</h2>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>📐 Erweiterung der Arbeitsfläche</h4><p>Flexibler Arbeitsplatz für die Bearbeitung überlanger Bauteile.</p></div>
        <div class="mini-karte"><h4>↔️ Variable Ausladung</h4><p>Beidseitige Verlängerung um jeweils bis zu 500 mm.</p></div>
        <div class="mini-karte"><h4>🧍 Ergonomie</h4><p>Individuelle Höhenanpassung für optimale Arbeitshaltung.</p></div>
      </div>
    </section>

    <section>
      <h2>Technische Ausführung &ndash; Teleskop-Rahmen</h2>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">CAD-Ansicht des Teleskop-Erweiterungsarms</span>
          <img src="img/erweiterungssystem-cad.png" alt="CAD-Darstellung des Teleskop-Erweiterungssystems: Führungsrohr mit Klemmschrauben und drei Auflageleisten mit Höhenverstellung" />
          <p class="bildtext">Zwei parallele Teleskop-Arme, an beiden Enden je eine Querleiste mit Höhenverstellung; die Klemmschrauben sitzen mittig auf den Führungsrohren.</p>
        </div>
      </div>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Segment</th><th>Material</th><th>Funktion</th></tr></thead>
          <tbody>
            <tr><td><strong>A &middot; Feststehendes Segment</strong></td><td>Vierkantrohr 50 × 50 × 4 mm</td><td>Integrierte Führung für den mobilen Teil; Arretierung mittels Klemmschraube &rarr; stufenlose Längenfixierung.</td></tr>
            <tr><td><strong>B &middot; Mobiles Segment (Auszug)</strong></td><td>Vierkantrohr 40 × 40 × 2 mm</td><td>Präzise Passung für reibungsloses Gleiten im Hauptrahmen.</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">Prinzip: 40×40 gleitet in 50×50 &rarr; Spiel ca. 1 mm pro Seite (50 &minus; 2×4 = 42 mm Innenmaß).</p>
    </section>

    <section>
      <h2>Teile &amp; Dokumente</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>000-005-003-1</strong>4-Kantrohr 40 × 40 × 2 &ndash; 1500 mm.</span></li>
        <li><span><strong>000-005-102-1</strong>Erweiterungssystem &ndash; Mobile Teil.</span></li>
      </ul>
    </section>

    <section>
      <h2>🧩 Gesamtzusammenbau: 000-005-200-1 (Baugruppenstruktur)</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Baugruppe</th><th>Zeichnungsnr.</th><th>Inhalt</th></tr></thead>
          <tbody>
            <tr><td>🔝 Oberteil</td><td>000-005-104</td><td>Rahmen 80×80×3 + 3 Lochplatten</td></tr>
            <tr><td>🔽 Unterteil / Basis</td><td>000-005-105</td><td>Beine 750 mm + Adapterplatten</td></tr>
            <tr><td>↔️ Erweiterungssystem</td><td>000-005-103</td><td>Teleskop 50×50 / 40×40</td></tr>
            <tr><td>🕳️ Lochplatten</td><td>000-005-013</td><td>3× D16 &middot; 800×500×12</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>Kennwerte des Gesamtsystems (Stand 10.04.)</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Merkmal</th><th>Wert</th></tr></thead>
          <tbody>
            <tr><td>Tischmaß (Grundkonzept)</td><td>ca. 1500 × 700 mm</td></tr>
            <tr><td>Arbeitsplatten</td><td>3 × 800 × 500 × 12 mm (D16)</td></tr>
            <tr><td>Rahmenprofil</td><td>80 × 80 × 3 mm Vierkantrohr</td></tr>
            <tr><td>Standhöhe (Beine)</td><td>750 mm</td></tr>
            <tr><td>Mobilität</td><td>Lenkrollen auf Adapterplatte 120 × 120 × 10</td></tr>
            <tr><td>Erweiterung</td><td>max. 1.000 mm (2 × 500 mm, Teleskop)</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        Zusammenfassung: Der Gesamtzusammenbau vereint Unterteil (fahrbar) + Oberteil
        (Lochplatten) + Erweiterungssystem (teleskopierbar) zu einem modularen
        Schweißarbeitsplatz nach 5S-Prinzip.
      </div>
    </section>

{projekt_nav("06-oberteil-unterteil.html", "Oberteil & Unterteil", "08-zeichnungssatz-10-april.html", "Zeichnungssatz 10.04.")}
  </main>
"""

write_page("07-erweiterung-gesamtzusammenbau.html", "Projekt 5: Erweiterung & Gesamtzusammenbau", body)
