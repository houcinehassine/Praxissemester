# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt5 import *

body = seiten_kopf(3, "Grundkonzept gewählt",
    "Die Entscheidung für das Grundkonzept: ein Schweißtisch von ca. 1500 × 700 mm mit "
    "Lochplatten zur Aufnahme von Spannklemmen und einem modularen Erweiterungssystem. "
    "9. April 2026.") + f"""
  <main class="projekt-detail">

    <section>
      <div class="info-box">
        Aufgabe Nr. 2 &middot; Datum 9. April 2026 &middot; Bezeichnung Tätigkeit 3 / 000-006
      </div>
    </section>

    <section>
      <h2>Gewähltes Konzept &ndash; 3D-Modell</h2>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">CAD-Modell des gewählten Konzepts</span>
          <img src="img/grundkonzept-3d-modell.png" alt="3D-CAD-Modell des gewählten Schweißtisch-Konzepts mit vier Lochplatten in Reihe, seitlichen Auslegern und vier Beinen mit Fußplatten" />
          <p class="bildtext">Frühe Konzeptdarstellung: Lochplatten in Reihe, seitliche Ausleger für überlange Werkstücke, vier Beine mit Fußplatten &ndash; die Grundform, aus der sich die spätere Konstruktion entwickelt hat.</p>
        </div>
      </div>
    </section>

    <section>
      <h2>Formulierung &ndash; Konzeptmerkmale</h2>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>📏 Tisch-Dimensionen</h4><p>Die Tischabmessungen betragen ca. 1500 × 700 mm.</p></div>
        <div class="mini-karte"><h4>🕳️ Lochplatten-System</h4><p>Lochplatten zur Aufnahme von Spannklemmen, um Werkstücke sicher zu fixieren.</p></div>
        <div class="mini-karte"><h4>➕ Erweiterungssystem</h4><p>Modulares Erweiterungssystem zur Bearbeitung überlanger Werkstücke.</p></div>
      </div>
    </section>

    <section>
      <h2>Referenz &amp; Hilfsmittel</h2>
      <p>
        Hauptreferenz für das gewählte Grundkonzept: „Welding Table DIY with Clamps and some
        other Ideas“ (YouTube-Video, Bauplan auf Etsy) &ndash; ein Schweißtisch mit Klemmen und
        Stauraum. Für die Ausarbeitung wurden ChatGPT, GoodNotes (PDF-Annotation) und Google
        Drive (Ablage) eingesetzt.
      </p>
    </section>

    <section>
      <h2>Entscheidung</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>Konzept festgelegt</strong>Schweißtisch 1500 × 700 mm mit 4 Lochplatten.</span></li>
        <li><span><strong>Kernfunktion</strong>Ø20-Lochraster für flexible Spannklemmen-Positionierung.</span></li>
        <li><span><strong>Besonderheit</strong>seitliche Ausleger für überlange Werkstücke.</span></li>
        <li><span><strong>Nächster Schritt</strong>Detailkonstruktion &amp; Stückliste.</span></li>
      </ul>
    </section>

{projekt_nav("02-ideen-sammeln.html", "Ideen sammeln", "04-erste-zeichnungen.html", "Erste Zeichnungen")}
  </main>
"""

write_page("03-grundkonzept-gewaehlt.html", "Projekt 5: Grundkonzept gewählt", body)
