# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt7 import *

body = seiten_kopf(6, "Werkbank &ndash; Maße &amp; Ergonomie",
    "Teilaufgabe B, erster Teil: Die Grundmaße der Werkbank &ndash; jedes mit einer Begründung "
    "und, wo vorhanden, mit dem Normbezug dahinter.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>📐 Werkbank-Grundmaße</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Maß</th><th>Wert</th><th>Warum dieser Wert</th></tr></thead>
          <tbody>
            <tr><td>Breite</td><td>1500&ndash;2000 mm</td><td>Platz für Arbeit, Ablage und Vorrichtungen &ndash; und für drei Personen an einer zentralen Bank</td></tr>
            <tr><td>Tiefe</td><td>600 mm</td><td>Kurze Greifwege, kein totes Volumen hinten, das nur zur Ablagefläche verkommt</td></tr>
            <tr><td>Arbeitshöhe</td><td>850&ndash;950 mm</td><td>Stehende Arbeit; höhenverstellbar wäre ideal</td></tr>
            <tr><td>Lochwand</td><td>+600&ndash;900 mm über der Platte</td><td>Bringt Zone A in Griffhöhe, ohne dass man sich strecken muss</td></tr>
            <tr><td>Traglast</td><td>≥ 500 kg</td><td>Schraubstock fest verschraubt und schwere Werkstücke aufgelegt</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>🧍 Ergonomie &ndash; woher die Arbeitshöhe kommt</h2>
      <p>
        Die Arbeitshöhe ist kein Erfahrungswert, sondern lässt sich aus der Ellenbogenhöhe
        ableiten. <strong>DIN EN ISO 14738</strong> gibt für stehende Arbeit einen Bereich von etwa
        <strong>850 bis 1050 mm</strong> vor. Innerhalb dieses Bereichs gilt:
      </p>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>🔍 Feinarbeit</h4><p>Höher ansetzen &ndash; näher an den Augen, weniger Bücken beim Anreißen und Messen.</p></div>
        <div class="mini-karte"><h4>🔨 Schwerarbeit</h4><p>Niedriger ansetzen &ndash; das Körpergewicht kann mitwirken, weniger Belastung der Schultern.</p></div>
        <div class="mini-karte"><h4>↕️ Höhenverstellung</h4><p>Ideal, weil drei Personen unterschiedlicher Größe denselben Platz nutzen. Bereich ca. 680&ndash;1150 mm.</p></div>
        <div class="mini-karte"><h4>📏 Körpermaße</h4><p>DIN 33402-2 liefert die Perzentil-Körpermaße als Auslegungsgrundlage.</p></div>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Warum die Höhenverstellung bei drei Nutzern besonders zählt:</strong> Eine feste
        Höhe ist immer ein Kompromiss zugunsten der mittleren Körpergröße &ndash; die größte und
        die kleinste Person arbeiten dauerhaft in ungünstiger Haltung. Genau das ist einer der
        Gründe, warum die Nutzwertanalyse auf Seite 9 das Kriterium Ergonomie mit 15 % gewichtet
        und Variante 1 (item-Profil) dort die volle Punktzahl erhält.
      </div>
    </section>

    <section>
      <h2>🔗 Wie die Maße mit dem Rest zusammenhängen</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Maß</th><th>Folgt aus</th><th>Wirkt sich aus auf</th></tr></thead>
          <tbody>
            <tr><td>Tiefe 600 mm</td><td>Greifweite im Stehen</td><td>Layout-Konzept 1 fällt durch: 700 mm Tiefe bedeutet weites Greifen (Seite 8)</td></tr>
            <tr><td>Breite bis 2000 mm</td><td>3 Personen an einer Bank</td><td>Im Grundriss mit 2000 mm eingezeichnet; Entscheidungsblatt legt ~1800 mm fest</td></tr>
            <tr><td>Traglast ≥ 500 kg</td><td>Schraubstock + Werkstücke</td><td>Schließt eine leichte Montagebank aus; alle vier Varianten sind entsprechend ausgelegt</td></tr>
            <tr><td>Lochwand +600&ndash;900 mm</td><td>Zone A in Griffhöhe</td><td>Bestimmt die Gesamthöhe und in Konzept 2 die Höhe der seitlichen Hochschränke</td></tr>
            <tr><td>Höhenverstellung</td><td>DIN EN ISO 14738</td><td>Bewertungskriterium Ergonomie in der Nutzwertanalyse</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>💡 Beleuchtung &ndash; oft vergessen, hier mitgeplant</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Tätigkeit</th><th>Wartungswert</th><th>Grundlage</th></tr></thead>
          <tbody>
            <tr><td>Grobbearbeitung</td><td>300 lx</td><td rowspan="3">DIN EN 12464-1 &middot; ASR A3.4</td></tr>
            <tr><td>Mittlere Maschinen- und Montagearbeit</td><td><strong>500 lx</strong></td></tr>
            <tr><td>Feinarbeit</td><td>750 lx</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">
        Für diesen Platz ist <strong>500 lx</strong> der maßgebende Wert. Er taucht deshalb auch in
        der Gefährdungsbeurteilung auf Seite 11 als Maßnahme gegen die Gefährdung „unzureichende
        Beleuchtung" wieder auf &ndash; schlechtes Licht führt hier nicht nur zu Ausschuss, sondern
        auch zu Unfällen.
      </p>
    </section>

    <section>
      <h2>❗ Was an dieser Stelle noch offen ist</h2>
      <div class="warn-box">
        <strong>Vom Maßbereich zum festen Maß:</strong> Breite (1500&ndash;2000), Arbeitshöhe
        (850&ndash;950) und Lochwandhöhe (600&ndash;900) sind noch Bereiche, keine Festlegungen. Das
        Entscheidungsblatt auf Seite 12 legt sich auf ~1800 × 600 × 850&ndash;950 mm fest &ndash;
        die Arbeitshöhe bleibt damit bewusst als Bereich stehen, weil sie erst mit der konkreten
        Variante (fest oder verstellbar) endgültig wird. Ebenfalls offen: die tatsächliche
        Tragfähigkeit des gewählten Fabrikats, die gegen die geforderten 500 kg zu prüfen ist.
      </div>
    </section>

{projekt_nav("05-5s-ordnung.html", "5S-Ordnung & Zonen", "07-varianten.html", "4 Bauvarianten")}
  </main>
"""

write_page("06-werkbank-masse.html", "Projekt 7: Werkbank – Maße & Ergonomie", body)
