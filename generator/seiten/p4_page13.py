# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt4 import *

quellen = """<table class="tabelle"><thead><tr><th>Thema</th><th>Norm / Regelwerk</th><th>Kernaussage</th></tr></thead><tbody>
<tr><td>Gefährdungsbeurteilung</td><td>ArbSchG § 5 &middot; BetrSichV</td><td>Pflicht zur Beurteilung &amp; sicheren Betrieb der Arbeitsmittel</td></tr>
<tr><td>Schweißrauch / Gefahrstoffe</td><td>TRGS 528 &middot; GefStoffV &middot; TRGS 900</td><td>Absaugung an der Quelle, Grenzwerte (Mn, Cr-VI, Ni)</td></tr>
<tr><td>Schweißen (Regeln)</td><td>DGUV Information 209-010 / 209-016</td><td>Sicheres Lichtbogen-/Schutzgasschweißen</td></tr>
<tr><td>Schutzkleidung Schweißen</td><td>DIN EN ISO 11611</td><td>Schutzkleidung gegen Hitze, Funken, Strahlung</td></tr>
<tr><td>Gesichts-/Augenschutz</td><td>EN 175 &middot; EN 169 &middot; EN 379</td><td>Schweißerschutz, Filterstufen, Automatikhelm</td></tr>
<tr><td>Schutzhandschuhe</td><td>DIN EN 12477</td><td>Handschuhe für Schweißer</td></tr>
<tr><td>Schweißstromquellen</td><td>DIN EN 60974-1/-9</td><td>Sicherheit &amp; Errichtung Lichtbogenschweißeinrichtungen</td></tr>
<tr><td>Ergonomie / Arbeitshöhe</td><td>DIN EN ISO 14738 &middot; DIN 33402-2</td><td>Arbeitsplatzmaße aus Körpermaßen</td></tr>
<tr><td>Beleuchtung</td><td>DIN EN 12464-1 &middot; ASR A3.4</td><td>Wartungswerte (Montage/Feinarbeit 500&ndash;750 lx)</td></tr>
<tr><td>Qualität Schweißen</td><td>DIN EN ISO 3834 &middot; EN ISO 9606</td><td>Qualitätsanforderungen &amp; Schweißerprüfung</td></tr>
<tr><td>5S-Methode</td><td>Lean / Toyota-Produktionssystem</td><td>Ordnungsmethode (kein DIN); ergänzt QM nach DIN EN ISO 9001</td></tr>
</tbody></table>"""

body = seiten_kopf(13, "Fazit &amp; Quellen",
    "Zeitplan, 5S-Audit-Checkliste, das Entscheidungsblatt und alle verwendeten Normen &ndash; "
    "der Abschluss dieses Projekts, das in Projekt 5 (Tisch) und Projekt 6 (Wagen) konkret wird.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>Zeitplan (grobe Meilensteine)</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Phase</th><th>Inhalt</th><th>Dauer</th></tr></thead>
          <tbody>
            <tr><td>1 &middot; Ist-Aufnahme</td><td>Verfahren, Bauteile, bestehende Plätze fotografieren</td><td>1 Woche</td></tr>
            <tr><td>2 &middot; Werkzeugliste</td><td>Liste + Marktrecherche + Preise</td><td>1&ndash;2 Wochen</td></tr>
            <tr><td>3 &middot; 5S &amp; Layout</td><td>Ordnungskonzept, Werkbank-Varianten zeichnen</td><td>2 Wochen</td></tr>
            <tr><td>4 &middot; Bewertung</td><td>Nutzwertanalyse, Kosten, Amortisation</td><td>1 Woche</td></tr>
            <tr><td>5 &middot; Doku &amp; Abgabe</td><td>Dokumentation, Empfehlung, Präsentation</td><td>1&ndash;2 Wochen</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>5S-Audit-Checkliste (0&ndash;2 Punkte je Punkt, max. 20)</h2>
      <ul class="ergebnis-liste">
        <li><span>Nur benötigte Werkzeuge am Platz (Sortieren)</span></li>
        <li><span>Jedes Werkzeug hat markierten festen Platz (Shadowboard)</span></li>
        <li><span>Brenner &amp; häufige Werkzeuge in Reichweite</span></li>
        <li><span>Absaugung funktionsfähig &amp; genutzt</span></li>
        <li><span>Fluchtweg frei, Feuerlöscher zugänglich</span></li>
        <li><span>Arbeitsfläche sauber (Schlacke/Funkenreste entfernt)</span></li>
        <li><span>Gasflasche gesichert</span></li>
        <li><span>Schrott/Reste getrennt &amp; markiert</span></li>
        <li><span>Betriebsanweisung sichtbar</span></li>
        <li><span>Standard dokumentiert &amp; eingehalten</span></li>
      </ul>
    </section>

    <section>
      <h2>Entscheidungsblatt (final)</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Frage</th><th>Ergebnis</th></tr></thead>
          <tbody>
            <tr><td>Technisch beste Variante (Konzeptphase)</td><td>item + Stahltisch (A) &ndash; Nutzwert 4,06</td></tr>
            <tr><td>Wirtschaftlich beste Variante (Konzeptphase)</td><td>Stahl-Werkbank (B) &ndash; deutlich günstiger</td></tr>
            <tr><td>Real umgesetzt</td><td>Stahl-Schweißtisch (Projekt 5) + Kaufteile-Station (Seiten 7&ndash;10) + Stahl-Wagen (Projekt 6)</td></tr>
            <tr><td>Für Arbeiten am Bauteil / mobil</td><td>Mobiles Schweißsystem &ndash; der Wagen aus Projekt 6</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>Quellen &amp; Normbezug</h2>
      <div class="tabelle-wrapper">{quellen}</div>
      <div class="info-box" style="margin-top:0.75rem">
        Datenhinweis: Preise sind Netto-Richtwerte aus Marktrecherche (Beispielwerte, keine
        Angebote); Maße im Layout sind Beispielannahmen. Vor Umsetzung durch reale Angebote und
        die jeweils gültige Normfassung ersetzen.
      </div>
    </section>

    <section>
      <h2>Fazit</h2>
      <div class="fazit-grid">
        <div class="karte">
          <span class="label">Fachlich</span>
          <h4>Erst analysieren, dann bewerten, dann konkret werden</h4>
          <p>Die abstrakte Nutzwertanalyse (Seite 5) hat die Bewertungskriterien geschärft &ndash; die reale Entscheidung fiel dann auf Basis der echten Rahmenbedingungen (Seite 3), nicht der abstrakt besten Variante.</p>
        </div>
        <div class="karte">
          <span class="label">Methodisch</span>
          <h4>5S zieht sich durch jede Ebene</h4>
          <p>Vom groben Zwei-Ebenen-Konzept über die Zonenaufteilung bis zur einzelnen Schublade &ndash; „fester Platz je Werkzeug“ war auf jeder Planungsstufe die Leitfrage.</p>
        </div>
        <div class="karte">
          <span class="label">Praktisch</span>
          <h4>Zwei eigenständige CAD-Projekte sind daraus entstanden</h4>
          <p>Der Schweißtisch (Projekt 5) und der Maschinenwagen (Projekt 6) wurden als eigene, detaillierte CAD-Konstruktionen ausgearbeitet.</p>
        </div>
      </div>
    </section>

    <nav class="projekt-nav">
      <a href="12-wirtschaftlichkeit-bezugsquellen.html">
        <span class="richtung">&larr; Zurück</span>
        Wirtschaftlichkeit & Einkauf
      </a>
      <a class="naechste" href="../projekt-5/index.html">
        <span class="richtung">Weiter zu Projekt 5 &rarr;</span>
        Neues Schweißtisch-Konzept
      </a>
    </nav>
  </main>
"""

write_page("13-fazit-quellen.html", "Projekt 4: Fazit & Quellen", body)
