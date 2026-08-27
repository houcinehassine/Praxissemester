# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt5 import *

body = seiten_kopf(2, "Ideen sammeln",
    "Der Startpunkt: Marktrecherche und Inspirationsquellen für Schweißtische, Werkzeugwissen zu "
    "Klemmenarten und die ersten wichtigen Erkenntnisse. 18.&ndash;19. März 2026.") + f"""
  <main class="projekt-detail">

    <section>
      <div class="info-box">
        Auftrag Nr. Tätigkeit 3 / 000-005 &middot; Zeitraum 18.&ndash;19. März 2026
      </div>
    </section>

    <section>
      <h2>Inspiration &amp; Referenzen für Schweißtische</h2>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>🛠️ Yeabett 3-Level Tool Wall Mount</h4><p>Tool Storage für 4 Power Tools, 42,5 × 20 × 31 cm &ndash; Anregung für Werkzeugverwaltung.</p></div>
        <div class="mini-karte"><h4>🔨 Welding Table DIY mit Klemmen</h4><p>DIY-Plan für Schweißtische mit integrierten Klemmen und Lagermöglichkeiten &ndash; wurde zur Hauptreferenz.</p></div>
        <div class="mini-karte"><h4>🏭 TRAUMWERKSTATT &ndash; Real Life Halle</h4><p>Video: professionelle Werkstattplanung und Einrichtung mit umfassender Ausrüstung.</p></div>
        <div class="mini-karte"><h4>⬆️ Lifting and Welding Table DIY</h4><p>Höhenverstellbarer Schweißtisch mit Hebemechanismus &ndash; Lift &amp; Lower für flexible Arbeitshöhe.</p></div>
        <div class="mini-karte"><h4>✨ DIY Schweißtisch &ndash; Einfach &amp; Praktisch</h4><p>Homemade Schweißtisch mit ausziehbarem Seitenteil &ndash; saubere, praktische Konstruktion.</p></div>
      </div>
    </section>

    <section>
      <h2>Klemmen nutzen &ndash; Werkzeugwissen</h2>
      <p>
        Definition: Der Begriff „Clamps“ (deutsch: Klemmen, Zwingen oder Schellen) bezeichnet je
        nach Kontext Werkzeuge zum Fixieren, technische Bauteile zur Verbindung oder spezifische
        Funktionen in Programmierung und Medizin. In der Holz- und Metallbearbeitung dienen
        Clamps dazu, Werkstücke sicher zu halten oder zusammenzupressen.
      </p>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <tbody>
            <tr><td>🔩 Schraubzwingen</td><td>Der Klassiker zum Festspannen mittels Gewinde &ndash; zuverlässig und kraftvoll.</td></tr>
            <tr><td>👆 Einhandzwingen</td><td>Ermöglichen das Fixieren mit nur einer Hand &ndash; perfekt für schnelle Arbeiten.</td></tr>
            <tr><td>🌀 Federzwingen</td><td>Kleine Klemmen mit Federkraft für leichtere Halteaufgaben &ndash; leicht zu bedienen.</td></tr>
            <tr><td>Ⓒ C-Clamps</td><td>Robuste Klemmen in C-Form, oft im Metallbau oder bei Schweißarbeiten genutzt.</td></tr>
            <tr><td>🔁 Rohrzwingen</td><td>Werden auf Rohre montiert, um sehr große Spannweiten zu erreichen.</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>Verwendete Materialien &amp; Dokumentationen</h2>
      <p>Vierkantrohr-Konstruktionen als Grundmaterial für die Schweißtischstruktur, dokumentiert in fünf PDFs: Teilen-Nummern, Tisch-Unten-Teile, Platte, Tisch-Obere-Teile, Stückliste.</p>
    </section>

    <section>
      <h2>Wichtige Erkenntnisse</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>Schweißtischdesign</strong>höhenverstellbar &amp; mit integrierten Klemmen.</span></li>
        <li><span><strong>Werkzeugverwaltung</strong>Wall-Mount-Systeme für bessere Übersichtlichkeit.</span></li>
        <li><span><strong>Material</strong>Vierkantrohr als Grundstruktur mit Beschichtung.</span></li>
        <li><span><strong>Funktionalität</strong>ausziehbare Teile und modulare Klemmsysteme.</span></li>
        <li><span><strong>5S-Prinzip</strong>Ordnung, Sauberkeit und Effizienz bei der Werkstattplanung.</span></li>
      </ul>
    </section>

{projekt_nav("index.html", "Überblick", "03-grundkonzept-gewaehlt.html", "Grundkonzept gewählt")}
  </main>
"""

write_page("02-ideen-sammeln.html", "Projekt 5: Ideen sammeln", body)
