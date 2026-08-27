# -*- coding: utf-8 -*-
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HIER))
sys.path.insert(0, HIER)
from _montage import BLOECKE, UEBERSICHT, INHALT

CSS = open(os.path.join(HIER, "bericht.css"), encoding="utf-8").read()

SCHRIFTEN = ('<link rel="preconnect" href="https://fonts.googleapis.com" />\n'
  '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />\n'
  '  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
  'family=Archivo:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500&'
  'family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&display=swap" />')

KOERPER = f"""  <div class="bogen">

    <header class="deckblatt">
      <div class="kopfzeile">
        <span>Praxissemester &middot; Ergebnisbericht</span>
        <span class="mono">Stand 27.08.2026</span>
      </div>

      <h1>Was aus dem Praxis&shy;semester im Betrieb bleibt</h1>
      <p class="untertitel">
        Sieben Projekte in Lager, Schwei&szlig;technik und Zerspanung &ndash; vollst&auml;ndig
        dokumentiert mit allen St&uuml;cklisten, Werkzeuglisten, Belegungspl&auml;nen,
        Bewertungsmatrizen und Gef&auml;hrdungsbeurteilungen. Dieser Bericht zeigt die fertigen
        Arbeitsergebnisse, nicht den Weg dorthin.
      </p>

      <dl class="stammdaten">
        <div><dt>Bearbeiter</dt><dd>Houcine Hassine</dd></div>
        <div><dt>Betrieb</dt><dd>Mechanische Werkst&auml;tte Schmidt e.K., Essing</dd></div>
        <div><dt>Hochschule</dt><dd>OTH Regensburg &middot; Produktions- &amp; Automatisierungstechnik</dd></div>
        <div><dt>Betreuer</dt><dd>Amine Halloul</dd></div>
        <div><dt>Zeitraum</dt><dd>M&auml;rz &ndash; September 2026</dd></div>
        <div><dt>Umfang dieses Berichts</dt><dd>7 Projekte &middot; 123 Tabellen &middot; 31 Abbildungen</dd></div>
      </dl>
    </header>

    <section class="abschnitt">
      <h2 data-nr="A">&Uuml;bergabe auf einen Blick</h2>
      <p class="leitsatz">
        Jede Zeile ist ein abgeschlossenes Ergebnis mit einem konkreten Reifegrad.
        <em>In Betrieb</em> hei&szlig;t: l&auml;uft heute. <em>Fertigungsreif</em> hei&szlig;t: der
        Zeichnungssatz reicht f&uuml;r den Zuschnitt. <em>Entscheidungsreif</em> hei&szlig;t: die
        Planung steht vollst&auml;ndig, es fehlt eine Freigabe oder ein Angebot.
      </p>
      <div class="tabellenrahmen">
        <table>
          <thead><tr><th>Nr.</th><th>Ergebnis</th><th>Bereich</th><th>Reifegrad</th></tr></thead>
          <tbody>
{UEBERSICHT}          </tbody>
        </table>
      </div>
    </section>

    <section class="abschnitt">
      <h2 data-nr="B">Inhalt</h2>
      <div class="inhaltsverzeichnis">
{INHALT}      </div>
    </section>

    <section class="abschnitt">
      <h2 data-nr="C">Die sieben Ergebnisse im Einzelnen</h2>
      <p class="leitsatz">
        Je Projekt: die Aufgabe, alle Listen und Zeichnungsunterlagen vollst&auml;ndig, die
        Bewertungen mit ihren Rechenwegen, die Abbildungen &ndash; und der Nutzen f&uuml;r den
        Betrieb.
      </p>
{BLOECKE}    </section>

    <section class="abschnitt">
      <h2 data-nr="D">Was jetzt eine Entscheidung braucht</h2>
      <p class="leitsatz">
        Die Planungen sind abgeschlossen. Damit sie in die Umsetzung gehen, sind sechs
        Entscheidungen oder Schritte n&ouml;tig &ndash; nach Dringlichkeit geordnet.
      </p>
      <div class="tabellenrahmen">
        <table>
          <thead><tr><th>Nr.</th><th>Zu entscheiden oder zu veranlassen</th><th>Warum</th></tr></thead>
          <tbody>
            <tr><td class="mono">01</td><td>Zeichnungs&shy;korrekturen am Schwei&szlig;wagen freigeben</td><td>Die Gasflaschen&shy;aufnahme fehlt noch im Zeichnungssatz, und das Schriftfeld tr&auml;gt auf allen 21 Bl&auml;ttern die falsche Projekt&shy;bezeichnung. Beides ist benannt und schnell korrigiert &ndash; danach ist der Satz fertigungs&shy;bereit.</td></tr>
            <tr><td class="mono">02</td><td>F&uuml;nf gefundene Fehler im Schwei&szlig;tisch-Satz korrigieren</td><td>Bei der eigenen Pr&uuml;fung belegt und dokumentiert. Nach der Korrektur kann der Zuschnitt aus dem Satz abgeleitet werden.</td></tr>
            <tr><td class="mono">03</td><td>Angebote f&uuml;r den Zerspan&shy;arbeitsplatz einholen</td><td>Die Nutzwertanalyse stellt item-Profil (4,15) und Systemmodule (3,95) praktisch gleich. Dieser Abstand tr&auml;gt keine Entscheidung &ndash; erst echte Preise entscheiden.</td></tr>
            <tr><td class="mono">04</td><td>Boxensystem f&uuml;r das Schrauben&shy;lager beschaffen</td><td>Die Variante S &middot; M &middot; L ist bewertet und konstruiert, der Kapazit&auml;ts&shy;nachweis liegt vor. Mit der Beschaffung kann der Umzug in den Keller beginnen.</td></tr>
            <tr><td class="mono">05</td><td>Werkstatt f&uuml;r den Zerspanplatz real aufmessen</td><td>Der Grundriss arbeitet mit Beispielma&szlig;en. Vor dem Aufbau ist zu pr&uuml;fen, ob die geplante Werkbank an der vorgesehenen Wand Platz findet und die Wand die Hochschr&auml;nke tr&auml;gt.</td></tr>
            <tr><td class="mono">06</td><td>Reste-Workflow im Lagersystem erproben</td><td>Die automatische Resteverwaltung ist die j&uuml;ngste Funktion und im Alltag noch wenig getestet. Ein bewusster Praxistest sichert sie ab.</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section class="abschnitt">
      <h2 data-nr="E">&Uuml;bergebene Unterlagen</h2>
      <p class="leitsatz">
        Was der Betrieb konkret in die Hand bekommt &ndash; unabh&auml;ngig davon, ob die Umsetzung
        schon begonnen hat.
      </p>
      <div class="tabellenrahmen">
        <table>
          <thead><tr><th>Unterlage</th><th>Inhalt</th><th>Umfang</th></tr></thead>
          <tbody>
            <tr><td>Zeichnungssatz Schwei&szlig;tisch</td><td>Einzelteile, Baugruppen, korrigierte Hauptst&uuml;ckliste, Make-or-Buy-Zuordnung</td><td class="zahl">15 Bl&auml;tter</td></tr>
            <tr><td>Zeichnungssatz Schwei&szlig;wagen</td><td>Einzelteile, Baugruppen, Gesamt&shy;st&uuml;ckliste, Werkstoff S235JRH</td><td class="zahl">21 Bl&auml;tter A3</td></tr>
            <tr><td>Lagersystem Excel/VBA</td><td>Lauff&auml;hige Arbeitsmappe mit Barcode&shy;buchung, Verlauf, Export, Resteverwaltung</td><td class="zahl">Stand V3.3</td></tr>
            <tr><td>Lagersystem Web-Anwendung</td><td>Lokaler Dienst mit t&auml;glichem Backup, Cloud-Zugang und Windows-Setup&shy;paket</td><td class="zahl">2 Betriebsarten</td></tr>
            <tr><td>Werkzeugliste Schwei&szlig;platz</td><td>Neun Kategorien A bis I mit Zweck, Menge und Kostensch&auml;tzung</td><td class="zahl">9 Listen</td></tr>
            <tr><td>Werkzeugliste Zerspanplatz</td><td>35 Positionen mit Menge, Einzelpreis und Gesamtsumme</td><td class="zahl">4.825 &euro; netto</td></tr>
            <tr><td>Bezugsquellen&shy;recherche</td><td>Je Kaufteil des Schwei&szlig;platzes drei Preisstufen mit Anbieter</td><td class="zahl">7 Tabellen</td></tr>
            <tr><td>Ordnungskonzept Schrauben&shy;lager</td><td>Bestandsmatrix, CAD der Sichtlager&shy;k&auml;sten, Belegungsplan, Kapazit&auml;ts&shy;nachweis</td><td class="zahl">135 Sorten</td></tr>
            <tr><td>Gef&auml;hrdungs&shy;beurteilungen</td><td>Schwei&szlig;platz und Zerspanplatz, je mit Ma&szlig;nahmen und Restrisiko</td><td class="zahl">2 Beurteilungen</td></tr>
            <tr><td>5S-Unterlagen</td><td>Zonenkonzepte, Audit-Checklisten, Entscheidungs&shy;bl&auml;tter je Arbeitsplatz</td><td class="zahl">je Platz</td></tr>
            <tr class="summe"><td>Projekt&shy;dokumentation</td><td>Vollst&auml;ndige Dokumentation aller sieben Projekte mit Quellennachweis</td><td class="zahl">7 Projekte</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <footer class="fusszeile">
      <span>Houcine Hassine &middot; Praxissemester bei der Mechanischen Werkst&auml;tte Schmidt e.K., Essing &middot; OTH Regensburg</span>
      <span class="mono">Ergebnisbericht &middot; Stand 27.08.2026</span>
    </footer>

  </div>
"""

voll = f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Ergebnisbericht Praxissemester</title>
  <meta name="description" content="Die vollständigen Arbeitsergebnisse des Praxissemesters von Houcine Hassine bei der Mechanischen Werkstätte Schmidt e.K. – mit allen Stücklisten, Werkzeuglisten, Bewertungsmatrizen und Gefährdungsbeurteilungen." />
  <meta name="author" content="Houcine Hassine" />
  {SCHRIFTEN}
  <style>
{CSS}  </style>
</head>
<body>
{KOERPER}</body>
</html>
"""

from verweise import umschreiben
voll, offen, rest = umschreiben(voll)
if offen:
    print("WARNUNG – Ersetzung nicht gefunden:", offen)
print("verbleibende Seitenverweise:", len(rest), rest[:3])

with open(os.path.join(ROOT, "Ergebnisbericht-Praxissemester.html"), "w", encoding="utf-8") as f:
    f.write(voll)
print("HTML:", f"{len(voll)/1024/1024:.2f} MB")

art = voll.split("<body>\n", 1)[1].rsplit("</body>", 1)[0]
art = f'<title>Ergebnisbericht Praxissemester</title>\n{SCHRIFTEN}\n<style>\n{CSS}</style>\n' + art
with open(os.path.join(HIER, "ergebnisbericht.html"), "w", encoding="utf-8") as f:
    f.write(art)
print("Artefakt:", f"{len(art)/1024/1024:.2f} MB")
