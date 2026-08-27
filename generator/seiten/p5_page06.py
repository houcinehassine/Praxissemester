# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt5 import *

body = seiten_kopf(6, "Oberteil &amp; Unterteil",
    "Aus dem Grundkonzept werden konkrete Baugruppen: Oberteil und Unterteil werden erstmals "
    "durchkonstruiert. 10. April 2026.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>🔝 Oberteil 000-005-104</h2>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Oberteil-Basis, Zeichnung Blatt 1</span>
          <img src="img/oberteil-basis-blatt1-10april.jpg" alt="Technische Zeichnung Oberteil-Basis 000-005-104-1 vom 10.04.2026: isometrische Ansicht mit drei Lochplatten auf Rahmen, Schriftfeld mit Gewicht 18,63 kg" />
          <p class="bildtext">Isometrische Ansicht &middot; zwei Darstellungen &ndash; oben der Rahmen mit teilweise abgehobenen Platten, unten der fertige Zusammenbau. Gewicht laut Schriftfeld: 18,63 kg.</p>
        </div>
      </div>
      <h3 style="margin-top:1rem">Teileliste</h3>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Teile-Nr.</th><th>Bauteil</th><th>Profil / Maß</th><th>Länge</th><th>Bearbeitung</th></tr></thead>
          <tbody>
            <tr><td>000-005-005-4</td><td>4-Kantrohr</td><td>80 × 80 × 3</td><td>1500 mm</td><td>gebohrt</td></tr>
            <tr><td>000-005-005-3</td><td>4-Kantrohr</td><td>80 × 80 × 3</td><td>1330 mm</td><td>gebohrt</td></tr>
            <tr><td>000-005-004-2</td><td>4-Kantrohr</td><td>80 × 80 × 3</td><td>500 mm</td><td>gebohrt</td></tr>
            <tr><td>000-005-013-2</td><td>Lochplatte D16</td><td>800 × 500 × 12</td><td>&ndash;</td><td>gebohrt &middot; 3×</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">Wandstärke: Alle Vierkantrohre einheitlich 80 × 80 × 3 mm &rarr; ein Materialtyp für den gesamten oberen Rahmen.</p>
      <div class="karten-grid-4" style="margin-top:0.75rem">
        <div class="mini-karte"><h4>🔥 Rahmenbau</h4><p>Grundkonstruktion aus Vierkantrohren, zunächst miteinander verschweißt.</p></div>
        <div class="mini-karte"><h4>🔩 Verbindungstechnik</h4><p>Platten werden mittels Schraubverbindungen fest mit den Vierkantrohren fixiert.</p></div>
        <div class="mini-karte"><h4>🎯 Vorbereitung</h4><p>Für die Montage ist eine präzise Bohrung der Vierkantrohre erforderlich.</p></div>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Kritische Betrachtung:</strong> Überstehende Schraubköpfe beeinträchtigen die
        Ebenheit der Arbeitsfläche und können den Arbeitsfluss stören.
      </div>
    </section>

    <section>
      <h2>💡 Drei Lösungsmethoden für das Verschraubungsproblem</h2>
      <div class="stepper">
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">1</span>
            <span class="schritt-titel">Senkbohrung &amp; Taschenfräsung</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p><strong>Verfahren:</strong> Durchgangsbohrung Ø12 mm mit zylindrischer Vertiefung Ø16 mm, Tiefe 10 mm. <strong>Ziel:</strong> vollständiges Versenken des Schraubenkopfes in der Platte &rarr; plane Oberfläche.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">2</span>
            <span class="schritt-titel">Direktverschraubung im Bauteil</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p><strong>Verfahren:</strong> Einbringen von Innengewinden in die bestehenden Bohrungen. <strong>Ziel:</strong> kraftschlüssige Verbindung ohne zusätzliche Muttern oder Bauteile.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">3</span>
            <span class="schritt-titel">Untergelegtes Gewindeblech (Schweißverbindung)</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p><strong>Verfahren:</strong> Fixierung eines Lochblechs mittels Schweißnähten unter der Hauptplatte. <strong>Ziel:</strong> vorhandene Bohrungen als Durchgangslöcher nutzen; Verschraubung im angeschweißten Hilfsblech.</p></div>
        </div>
      </div>
    </section>

    <section>
      <h2>🔽 Unterteil &ndash; Basis: 000-005-105</h2>
      <h3>Teileliste</h3>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Teile-Nr.</th><th>Bauteil</th><th>Profil / Maß</th><th>Länge</th><th>Funktion</th></tr></thead>
          <tbody>
            <tr><td>000-005-005-1</td><td>4-Kantrohr</td><td>80 × 80 × 3</td><td>1500 mm</td><td>Längsstrebe Rahmen</td></tr>
            <tr><td>000-005-006-1</td><td>4-Kantrohr</td><td>80 × 80 × 3</td><td>750 mm</td><td>Tischbein / Standhöhe</td></tr>
            <tr><td>000-005-004-1</td><td>4-Kantrohr</td><td>80 × 80 × 3</td><td>500 mm</td><td>Querstrebe Rahmen</td></tr>
            <tr><td>000-005-012-2</td><td>Platte</td><td>120 × 120 × 10</td><td>&ndash;</td><td>Adapterplatte für Lenkrollen &middot; gebohrt</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">Unterschied zum Oberteil: Hier sind die Rohre ungebohrt (reine Schweißkonstruktion) &ndash; nur die Adapterplatte 120×120×10 ist gebohrt.</p>
      <div class="karten-grid-4" style="margin-top:0.75rem">
        <div class="mini-karte"><h4>🔥 Rahmenkonstruktion</h4><p>Stabiler Grundkörper aus verschweißten Vierkantrohren.</p></div>
        <div class="mini-karte"><h4>🛞 Mobilität</h4><p>Montage von Lenkrollen über angeschweißte Adapterplatten an der Unterseite.</p></div>
        <div class="mini-karte"><h4>🧰 Flexibilität</h4><p>Modularer Aufbau bietet zusätzlichen Stauraum für Werkzeuge und Materialien.</p></div>
      </div>
    </section>

    <section>
      <h2>Kurzfassung</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>Baugruppe</strong>Untergestell des Schweißtischs (Beine + unterer Rahmen).</span></li>
        <li><span><strong>Material</strong>durchgängig Vierkantrohr 80 × 80 × 3 mm.</span></li>
        <li><span><strong>Verbindung</strong>vollständig geschweißt &ndash; keine Schraubverbindung nötig.</span></li>
        <li><span><strong>Neu gegenüber der ersten Zeichnung</strong>Adapterplatte 120 × 120 × 10 statt Fußplatte 160 × 160 × 10 &rarr; für Lenkrollen statt Bodenverankerung.</span></li>
      </ul>
    </section>

{projekt_nav("05-lochplatte.html", "Lochplatte auswählen", "07-erweiterung-gesamtzusammenbau.html", "Erweiterung & Gesamtzusammenbau")}
  </main>
"""

write_page("06-oberteil-unterteil.html", "Projekt 5: Oberteil & Unterteil", body)
