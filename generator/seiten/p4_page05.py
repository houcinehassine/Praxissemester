# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt4 import *

body = seiten_kopf(5, "Konzeptphase &amp; Bewertung",
    "Bevor die konkrete CAD-Lösung feststand, wurde formal bewertet: vier abstrakte "
    "Werkbank-Varianten und drei Layout-Konzepte, jeweils per Nutzwertanalyse verglichen.") + f"""
  <main class="projekt-detail">

    <section>
      <div class="info-box">
        <strong>Einordnung:</strong> Diese Seite zeigt die erste, noch allgemeine Bewertungsphase des
        Projekts &ndash; mit abstrakten Varianten und generischen Marktpreisen. Sie war die
        methodische Grundlage für die spätere, konkrete Entscheidung (ab Seite 6), die auf Basis
        der echten Rahmenbedingungen (Seite 3) teils anders ausfiel.
      </div>
    </section>

    <section>
      <h2>Vier Werkbank-Varianten</h2>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>A &middot; Item-Aluprofil + Stahltisch</h4><p>Modularer Alu-Baukasten mit separatem Stahl-Schweißaufsatz. Sehr flexibel, teurer.</p></div>
        <div class="mini-karte"><h4>B &middot; Klassische Stahl-Werkbank</h4><p>Robuste geschweißte Stahlbank, direkt schweißgeeignet, günstiger, wenig flexibel.</p></div>
        <div class="mini-karte"><h4>C &middot; Mobiles System (Basis)</h4><p>Fahrbarer „Alles-Träger“ mit den wichtigsten Dingen &ndash; als Ergänzung zum festen Platz.</p></div>
        <div class="mini-karte"><h4>D &middot; Mobile Karosserie (Vollausbau)</h4><p>Weiterentwicklung von C: fahrbare Multiprozess-Stromquelle (MIG/MAG · WIG · E-Hand) plus komplette Werkzeugbestückung auf Rädern.</p></div>
      </div>
    </section>

    <section>
      <h2>A) Nutzwertanalyse Werkbank-Ausführung</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Kriterium</th><th>Gew.</th><th>A item+Stahltisch</th><th>B Stahl-Werkbank</th><th>C Mobil (Basis)</th><th>D Karosserie</th></tr></thead>
          <tbody>
            <tr><td>Schweißeignung (Hitze/Erdung)</td><td>20%</td><td>4</td><td>5</td><td>3</td><td>4</td></tr>
            <tr><td>Flexibilität / Mobilität</td><td>18%</td><td>5</td><td>2</td><td>5</td><td>5</td></tr>
            <tr><td>5S-Eignung / Ordnung</td><td>17%</td><td>5</td><td>3</td><td>4</td><td>5</td></tr>
            <tr><td>Ergonomie</td><td>12%</td><td>5</td><td>3</td><td>3</td><td>4</td></tr>
            <tr><td>Anschaffungskosten</td><td>18%</td><td>2</td><td>5</td><td>4</td><td>3</td></tr>
            <tr><td>Robustheit / Standzeit</td><td>10%</td><td>4</td><td>5</td><td>3</td><td>4</td></tr>
            <tr><td>Aufwand bis einsatzbereit</td><td>5%</td><td>3</td><td>5</td><td>5</td><td>4</td></tr>
            <tr class="total-row"><td>Nutzwert (max 5,0)</td><td>100%</td><td>4,06</td><td>3,88</td><td>3,81</td><td>4,17</td></tr>
            <tr><td>Rang</td><td>&mdash;</td><td>2</td><td>3</td><td>4</td><td>🏆 1</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">
        Die Mobile Karosserie (D) führt in dieser abstrakten Bewertung: fahrbar, Multiprozess,
        alles integriert und 5S-optimal &ndash; knapp vor dem festen item-Platz (A).
      </p>
    </section>

    <section>
      <h2>B) Nutzwertanalyse Layout-Konzept</h2>
      <p class="section-intro">Drei mögliche Anordnungen von Tisch und Lochwand, bewertet nach Erreichbarkeit, Ergonomie und Platzbedarf.</p>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>K1 &middot; Linear</h4><p>Lochwand hinter dem Tisch &ndash; Werkzeuge über die heiße Fläche greifen.</p></div>
        <div class="mini-karte"><h4>K2 &middot; Über-Eck</h4><p>Werkzeuge seitlich (90° zum Tisch) &amp; am Wagen &ndash; ohne über den Tisch zu langen.</p></div>
        <div class="mini-karte"><h4>K3 &middot; Bediengang</h4><p>Tisch von der Wand abgerückt, Schweißer steht im ~700-mm-Gang dazwischen &ndash; Werkzeuge durch 180°-Drehung erreichbar.</p></div>
      </div>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Kriterium</th><th>Gew.</th><th>K1 Linear</th><th>K2 Über-Eck</th><th>K3 Bediengang</th></tr></thead>
          <tbody>
            <tr><td>Werkzeug-Erreichbarkeit</td><td>30%</td><td>2</td><td>4</td><td>5</td></tr>
            <tr><td>Ergonomie / Bewegungsökonomie</td><td>25%</td><td>3</td><td>5</td><td>5</td></tr>
            <tr><td>Platzbedarf (klein = besser)</td><td>20%</td><td>5</td><td>3</td><td>2</td></tr>
            <tr><td>Große Bauteile / Tischfront frei</td><td>15%</td><td>4</td><td>3</td><td>5</td></tr>
            <tr><td>Umsetzungsaufwand</td><td>10%</td><td>5</td><td>4</td><td>3</td></tr>
            <tr class="total-row"><td>Nutzwert (max 5,0)</td><td>100%</td><td>3,45</td><td>3,90</td><td>4,20</td></tr>
            <tr><td>Rang</td><td>&mdash;</td><td>3</td><td>2</td><td>🏆 1</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">
        K3 Bediengang gewinnt in der abstrakten Bewertung (beste Erreichbarkeit, Ergonomie, freie
        Tischfront) &ndash; braucht dafür aber am meisten Grundfläche. Bei weniger Platz wäre K2
        Über-Eck die fast gleich gute, kompaktere Wahl.
      </p>
    </section>

    <section>
      <h2>C) Kostenschätzung je Variante (netto, pro Platz)</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Ausführung</th><th>Anschaffung</th><th>Charakter</th></tr></thead>
          <tbody>
            <tr><td>A item-Aluprofil + Stahl-Schweißaufsatz</td><td>3.500&ndash;5.500 €</td><td>fest, sehr flexibel &amp; 5S-stark</td></tr>
            <tr><td>B Stahl-Werkbank / Schweißtisch</td><td>1.400&ndash;3.000 €</td><td>fest, robust, günstig</td></tr>
            <tr><td>C Einfaches mobiles System (Wagen)</td><td>2.000&ndash;4.000 €</td><td>fahrbar, Basis</td></tr>
            <tr><td>D Mobile Karosserie (Vollausbau)</td><td>4.500&ndash;7.000 €</td><td>fahrbar, alles integriert</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>Die abstrakte Empfehlung dieser Phase</h2>
      <div class="ergebnis-liste" style="list-style:none; padding:0; margin:0;">
        <ul class="ergebnis-liste">
          <li><span><strong>Ausführung</strong>Mobile Karosserie (D) &ndash; Nutzwert 4,17. Alternative: fester item-Platz (A, 4,06) für stationäre Präzision.</span></li>
          <li><span><strong>Layout</strong>K3 Bediengang (4,20) bei genug Fläche, sonst K2 Über-Eck (3,90).</span></li>
          <li><span><strong>Stromquelle</strong>Fahrbares Multiprozess-Gerät (MIG/MAG + WIG + E-Hand).</span></li>
        </ul>
      </div>
    </section>

    <section>
      <h2>Warum die reale Umsetzung anders ausfiel</h2>
      <p>
        Diese Bewertung geht von generischen Annahmen aus (offene Fläche, freie Geräteauswahl,
        Neuanschaffung aller Komponenten). Die echte Bestandsaufnahme (Seite 3) hat andere
        Randbedingungen gesetzt: eine vorhandene, funktionierende MIG/MAG-Maschine, die
        weiterverwendet werden sollte, eine konkrete Ecke mit zwei nutzbaren Wänden statt freier
        Flächenwahl, und ein Tisch, der zum Zeitpunkt der Bestandsaufnahme bereits als
        CAD-Konstruktion vorlag. Auf dieser Basis fiel die Entscheidung für eine klassische
        Stahl-Werkbank (nahe Variante B) plus eine Kaufteile-Station plus einen eigenen,
        neu konstruierten Stahl-Wagen &ndash; ein aus der Praxis abgeleiteter Kompromiss statt der
        rein abstrakt optimalen Variante D.
      </p>
    </section>

{projekt_nav("04-werkzeugliste.html", "Werkzeugliste", "06-gesamtplan-layout.html", "Gesamtplan & Layout")}
  </main>
"""

write_page("05-konzeptphase-bewertung.html", "Projekt 4: Konzeptphase & Bewertung", body)
