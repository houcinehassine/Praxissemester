# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt4 import *

body = seiten_kopf(8, "Feste Station: Lochwände &amp; Schubladen",
    "Drei Lochwände für Handwerkzeug, Spannen und Messen &ndash; sowie zwei Schubladenschränke "
    "für Verbrauchsmaterial und Messwerkzeug. Inhalt, Platzbedarf und die gewählten Produkte.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>&#129506; Lochwände</h2>
      <div class="info-box">
        <strong>Gewählt:</strong> 2× AREBOS Lochwand 120×60 (manomano) + 1× Kreher XL 98×46 (norma24)
      </div>
      <h3 style="margin-top:1rem">1. Inhalt / Werkzeuge</h3>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>LW1 &middot; Handwerkzeug (hochkant)</h4><p>Schlackenhammer, Drahtbürste, Meißel, Kombizange, Grip-/Schweißzange, Feilen.</p></div>
        <div class="mini-karte"><h4>LW2 &middot; Spannen (quer)</h4><p>Schweißmagnete (45/90°), Schraubzwingen, Grip-/Klemmzangen.</p></div>
        <div class="mini-karte"><h4>LW3 &middot; Messen/Anreißen (hochkant)</h4><p>Anschlagwinkel, Maßband, Lineal, Wasserwaage, Anreißnadel, Körner, Silberstift.</p></div>
      </div>
      <h3 style="margin-top:1rem">2. Platzbedarf (Bemessung)</h3>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Lochwand</th><th>Ziel-Maß</th><th>Gewähltes Produkt</th></tr></thead>
          <tbody>
            <tr><td>LW1</td><td>~600×1200 (hochkant)</td><td>AREBOS 60×120</td></tr>
            <tr><td>LW2</td><td>~1200×600 (quer)</td><td>AREBOS 120×60</td></tr>
            <tr><td>LW3</td><td>~460×980 (hochkant)</td><td>Kreher 46×98</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">
        Die drei Lochwände hängen an der rechten Wand (Tiefenwand), mit den zwei
        Schubladenschränken darunter &ndash; Abstände von ca. 200&ndash;430 mm zwischen den Elementen.
      </p>
    </section>

    <section>
      <h2>&#128193; Schubladen</h2>
      <div class="info-box">
        <strong>Gewählt:</strong> 2× MASKO Werkstattwagen 7 Schubladen (Amazon B0FFNCBQ79)
      </div>
      <h3 style="margin-top:1rem">1. Inhalt / Werkzeuge</h3>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>Schrank 1 &middot; Verbrauch</h4><p>Schub 1: Schweißdraht-Rollen. Schub 2: Elektroden (Trockenbox), Düsen. Schub 3: Trenn-/Schleifscheiben. Schub 4: Kleinteile, Anti-Spritzer.</p></div>
        <div class="mini-karte"><h4>Schrank 2 &middot; Messen/Ersatz</h4><p>Messschieber, Schweißnahtlehre, Ersatz-Kontaktdüsen, Verschleißteile, Schrauben/Kleinteile sortiert, Verbrauch/Nachschub.</p></div>
      </div>
      <h3 style="margin-top:1rem">2. Platzbedarf (Bemessung)</h3>
      <p>Je Schrank ~680 × 460 × 910 mm, 2 nebeneinander mit 430 mm Abstand, ~20 mm unter den Lochwänden.</p>
    </section>

{projekt_nav("07-feste-station-idee-aufbau.html", "Station: Idee & Aufbau", "09-feste-station-reinigung-psa.html", "Station: Reinigung & PSA")}
  </main>
"""

write_page("08-feste-station-lochwaende-schubladen.html", "Projekt 4: Station – Lochwände & Schubladen", body)
