# -*- coding: utf-8 -*-
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
from helfer import tab, bild, bildreihe

WZ = [("A · Schweißen", "A · Schweißen – MAG/MIG"),
      ("B · Schweißen", "B · Schweißen – E-Hand"),
      ("C · Spannen", "C · Spannen &amp; Fixieren"),
      ("D · Nachbearbeitung", "D · Nachbearbeitung (Trennen · Schleifen · Reinigen)"),
      ("E · Anreißen", "E · Anreißen &amp; Messen"),
      ("F · Persönliche Schutzausrüstung", "F · Persönliche Schutzausrüstung – für 3 Personen"),
      ("G · Sicherheit", "G · Sicherheit &amp; Umgebung"),
      ("H · Verbrauchsmaterial", "H · Verbrauchsmaterial &amp; Vorrat"),
      ("I · Ordnung", "I · Ordnung &amp; Lagerung (5S-Möbel)")]
werkzeug = "".join(tab("projekt-4/04-werkzeugliste.html", such, titel=t) for such, t in WZ)

BEZUG = "".join(tab("projekt-4/12-wirtschaftlichkeit-bezugsquellen.html", "Bezugsquellen je Kaufteil", nr=i)
                for i in range(7))

P4 = f"""
    <div class="blatt-korpus">

      <section class="feld">
        <h4>Aufgabe</h4>
        <p>Einen kompletten Schwei&szlig;arbeitsplatz f&uuml;r drei Mitarbeiter auf 29 m&sup2;
        planen: welche Werkzeuge ein Schwei&szlig;er wirklich braucht, wie der Arbeitsplatz
        aufgebaut ist, und das Ganze geordnet nach der 5S-Methode. Die konkrete CAD-Konstruktion
        von Schwei&szlig;tisch und Maschinenwagen ist in den Projekten 05 und 06 ausgearbeitet.</p>
{tab("projekt-4/index.html", "Die Aufgabe entschlüsselt", titel="Die Aufgabenstellung im Einzelnen")}
      </section>

      <div class="kennzahlen">
        <div><b>3</b><span>Mitarbeiter am Platz</span></div>
        <div><b>29</b><span>m&sup2; verf&uuml;gbare Fl&auml;che</span></div>
        <div><b>9</b><span>Werkzeug-Kategorien A&ndash;I</span></div>
        <div><b>2</b><span>Verfahren: MAG/MIG und E-Hand</span></div>
        <div><b>3</b><span>Layout-Konzepte gepr&uuml;ft</span></div>
        <div><b>10</b><span>Gef&auml;hrdungen beurteilt</span></div>
      </div>

      <section class="feld">
        <h4>1 &middot; Rahmenbedingungen</h4>
{tab("projekt-4/02-grundlagen.html", "MAG/MIG vs. E-Hand", titel="Die beiden Schweißverfahren im Vergleich")}
{tab("projekt-4/03-rahmenbedingungen.html", "Was fest ist, was mobil", titel="Aufteilung: was fest steht, was mitfährt")}
      </section>

      <section class="feld feld--gross">
        <h4>2 &middot; Vollst&auml;ndige Werkzeugliste &ndash; neun Kategorien</h4>
        <p>Das Kernst&uuml;ck der Planung: Jedes Werkzeug, das am Schwei&szlig;platz gebraucht wird,
        mit Zweck und Menge. Die Mengen ber&uuml;cksichtigen die drei Mitarbeiter &ndash;
        personengebundene Ausr&uuml;stung dreifach, geteilte Werkzeuge einfach.</p>
        <p class="legende-zeile">
          <span>&#127968; <b>Station</b> &ndash; fester Platz am Schwei&szlig;platz</span>
          <span>&#128722; <b>Wagen</b> &ndash; reist zum Werkst&uuml;ck</span>
          <span>&harr; <b>Beides</b> &ndash; Grundausstattung plus mobile Kopie</span>
        </p>
{werkzeug}
{tab("projekt-4/04-werkzeugliste.html", "Kostenschätzung aus der frühen Konzeptphase", titel="Kostenschätzung der Werkzeugausstattung")}
      </section>

      <section class="feld">
        <h4>3 &middot; Bewertung der Ausf&uuml;hrungsvarianten</h4>
{tab("projekt-4/05-konzeptphase-bewertung.html", "Nutzwertanalyse Werkbank-Ausführung", titel="A · Nutzwertanalyse Werkbank-Ausführung")}
{tab("projekt-4/05-konzeptphase-bewertung.html", "Nutzwertanalyse Layout-Konzept", titel="B · Nutzwertanalyse Layout-Konzept")}
{tab("projekt-4/05-konzeptphase-bewertung.html", "Kostenschätzung je Variante", titel="C · Kostenschätzung je Variante (netto, pro Platz)")}
      </section>

      <section class="feld">
        <h4>4 &middot; Gesamtplan und Ergonomie</h4>
{tab("projekt-4/06-gesamtplan-layout.html", "Bestandteile des Arbeitsplatzes", titel="Bestandteile des Arbeitsplatzes")}
{tab("projekt-4/06-gesamtplan-layout.html", "Ergonomie", titel="Ergonomie – die maßgebenden Grundmaße")}
      </section>

      <section class="feld feld--gross">
        <h4>5 &middot; Die feste Station &ndash; Aufbau und Best&uuml;ckung</h4>
{tab("projekt-4/07-feste-station-idee-aufbau.html", "Werkzeugliste", titel="Werkzeugzuordnung – was gehört wohin")}
{tab("projekt-4/07-feste-station-idee-aufbau.html", "Maße der Produkte", titel="Maße der gewählten Produkte")}
{tab("projekt-4/08-feste-station-lochwaende-schubladen.html", "Lochwände", titel="Lochwände – Ausführung")}
{tab("projekt-4/10-feste-station-material-zusammenbau.html", "Finaler Zusammenbau", titel="Finaler Zusammenbau der Station")}
{tab("projekt-4/10-feste-station-material-zusammenbau.html", "Einkaufsliste Station", titel="Einkaufsliste der Station – gewählte Produkte")}
      </section>

      <section class="feld feld--gross">
        <h4>6 &middot; Bezugsquellen je Kaufteil</h4>
        <p>F&uuml;r jedes Kaufteil drei Preisstufen recherchiert &ndash; g&uuml;nstig, mittel,
        hochwertig &ndash; damit die Beschaffung ohne weitere Recherche entscheiden kann.</p>
{BEZUG}
      </section>

      <section class="feld">
        <h4>7 &middot; Arbeitssicherheit</h4>
{tab("projekt-4/11-sicherheit.html", "Gefährdungsbeurteilung Schweißplatz", titel="Gefährdungsbeurteilung Schweißarbeitsplatz")}
      </section>

      <section class="feld">
        <h4>8 &middot; Wirtschaftlichkeit</h4>
{tab("projekt-4/12-wirtschaftlichkeit-bezugsquellen.html", "Amortisationsgedanke", titel="Amortisationsbetrachtung")}
      </section>

      <section class="feld">
        <h4>9 &middot; Entscheidungsblatt und Normbezug</h4>
{tab("projekt-4/13-fazit-quellen.html", "Entscheidungsblatt", titel="Entscheidungsblatt (final)")}
{tab("projekt-4/13-fazit-quellen.html", "Quellen", titel="Quellen und Normbezug")}
      </section>

      <section class="feld feld--nutzen">
        <h4>Nutzen f&uuml;r den Betrieb</h4>
        <p>Der Platz ist als Ganzes geplant, nicht in Einzelteilen: Werkzeugbedarf, Anordnung,
        Ordnung und Sicherheit greifen ineinander. Die Werkzeugliste ist vollst&auml;ndig und
        bepreist, die Bezugsquellen sind je Teil in drei Preisstufen recherchiert &ndash; die
        Beschaffung kann ohne weitere Vorarbeit starten. Die geltenden Sicherheitsanforderungen sind
        benannt und mit konkreten Ma&szlig;nahmen hinterlegt: eine belastbare Grundlage f&uuml;r die
        Gef&auml;hrdungsbeurteilung nach &sect; 5 ArbSchG.</p>
      </section>

    </div>
"""

open(os.path.join(HIER, "_k4.py"), "w", encoding="utf-8").write("P4 = " + repr(P4) + "\n")
print("Kapitel 4 gebaut:", len(P4), "| Tabellen:", P4.count("<table>"))
