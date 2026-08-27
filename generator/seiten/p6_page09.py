# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt6 import *

body = seiten_kopf(9, "Gewähltes Konzept &ndash; 4-Etagen-Aufbau",
    "Die Konzeptentscheidung: Der Wagen besteht aus vier Etagen. Damit ist der modulare Aufbau "
    "festgelegt und das Konzept vom groben Portalgestell zur konkreten Baugruppenstruktur "
    "weiterentwickelt.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>🏗️ Etagen-Übersicht</h2>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>1️⃣ Etage 1</h4><p>Freier Platz für Schweißmaschine / Bestandswagen + Fixationssystem.</p></div>
        <div class="mini-karte"><h4>2️⃣ Etage 2</h4><p>Schublade.</p></div>
        <div class="mini-karte"><h4>3️⃣ Etage 3</h4><p>Schublade (identisch zu Etage 2).</p></div>
        <div class="mini-karte"><h4>4️⃣ Etage 4</h4><p>Oberer Deckel + seitliche Lochwände.</p></div>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Vorteil des Etagenkonzepts:</strong>
        Modularität (jede Etage ist eine eigene Baugruppe, getrennt konstruierbar und fertigbar)
        &middot; Wiederholteile (Etage 2 und 3 sind identisch &rarr; nur eine Konstruktion,
        doppelte Stückzahl) &middot; Änderungsfreundlich (Etagen später ergänz- oder tauschbar)
        &middot; Fertigung in kleineren, handhabbaren Schweiß-/Montagegruppen.
      </div>
    </section>

    <section>
      <h2>1️⃣ Etage 1 &ndash; Aufnahme für Maschine / Bestandswagen</h2>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Etage 1 in vier Ansichten</span>
          <img src="img/etage1-aufnahme-bestandswagen.jpg" alt="CAD-Vieransicht der Etage 1: offener U-förmiger Rahmen aus Profilen mit vier Ständern, Draufsicht, Front- und Seitenansicht mit Querriegeln zur Aussteifung" />
          <p class="bildtext">Offener Rahmen &ndash; eine Seite bleibt frei (U-förmig), der Bestandswagen fährt von dort ein. Auf der Rückseite mehrere waagerechte Querriegel zur Aussteifung.</p>
        </div>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Offener Punkt &ndash; Fixationssystem:</strong> Das Fixationssystem ist im Text
        genannt, aber in den Ansichten nicht dargestellt. Zu klären: Wie wird der Bestandswagen
        arretiert (Anschlag, Bolzen, Klemme, Rastung)? Wird er nur positioniert oder auch gegen
        Herausrollen gesichert? Muss die Fixierung werkzeuglos bedienbar sein?
      </div>
    </section>

    <section>
      <h2>2️⃣3️⃣ Etage 2 &amp; 3 &ndash; Schubladenetagen</h2>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Zusammengesetzte Baugruppe: Etagen 2&ndash;4</span>
          <img src="img/etagen-schubladen-lochwand.jpg" alt="CAD-Detailansicht der montierten Etagen: zwei übereinanderliegende Schubladenebenen mit sichtbaren Führungsschienen, oberer Deckelrahmen und seitlich angehängte Lochwand" />
          <p class="bildtext">Zwei Schubladenebenen mit sichtbaren Führungsschienen, oberer offener Rahmen als Ablage, seitlich angehängte Lochwand über die gesamte Wagenbreite.</p>
        </div>
      </div>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Merkmal</th><th>Ausführung</th></tr></thead>
          <tbody>
            <tr><td>Bauform</td><td>Rechteckige Blechwanne mit umlaufendem Profilrahmen</td></tr>
            <tr><td>Führung</td><td>Seitliche Auszugsschienen (als C-Profile erkennbar)</td></tr>
            <tr><td>Wiederholteil</td><td>Etage 2 und 3 identisch &rarr; 2× dieselbe Baugruppe</td></tr>
            <tr><td>Rahmenanbindung</td><td>Über Profilrahmen an den Ständern verschraubt</td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Zwei Abweichungen vom Lastenheft:</strong>
        (1) Ursprünglich war ein fertiger Schubladenblock als Zukaufteil vorgesehen (A-04) &ndash;
        hier werden die Schubladen nun als Eigenkonstruktion ausgeführt. Vorteil: Maße passen
        exakt zum Rahmen. Nachteil: höherer Konstruktions- und Fertigungsaufwand.
        (2) Das Lastenheft nennt drei Schubladen, das gewählte Konzept sieht nur zwei vor
        &ndash; zu prüfen, ob der Stauraum ausreicht.
      </div>
    </section>

    <section>
      <h2>4️⃣ Etage 4 &ndash; Deckel und Lochwände</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Festlegung</th><th>Beschreibung</th><th>Konstruktive Folge</th></tr></thead>
          <tbody>
            <tr><td>Nur ein Deckel oben</td><td>Obere Etage wird als Deckel/Ablage ausgeführt</td><td>Vereinfachung gegenüber Version 1</td></tr>
            <tr><td>Lochwand seitlich</td><td>Lochwände werden an der Seite angehängt &ndash; nicht umlaufend fest verbaut</td><td>Demontierbar, austauschbar</td></tr>
            <tr><td>Breite der Lochwand</td><td>Entspricht der Breite des Wagens</td><td>Maßbezug zum Rahmen</td></tr>
            <tr><td>Höhe der Lochwand</td><td>Entspricht der Höhe der 2 Schubladen</td><td>Maßbezug zu Etage 2+3</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Gut gelöst:</strong> Die Lochwandmaße sind relativ definiert (Wagenbreite × Höhe
        der zwei Schubladenetagen). Dadurch passt sich die Wand automatisch an, wenn sich die
        Rahmenmaße noch ändern &ndash; ein sauberer parametrischer Ansatz.
      </div>
    </section>

    <section>
      <h2>🔧 Bauweise &ndash; Profilsystem oder Schweißkonstruktion?</h2>
      <p>
        Alle Etagen sind in den CAD-Modellen erkennbar aus Nutprofil (Item-Aluprofil) aufgebaut
        &ndash; mit Eckverbindern und Nutensteinen, nicht geschweißt. Damit wäre faktisch
        Variante A aus dem Schriftfeld von SW-001 gewählt.
      </p>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Kriterium</th><th>Variante A: Item-Aluprofil</th><th>Variante B: Stahl geschweißt</th></tr></thead>
          <tbody>
            <tr><td>Fertigung</td><td>Sägen + Schrauben, keine Schweißnähte</td><td>Zuschnitt + Schweißen + Richten</td></tr>
            <tr><td>Änderbarkeit</td><td><span class="st-ok">✅ Sehr hoch &ndash; lösbar, umbaubar</span></td><td><span class="st-no">❌ Gering</span></td></tr>
            <tr><td>Gewicht</td><td><span class="st-ok">✅ Leichter (Aluminium)</span></td><td>Schwerer</td></tr>
            <tr><td>Materialkosten</td><td><span class="st-no">❌ Höher (Profil + Verbinder)</span></td><td><span class="st-ok">✅ Niedriger (Kantrohr)</span></td></tr>
            <tr><td>Fertigungszeit</td><td><span class="st-ok">✅ Kürzer</span></td><td>Länger</td></tr>
            <tr><td>Werkstattkompetenz</td><td>Montage</td><td><span class="st-ok">✅ Kernkompetenz des Betriebs (Metallbau)</span></td></tr>
            <tr><td>Steifigkeit</td><td>Gut bei richtiger Verbindertechnik</td><td><span class="st-ok">✅ Sehr hoch</span></td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Für den Bericht:</strong> Genau dieser Vergleich ist die von der Hochschule
        geforderte „technisch-wirtschaftliche Gegenüberstellung: Item-Profile vs. normale
        Werkbank“. Beide Varianten liegen vor &ndash; es fehlt nur noch die Kostenaufstellung.
        <em>Wie der Zeichnungssatz auf Seite 10 zeigt, wurde am Ende tatsächlich Stahl ausgeführt.</em>
      </div>
    </section>

    <section>
      <h2>🚨 Kritische Punkte dieses Konzeptstands</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>#</th><th>Punkt</th><th>Hintergrund</th></tr></thead>
          <tbody>
            <tr><td>1</td><td>Wo bleibt die Gasflasche?</td><td>Im 4-Etagen-Konzept ist keine Gasflaschenaufnahme vorgesehen. Zu klären: Bleibt die Flasche auf dem Bestandswagen (Etage 1) oder braucht sie eine eigene Halterung?</td></tr>
            <tr><td>2</td><td>Erdung bei Aluprofil-Bauweise</td><td>Nutprofile sind oft eloxiert &ndash; die Oxidschicht ist elektrisch isolierend. Für eine sichere Masse-/Erdungsverbindung (A-13) sind gezielte Kontaktstellen nötig. Bei geschweißtem Stahl entfällt dieses Problem.</td></tr>
            <tr><td>3</td><td>Weiterhin keine Bemaßung</td><td>Auch dieses Dokument enthält keine Maße. Für Fertigung, Stückliste und Kostenvergleich sind Hauptmaße zwingend erforderlich.</td></tr>
            <tr><td>4</td><td>Hitzebeständigkeit</td><td>Am Schweißplatz fallen Funken und heiße Schlacke an. Aluminium schmilzt bei ca. 660 °C, Stahl deutlich später. Prüfen, ob Ablageflächen im Funkenflugbereich aus Stahlblech ausgeführt werden sollten.</td></tr>
          </tbody>
        </table>
      </div>
    </section>

{projekt_nav("08-variante-b-zusatzwagen.html", "Variante B: Zusatzwagen", "10-zeichnungssatz.html", "Zeichnungssatz (21 Blätter)")}
  </main>
"""

write_page("09-gewaehltes-konzept.html", "Projekt 6: Gewähltes Konzept", body)
