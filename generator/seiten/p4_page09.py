# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt4 import *

body = seiten_kopf(9, "Feste Station: Reinigung &amp; PSA",
    "Die Reinigungsecke hält den Platz sauber (5S-Schritt 3), der PSA-Schrank sichert jedem der "
    "3 Mitarbeiter ein eigenes Fach für die persönliche Schutzausrüstung.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>&#129537; Reinigung</h2>
      <div class="info-box">
        <strong>Gewählt:</strong> Variante 2 &ndash; Reinigungsschrank (Amazon B09NRV2RLW)
      </div>
      <h3 style="margin-top:1rem">1. Inhalt / Werkzeuge</h3>
      <ul class="ergebnis-liste">
        <li><span><strong>Industriesauger</strong>(Nass/Trocken) &ndash; Staub &amp; Späne.</span></li>
        <li><span><strong>Kehrgarnitur</strong>&ndash; grober Schmutz.</span></li>
        <li><span><strong>Abfallbehälter</strong>&ndash; Metallreste getrennt.</span></li>
        <li><span><strong>Lappen / Handreiniger</strong></span></li>
      </ul>
      <h3 style="margin-top:1rem">2. Platzbedarf (Bemessung)</h3>
      <p>
        Variante 1 wäre eine offene Ecke gewesen (~900 mm Breite, Anordnung Kehrgarnitur,
        Lappen/Handreiniger, Industriesauger, Abfall). Gewählt wurde stattdessen Variante 2: der
        fertige Reinigungsschrank, 180 × 60 × 34 cm.
      </p>
    </section>

    <section>
      <h2>&#129508; PSA-Schrank</h2>
      <div class="info-box">
        <strong>Gewählt:</strong> PSA-Schrank &ndash; Amazon B0FR495VJR
      </div>
      <p>
        Metall-Spind, 2 Türen, abschließbar. Innen: Ablagen + Kleiderstange + Schuhbereich &ndash;
        ideal für Helm, Handschuhe, Schürze, Jacke, Sicherheitsschuhe. Pro Mitarbeiter ein Abteil.
      </p>
      <h3 style="margin-top:1rem">1. Inhalt / Werkzeuge</h3>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>Persönlich (je 3×)</h4><p>3× Automatik-Schweißhelm, 3× Schweißerhandschuhe (+Ersatz), 3× Lederschürze/Jacke.</p></div>
        <div class="mini-karte"><h4>Gemeinsam</h4><p>Schutzbrillen, Gehörschutz, Atemschutz/Masken.</p></div>
      </div>
      <h3 style="margin-top:1rem">2. Platzbedarf (Bemessung)</h3>
      <p>PSA-Schrank mit 3 Fächern &ndash; je Mitarbeiter eines. Zielmaß ~1200 × 500 × 1800 mm.</p>
    </section>

{projekt_nav("08-feste-station-lochwaende-schubladen.html", "Station: Lochwände & Schubladen", "10-feste-station-material-zusammenbau.html", "Station: Material & Zusammenbau")}
  </main>
"""

write_page("09-feste-station-reinigung-psa.html", "Projekt 4: Station – Reinigung & PSA", body)
