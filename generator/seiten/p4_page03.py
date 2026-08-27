# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt4 import *

body = seiten_kopf(3, "Rahmenbedingungen &amp; Nutzungskonzept",
    "Der reale Platz, die vorhandene Maschine, das Budget &ndash; und die daraus abgeleitete "
    "Grundsatzentscheidung für ein Zwei-Ebenen-Konzept aus fester Station und mobilem Wagen.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>1 &middot; Der Platz &ndash; eine Ecke in der Halle</h2>
      <p>Aus dem Hallenplan: Die Ecke rechts unten ist für den Schweißarbeitsplatz reserviert.</p>
      <ul class="ergebnis-liste">
        <li><span><strong>~5900 mm</strong>entlang der Wand (fest).</span></li>
        <li><span><strong>~5000 mm</strong>tief &ndash; kann kürzer oder länger werden; Ziel: so kurz wie möglich halten (spart Hallenfläche).</span></li>
        <li><span><strong>Lage</strong>echte Ecke &rarr; zwei Wände nutzbar (lange Wand 5900 mm, Tiefenwand 4000 mm).</span></li>
        <li><span><strong>Fläche</strong>ca. 29 m² maximal verfügbar.</span></li>
      </ul>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Planungsleitsatz:</strong> Alles Nötige unterbringen, aber die Tiefe (5000 mm)
        minimieren. Kompakt = gut.
      </div>
    </section>

    <section>
      <h2>2 &middot; Vorhandene Schweißmaschine</h2>
      <p>Aus dem Foto der Maschine &ndash; wichtig: diese wird weiterverwendet, nicht neu gekauft.</p>
      <ul class="ergebnis-liste">
        <li><span><strong>Typ</strong>MIG/MAG-Schutzgasgerät (rot, Modell „&hellip;70“).</span></li>
        <li><span><strong>Fahrbar</strong>auf Rollen &rarr; flexibel positionierbar.</span></li>
        <li><span><strong>Gasflasche vorhanden</strong>Mischgas, große Flasche.</span></li>
        <li><span><strong>Drahtvorschub integriert</strong>Brenner + Massekabel dran.</span></li>
        <li><span><strong>Absaugung „FES-200“</strong>in der Nähe (Schweißrauch), Atemschutz-Filter &amp; Handschuhe liegen bereit.</span></li>
      </ul>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Offene Frage:</strong> Für E-Hand (2. gefordertes Verfahren) ist an der Maschine noch
        nichts zu sehen &ndash; zu klären, ob das Gerät E-Hand kann oder ob ein Inverter dazukommt.
        Ebenso offen: das genaue Typenschild (Marke/Modell/Ampere) und die Gasart auf der Flasche.
      </div>
    </section>

    <section>
      <h2>3 &middot; Der Schweißtisch &ndash; bereits konstruiert</h2>
      <p>
        Aus „000-005-200-2 Gesamtzusammenbau.pdf“ &ndash; die CAD-Konstruktion stand zum Zeitpunkt
        dieser Bestandsaufnahme bereits: Tischplatte mit Lochraster (zum Spannen/Fixieren der
        Werkstücke), untere Ablage für Material/Werkzeug, 4 Beine mit Fußplatten zum
        Verschrauben am Boden. Gewicht laut Zeichnung 32,98 kg, Maßstab 1:12, gezeichnet am
        10.04.2026. Vollständige Maße &amp; Stückliste in <a href="../projekt-5/index.html">Projekt 5</a>.
      </p>
    </section>

    <section>
      <h2>4 &middot; Budget &amp; Ziel</h2>
      <p>
        Budget: offen &ndash; aber so gering wie möglich, bei gleichzeitig der besten sinnvollen
        Variante. Übersetzt heißt das: bestes Preis-Leistungs-Verhältnis, nicht „billigste um
        jeden Preis“. Vorhandenes (Maschine, Gas, teils Tisch) weiterzuverwenden spart Geld.
      </p>
    </section>

    <section>
      <h2>Nutzungskonzept: das Zwei-Ebenen-System</h2>
      <p>
        Aus den Rahmenbedingungen ergab sich eine wichtige Entscheidung: ein Zwei-Ebenen-System
        &ndash; eine feste Werkzeug-Station am Platz und ein neuer, mobiler Maschinenwagen mit
        eigenem Werkzeugplatz. Genau richtig für 5S und für 3 Mitarbeiter, von denen teilweise
        zwei gleichzeitig aktiv sind.
      </p>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Ebene 1</span>
          <p class="bildtext"><strong>🏠 Feste Station</strong> am Schweißplatz: alle Werkzeuge, fester
          Platz je Werkzeug, Lochwand/Schattenbrett &ndash; man sieht sofort, was fehlt. Vorrat:
          Drahtrollen, Düsen, Schleifscheiben, PSA für 3 Personen.</p>
        </div>
        <div class="bild-box">
          <span class="label">Ebene 2</span>
          <p class="bildtext"><strong>🛒 Mobiler Wagen</strong>: Maschine + Gas + Essentials. Nur die
          meistgenutzten Werkzeuge, fährt zum Werkstück, feste Halter/Ablagen, damit nichts
          herunterfällt &ndash; kompakt, nicht überladen.</p>
        </div>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>5S steckt schon im Konzept:</strong> Fester Platz je Werkzeug = „Seiton“ (Ordnung).
        Zurücklegen nach Gebrauch = „Seiketsu“ (Standard halten). Das Konzept setzt das praktisch
        bereits um, bevor die einzelnen Möbel überhaupt gewählt waren.
      </div>
    </section>

    <section>
      <h2>Was fest ist, was mobil &ndash; die grobe Aufteilung</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>🏠 Eher fest an der Station</th><th>🛒 Eher mobil am Wagen</th></tr></thead>
          <tbody>
            <tr><td>Standschleifer / großer Winkelschleifer</td><td>Schlackenhammer &amp; Drahtbürste</td></tr>
            <tr><td>Schraubstock, große Spannmittel-Sortimente</td><td>Kleiner Winkelschleifer</td></tr>
            <tr><td>Mess- &amp; Anreißwerkzeuge</td><td>Schweiß-/Kombizange, Magnet-Schweißwinkel</td></tr>
            <tr><td>Nachbearbeitung: Feilen, Bürsten, Schleifscheiben-Vorrat</td><td>Ein paar Schraubzwingen</td></tr>
            <tr><td>Verbrauchsmaterial-Vorrat (Draht, Düsen, Elektroden)</td><td>Ersatz-Kontaktdüsen, Anreißkreide/Körner</td></tr>
            <tr><td>PSA-Depot für 3 Personen, Reinigung</td><td>Persönliche PSA des aktiven Schweißers</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>Weil teilweise 2 Personen gleichzeitig schweißen</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>Abstand &amp; Trennung</strong>Schweißschutzvorhang/-wand zwischen zwei Arbeitsbereichen (Blendschutz).</span></li>
        <li><span><strong>Genug Bewegungsfläche</strong>für 2 Personen einplanen &ndash; spricht dafür, die Tiefe (5000 mm) nicht zu knapp zu wählen.</span></li>
        <li><span><strong>Absaugung</strong>muss ggf. 2 Bereiche abdecken.</span></li>
        <li><span><strong>Option offenhalten</strong>Platz für einen 2. Schweißpunkt, falls später nötig.</span></li>
      </ul>
    </section>

    <section>
      <div class="info-box">
        <strong>Entscheidung getroffen:</strong> Kein Item-Aufbau &ndash; der Tisch aus Stahl (eigene
        Konstruktion, siehe Projekt 5), die Station aus Kaufteilen (Seiten 7&ndash;10), der Wagen
        aus Stahl (siehe Projekt 6). Das hält Kosten und CAD-Aufwand gering.
      </div>
    </section>

{projekt_nav("02-grundlagen.html", "Grundlagen", "04-werkzeugliste.html", "Werkzeugliste")}
  </main>
"""

write_page("03-rahmenbedingungen.html", "Projekt 4: Rahmenbedingungen", body)
