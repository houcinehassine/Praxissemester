# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt6 import *

body = seiten_kopf(2, "IST-Aufnahme des vorhandenen Wagens",
    "Erfassung des vorhandenen Schweißwagens im Betrieb: fotografische Dokumentation, Aufmaß der "
    "realen Bauteile und Vereinfachung als CAD-Modell &ndash; die Grundlage für alle "
    "Konstruktionsentscheidungen.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>📷 Fotodokumentation</h2>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Abb. 1 &middot; Der vorhandene Wagen im Betrieb</span>
          <img src="img/ist-wagen-foto1.jpg" alt="Foto des vorhandenen Schweißwagens in der Werkstatt: rotes Lorch-Schweißgerät auf Fahrgestell, Gasflasche dahinter, Schlauchpaket lose darüber gelegt" />
          <p class="bildtext">Einfaches Fahrgestell: Schweißgerät auf Plattform, Gasflasche senkrecht dahinter. Das Schlauchpaket liegt lose über der Flasche.</p>
        </div>
        <div class="bild-box">
          <span class="label">Abb. 2 &middot; Seitenansicht</span>
          <img src="img/ist-wagen-foto2.jpg" alt="Zweite Ansicht des vorhandenen Schweißwagens mit Gasflasche und Schlauchführung" />
          <p class="bildtext">Keine definierte Ablage für das Schlauchpaket, keine Werkzeugaufnahme am Wagen.</p>
        </div>
      </div>
    </section>

    <section>
      <h2>🔍 Beobachtungen zum IST-Zustand</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Beobachtung</th><th>Beschreibung / Auswirkung</th></tr></thead>
          <tbody>
            <tr><td>Aufbau</td><td>Einfaches Fahrgestell: Schweißgerät auf Plattform, Gasflasche senkrecht dahinter</td></tr>
            <tr><td>Schlauchpaket</td><td>Lose über die Gasflasche gelegt &ndash; keine definierte Ablage, Stolper- und Beschädigungsrisiko</td></tr>
            <tr><td>Werkzeugablage</td><td>Nicht vorhanden &ndash; Zubehör (Bürste, Hammer, Elektroden) muss separat mitgeführt werden</td></tr>
            <tr><td>Flaschenanzahl</td><td>Nur eine Gasflasche &ndash; Gaswechsel erfordert Rüstzeit</td></tr>
            <tr><td>Schwerpunkt</td><td>Flasche (ca. 1640 mm hoch) ragt weit über den Wagen &ndash; hoher Schwerpunkt, Kippneigung</td></tr>
            <tr><td>Stellfläche</td><td>Sehr kompakt (ca. 410 × 300 mm) &ndash; gut für enge Werkstattgänge, aber kein Stauraum</td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Hauptdefizite des IST-Zustands:</strong>
        Keine 5S-Ordnung (kein fester Platz für Werkzeuge und Verbrauchsmaterial) &middot;
        Kabel/Schlauch ungeordnet &rarr; Verschleiß und Unfallgefahr &middot;
        nur ein Gerät + eine Flasche transportierbar &middot;
        keine Nachbearbeitungswerkzeuge am Arbeitsplatz verfügbar.
      </div>
    </section>

    <section>
      <h2>📐 Aufmaß vor Ort</h2>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Abb. 3 &middot; Handskizze mit gemessenen Maßen</span>
          <img src="img/ist-handskizze-aufmass.jpg" alt="Handgezeichnete Skizze auf kariertem Papier mit den vor Ort gemessenen Maßen von Schweißgerät (610/520/430), Wagen (410/300) und Schweißflasche (Höhe 1640 mm, Durchmesser 220 mm)" />
          <p class="bildtext">Die Originalskizze aus der Werkstatt &ndash; Basis aller weiteren Bauraum-Entscheidungen.</p>
        </div>
      </div>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Bauteil</th><th>Maß</th><th>Wert</th></tr></thead>
          <tbody>
            <tr><td rowspan="3">Schweißgerät</td><td>Länge / Tiefe</td><td>610 mm</td></tr>
            <tr><td>Höhe</td><td>520 mm</td></tr>
            <tr><td>Breite</td><td>430 mm</td></tr>
            <tr><td rowspan="2">Wagen (Plattform)</td><td>Breite</td><td>410 mm</td></tr>
            <tr><td>Tiefe</td><td>300 mm</td></tr>
            <tr><td rowspan="2">Schweißflasche</td><td>Höhe</td><td>1640 mm</td></tr>
            <tr><td>Durchmesser</td><td>220 mm</td></tr>
            <tr><td>Aufbauhöhe</td><td>Boden &rarr; Schweißgerät</td><td>160 mm</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>🧮 Ableitungen für die Neukonstruktion</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>Mindest-Stellfläche je Gerät</strong>610 × 430 mm &rarr; Ablageebene muss ≥ 650 × 470 mm sein (mit Zugabe).</span></li>
        <li><span><strong>Lichte Höhe je Geräteebene</strong>≥ 520 mm + Zugabe für Anschlüsse/Bedienung &rarr; ca. 600 mm.</span></li>
        <li><span><strong>Flaschenaufnahme</strong>Ø 220 mm &rarr; Ausschnitt/Ring Ø ca. 240 mm; Sicherungskette in ca. 900&ndash;1100 mm Höhe.</span></li>
        <li><span><strong>Flaschenhöhe 1640 mm</strong>begrenzt die maximale Wagenhöhe &ndash; Gerät nicht über Flaschenoberkante stapeln.</span></li>
        <li><span><strong>Aufbauhöhe 160 mm</strong>als Referenz für Bodenfreiheit + Rollenhöhe im neuen Entwurf.</span></li>
        <li><span><strong>Bei 3 Geräten + 2 Flaschen</strong>Grundfläche der Neukonstruktion deutlich größer als 410 × 300 mm erforderlich.</span></li>
      </ul>
    </section>

    <section>
      <h2>💻 CAD-Vereinfachung des Bestandswagens</h2>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Abb. 4 &middot; Vereinfachtes CAD-Modell</span>
          <img src="img/ist-cad-vereinfachung.jpg" alt="Vereinfachtes CAD-Modell in vier Ansichten: roter Quader als Schweißgerät, oranger Zylinder als Gasflasche, graue Grundplatte und schwarze Rollen" />
          <p class="bildtext">Isometrie, Draufsicht, Seiten- und Frontansicht &ndash; reduzierte Geometrie als Bauraum-Platzhalter.</p>
        </div>
      </div>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Element</th><th>Darstellung im Modell</th><th>Zweck</th></tr></thead>
          <tbody>
            <tr><td>Roter Quader</td><td>Schweißgerät (610 × 430 × 520 mm)</td><td>Bauraum-Platzhalter</td></tr>
            <tr><td>Oranger Zylinder</td><td>Gasflasche (Ø 220 × 1640 mm)</td><td>Höhen- und Kollisionsprüfung</td></tr>
            <tr><td>Graue Platte</td><td>Grundplatte / Fahrgestell</td><td>Referenzebene</td></tr>
            <tr><td>Schwarze Klötze</td><td>Rollen / Füße</td><td>Bodenfreiheit 160 mm</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Warum vereinfachen?</strong>
        Reduzierte Geometrie = schnelle Rechenzeit bei Baugruppen-Untersuchungen; ausreichend für
        Bauraum-, Kollisions- und Ergonomieprüfung; die Platzhalter lassen sich direkt in die
        neuen Wagenkonzepte einsetzen.
      </div>
    </section>

    <section>
      <h2>🔗 Erste Verknüpfung mit den Konzeptentwürfen</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Anforderung aus IST-Analyse</th><th>Idee 1 (Kompaktrahmen)</th><th>Idee 2 (Werkstattwagen)</th></tr></thead>
          <tbody>
            <tr><td>Ablagefläche ≥ 650 × 470 mm</td><td><span class="st-no">❌ zu schmal</span></td><td><span class="st-ok">✅ 700 mm Breite passt</span></td></tr>
            <tr><td>2 Gasflaschen (Ø 220 mm)</td><td><span class="st-no">❌ nur 1 Platz</span></td><td><span class="st-ok">✅ untere Ebene ausreichend</span></td></tr>
            <tr><td>Definierte Schlauchablage</td><td><span class="st-warn">⚠️ Lamellenwand</span></td><td><span class="st-ok">✅ Einhängehaken oben</span></td></tr>
            <tr><td>Werkzeugordnung (5S)</td><td><span class="st-warn">⚠️ eingeschränkt</span></td><td><span class="st-ok">✅ Lochblech, 3 Seiten</span></td></tr>
            <tr><td>Standsicherheit bei 1640 mm Flasche</td><td><span class="st-no">❌ kippgefährdet</span></td><td><span class="st-ok">✅ breite Basis</span></td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Fazit:</strong> Die IST-Aufnahme bestätigt die Wahl von Idee 2 als Vorzugsvariante
        &ndash; die realen Bauteilmaße passen in den Bauraum von Idee 2, nicht jedoch in Idee 1.
      </div>
    </section>

{projekt_nav("index.html", "Überblick", "03-anforderungen.html", "Anforderungen (Lastenheft)")}
  </main>
"""

write_page("02-ist-aufnahme.html", "Projekt 6: IST-Aufnahme", body)
