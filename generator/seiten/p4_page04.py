# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt4 import *

body = seiten_kopf(4, "Werkzeuge erfassen",
    "Die vollständige Liste aller Werkzeuge, Geräte und Verbrauchsmaterialien für alle "
    "Schweiß- und Nachbearbeitungsaufgaben &ndash; jedes Teil bereits einem Ort zugeordnet: "
    "feste Station &#127968; oder mobiler Wagen &#128722;.") + f"""
  <main class="projekt-detail">

    <section>
      <div class="legende">
        <span>&#127968; Station &ndash; fester Platz am Schweißplatz</span>
        <span>&#128722; Wagen &ndash; reist zum Werkstück</span>
        <span>&harr; Beides &ndash; Grundausstattung + mobile Kopie</span>
      </div>
      <p style="margin-top:0.75rem">
        Diese Liste ist bewusst vollständig. Erst in den Detailseiten (7&ndash;10 sowie Projekt 6)
        wird sie konkret auf die Möbel verteilt; hier geht es erst ums Erfassen &ndash; 5S-Schritt 1:
        „was brauchen wir wirklich?“.
      </p>
    </section>

    <section>
      <h2>A &middot; Schweißen &ndash; MAG/MIG</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <tbody>
            <tr><td>Schweißgerät MAG/MIG</td><td>Hauptgerät (vorhanden, wird weiterverwendet)</td><td>&#128722;</td></tr>
            <tr><td>Brenner + Schlauchpaket</td><td>Führt Draht, Gas &amp; Strom zum Werkstück</td><td>&#128722;</td></tr>
            <tr><td>Massekabel + Masseklemme</td><td>Strom-Rückleitung, Klemme am Werkstück/Tisch</td><td>&#128722;</td></tr>
            <tr><td>Gasflasche Mischgas + Druckminderer</td><td>Schutzgas (z. B. M21) mit Flowmeter</td><td>&#128722;</td></tr>
            <tr><td>Brennerreinigung / Düsenreiniger</td><td>Spritzer aus Gasdüse entfernen</td><td>&#128722;</td></tr>
            <tr><td>Anti-Spritzer-Spray</td><td>Schützt Düse &amp; Werkstück vor Anhaftungen</td><td>&#128722;</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>B &middot; Schweißen &ndash; E-Hand</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <tbody>
            <tr><td>E-Hand-Gerät (Inverter)</td><td>Falls die MAG-Maschine kein E-Hand kann &ndash; noch zu klären</td><td>&harr;</td></tr>
            <tr><td>Elektrodenhalter + Schweißkabel</td><td>Hält die Stabelektrode</td><td>&#128722;</td></tr>
            <tr><td>Elektroden-Köcher / Trockenbox</td><td>Elektroden trocken lagern (sonst Nahtfehler)</td><td>&#127968;</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>C &middot; Spannen &amp; Fixieren</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <tbody>
            <tr><td>Spannwerkzeug-Set fürs Lochraster</td><td>Bolzen, Spanneisen, Anschläge für den Tisch</td><td>&#127968;</td></tr>
            <tr><td>Schraubstock</td><td>Feste Einspannung am Tischrand</td><td>&#127968;</td></tr>
            <tr><td>Schraubzwingen (versch. Größen)</td><td>Werkstücke festhalten/heften</td><td>&harr;</td></tr>
            <tr><td>Magnet-Schweißwinkel</td><td>Teile im Winkel (45/90°) halten ohne Hände</td><td>&#128722;</td></tr>
            <tr><td>Grip-/Klemmzangen</td><td>Schnelles Fixieren/Heften</td><td>&#128722;</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>D &middot; Nachbearbeitung (Trennen &middot; Schleifen &middot; Reinigen)</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <tbody>
            <tr><td>Winkelschleifer groß (125/230 mm)</td><td>Trennen, Schruppen, Nähte glätten</td><td>&#127968;</td></tr>
            <tr><td>Winkelschleifer klein</td><td>Feinarbeit direkt am Werkstück</td><td>&#128722;</td></tr>
            <tr><td>Schlackenhammer</td><td>Schlacke nach E-Hand abklopfen</td><td>&#128722;</td></tr>
            <tr><td>Handdrahtbürste</td><td>Naht &amp; Rost reinigen</td><td>&#128722;</td></tr>
            <tr><td>Meißel &amp; Feilen</td><td>Grate, Spritzer, Kanten</td><td>&#127968;</td></tr>
            <tr><td>Entgrater</td><td>Kanten sauber brechen</td><td>&harr;</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>E &middot; Anreißen &amp; Messen</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <tbody>
            <tr><td>Stahlmaßband &amp; Stahllineal</td><td>Längen messen/anzeichnen</td><td>&harr;</td></tr>
            <tr><td>Anschlagwinkel &amp; Wasserwaage</td><td>Rechtwinkligkeit &amp; Ausrichtung prüfen</td><td>&harr;</td></tr>
            <tr><td>Anreißnadel, Körner, Kreide/Silberstift</td><td>Markieren auf Metall</td><td>&#128722;</td></tr>
            <tr><td>Messschieber &amp; Schweißnahtlehre</td><td>Maße &amp; Nahtdicke kontrollieren</td><td>&#127968;</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>F &middot; Persönliche Schutzausrüstung &ndash; für 3 Personen</h2>
      <p class="section-intro">PSA ist persönlich &rarr; pro Mitarbeiter ein Satz. Depot an der Station, aktiver Satz am Wagen.</p>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <tbody>
            <tr><td>Automatik-Schweißhelm &times;3</td><td>Blend- &amp; UV-Schutz, verdunkelt automatisch</td><td>&harr;</td></tr>
            <tr><td>Schweißerhandschuhe (mehrere Paar)</td><td>Hitze-/Funkenschutz</td><td>&harr;</td></tr>
            <tr><td>Lederschürze / Schweißjacke &times;3</td><td>Körperschutz vor Funken</td><td>&#127968;</td></tr>
            <tr><td>Schutzbrille &amp; Gehörschutz</td><td>fürs Schleifen/Trennen</td><td>&harr;</td></tr>
            <tr><td>Atemschutz / Maske</td><td>Zusätzlich zur Absaugung</td><td>&#127968;</td></tr>
            <tr><td>Sicherheitsschuhe</td><td>persönlich (nicht am Platz gelagert)</td><td>&mdash;</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>G &middot; Sicherheit &amp; Umgebung</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <tbody>
            <tr><td>Schweißrauchabsaugung + Arm</td><td>FES-200 vorhanden &ndash; Absaugarm über den Platz</td><td>&#127968;</td></tr>
            <tr><td>Schweißschutzvorhang / -wand</td><td>Blendschutz &ndash; wichtig, weil teils 2 gleichzeitig</td><td>&#127968;</td></tr>
            <tr><td>Feuerlöscher + Löschdecke</td><td>Brandschutz (Pflicht)</td><td>&#127968;</td></tr>
            <tr><td>Erste-Hilfe-Kasten</td><td>Verbandmaterial griffbereit</td><td>&#127968;</td></tr>
            <tr><td>Arbeitsplatzbeleuchtung</td><td>Gute Sicht auf die Naht</td><td>&#127968;</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>H &middot; Verbrauchsmaterial &amp; Vorrat</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <tbody>
            <tr><td>Schweißdraht-Rollen</td><td>z. B. G3Si1 0,8/1,0 mm (je nach Material)</td><td>&#127968;</td></tr>
            <tr><td>Stabelektroden-Sortiment</td><td>Rutil/Basisch, versch. Ø &ndash; trocken lagern</td><td>&#127968;</td></tr>
            <tr><td>Kontakt- &amp; Gasdüsen (Ersatz)</td><td>Verschleißteile des Brenners</td><td>&harr;</td></tr>
            <tr><td>Trenn-, Schrupp-, Fächerscheiben</td><td>Verschleiß fürs Schleifen</td><td>&#127968;</td></tr>
            <tr><td>Reinigungstücher, Handreiniger</td><td>Sauberkeit (5S-Schritt 3)</td><td>&#127968;</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>I &middot; Ordnung &amp; Lagerung (5S-Möbel)</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <tbody>
            <tr><td>Lochwand / Schattenbrett</td><td>Umriss je Werkzeug &rarr; man sieht, was fehlt</td><td>&#127968;</td></tr>
            <tr><td>Werkzeugschrank / Schubladen</td><td>Kleinteile, Verbrauch, Messwerkzeug</td><td>&#127968;</td></tr>
            <tr><td>Materialregal / Reste-Ablage</td><td>Rohmaterial &amp; Halbzeug</td><td>&#127968;</td></tr>
            <tr><td>Abfallbehälter (Metallreste getrennt)</td><td>Ordnung &amp; Entsorgung</td><td>&#127968;</td></tr>
            <tr><td>Industriesauger / Kehrset</td><td>Schleifstaub &amp; Späne</td><td>&#127968;</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Damit die Liste 100&nbsp;% passt:</strong> zwei Dinge verfeinern sie noch &ndash;
        welche Materialien geschweißt werden (nur Baustahl, oder auch Edelstahl/Alu? bestimmt
        Draht/Scheiben) und ob die Maschine E-Hand kann.
      </div>
    </section>

    <section>
      <h2>Kostenschätzung aus der frühen Konzeptphase</h2>
      <p class="section-intro">
        Aus der ersten, formalen Bewertungsphase (siehe Seite 5): eine bepreiste Version derselben
        Werkzeugliste, nach Aufgaben statt nach Lagerort gruppiert. Netto-Richtwerte aus
        Marktrecherche &ndash; Beispielwerte, keine echten Angebote.
      </p>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Aufgabe</th><th>Zwischensumme</th></tr></thead>
          <tbody>
            <tr><td>1 &middot; Schweißen (Geräte, Tisch, Gas, Draht)</td><td>5.050 €</td></tr>
            <tr><td>2 &middot; Spannen &amp; Vorrichtung</td><td>600 €</td></tr>
            <tr><td>3 &middot; PSA, Schutz &amp; Absaugung</td><td>2.950 €</td></tr>
            <tr><td>4 &middot; Nacharbeit</td><td>550 €</td></tr>
            <tr><td>5 &middot; Messen &amp; Prüfen</td><td>180 €</td></tr>
            <tr><td>6 &middot; Ordnung (5S)</td><td>700 €</td></tr>
            <tr class="total-row"><td>Gesamtsumme (netto, ohne Werkbank)</td><td>~10.030 €</td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        Diese Summe stammt aus der frühen Konzeptphase mit einem größeren Geräte-Ansatz (u. a.
        eigenes WIG-Gerät, 2.200-€-Absauggerät). Die real umgesetzte Lösung nutzt die vorhandene
        MIG/MAG-Maschine weiter und kauft gezielter ein &ndash; die tatsächlichen Bezugsquellen
        und Preise für die Station stehen auf Seite 12.
      </div>
    </section>

{projekt_nav("03-rahmenbedingungen.html", "Rahmenbedingungen", "05-konzeptphase-bewertung.html", "Konzeptphase & Bewertung")}
  </main>
"""

write_page("04-werkzeugliste.html", "Projekt 4: Werkzeugliste", body)
