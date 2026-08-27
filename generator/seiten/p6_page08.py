# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt6 import *

body = seiten_kopf(8, "Variante B &ndash; Zusatzwagen (Portalgestell)",
    "Ein wesentlicher Konzeptwechsel: statt eines kompletten Neubaus ein Aufsatzgestell, das über "
    "den bestehenden Wagen fährt und ihn überspannt &ndash; entwickelt in zwei Versionen.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>🔀 Der Konzeptwechsel</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Aspekt</th><th>Konzept SW-001 (Neubau)</th><th>Zusatzwagen</th></tr></thead>
          <tbody>
            <tr><td>Grundidee</td><td>Kompletter neuer Wagen, Maschine im Gerätefach</td><td>Aufsatzgestell über dem vorhandenen Wagen</td></tr>
            <tr><td>Bestandswagen</td><td>wird ersetzt</td><td>bleibt in Nutzung, fährt unter das Gestell</td></tr>
            <tr><td>Bauaufwand</td><td>hoch &ndash; Rahmen + Gerätefach + Flaschenaufnahme</td><td>geringer &ndash; nur Portalrahmen mit Ablagen</td></tr>
            <tr><td>Investition</td><td>höher</td><td>niedriger (Bestand weiter genutzt)</td></tr>
            <tr><td>Maßkonflikt Gerätefach</td><td><span class="st-no">❌ Maschine passt nicht (430 vs. 520 mm)</span></td><td><span class="st-ok">✅ entfällt</span></td></tr>
            <tr><td>Werkzeugordnung</td><td>am Neubau</td><td>am Zusatzgestell (Lochblech + Ablagen)</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Der entscheidende Vorteil:</strong> Der auf Seite 7 festgestellte Maßkonflikt
        (Gerätefach 430 mm zu niedrig für die 520 mm hohe MIG-Maschine) löst sich auf, weil die
        Maschine auf ihrem angestammten Fahrgestell verbleibt. Der Zusatzwagen ergänzt nur die
        fehlende Werkzeug- und Ablageordnung.
      </div>
    </section>

    <section>
      <h2>1️⃣ Version 1 &ndash; erster Entwurf</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Merkmal</th><th>Ausführung</th></tr></thead>
          <tbody>
            <tr><td>Grundprinzip</td><td>Portalrahmen auf 4 Lenkrollen, überspannt den Bestandswagen</td></tr>
            <tr><td>Ablageebenen</td><td>2 Ebenen im oberen Bereich (Wanne + Zwischenboden)</td></tr>
            <tr><td>Werkzeugwand</td><td>Lochblech-Panel, hochstehend an einer Seite</td></tr>
            <tr><td>Flaschenposition</td><td>Flasche steht außerhalb des Gestells, seitlich versetzt</td></tr>
            <tr><td>Rollen</td><td>4 Lenkrollen mit Montageplatten</td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Schwächen von Version 1:</strong> Gasflasche steht seitlich außerhalb der
        Radaufstandsfläche &rarr; ungünstige Lastverteilung &middot; Gesamtbreite dadurch groß,
        widerspricht der Kompaktheitsanforderung A-12 &middot; Flasche nicht in das Gestell
        eingebunden &rarr; Sicherung schwieriger.
      </div>
    </section>

    <section>
      <h2>2️⃣ Version 2 &ndash; aktueller Stand</h2>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Version 2 mit eingeschobenem Bestandswagen</span>
          <img src="img/zusatzwagen-v2-mit-bestandswagen.jpg" alt="CAD-Ansicht des Zusatzwagens Version 2: Portalgestell mit Lochblechwand und Ablagewanne, darunter der rote Bestandswagen mit oranger Gasflasche, links Isometrie, rechts Draufsicht" />
          <p class="bildtext">Der Bestandswagen (rot) fährt vollständig unter das Portal, die Gasflasche (orange) steht nun innerhalb der Aufstandsfläche.</p>
        </div>
      </div>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Baugruppe</th><th>Ausführung / Funktion</th></tr></thead>
          <tbody>
            <tr><td>Portalrahmen</td><td>Vier Ständer aus Nutprofil, oben zum Kasten geschlossen</td></tr>
            <tr><td>Obere Wanne</td><td>Offene Ablagewanne &ndash; Arbeits- und Ablagefläche</td></tr>
            <tr><td>Zwischenebenen</td><td>Zwei Ablageböden unterhalb der Wanne</td></tr>
            <tr><td>Lochblech-Panel</td><td>Umlaufend an den Kastenseiten &ndash; Aufnahme für Werkzeughaken</td></tr>
            <tr><td>Untergestell</td><td>Offene Durchfahrt &ndash; Bestandswagen fährt komplett darunter</td></tr>
            <tr><td>Querstreben</td><td>Untere Längs-/Querriegel zur Aussteifung des Portals</td></tr>
            <tr><td>Rollen</td><td>4 Lenkrollen mit Anschraubplatten, teils mit Feststeller</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>⚖️ Vergleich Version 1 ↔ Version 2</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Kriterium</th><th>Version 1</th><th>Version 2 (aktuell)</th></tr></thead>
          <tbody>
            <tr><td>Flaschenposition</td><td>seitlich außerhalb des Gestells</td><td><span class="st-ok">✅ mittig/innen, innerhalb der Aufstandsfläche</span></td></tr>
            <tr><td>Baubreite</td><td>groß (Flasche ragt heraus)</td><td><span class="st-ok">✅ deutlich kompakter</span></td></tr>
            <tr><td>Lastverteilung</td><td><span class="st-warn">⚠️ einseitig</span></td><td><span class="st-ok">✅ gleichmäßiger</span></td></tr>
            <tr><td>Aussteifung</td><td>weniger Querriegel</td><td><span class="st-ok">✅ zusätzliche untere Streben</span></td></tr>
            <tr><td>Werkzeugwand</td><td>einseitig hochstehend</td><td><span class="st-ok">✅ umlaufend am Kasten</span></td></tr>
            <tr><td>Integration Bestandswagen</td><td>teilweise darunter</td><td><span class="st-ok">✅ vollständige Durchfahrt</span></td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Fazit:</strong> Version 2 ist in allen Kriterien besser &ndash; insbesondere durch
        die kompaktere Bauform und die günstigere Lage der Gasflasche innerhalb der
        Radaufstandsfläche.
      </div>
    </section>

    <section>
      <h2>📋 Erfüllungsgrad &ndash; und warum er niedriger ist</h2>
      <div class="kennzahlen-grid">
        <div class="kennzahl"><strong>4</strong><span>erfüllt</span></div>
        <div class="kennzahl"><strong>6</strong><span>offen</span></div>
        <div class="kennzahl"><strong>4</strong><span>fehlen</span></div>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Warum der Erfüllungsgrad hier niedriger ausfällt:</strong>
        Der Zusatzwagen ist bisher nur als Rohgestell konstruiert. Die Ausrüstung (Schubladen,
        Haspel, Halterungen, Feuerlöscher) fehlt noch vollständig. Das ist normal für diesen
        Konstruktionsstand &ndash; muss aber ergänzt werden. Positiv: A-10 (4 Lenkrollen, 2 mit
        Bremse) ist hier erstmals konstruktiv umgesetzt.
      </div>
    </section>

    <section>
      <h2>❓ Offene Punkte Z-01 bis Z-08</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Nr.</th><th>Offener Punkt</th><th>Priorität</th></tr></thead>
          <tbody>
            <tr><td>Z-01</td><td>Keine Bemaßung vorhanden &ndash; Hauptmaße fehlen komplett</td><td><span class="prio prio--hoch">hoch</span></td></tr>
            <tr><td>Z-02</td><td>Lichte Durchfahrtshöhe/-breite für den Bestandswagen nicht angegeben</td><td><span class="prio prio--hoch">hoch</span></td></tr>
            <tr><td>Z-03</td><td>Gasflaschensicherung (Kette/Ring) nicht konstruiert</td><td><span class="prio prio--hoch">hoch</span></td></tr>
            <tr><td>Z-04</td><td>Werkstoffvariante: Item-Aluprofil oder Stahl?</td><td><span class="prio prio--mittel">mittel</span></td></tr>
            <tr><td>Z-05</td><td>Belegungsplan der Lochblechwand</td><td><span class="prio prio--mittel">mittel</span></td></tr>
            <tr><td>Z-06</td><td>Schubladenblock, Haspel, Feuerlöscherhalter ergänzen</td><td><span class="prio prio--mittel">mittel</span></td></tr>
            <tr><td>Z-07</td><td>Verhalten beim gemeinsamen Verfahren: zwei Wagen einzeln oder gekoppelt?</td><td><span class="prio prio--mittel">mittel</span></td></tr>
            <tr><td>Z-08</td><td>Rollen-Tragkraft gegen Gesamtmasse prüfen</td><td><span class="prio prio--niedrig">niedrig</span></td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>🤔 Grundsatzfrage: zwei Wagen oder ein Wagen?</h2>
      <p>
        Beim Zusatzwagen-Konzept entstehen zwei getrennt fahrbare Einheiten. Daraus ergeben sich
        Fragen, die vor der Weiterkonstruktion zu klären sind: Werden beide Wagen gemeinsam zum
        Werkstück gefahren (dann sind 8 Rollen zu bewegen)? Gibt es eine Kopplung
        (Rastung/Bolzen), damit sie nicht auseinanderfahren? Wie verhält sich das Gespann beim
        Rangieren in engen Bereichen? Oder sollte der Bestandswagen fest integriert werden statt
        lose eingeschoben?
      </p>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Empfehlung für den Bericht:</strong> Diese Konzeptentscheidung ist ein sehr guter
        Inhalt für die geforderte technisch-wirtschaftliche Gegenüberstellung. Drei Varianten
        lassen sich vergleichen: A &ndash; kompletter Neubau (SW-001) &middot; B &ndash;
        Zusatzwagen aus Item-Aluprofil &middot; C &ndash; Zusatzwagen aus Stahl (Eigenbau,
        geschweißt).
      </div>
    </section>

{projekt_nav("07-variante-a-neubau.html", "Variante A: Neubau SW-001", "09-gewaehltes-konzept.html", "Gewähltes Konzept")}
  </main>
"""

write_page("08-variante-b-zusatzwagen.html", "Projekt 6: Variante B – Zusatzwagen", body)
