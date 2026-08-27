# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt4 import *

body = seiten_kopf(10, "Feste Station: Materialregal &amp; Zusammenbau",
    "Lager für Rohmaterial &amp; Reste &ndash; und der finale Zusammenbau der kompletten Station "
    "mit vollständiger Einkaufsliste.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>&#128230; Materialregal</h2>
      <p>Maß 300×300×60 cm (noch nicht final).</p>
      <h3 style="margin-top:0.75rem">1. Inhalt / Material</h3>
      <ul class="ergebnis-liste">
        <li><span><strong>Rohmaterial</strong>Bleche, Flachstahl, Profile, Rohre, Rundmaterial.</span></li>
        <li><span><strong>Reste/Verschnitt</strong>getrennt gelagert.</span></li>
        <li><span><strong>Schwere Teile unten, leichte oben</strong>&ndash; sicher &amp; übersichtlich.</span></li>
      </ul>
      <h3 style="margin-top:0.75rem">2. Platzbedarf (Bemessung)</h3>
      <p>
        ~300 × 300 × 60 cm (Höhe ggf. an Raumhöhe ~2000 anpassen) &ndash; vorläufig. An der langen
        Wand (5900 mm), großes Schwerlast-/Fachbodenregal &ndash; Traglast pro Boden beachten
        (Stahl ist schwer!).
      </p>
    </section>

    <section>
      <h2>&#9989; Finaler Zusammenbau</h2>
      <p>Die komplette Station: aktueller CAD-Stand, was gebraucht wird, und die Einkaufsliste mit den gewählten Produkten.</p>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Teil</th><th>Anzahl</th><th>Wofür</th></tr></thead>
          <tbody>
            <tr><td>Lochwand 1</td><td>1</td><td>Handwerkzeug (schnell zur Hand)</td></tr>
            <tr><td>Lochwand 2</td><td>1</td><td>Spannmittel (Magnete, Zwingen)</td></tr>
            <tr><td>Lochwand 3</td><td>1</td><td>Messen &amp; Anreißen (lange, dünne Teile)</td></tr>
            <tr><td>Schubladenschrank 1</td><td>1</td><td>Verbrauch: Draht, Elektroden, Düsen, Scheiben</td></tr>
            <tr><td>Schubladenschrank 2</td><td>1</td><td>Messwerkzeug, Ersatzteile, Kleinteile</td></tr>
            <tr><td>Reinigung</td><td>1 Ecke</td><td>Sauber halten: Sauger, Kehrset, Abfall</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">
        3D-Anordnung: Tiefenwand (4000 mm) trägt Lochwände + Schubladen, lange Wand (5900 mm)
        trägt Materialregal + PSA-Schrank + Reinigungsschrank, der Schweißtisch steht mittig.
      </p>
    </section>

    <section>
      <h2>Gewählte Produkte &ndash; Einkaufsliste Station</h2>
      <p class="section-intro">Günstige, stimmige Zusammenstellung. Preise sind Richtwerte &ndash; im Shop prüfen.</p>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Bauteil</th><th>Gewählt</th><th>Menge</th><th>Preis</th></tr></thead>
          <tbody>
            <tr><td>Lochwände</td><td>AREBOS 120×60 (2×) + Kreher XL 98×46 (1×)</td><td>3×</td><td>~95 €</td></tr>
            <tr><td>Schubladenschrank</td><td>MASKO Werkstattwagen 7 Schubl.</td><td>2×</td><td>~240 €</td></tr>
            <tr><td>PSA-Schrank</td><td>PSA-Schrank B0FR495VJR</td><td>1×</td><td>Amazon</td></tr>
            <tr><td>Reinigungsschrank</td><td>Reinigungsschrank B09NRV2RLW (Variante 2)</td><td>1×</td><td>Amazon</td></tr>
            <tr><td>Materialregal</td><td>Eigenbau/Regal &middot; 300×300×60 cm (nicht final)</td><td>1×</td><td>&mdash;</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Summe (Richtwert):</strong> Lochwände ~95 € + Schränke ~240 € + PSA-/Reinigungsschrank
        (Amazon-Preise prüfen) + Materialregal (offen). Grobe Basis ~ 600&ndash;900 € ohne
        Materialregal &amp; PSA-Artikel. Alle Anbieter &amp; Preisstufen auf Seite 12.
      </div>
    </section>

{projekt_nav("09-feste-station-reinigung-psa.html", "Station: Reinigung & PSA", "11-sicherheit.html", "Sicherheit")}
  </main>
"""

write_page("10-feste-station-material-zusammenbau.html", "Projekt 4: Station – Material & Zusammenbau", body)
