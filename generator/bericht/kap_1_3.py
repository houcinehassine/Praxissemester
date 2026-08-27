# -*- coding: utf-8 -*-
import os, sys
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
from helfer import tab, bild, bildreihe

P1 = f"""
    <div class="blatt-korpus">

      <section class="feld">
        <h4>Aufgabe</h4>
        <p>Das Schraubenlager zieht vom Erdgeschoss in den Keller. F&uuml;r sechs neue Regalf&auml;cher
        war zu ermitteln, welche Boxengr&ouml;&szlig;en gebraucht werden, wie viele nebeneinander
        passen und wie das Trennsystem aussehen muss &ndash; damit jede der 135 Schraubensorten
        einen festen, beschrifteten und sofort auffindbaren Platz bekommt.</p>
      </section>

      <div class="kennzahlen">
        <div><b>135</b><span>Schraubensorten erfasst</span></div>
        <div><b>4</b><span>Schraubentypen</span></div>
        <div><b>259</b><span>Datenpunkte in der Matrix</span></div>
        <div><b>6</b><span>Regalf&auml;cher beplant</span></div>
        <div><b>3</b><span>Boxgr&ouml;&szlig;en konstruiert</span></div>
        <div><b>144</b><span>Pl&auml;tze nachgewiesen</span></div>
      </div>

      <section class="feld">
        <h4>1 &middot; Bestandsaufnahme &ndash; was tats&auml;chlich im Lager liegt</h4>
        <p>Grundlage aller weiteren Entscheidungen: Jede vorhandene Schraubensorte wurde nach Typ,
        Gewindegr&ouml;&szlig;e und L&auml;nge erfasst und in einer Matrix ausgewertet.</p>
{tab("projekt-1/04-bestandsanalyse.html", "Verteilung nach Schraubentyp", titel="Verteilung nach Schraubentyp")}
{tab("projekt-1/04-bestandsanalyse.html", "Verteilung nach Gewindegröße", titel="Verteilung nach Gewindegröße")}
      </section>

      <section class="feld">
        <h4>2 &middot; Zusammenf&uuml;hrung &ndash; die Summentabelle</h4>
        <p>Aus den vier Einzelanalysen entstand eine Summentabelle: Welche L&auml;ngen kommen bei
        welchem Gewinde vor, und wie viele Pl&auml;tze braucht das je Schublade.</p>
{tab("projekt-1/09-zusammenfuehrung.html", "Die 8 Schubladen der Summentabelle", titel="Die acht Schubladen der Summentabelle")}
      </section>

      <section class="feld">
        <h4>3 &middot; Konstruktion &ndash; Sichtlagerk&auml;sten und Regalbest&uuml;ckung</h4>
{bildreihe(
 ("projekte/projekt-1/img/regalfach-massskizze.png",
  "Maßskizze eines Regalfachs mit Breiten- und Höhenangaben",
  "Ma&szlig;skizze des Regalfachs &ndash; Ausgangsma&szlig;e f&uuml;r die Boxenauslegung."),
 ("projekte/projekt-1/img/cad-fach-varianten.jpg",
  "CAD-Darstellung mehrerer Bestückungsvarianten eines Regalfachs",
  "Gepr&uuml;fte Best&uuml;ckungsvarianten je Fach."))}
{tab("projekt-1/11-cad-konstruktion.html", "Das komplette Regal", titel="Das komplette Regal – drei Bestückungsvarianten")}
{bild("projekte/projekt-1/img/3d-sichtlagerkaesten.png",
  "CAD-Rendering eines Regalfachs mit Sichtlagerkästen in drei Größen, farblich getrennt in grün, gelb und rot",
  "Empfohlene Variante S &middot; M &middot; L &ndash; jede Schraubenl&auml;nge bekommt die passende Boxgr&ouml;&szlig;e.", True)}
      </section>

      <section class="feld">
        <h4>4 &middot; Belegungsplan &ndash; welche Sorte in welche Box</h4>
        <p>Der Belegungsplan ist das eigentliche Arbeitsdokument f&uuml;r den Umzug: Er sagt f&uuml;r
        jedes Fach und jede Box, welche Schraubensorte dort hingeh&ouml;rt.</p>
{tab("projekt-1/11-cad-konstruktion.html", "Belegungsplan", titel="Belegungsplan – Regal gefüllt")}
{tab("projekt-1/11-cad-konstruktion.html", "Belegungsplan", nr=1)}
{bild("projekte/projekt-1/img/belegungsplan.jpg",
  "Handkolorierter Belegungsplan mehrerer Regalfächer mit eingetragenen Schraubenbezeichnungen wie M6x60, M8x30, farblich nach Boxgröße getrennt",
  "Belegungsplan aus der Planungsphase &ndash; jede Box tr&auml;gt ihre Schraubenbezeichnung, Farbe kennzeichnet die Boxgr&ouml;&szlig;e.", True)}
      </section>

      <section class="feld">
        <h4>5 &middot; Variantenbewertung und Empfehlung</h4>
{tab("projekt-1/13-bewertung-ausblick.html", "Nutzwertanalyse der Regalvarianten", titel="Nutzwertanalyse der drei Regalvarianten",
     hinweis="Bewertung 1–5, gewichtet. Empfehlung: <b>Volle S · M · L</b> – höchster Nutzwert, jede Schraubenlänge bekommt die passende Boxgröße. Die 144 Plätze reichen für die 135 Sorten aus.")}
{bild("projekte/projekt-1/img/regal-sml-konzept.jpg",
  "CAD-Rendering des kompletten Regals in der empfohlenen Variante S, M und L",
  "Empfohlene Gesamtl&ouml;sung f&uuml;r alle sechs Regalf&auml;cher.", True)}
      </section>

      <section class="feld feld--nutzen">
        <h4>Nutzen f&uuml;r den Betrieb</h4>
        <p>Jede Schraubensorte bekommt einen festen, beschrifteten Platz. Der Umzug in den Keller
        l&auml;sst sich nach Plan durchf&uuml;hren, statt beim Einr&auml;umen zu improvisieren. Der
        Kapazit&auml;tsnachweis belegt vor der Beschaffung, dass die gew&auml;hlte L&ouml;sung
        aufgeht &ndash; 144 Pl&auml;tze f&uuml;r 135 Sorten, mit Reserve.</p>
      </section>

      <section class="feld feld--offen">
        <h4>Was zur Umsetzung noch n&ouml;tig ist</h4>
        <p>Beschaffung der Sichtlagerk&auml;sten in den drei Gr&ouml;&szlig;en gem&auml;&szlig;
        Empfehlung, Anfertigung der Beschriftung nach Belegungsplan und die Einlagerung selbst.
        Alle Planungsunterlagen daf&uuml;r liegen vollst&auml;ndig vor.</p>
      </section>

    </div>
"""

P2 = f"""
    <div class="blatt-korpus">

      <section class="feld">
        <h4>Aufgabe</h4>
        <p>Den Lagerbestand digital f&uuml;hren statt auf Zetteln &ndash; bedienbar wie eine App,
        aber ohne neue Software im Betrieb einf&uuml;hren zu m&uuml;ssen. &Uuml;ber vier Monate von
        einer einfachen Ein-Datei-L&ouml;sung zu einem modular aufgebauten System mit Tablet- und
        Entwicklermodus entwickelt.</p>
      </section>

      <div class="kennzahlen">
        <div><b>V3.3</b><span>Stand im Einsatz</span></div>
        <div><b>5</b><span>Arbeitsbl&auml;tter</span></div>
        <div><b>4</b><span>eigene Eingabemasken</span></div>
        <div><b>A&ndash;H</b><span>Modulgruppen</span></div>
        <div><b>18</b><span>Entwicklungsschritte</span></div>
        <div><b>~4</b><span>Monate Entwicklung</span></div>
      </div>

      <section class="feld">
        <h4>1 &middot; Die Bedienoberfl&auml;che</h4>
{bildreihe(
 ("projekte/projekt-2/img/design-dashboard.jpg",
  "Bildschirmfoto des Dashboards: Eingabefeld für den Barcode oben, links die Scannfunktionen Einbuchen, Ausbuchen, Artikel hinzufügen und löschen, in der Mitte das Suchergebnis mit allen Artikelfeldern, rechts der Exportbereich",
  "Dashboard: Barcode scannen, Menge eingeben, fertig. Links die Buchungsfunktionen, in der Mitte das Suchergebnis, rechts der Export."),
 ("projekte/projekt-2/img/tablet-modus.jpg",
  "Bildschirmfoto des Tablet-Modus: Vollbild-Oberfläche mit Symbolleiste links, Filterfeldern und der Artikelliste",
  "Tablet-Modus f&uuml;r die Bedienung direkt an der Maschine &ndash; ohne Excel-Bedienelemente."))}
{bildreihe(
 ("projekte/projekt-2/img/design-artikelliste.png",
  "Bildschirmfoto der Artikelliste mit Spalten für Barcode, Bezeichnung, Profil, Maß, Material, Bestand und Preis",
  "Artikelliste &ndash; die zentrale Datentabelle."),
 ("projekte/projekt-2/img/verlauf-testdaten.jpg",
  "Bildschirmfoto des Verlaufsprotokolls mit Zeitstempeln, Buchungsart und Mengenänderungen",
  "Verlaufsprotokoll: jede Buchung mit Zeitstempel und Mengen&auml;nderung."))}
      </section>

      <section class="feld">
        <h4>2 &middot; Datenmodell &ndash; was das System speichert</h4>
{tab("projekt-2/02-ausgangslage.html", "Artikeln Liste", titel="Blatt „Artikeln Liste“ – Spaltenaufbau")}
{tab("projekt-2/02-ausgangslage.html", "Verlauf", titel="Blatt „Verlauf“ – Protokollaufbau")}
      </section>

      <section class="feld">
        <h4>3 &middot; Kernfunktionen</h4>
{tab("projekt-2/04-kernfunktionen.html", "Zusammenspiel der drei Makros", titel="Zusammenspiel der Kernmakros")}
      </section>

      <section class="feld">
        <h4>4 &middot; Material-Entnahme mit automatischer Resteverwaltung</h4>
        <p>Die j&uuml;ngste und betrieblich wichtigste Funktion: Beim Zuschnitt wird die Restl&auml;nge
        selbstst&auml;ndig eingebucht oder mit vorhandenen gleich langen Resten zusammengefasst.
        Damit ist die Aufgabe &bdquo;Reste besser nutzen&ldquo; nicht nur sichtbar gemacht, sondern
        automatisiert.</p>
{tab("projekt-2/09-material-entnahme.html", "Was im Hintergrund passiert", titel="Ablauf der Material-Entnahme")}
      </section>

      <section class="feld">
        <h4>5 &middot; Entwicklerzugang</h4>
{bild("projekte/projekt-2/img/entwickler-modus.jpg",
  "Bildschirmfoto des Entwicklermodus mit eingeblendeten Excel-Bedienelementen und Zugriff auf die Einstellungen",
  "Entwicklermodus: blendet die Excel-Oberfl&auml;che wieder ein, f&uuml;r Wartung und Anpassungen.", True)}
      </section>

      <section class="feld feld--nutzen">
        <h4>Nutzen f&uuml;r den Betrieb</h4>
        <p>Der Bestand ist durchsuchbar statt verstreut. Buchen per Scan statt Tippen reduziert
        Erfassungsfehler. Knapper Bestand f&auml;llt durch die automatische F&auml;rbung sofort
        optisch auf, statt erst beim Nachz&auml;hlen entdeckt zu werden. Jede Bewegung ist mit
        Zeitstempel nachvollziehbar &ndash; n&uuml;tzlich bei R&uuml;ckfragen und Inventur. Und der
        Verschnitt wird automatisch erfasst, statt verloren zu gehen.</p>
      </section>

      <section class="feld feld--offen">
        <h4>Bekannte offene Punkte</h4>
{tab("projekt-2/10-fazit.html", "Offene Punkte", titel="Offene Punkte und nächste Schritte")}
      </section>

    </div>
"""

P3 = f"""
    <div class="blatt-korpus">

      <section class="feld">
        <h4>Aufgabe</h4>
        <p>Das Lagersystem aus Projekt 02 lief zuverl&auml;ssig, war aber an eine Excel-Datei auf
        einem einzelnen Rechner gebunden. Es sollte unabh&auml;ngig von Ger&auml;t und Person laufen
        &ndash; mehrbenutzerf&auml;hig, plattformunabh&auml;ngig und ohne die bekannten Schwachstellen
        des Originals.</p>
      </section>

      <div class="kennzahlen">
        <div><b>86</b><span>echte Datens&auml;tze &uuml;bernommen</span></div>
        <div><b>50</b><span>Artikelgruppen</span></div>
        <div><b>3</b><span>Code-Schichten</span></div>
        <div><b>100</b><span>gleichzeitige Schreibzugriffe gepr&uuml;ft</span></div>
        <div><b>2</b><span>Betriebsarten fertig</span></div>
        <div><b>24</b><span>VBA-Module abgel&ouml;st</span></div>
      </div>

      <section class="feld">
        <h4>1 &middot; Was abgel&ouml;st wurde</h4>
{tab("projekt-3/02-original-system.html", "Die sechs Tabellenblätter", titel="Die sechs Tabellenblätter des Originals")}
{tab("projekt-3/02-original-system.html", "VBA-Module", titel="Die 24 VBA-Module nach Themenbereich A bis H")}
{tab("projekt-3/02-original-system.html", "Datenmodell", titel="Datenmodell der Excel-Tabellen")}
      </section>

      <section class="feld">
        <h4>2 &middot; Warum eine Neuentwicklung n&ouml;tig war</h4>
{tab("projekt-3/03-schwachstellen.html", "Sechs konkrete Schwachpunkte", titel="Schwachstellen des Excel-Systems")}
      </section>

      <section class="feld">
        <h4>3 &middot; Aufbau der neuen Anwendung</h4>
{tab("projekt-3/04-architektur.html", "Drei klar getrennte Schichten", titel="Drei-Schichten-Architektur")}
{tab("projekt-3/05-vba-python-portierung.html", "Die Gegenüberstellung", titel="Gegenüberstellung VBA zu Python")}
      </section>

      <section class="feld">
        <h4>4 &middot; Cloud-Betrieb</h4>
{tab("projekt-3/10-cloud-migration.html", "Zwei Wege", titel="Zwei geprüfte Wege in die Cloud")}
{tab("projekt-3/10-cloud-migration.html", "Postgres-Fallstricke", titel="Vier gelöste Postgres-Fallstricke")}
      </section>

      <section class="feld">
        <h4>5 &middot; Betrieb und Wartung</h4>
{tab("projekt-3/12-code-vertiefung.html", "Betriebs-Skripte", titel="Betriebs-Skripte im Überblick")}
      </section>

      <section class="feld feld--nutzen">
        <h4>Nutzen f&uuml;r den Betrieb</h4>
        <p>Das Lager h&auml;ngt nicht mehr an einem Rechner und nicht mehr an einer Person. Mehrere
        Personen k&ouml;nnen gleichzeitig buchen &ndash; ein Lasttest mit 100 gleichzeitigen
        Schreibzugriffen wurde bestanden. Papierkorb und L&ouml;sch-Sicherheitsabfrage sch&uuml;tzen
        vor Bedienfehlern. Der lokale Betrieb auf dem Mac l&auml;uft unver&auml;ndert mit
        t&auml;glichem Backup weiter; die Cloud-Version ist unter einer privaten, einladungsbasierten
        Adresse erreichbar. Ein Windows-Setup-Paket liegt als R&uuml;ckfalloption bereit, falls der
        Betrieb auf einen Firmenrechner umzieht.</p>
      </section>

      <section class="feld feld--offen">
        <h4>Bekannte Einschr&auml;nkungen</h4>
{tab("projekt-3/13-fazit.html", "Bekannte Einschränkungen", titel="Bekannte Einschränkungen im Betrieb")}
      </section>

    </div>
"""

open(os.path.join(HIER, "_k13.py"), "w", encoding="utf-8").write(
    "P1 = " + repr(P1) + "\nP2 = " + repr(P2) + "\nP3 = " + repr(P3) + "\n")
print("Kapitel 1-3 gebaut:", len(P1), len(P2), len(P3))
