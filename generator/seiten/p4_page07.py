# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt4 import *

body = seiten_kopf(7, "Feste Station: Idee &amp; Aufbau",
    "Das Zuhause aller Werkzeuge für die 3 Mitarbeiter, geordnet nach 5S &ndash; aufgebaut an den "
    "zwei nutzbaren Wänden der realen Hallen-Ecke.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>1 &middot; Idee &amp; Zweck</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>Warum</strong>ruhender Pol &ndash; kompletter Werkzeugsatz für alle 3 Mitarbeiter, fester Platz je Werkzeug (5S).</span></li>
        <li><span><strong>Ergänzt den Wagen</strong>Station = Zuhause aller Werkzeuge, Wagen = die wichtigsten reisen mit.</span></li>
        <li><span><strong>Bauweise</strong>fertige Kaufteile (Lochwände + Schränke), kein Eigenbau-Rahmen.</span></li>
      </ul>
    </section>

    <section>
      <h2>2 &middot; Aufbau &ndash; wie sie gebaut ist</h2>
      <p>
        Aktuell steht nur der vorhandene Schweißtisch + die MIG-Maschine &ndash; die Station wird
        komplett neu aufgebaut. Nutzbar sind die zwei Wände der Ecke: die lange Wand (5900 mm)
        und die Tiefenwand (4000 mm).
      </p>
      <div class="bild-vergleich" style="margin-top:0.75rem">
        <div class="bild-box">
          <span class="label">Lange Wand &ndash; 5900 mm</span>
          <p class="bildtext">Von links nach rechts: Reinigung (600) &middot; Schubladenschrank 1 (680)
          &middot; Schubladenschrank 2 (680) &middot; Lochwand 1 „Handwerkzeug“, quer (1000) &middot;
          Lochwand 2 „Spannen“, quer (980) &middot; PSA-Schrank (1200).</p>
        </div>
        <div class="bild-box">
          <span class="label">Tiefenwand &ndash; 4000 mm</span>
          <p class="bildtext">Materialregal (900) &middot; Lochwand 3 „Messen/Anreißen“, hochkant (600)
          &middot; Reinigung/Sauger (600) &middot; Feuerlöscher (300).</p>
        </div>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Anordnung flexibel:</strong> Lochwand-Größen &amp; -Ausrichtung sind an den Platz
        angepasst (eine groß/quer, eine hochkant) &ndash; nicht fix. Endgültig festgelegt, sobald
        die Möbel gewählt sind (siehe Seite 8).
      </div>
    </section>

    <section>
      <h2>3 &middot; Werkzeugliste &ndash; was gehört wohin</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <tbody>
            <tr><td>Lochwand 1 &middot; Handwerkzeug</td><td>Schlackenhammer, Drahtbürste, Meißel, Kombizange, Grip-/Schweißzange</td></tr>
            <tr><td>Lochwand 2 &middot; Spannen</td><td>Schweißmagnete (45/90°), Schraubzwingen (klein/mittel), Grip-Zangen</td></tr>
            <tr><td>Lochwand 3 &middot; Messen/Anreißen</td><td>Anschlagwinkel, Maßband, Lineal, Wasserwaage, Anreißnadel, Körner, Silberstift</td></tr>
            <tr><td>Schubladenschrank 1</td><td>Draht/Düsen &middot; Elektroden (Trockenbox) &middot; Trenn-/Schleifscheiben &middot; Kleinteile</td></tr>
            <tr><td>Schubladenschrank 2</td><td>Messwerkzeug, Ersatzteile, Verbrauch (Anti-Spritzer u. a.)</td></tr>
            <tr><td>PSA-Schrank (3 Fächer)</td><td>je Mitarbeiter: Helm, Handschuhe, Schürze &middot; gemeinsam: Brille, Gehörschutz, Atemschutz</td></tr>
            <tr><td>Materialregal</td><td>Rohmaterial (Bleche/Profile/Rohre), Reste getrennt</td></tr>
            <tr><td>Standfläche / Wand</td><td>großer Winkelschleifer, Schraubstock (fest), Industriesauger, Feuerlöscher, Erste Hilfe</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>4 &middot; Maße der Produkte (optimal)</h2>
      <p class="section-intro">Richtmaße, passend zum Platz (Tiefe an der Wand ~500 mm).</p>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Produkt</th><th>Optimale Maße (B × T × H)</th><th>Lage</th></tr></thead>
          <tbody>
            <tr><td>Lochwand 1 &middot; Handwerkzeug</td><td>~1000 × 46 × 600</td><td>lange Wand, quer</td></tr>
            <tr><td>Lochwand 2 &middot; Spannen</td><td>~980 × 46 × 600</td><td>lange Wand, quer</td></tr>
            <tr><td>Lochwand 3 &middot; Messen/Anreißen</td><td>~600 × 46 × 1200</td><td>Tiefenwand, hochkant</td></tr>
            <tr><td>Schubladenschrank &times;2</td><td>680 × 460 × 910</td><td>lange Wand, Boden</td></tr>
            <tr><td>PSA-Schrank</td><td>1200 × 500 × 1800</td><td>lange Wand, Boden</td></tr>
            <tr><td>Materialregal</td><td>300 × 300 × 60 cm (vorläufig)</td><td>große Wand &middot; noch nicht final</td></tr>
          </tbody>
        </table>
      </div>
    </section>

{projekt_nav("06-gesamtplan-layout.html", "Gesamtplan & Layout", "08-feste-station-lochwaende-schubladen.html", "Station: Lochwände & Schubladen")}
  </main>
"""

write_page("07-feste-station-idee-aufbau.html", "Projekt 4: Station – Idee & Aufbau", body)
