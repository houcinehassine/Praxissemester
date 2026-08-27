# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt4 import *

body = seiten_kopf(11, "Arbeitssicherheit",
    "Schweißen ist sicherheitskritisch: Rauch/Gase, UV-Strahlung, Brand- und Stromgefahr. Eine "
    "Gefährdungsbeurteilung ist gesetzlich vorgeschrieben (§&nbsp;5 ArbSchG).") + f"""
  <main class="projekt-detail">

    <section>
      <h2>Rechtsgrundlage</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>ArbSchG § 5</strong>Pflicht zur Gefährdungsbeurteilung für jeden Arbeitsplatz.</span></li>
        <li><span><strong>TRGS 528</strong>Schweißtechnische Arbeiten (Gefahrstoffe, Absaugung).</span></li>
        <li><span><strong>GefStoffV + TRGS 900</strong>Grenzwerte für Schweißrauch (u. a. Mangan, Chrom-VI, Nickel).</span></li>
        <li><span><strong>DGUV Information 209-010/-016</strong>Lichtbogen-/Schutzgasschweißen.</span></li>
        <li><span><strong>Erlaubnisschein „feuergefährliche Arbeiten“</strong>bei Arbeiten außerhalb fester Schweißplätze.</span></li>
      </ul>
    </section>

    <section>
      <h2>STOP-Prinzip &ndash; Rangfolge der Maßnahmen</h2>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>S &ndash; Substitution</h4><p>Emissionsärmeres Verfahren/Zusatz, weniger CrNi wo möglich.</p></div>
        <div class="mini-karte"><h4>T &ndash; Technisch</h4><p>Absaugung an der Quelle (W3), Schweißvorhang, Belüftung.</p></div>
        <div class="mini-karte"><h4>O &ndash; Organisatorisch</h4><p>Unterweisung, Vorsorge, Pausen, Freigabescheine.</p></div>
        <div class="mini-karte"><h4>P &ndash; Persönlich</h4><p>Helm, Atemschutz, Schutzkleidung, Handschuhe.</p></div>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Wichtig:</strong> Reihenfolge einhalten &ndash; PSA ist die letzte Maßnahme, nicht die
        erste. Zuerst Absaugung &amp; Technik.
      </div>
    </section>

    <section>
      <h2>Gefährdungsbeurteilung Schweißplatz</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Gefährdung</th><th>Risiko</th><th>Maßnahme</th></tr></thead>
          <tbody>
            <tr><td>Schweißrauch &amp; Gase (Mn, Cr-VI, Ni, Ozon)</td><td><span class="prio prio--hoch">hoch</span></td><td>Absaugung an der Quelle (W3 bei Edelstahl), Belüftung, ggf. Atemschutz</td></tr>
            <tr><td>UV-/IR-Strahlung („Verblitzen“)</td><td><span class="prio prio--hoch">hoch</span></td><td>Automatikhelm EN 379, Schweißvorhang, Hautschutz</td></tr>
            <tr><td>Brand- &amp; Explosionsgefahr (Funken)</td><td><span class="prio prio--hoch">hoch</span></td><td>Brennbares fernhalten, Löscher, Freigabeschein, feuerfester Untergrund</td></tr>
            <tr><td>Elektrische Gefährdung</td><td><span class="prio prio--mittel">mittel</span></td><td>Gerät nach EN 60974, trockener Stand, Isolierung, Prüfung</td></tr>
            <tr><td>Verbrennungen / heiße Teile</td><td><span class="prio prio--mittel">mittel</span></td><td>Schutzkleidung EN ISO 11611, Handschuhe, Ablagekennzeichnung</td></tr>
            <tr><td>Gasflaschen (Sturz/Undicht)</td><td><span class="prio prio--mittel">mittel</span></td><td>Flaschen sichern (Kette), Dichtprüfung, Rückschlagsicherung</td></tr>
            <tr><td>Lärm (Schleifen/Nacharbeit)</td><td><span class="prio prio--mittel">mittel</span></td><td>Gehörschutz, lärmarme Werkzeuge</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>Unterweisung &amp; Vorsorge</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>Unterweisung</strong>vor Aufnahme und danach mindestens jährlich (DGUV).</span></li>
        <li><span><strong>Arbeitsmedizinische Vorsorge</strong>bei Schweißrauchexposition (Angebots-/Pflichtvorsorge).</span></li>
        <li><span><strong>Betriebsanweisung</strong>sichtbar am Platz, dokumentierte Unterweisung.</span></li>
      </ul>
    </section>

    <section>
      <div class="info-box">
        <strong>Bezug zum Layout (Seite 6):</strong> Absaugarm über der Tischmitte, freier Fluchtweg,
        Feuerlöscher gut erreichbar und der Schweißvorhang zwischen zwei Arbeitsplätzen setzen
        genau die Punkte „T“ (technisch) und teilweise „O“ (organisatorisch) aus dem
        STOP-Prinzip bereits im Grundriss um.
      </div>
    </section>

{projekt_nav("10-feste-station-material-zusammenbau.html", "Station: Material & Zusammenbau", "12-wirtschaftlichkeit-bezugsquellen.html", "Wirtschaftlichkeit & Einkauf")}
  </main>
"""

write_page("11-sicherheit.html", "Projekt 4: Arbeitssicherheit", body)
