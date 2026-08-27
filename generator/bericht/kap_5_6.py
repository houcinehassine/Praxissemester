# -*- coding: utf-8 -*-
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
from helfer import tab, bild, bildreihe

P5 = f"""
    <div class="blatt-korpus">

      <section class="feld">
        <h4>Aufgabe</h4>
        <p>Einen modularen Schwei&szlig;tisch konstruieren, der lange Bauteile aufnehmen kann und
        trotzdem in die Werkstatt passt &ndash; fahrbar, mit einem Spannsystem, das flexible
        Aufspannungen erlaubt.</p>
      </section>

      <div class="kennzahlen">
        <div><b>1600&times;1000</b><span>mm Arbeitsfl&auml;che</span></div>
        <div><b>3,1</b><span>m beidseitig ausgezogen</span></div>
        <div><b>~900</b><span>mm Arbeitsh&ouml;he</span></div>
        <div><b>~320</b><span>kg real</span></div>
        <div><b>40</b><span>Teile, 12 verschiedene</span></div>
        <div><b>15</b><span>Zeichnungsbl&auml;tter</span></div>
      </div>

      <section class="feld">
        <h4>1 &middot; Das Grundkonzept</h4>
{bildreihe(
 ("projekte/projekt-5/img/grundkonzept-3d-modell.png",
  "3D-Modell des Schweißtisches mit Rahmen, Tischplatte und Untergestell",
  "Grundkonzept: Rahmen mit Lochplatten-Auflage auf fahrbarem Untergestell."),
 ("projekte/projekt-5/img/teilennummern-isometrie.png",
  "Isometrische Ansicht mit eingeblendeten Teilenummern der Gesamtbaugruppe",
  "Gesamtbaugruppe mit Teilenummern der Hauptkomponenten."))}
{tab("projekt-5/04-erste-zeichnungen.html", "Teilen-Nummern", titel="Teilenummern der Gesamtbaugruppe")}
      </section>

      <section class="feld">
        <h4>2 &middot; Das Spannsystem &ndash; Lochplattenauswahl</h4>
{tab("projekt-5/05-lochplatte.html", "Marktrecherche", titel="Marktrecherche Lochplatte – geprüfte Angebote")}
{bild("projekte/projekt-5/img/lochplatten-auf-rahmen.png",
  "CAD-Ansicht der D16-Lochplatten auf dem Tischrahmen, mit sichtbarem Lochraster",
  "D16-Lochplatten auf dem Rahmen &ndash; das Spannraster f&uuml;r Vorrichtungen und Zwingen.", True)}
      </section>

      <section class="feld">
        <h4>3 &middot; Baugruppen</h4>
{tab("projekt-5/06-oberteil-unterteil.html", "Oberteil", titel="Oberteil 000-005-104")}
{tab("projekt-5/06-oberteil-unterteil.html", "Unterteil", titel="Unterteil – Basis 000-005-105")}
{tab("projekt-5/07-erweiterung-gesamtzusammenbau.html", "Technische Ausführung", titel="Erweiterungssystem – Teleskop-Rahmen")}
{bild("projekte/projekt-5/img/erweiterungssystem-cad.png",
  "CAD-Darstellung des ausziehbaren Teleskop-Rahmens in eingefahrenem und ausgefahrenem Zustand",
  "Das Erweiterungssystem: beidseitig ausziehbar auf insgesamt 3,1 m.", True)}
{tab("projekt-5/07-erweiterung-gesamtzusammenbau.html", "Gesamtzusammenbau", titel="Baugruppenstruktur 000-005-200-1")}
      </section>

      <section class="feld feld--gross">
        <h4>4 &middot; St&uuml;cklisten</h4>
{tab("projekt-5/08-zeichnungssatz-10-april.html", "Stückliste 000-005-104-1", titel="Stückliste 000-005-104-1 – Oberteil Basic")}
{tab("projekt-5/08-zeichnungssatz-10-april.html", "Stückliste 000-005-105-1", titel="Stückliste 000-005-105-1 – Unterteil Basic")}
{tab("projekt-5/08-zeichnungssatz-10-april.html", "Stückliste 000-005-103-3", titel="Stückliste 000-005-103-3 – Erweiterungssystem")}
{tab("projekt-5/09-gesamtzusammenbau-stueckliste.html", "Summenstückliste", titel="Summenstückliste")}
{tab("projekt-5/09-gesamtzusammenbau-stueckliste.html", "Abgeleiteter Materialbedarf", titel="Abgeleiteter Materialbedarf – Rohre")}
      </section>

      <section class="feld feld--gross">
        <h4>5 &middot; Endstand nach der Pr&uuml;fung</h4>
        <p>Vor der Freigabe wurde der gesamte Zeichnungssatz selbst gepr&uuml;ft. Dabei kamen f&uuml;nf
        belegte Fehler zutage &ndash; unter anderem dasselbe Teil mit zwei verschiedenen Gewichten und
        ein L&auml;ngenwiderspruch von 820 gegen 980 mm. Die folgenden Listen zeigen den
        <b>korrigierten Endstand</b>.</p>
{tab("projekt-5/13-endstand-technische-daten.html", "Korrigierte Hauptstückliste", titel="Korrigierte Hauptstückliste (Endstand)")}
{tab("projekt-5/13-endstand-technische-daten.html", "Make-or-Buy", titel="Make-or-Buy nach Korrektur")}
{tab("projekt-5/13-endstand-technische-daten.html", "Auslegung der Lenkrollen", titel="Auslegung der Lenkrollen")}
{tab("projekt-5/13-endstand-technische-daten.html", "Prüfstand aller 7 Baugruppen", titel="Prüfstand aller sieben Baugruppen des Endstands")}
      </section>

      <section class="feld">
        <h4>6 &middot; Zeichnungssatz</h4>
{tab("projekt-5/10-finale-anpassungen.html", "Gewichtsverteilung der Baugruppen", titel="Gewichtsverteilung der Baugruppen")}
{tab("projekt-5/10-finale-anpassungen.html", "Alle 15 Zeichnungsblätter", titel="Alle 15 Zeichnungsblätter im Überblick")}
{bildreihe(
 ("projekte/projekt-5/img/oberteil-basis-blatt1-10april.jpg",
  "Technische Zeichnung des Oberteils, Blatt 1, mit bemaßten Ansichten und Schriftfeld",
  "Oberteil Basis &ndash; Blatt 1 des Zeichnungssatzes."),
 ("projekte/projekt-5/img/endstand-blatt1-15-17april.jpg",
  "Technische Zeichnung des Endstands, Blatt 1, mit bemaßten Ansichten, Stückliste und Schriftfeld",
  "Endstand &ndash; Blatt 1 mit Schriftfeld und St&uuml;cklistenbezug."))}
      </section>

      <section class="feld feld--nutzen">
        <h4>Nutzen f&uuml;r den Betrieb</h4>
        <p>Ein Spanntisch f&uuml;r lange Bauteile, der im eingefahrenen Zustand keinen zus&auml;tzlichen
        Platz kostet. Das D16-Lochraster erlaubt es, Vorrichtungen und Zwingen frei zu setzen, statt
        f&uuml;r jede Aufspannung improvisieren zu m&uuml;ssen. Der Zeichnungssatz mit vollst&auml;ndiger
        St&uuml;ckliste und Make-or-Buy-Zuordnung reicht aus, um Zuschnitt und Beschaffung
        anzusto&szlig;en.</p>
      </section>

      <section class="feld feld--offen">
        <h4>Offene Punkte</h4>
{tab("projekt-5/14-fazit-ausblick.html", "Offene Punkte", titel="Offene Punkte und nächste Schritte")}
      </section>

    </div>
"""

P6 = f"""
    <div class="blatt-korpus">

      <section class="feld">
        <h4>Aufgabe</h4>
        <p>Einen fahrbaren Wagen konstruieren, der Schwei&szlig;maschine, Gasflasche und die
        wichtigsten Werkzeuge zum Werkst&uuml;ck bringt &ndash; als mobile Erg&auml;nzung zur festen
        Station aus Projekt 04.</p>
      </section>

      <div class="kennzahlen">
        <div><b>91,05</b><span>kg Gesamtgewicht</span></div>
        <div><b>58</b><span>Teile, 15 verschiedene</span></div>
        <div><b>21</b><span>Zeichnungsbl&auml;tter A3</span></div>
        <div><b>14</b><span>Anforderungen A-01 bis A-14</span></div>
        <div><b>4</b><span>Etagen im Endkonzept</span></div>
        <div><b>S235JRH</b><span>Werkstoff</span></div>
      </div>

      <section class="feld">
        <h4>1 &middot; Ausgangslage &ndash; Aufma&szlig; des Bestandswagens</h4>
{bildreihe(
 ("projekte/projekt-6/img/ist-wagen-foto1.jpg",
  "Werkstattfoto des vorhandenen Schweißwagens mit rotem Schweißgerät und Gasflasche",
  "Der vorhandene Wagen im Betrieb."),
 ("projekte/projekt-6/img/ist-handskizze-aufmass.jpg",
  "Handskizze auf Karopapier mit eingetragenen Maßen 610, 520, 430, 410, 300 sowie Höhe 1640 mm und Durchmesser 220 mm",
  "Aufma&szlig; vor Ort &ndash; Ger&auml;t und Flasche vermessen."))}
{tab("projekt-6/02-ist-aufnahme.html", "Aufmaß vor Ort", titel="Aufmaß vor Ort – gemessene Bauräume")}
      </section>

      <section class="feld feld--gross">
        <h4>2 &middot; Anforderungsliste</h4>
{tab("projekt-6/03-anforderungen.html", "Was muss der Wagen tragen", titel="Was der Wagen tragen muss")}
{tab("projekt-6/03-anforderungen.html", "Was muss der Wagen können", titel="Was der Wagen können muss")}
{tab("projekt-6/03-anforderungen.html", "Anforderungsliste A-01 bis A-14", titel="Vollständige Anforderungsliste A-01 bis A-14")}
      </section>

      <section class="feld">
        <h4>3 &middot; Belegungsplan &ndash; wo welches Werkzeug sitzt</h4>
{tab("projekt-6/07-variante-a-neubau.html", "Belegungsplan", titel="Belegungsplan – 16 Positionen")}
      </section>

      <section class="feld">
        <h4>4 &middot; Gew&auml;hltes Konzept &ndash; vier Etagen</h4>
{bildreihe(
 ("projekte/projekt-6/img/etage1-aufnahme-bestandswagen.jpg",
  "CAD-Vieransicht der Etage 1: offener U-förmiger Rahmen mit vier Ständern, Draufsicht, Front- und Seitenansicht",
  "Etage 1 &ndash; Aufnahme f&uuml;r Maschine und Bestandswagen."),
 ("projekte/projekt-6/img/etagen-schubladen-lochwand.jpg",
  "CAD-Detailansicht der montierten Etagen mit zwei Schubladenebenen, Führungsschienen, Deckelrahmen und seitlicher Lochwand",
  "Etagen 2 bis 4 &ndash; Schubladen, Deckel und anh&auml;ngbare Lochwand."))}
{tab("projekt-6/09-gewaehltes-konzept.html", "Etage 2", titel="Schubladenetagen – Ausführung")}
{tab("projekt-6/09-gewaehltes-konzept.html", "Etage 4", titel="Deckel und Lochwände – Festlegungen")}
{tab("projekt-6/09-gewaehltes-konzept.html", "Bauweise", titel="Bauweise – Profilsystem gegen Schweißkonstruktion")}
      </section>

      <section class="feld feld--gross">
        <h4>5 &middot; Zeichnungssatz und St&uuml;ckliste</h4>
{tab("projekt-6/10-zeichnungssatz.html", "Zeichnungsnormen", titel="Zeichnungsnormen und Vorgaben")}
{tab("projekt-6/10-zeichnungssatz.html", "Gesamtstückliste", titel="Gesamtstückliste – Blatt 21/21 · 000-006-200-1")}
{tab("projekt-6/10-zeichnungssatz.html", "Baugruppenstruktur", titel="Baugruppenstruktur")}
{tab("projekt-6/10-zeichnungssatz.html", "Alle 21 Zeichnungsblätter", titel="Alle 21 Zeichnungsblätter")}
{bild("projekte/projekt-6/img/zeichnung-blatt21-gesamtbaugruppe.jpg",
  "Technische Zeichnung Blatt 21 von 21: Gesamtbaugruppe des Schweißwagens mit Positionsnummern, Stückliste und Schriftfeld",
  "Blatt 21/21 &ndash; Gesamtbaugruppe mit Positionsnummern und St&uuml;ckliste, 91,05 kg, Werkstoff S235JRH.", True)}
      </section>

      <section class="feld feld--nutzen">
        <h4>Nutzen f&uuml;r den Betrieb</h4>
        <p>Maschine, Gas und Werkzeug fahren zum Werkst&uuml;ck statt umgekehrt. Der modulare
        Etagenaufbau macht die Fertigung in handhabbaren Baugruppen m&ouml;glich, und Etage 2 und 3
        sind identisch &ndash; eine Konstruktion, doppelte St&uuml;ckzahl. Der Belegungsplan gibt
        jedem der 16 Werkzeuge einen festen Platz.</p>
      </section>

      <section class="feld feld--offen">
        <h4>Offene Punkte aus der Eigenpr&uuml;fung</h4>
{tab("projekt-6/11-pruefung-funde.html", "Offene Punkte", titel="Offene Punkte – priorisierte Gesamtübersicht")}
      </section>

    </div>
"""

open(os.path.join(HIER, "_k56.py"), "w", encoding="utf-8").write(
    "P5 = " + repr(P5) + "\nP6 = " + repr(P6) + "\n")
print("Kapitel 5/6 gebaut:", len(P5), len(P6))
