# -*- coding: utf-8 -*-
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
from helfer import tab, bild, bildreihe

WG = [("Werkzeuge zum Drehen", "1 · Werkzeuge zum Drehen"),
      ("Werkzeuge zum Fräsen", "2 · Werkzeuge zum Fräsen"),
      ("Spann-", "3 · Spann- und Aufspannmittel"),
      ("Mess-", "4 · Mess- und Prüfmittel"),
      ("Nacharbeit", "5 · Nacharbeit und 6 · Hilfsmittel")]
gruppen = "".join(tab("projekt-7/03-werkzeugbedarf.html", s, titel=t) for s, t in WG)

P7 = f"""
    <div class="blatt-korpus">

      <section class="feld">
        <h4>Aufgabe</h4>
        <p>Einen kompletten Arbeitsplatz zum konventionellen Drehen und Fr&auml;sen planen, mit allen
        Werkzeugen f&uuml;r Zerspan- und Nacharbeit, geordnet nach der 5S-Methode &ndash; in mehreren
        Varianten mit technisch-wirtschaftlichem Vergleich.</p>
{tab("projekt-7/02-aufgabe-rahmen.html", "Die fünf bewerteten Teilaufgaben", titel="Die fünf Teilaufgaben")}
{tab("projekt-7/02-aufgabe-rahmen.html", "Was aus den Rahmenbedingungen folgt", titel="Rahmenbedingungen und ihre Folgen für die Planung")}
      </section>

      <div class="kennzahlen">
        <div><b>35</b><span>Werkzeugpositionen</span></div>
        <div><b>4.825</b><span>&euro; netto Werkzeug</span></div>
        <div><b>5.742</b><span>&euro; brutto Werkzeug</span></div>
        <div><b>8</b><span>Varianten bewertet</span></div>
        <div><b>10</b><span>Gef&auml;hrdungen beurteilt</span></div>
        <div><b>26,5</b><span>Monate Amortisation</span></div>
      </div>

      <section class="feld feld--gross">
        <h4>1 &middot; Vollst&auml;ndiger Werkzeugbedarf</h4>
        <p>Nach Arbeitsschritt gegliedert, nicht nach Katalog &ndash; so fallen Lücken beim Durchgehen
        auf. Die Mengen ber&uuml;cksichtigen bereits die drei Personen pro Schicht.</p>
{gruppen}
{tab("projekt-7/03-werkzeugbedarf.html", "Warum manche Positionen dreifach", titel="Begründung der Mengen")}
      </section>

      <section class="feld feld--gross">
        <h4>2 &middot; Bepreiste Werkzeugliste</h4>
{tab("projekt-7/04-kostenliste.html", "Verteilung nach Kategorien", titel="Verteilung der Kosten nach Kategorien")}
{tab("projekt-7/04-kostenliste.html", "Die sechs teuersten Positionen", titel="Die sechs teuersten Positionen")}
{tab("projekt-7/04-kostenliste.html", "Vollständige Liste", titel="Vollständige Werkzeugliste – alle 35 Positionen",
     hinweis="Netto-Richtwerte aus Marktrecherche, keine Angebote. Werkbank und Maschinen sind nicht enthalten.")}
      </section>

      <section class="feld">
        <h4>3 &middot; 5S-Ordnung und Zonenzuordnung</h4>
{tab("projekt-7/05-5s-ordnung.html", "Die fünf Schritte", titel="Die fünf Schritte am Arbeitsplatz")}
{tab("projekt-7/05-5s-ordnung.html", "Zonen-Zuordnung", titel="Zonen-Zuordnung – welches Werkzeug wohin")}
{tab("projekt-7/05-5s-ordnung.html", "Warum diese Zuordnung", titel="Begründung der Zonenzuordnung")}
      </section>

      <section class="feld">
        <h4>4 &middot; Werkbank &ndash; Ma&szlig;e, Ergonomie, Beleuchtung</h4>
{tab("projekt-7/06-werkbank-masse.html", "Werkbank-Grundmaße", titel="Werkbank-Grundmaße mit Begründung")}
{tab("projekt-7/06-werkbank-masse.html", "Beleuchtung", titel="Beleuchtung nach DIN EN 12464-1 und ASR A3.4")}
      </section>

      <section class="feld feld--gross">
        <h4>5 &middot; Vier Bauvarianten</h4>
{bildreihe(
 ("projekte/projekt-7/img/variante1-item-profil.png",
  "Isometrische Darstellung einer Werkbank aus blauem Aluminium-Nutprofil mit Holzarbeitsplatte und Lochwand",
  "Variante 1 &middot; item-Profil (Alu-Baukasten)"),
 ("projekte/projekt-7/img/variante2-stahl-standard.png",
  "Isometrische Darstellung einer klassischen Stahlwerkbank mit geschlossenem Unterschrank, Schubladen und Lochwand",
  "Variante 2 &middot; Stahl-Standard"))}
{bildreihe(
 ("projekte/projekt-7/img/variante3-systemmodule.png",
  "Isometrische Darstellung einer Werkbank aus drei getrennten Schrankmodulen unter einer durchgehenden Arbeitsplatte",
  "Variante 3 &middot; Systemmodule"),
 ("projekte/projekt-7/img/variante4-eigenbau.png",
  "Isometrische Darstellung einer selbstgebauten Werkbank aus geschweißten Stahl-Vierkantrohren mit zwei Holzplatten",
  "Variante 4 &middot; Eigenbau (Schwei&szlig;konstruktion)"))}
{tab("projekt-7/07-varianten.html", "Alle vier im direkten Vergleich", titel="Alle vier Bauvarianten im Vergleich")}
      </section>

      <section class="feld feld--gross">
        <h4>6 &middot; Vier Layout-Konzepte</h4>
{bildreihe(
 ("projekte/projekt-7/img/konzept1-tiefe-unterschraenke.png",
  "Isometrische Darstellung einer Werkbank mit durchgehend tiefem Unterschrank und Lochwand",
  "Konzept 1 &middot; Tiefe Unterschr&auml;nke"),
 ("projekte/projekt-7/img/konzept2-lochwand-mittig.png",
  "Isometrische Darstellung einer schmalen Werkbank mit Lochwand in der Mitte und zwei hohen Seitenschränken",
  "Konzept 2 &middot; Lochwand mittig + Hochschr&auml;nke &ndash; gew&auml;hlt"))}
{bildreihe(
 ("projekte/projekt-7/img/konzept3-bank-wagen.png",
  "Isometrische Darstellung einer offenen schlanken Werkbank mit Lochwand und einem fahrbaren roten Werkzeugwagen daneben",
  "Konzept 3 &middot; Schlanke Bank + mobiler Wagen"),
 ("projekte/projekt-7/img/konzept4-systemwand.png",
  "Isometrische Darstellung einer offenen Bank vor einer durchgehenden Lochwand mit drei Ablageborden",
  "Konzept 4 &middot; Systemwand &uuml;ber die L&auml;nge"))}
{tab("projekt-7/08-layout-konzepte.html", "Die vier Konzepte im Vergleich", titel="Die vier Layout-Konzepte im Vergleich",
     hinweis="Gewählt: <b>Konzept 2</b> als Basis, ergänzt um den mobilen Werkzeugwagen aus Konzept 3 für die Wege zu den Maschinen.")}
{bild("projekte/projekt-7/img/konzept2-3d-zonen.png",
  "3D-Ansicht des gewählten Konzepts mit beschrifteten Zonen A an der mittigen Lochwand, B am linken und C am rechten Hochschrank",
  "Gew&auml;hltes Konzept mit Zonenzuordnung: die 5S-Zonen A, B und C sind baulich abgebildet.", True)}
{bild("projekte/projekt-7/img/werkstatt-grundriss.png",
  "Maßstäblicher Grundriss der Werkstatt in Draufsicht: Raum 6000 mal 4500 mm, Drehmaschine links oben, Fräsmaschine rechts oben, Werkbank unten mittig, Werkzeugwagen rechts unten",
  "Werkstatt-Grundriss in U-Anordnung &ndash; Raum- und Maschinenma&szlig;e sind Beispielannahmen und vor der Umsetzung real aufzumessen.", True)}
{tab("projekt-7/08-layout-konzepte.html", "Werkstatt-Grundriss", titel="Maße im Grundriss")}
      </section>

      <section class="feld feld--gross">
        <h4>7 &middot; Nutzwertanalyse</h4>
{tab("projekt-7/09-nutzwertanalyse.html", "Die sieben Kriterien", titel="Die sieben Kriterien und ihre Gewichtung")}
{tab("projekt-7/09-nutzwertanalyse.html", "Die vollständige Bewertungsmatrix", titel="Vollständige Bewertungsmatrix")}
{tab("projekt-7/09-nutzwertanalyse.html", "Ergebnis der Rechnung", titel="Ergebnis der Rechnung",
     hinweis="Zwischen Platz 1 und Platz 2 liegen 0,20 Punkte – 4 % der Skala. Bei geschätzten Einzelnoten ist das kein belastbarer Vorsprung: item-Profil und Systemmodule sind gleichwertig, Stahl-Standard und Eigenbau fallen ab.")}
{tab("projekt-7/09-nutzwertanalyse.html", "Kostenschätzung je Variante", titel="Kostenschätzung je Variante")}
      </section>

      <section class="feld feld--gross">
        <h4>8 &middot; Wirtschaftlichkeit</h4>
{tab("projekt-7/10-wirtschaftlichkeit.html", "Die Rechenlogik", titel="Rechenlogik und Annahmen")}
{tab("projekt-7/10-wirtschaftlichkeit.html", "Die Investition", titel="Die Investition")}
{tab("projekt-7/10-wirtschaftlichkeit.html", "Amortisation je Bauvariante", titel="Amortisation je Bauvariante")}
{tab("projekt-7/10-wirtschaftlichkeit.html", "Wie empfindlich ist die Rechnung", titel="Empfindlichkeit gegenüber der Zeitannahme",
     hinweis="Selbst im vorsichtigsten Fall – nur fünf Minuten gesparte Suchzeit je Person und Tag – ist die Investition nach gut vier Jahren bezahlt, bei einer Nutzungsdauer von 10 bis 20 Jahren.")}
      </section>

      <section class="feld feld--gross">
        <h4>9 &middot; Arbeitssicherheit</h4>
{tab("projekt-7/11-arbeitssicherheit.html", "Rechtsgrundlage", titel="Rechtsgrundlage")}
{tab("projekt-7/11-arbeitssicherheit.html", "Gefährdungsbeurteilung Zerspanplatz", titel="Gefährdungsbeurteilung Zerspanarbeitsplatz")}
{tab("projekt-7/11-arbeitssicherheit.html", "Die beiden mittleren Restrisiken", titel="Die beiden verbleibenden mittleren Restrisiken")}
      </section>

      <section class="feld feld--gross">
        <h4>10 &middot; Umsetzung, Audit und Entscheidung</h4>
{tab("projekt-7/12-umsetzung-audit.html", "Zeitplan", titel="Zeitplan – sieben Phasen mit Meilensteinen")}
{tab("projekt-7/12-umsetzung-audit.html", "5S-Audit-Checkliste", titel="5S-Audit-Checkliste – zehn Prüfpunkte, max. 20 Punkte")}
{tab("projekt-7/12-umsetzung-audit.html", "5S-Audit-Checkliste", nr=1, titel="Bewertung der Audit-Punktzahl")}
{tab("projekt-7/12-umsetzung-audit.html", "Entscheidungsblatt", titel="Entscheidungsblatt (final)")}
{tab("projekt-7/12-umsetzung-audit.html", "Was für die Umsetzung noch zu tun ist", titel="Was für die Umsetzung noch zu tun ist")}
      </section>

      <section class="feld">
        <h4>11 &middot; Quellen und Normbezug</h4>
{tab("projekt-7/13-fazit-quellen.html", "Quellen", titel="Normen und Regelwerke, an denen sich die Planung orientiert")}
      </section>

      <section class="feld feld--nutzen">
        <h4>Nutzen f&uuml;r den Betrieb</h4>
        <p>Die Investition ist durchgerechnet, nicht gesch&auml;tzt: Bei zehn Minuten gesparter
        Suchzeit je Person und Tag ist der Platz nach rund 26 Monaten bezahlt. Die Werkzeugliste ist
        vollst&auml;ndig und bepreist, die Ordnung ist bis auf die einzelne Zone festgelegt, und die
        Gef&auml;hrdungsbeurteilung liegt mit zehn beurteilten Gef&auml;hrdungen und zugeordneten
        Ma&szlig;nahmen vor. Was zur Beschaffung fehlt, sind ausschlie&szlig;lich echte Angebote.</p>
      </section>

    </div>
"""

open(os.path.join(HIER, "_k7.py"), "w", encoding="utf-8").write("P7 = " + repr(P7) + "\n")
print("Kapitel 7 gebaut:", len(P7))
