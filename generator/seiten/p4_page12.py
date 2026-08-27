# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt4 import *

body = seiten_kopf(12, "Wirtschaftlichkeit &amp; Einkauf",
    "Lohnt sich die Investition? Die 5S-Ordnung spart täglich Suchzeit &ndash; und die konkreten "
    "Bezugsquellen je Kaufteil in drei Preisstufen.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>Amortisationsgedanke</h2>
      <p>
        Die 5S-Ordnung (feste Plätze, Shadowboards, klar getrennte Zonen) spart täglich Suchzeit
        &ndash; über mehrere Mitarbeiter und Arbeitstage gerechnet, kommt dabei schnell eine
        relevante Summe zusammen. Die Grundrechnung: gesparte Minuten je Person und Tag ×
        Personenzahl × Arbeitstage im Jahr × Stundensatz, gegen die einmalige Investition
        gerechnet.
      </p>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Posten</th><th>Betrag</th></tr></thead>
          <tbody>
            <tr><td>Werkzeuge &amp; Ausrüstung (Konzeptphase, Seite 4)</td><td>~10.030 €</td></tr>
            <tr><td>Werkbank / Schweißtisch (Stahl-Variante)</td><td>~2.500 €</td></tr>
            <tr class="total-row"><td>Summe (Beispielrechnung)</td><td>~12.530 €</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        Dies ist die Investition aus der frühen Konzeptphase (Seite 5) als Rechenbeispiel &ndash;
        sobald echte Angebote für die real gewählten Produkte (unten) vorliegen, lässt sich die
        Rechnung mit den tatsächlichen Zahlen wiederholen.
      </div>
    </section>

    <section>
      <h2>Weiterer Nutzen (nicht in € gerechnet)</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>Weniger Nahtfehler &amp; Nacharbeit</strong>durch Ordnung und passende Werkzeuge.</span></li>
        <li><span><strong>Höhere Arbeitssicherheit</strong>Absaugung, freie Wege, feste Plätze.</span></li>
        <li><span><strong>Weniger Werkzeugverlust und Doppelkäufe</strong></span></li>
        <li><span><strong>Schnelleres Einarbeiten</strong>neuer Mitarbeiter dank fester, beschrifteter Plätze.</span></li>
      </ul>
    </section>

    <section>
      <h2>Bezugsquellen je Kaufteil &ndash; drei Preisstufen</h2>
      <p class="section-intro">Konkrete Artikel in Günstig · Mittel · Premium, passend zu den realen Maßen aus Seite 7.</p>

      <h3>Werkzeug-Lochwand &ndash; 3× nötig</h3>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Produkt</th><th>Details</th><th>Shop</th><th>Stufe</th><th>Preis</th></tr></thead>
          <tbody>
            <tr><td>AREBOS Werkzeugwand 120×60</td><td>+ 17 Haken, Metall, sehr günstig</td><td>manomano.de</td><td>Günstig</td><td>~30 €</td></tr>
            <tr><td>Kreher XL Lochwand + 52 Haken</td><td>98×46 cm, Stahlblech, solide</td><td>norma24.de</td><td>Mittel</td><td>34,99 €</td></tr>
            <tr><td>Kreher 2× Lochwand 120×60 + Haken</td><td>2 Stück, größere Fläche</td><td>kreher-shop.de</td><td>Premium</td><td>im Shop</td></tr>
          </tbody>
        </table>
      </div>

      <h3 style="margin-top:1.25rem">Schubladenschrank &ndash; 2× nötig</h3>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Produkt</th><th>Details</th><th>Shop</th><th>Stufe</th></tr></thead>
          <tbody>
            <tr><td>Werkstattwagen 7 Schubladen, abschließbar</td><td>Kugellager-Auszüge, fahrbar</td><td>amazon.de</td><td>Günstig</td></tr>
            <tr><td>MASKO Werkstattwagen 7 Schubladen</td><td>unbestückt, robust</td><td>amazon.de</td><td>Günstig</td></tr>
            <tr><td>BIZOEIRON Werkzeugschrank</td><td>Metall, Garagen-/Werkstattschrank</td><td>amazon.de</td><td>Mittel</td></tr>
            <tr><td>Arebos Werkstattwagen</td><td>Feststellbremse, abschließbar, Anti-Rutsch</td><td>amazon.de</td><td>Mittel</td></tr>
            <tr><td>Powerplustools 7-Schubladen-Schrank</td><td>68×46×91, Maß passt genau</td><td>powerplustools.de</td><td>Passend, ~350 €</td></tr>
          </tbody>
        </table>
      </div>

      <h3 style="margin-top:1.25rem">PSA-Schrank &ndash; für 3 Mitarbeiter</h3>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Produkt</th><th>Details</th><th>Shop</th><th>Stufe</th><th>Preis</th></tr></thead>
          <tbody>
            <tr><td>Spind 3 Abteile Metall</td><td>3 Fächer, Helm/Handschuhe/Schürze</td><td>amazon.de</td><td>Günstig</td><td>~150&ndash;250 €</td></tr>
            <tr><td>Kleiderschränke Metall (3-teilig)</td><td>robuste Werkstatt-Ausführung</td><td>der-rollende-shop.de</td><td>Mittel</td><td>im Shop</td></tr>
            <tr><td>Kaiserkraft Garderoben-/PSA-Schrank</td><td>Industriequalität</td><td>kaiserkraft.de</td><td>Premium</td><td>Profi</td></tr>
          </tbody>
        </table>
      </div>

      <h3 style="margin-top:1.25rem">Materialregal (Schwerlast) &ndash; 180×90×40</h3>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Produkt</th><th>Details</th><th>Shop</th><th>Stufe</th><th>Preis</th></tr></thead>
          <tbody>
            <tr><td>KRAFT Schwerlastregal 180×90×40</td><td>5 Ablagen, je 175 kg</td><td>norma24.de</td><td>Günstig</td><td>19,99 €</td></tr>
            <tr><td>Schwerlastregal 180×90×40, 2er-Set</td><td>2 Regale, mehr Lagerfläche</td><td>norma24.de</td><td>Mittel</td><td>29,99 €</td></tr>
            <tr><td>Schwerlastregal mit Werkbank 180×100×60</td><td>gesamt 800 kg, mit Arbeitsfläche</td><td>norma24.de</td><td>Premium</td><td>34,99 €</td></tr>
          </tbody>
        </table>
      </div>

      <h3 style="margin-top:1.25rem">Lenkrollen (Wagen) &ndash; 4×, 2 mit Bremse</h3>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Produkt</th><th>Details</th><th>Shop</th><th>Stufe</th><th>Preis</th></tr></thead>
          <tbody>
            <tr><td>PU-Lenkrolle 160 mm, Feststeller</td><td>600 kg/Rolle, PU, Bauhöhe 195 mm</td><td>der-rollende-shop.de</td><td>Günstig</td><td>29,02 €</td></tr>
            <tr><td>Torwegge Lenkrolle 160 mm, Doppelstopp</td><td>180 kg/Rolle, spurlos, Bauhöhe 190 mm</td><td>torwegge.shop</td><td>Mittel</td><td>~34 €</td></tr>
            <tr><td>Blickle 607440 Lenkrolle 160 mm</td><td>Marken-Qualität, sehr langlebig</td><td>conrad.de</td><td>Premium</td><td>~59,50 €</td></tr>
          </tbody>
        </table>
      </div>

      <h3 style="margin-top:1.25rem">Lochplatte D16 (Schweißtisch) &ndash; 3×</h3>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Produkt</th><th>Details</th><th>Shop</th><th>Stufe</th><th>Preis</th></tr></thead>
          <tbody>
            <tr><td>Lochplatte D16 &middot; 8 mm</td><td>dünner/leichter, günstiger</td><td>hot-tabledance.de</td><td>Günstig</td><td>im Shop</td></tr>
            <tr><td>Lochplatte D16 &middot; 12 mm (gewählt)</td><td>800×500, Premiumstahl, System 16</td><td>hot-tabledance.de</td><td>Mittel</td><td>~89 €</td></tr>
          </tbody>
        </table>
      </div>

      <h3 style="margin-top:1.25rem">Gasflaschenhalter (Wagen)</h3>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Produkt</th><th>Details</th><th>Shop</th><th>Stufe</th><th>Preis</th></tr></thead>
          <tbody>
            <tr><td>Gasflasche Wandhalter + Kette</td><td>für Stahlflasche, einfach</td><td>ebay.de</td><td>Günstig</td><td>im Shop</td></tr>
            <tr><td>Wandhalterung 40/50 L Ø229 + Spanngurt</td><td>passend für große Flasche</td><td>schweissfachhandel24.de</td><td>Mittel</td><td>62,73 €</td></tr>
          </tbody>
        </table>
      </div>

      <div class="warn-box" style="margin-top:1rem">
        <strong>Tipp:</strong> Preise/Verfügbarkeit vor dem Bestellen im Shop prüfen. Je Teil eine
        Stufe wählen &ndash; daraus lässt sich eine Kostenübersicht (billig / mittel / premium
        Gesamtsumme) bauen.
      </div>
    </section>

{projekt_nav("11-sicherheit.html", "Sicherheit", "13-fazit-quellen.html", "Fazit & Quellen")}
  </main>
"""

write_page("12-wirtschaftlichkeit-bezugsquellen.html", "Projekt 4: Wirtschaftlichkeit & Einkauf", body)
