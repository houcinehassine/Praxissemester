# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt4 import *

body = seiten_kopf(6, "Gesamtplan &amp; Layout",
    "Wo alles in der Ecke steht: Schweißtisch, feste Station, Wagen, Material und mehr &ndash; "
    "danach folgen alle Bauteile einzeln in ihren Detailseiten.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>Bestandteile des Arbeitsplatzes</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Bauteil</th><th>Rolle im Plan</th><th>Detail</th></tr></thead>
          <tbody>
            <tr><td>Schweißtisch</td><td>Kernzone; ausziehbar, fahrbar, Stahl-Lochraster</td><td><a href="../projekt-5/index.html">Projekt 5</a></td></tr>
            <tr><td>Feste Station</td><td>Lochwand + Schränke, voller Werkzeugsatz (5S)</td><td>Seiten 7&ndash;10</td></tr>
            <tr><td>Schweißmaschinenwagen</td><td>MIG + Gas + wichtigste Werkzeuge, fahrbar</td><td><a href="../projekt-6/index.html">Projekt 6</a></td></tr>
            <tr><td>Materialregal / Lager</td><td>Rohmaterial &amp; Reste, getrennt</td><td>Seite 10</td></tr>
            <tr><td>Absaugung + Schweißvorhang</td><td>Rauch weg, Blendschutz (2 Plätze)</td><td>unten</td></tr>
            <tr><td>Sicherheit</td><td>Feuerlöscher, Erste Hilfe, Beleuchtung</td><td>Seite 11</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>Ergonomie &ndash; die wichtigen Grundmaße</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Maß</th><th>Richtwert</th><th>Warum</th></tr></thead>
          <tbody>
            <tr><td>Arbeitshöhe Tisch</td><td>850&ndash;900 mm</td><td>Stehend arbeiten ohne Bücken; bei viel Kraft eher niedriger</td></tr>
            <tr><td>Greifraum (oft genutzt)</td><td>&le; 600 mm</td><td>Häufige Werkzeuge in Armreichweite</td></tr>
            <tr><td>Freie Gangbreite</td><td>&ge; 1000 mm</td><td>Platz zum Bewegen, auch mit Werkstück</td></tr>
            <tr><td>Abstand 2 Schweißer</td><td>+ Vorhang</td><td>Blendschutz, weil teils 2 gleichzeitig</td></tr>
            <tr><td>Absaugarm-Reichweite</td><td>über Tischmitte</td><td>Rauch direkt an der Quelle absaugen</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>Der Schweißtisch im Plan</h2>
      <p>
        Echte Maße: ausziehbar 1700 ↔ 2860 mm &middot; Breite 980 mm &middot; Höhe ~950 mm &ndash;
        fahrbar, Stahl-Lochraster. Geschlossen kompakt halten, nur ausziehen bei langen Teilen
        (spart Tiefe). Vollständige Maße &amp; Zeichnung in <a href="../projekt-5/index.html">Projekt 5</a>.
      </p>
    </section>

    <section>
      <h2>Gesamt-Layout der Ecke</h2>
      <p>
        Nach dem CAD-Stand: die lange Wand (5900 mm) trägt Materialregal (groß), PSA-Schrank und
        Reinigungsschrank; die rechte/Tiefenwand (4000 mm) trägt die drei Lochwände und zwei
        Schubladenschränke; der Schweißtisch steht mittig, der Wagen hat einen eigenen
        Parkplatz (500 × 800 mm).
      </p>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>🟩 Station (Wand)</h4><p>Lochwände, Schubladen, PSA-, Reinigungs- und Materialregal an den zwei Wänden.</p></div>
        <div class="mini-karte"><h4>⬜ Schweißtisch</h4><p>Fahrbar, mittig in der Ecke, ausziehbar bei Bedarf.</p></div>
        <div class="mini-karte"><h4>🟧 Maschinenwagen</h4><p>Eigener Parkplatz, fährt bei Bedarf zum Werkstück.</p></div>
        <div class="mini-karte"><h4>┋ Schweißvorhang</h4><p>Trennt einen optionalen zweiten Platz &ndash; Blendschutz bei gleichzeitigem Schweißen.</p></div>
      </div>
    </section>

    <section>
      <h2>Arbeitszonen nach 5S</h2>
      <p class="section-intro">Klarer Ablauf von links nach rechts &ndash; jede Tätigkeit hat ihren Bereich. Das vermeidet Chaos und trennt Funken/Staub vom Schweißen.</p>
      <div class="stepper">
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">1</span>
            <span class="schritt-titel">Vorbereiten</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Material, Anreißen, Messen, Zuschnitt bereitlegen.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">2</span>
            <span class="schritt-titel">Schweißen</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Lochtisch, Absaugung, Masse, Spannmittel &ndash; Kernzone.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">3</span>
            <span class="schritt-titel">Nachbearbeiten</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Schleifen &amp; Bürsten &ndash; bewusst getrennt (Funken/Staub).</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">4</span>
            <span class="schritt-titel">Ablage / fertig</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Fertigteile, Reste zurück ins Regal, Abfall getrennt.</p></div>
        </div>
      </div>
    </section>

    <section>
      <h2>Wege &amp; Sicherheit</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>Wagen-Weg freihalten</strong>der Wagen fährt vom Tisch zum Werkstück und zurück (&ge; 1000 mm frei).</span></li>
        <li><span><strong>Schweißvorhang</strong>trennt den optionalen 2. Platz &rarr; Blendschutz.</span></li>
        <li><span><strong>Absaugarm über der Tischmitte</strong>bei 2 Plätzen ggf. mit 2. Erfassung.</span></li>
        <li><span><strong>Feuerlöscher &amp; Erste Hilfe</strong>an fester, freier Stelle (Fluchtweg beachten).</span></li>
        <li><span><strong>Nichts Brennbares</strong>im Funkenflug-Bereich lagern.</span></li>
      </ul>
    </section>

{projekt_nav("05-konzeptphase-bewertung.html", "Konzeptphase & Bewertung", "07-feste-station-idee-aufbau.html", "Station: Idee & Aufbau")}
  </main>
"""

write_page("06-gesamtplan-layout.html", "Projekt 4: Gesamtplan & Layout", body)
