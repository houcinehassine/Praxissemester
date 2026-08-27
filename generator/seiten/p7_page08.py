# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt7 import *

body = seiten_kopf(8, "Vier Layout-Konzepte",
    "Teilaufgabe B, zweiter Teil: Nicht woraus die Bank gebaut ist, sondern wie sie aufgebaut und "
    "im Raum angeordnet wird &ndash; vier Konzepte, eine Entscheidung und der Werkstatt-Grundriss.") + f"""
  <main class="projekt-detail">

    <section>
      <div class="info-box">
        <strong>Wichtige Unterscheidung:</strong> Die Bauvarianten von Seite 7 beantworten die
        Frage <em>woraus</em> (Aluprofil, Stahl, Module, Eigenbau). Die Layout-Konzepte auf dieser
        Seite beantworten die Frage <em>wie angeordnet</em> (tiefe Schränke, Lochwand mittig,
        mobiler Wagen, Systemwand). Beide Entscheidungen sind unabhängig voneinander &ndash; jedes
        Layout ließe sich in jeder Bauweise ausführen.
      </div>
    </section>

    <section>
      <h2>1️⃣ Konzept 1 &middot; Tiefe Unterschränke</h2>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Konzept 1</span>
          <img src="img/konzept1-tiefe-unterschraenke.png" alt="Isometrische Darstellung einer Werkbank mit durchgehend tiefem, geschlossenem Unterschrank über die volle Länge, Schubladen an der Front und Lochwand als Rückwand" />
          <p class="bildtext">Durchgehender tiefer Unterschrank &ndash; viel Volumen, aber 700 mm Tiefe bedeuten weites Greifen.</p>
        </div>
      </div>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Vorteile</th><th>Nachteile</th></tr></thead>
          <tbody><tr><td>Große Arbeitsfläche, viel Stauvolumen</td><td>Tiefe 700 mm &rarr; weites Greifen; hinten entsteht toter Raum</td></tr></tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>2️⃣ Konzept 2 &middot; Lochwand mittig + Hochschränke &nbsp;<span class="st-ok">✅ gewählt</span></h2>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Konzept 2 &ndash; die gewählte Lösung</span>
          <img src="img/konzept2-lochwand-mittig.png" alt="Isometrische Darstellung: schmale Werkbank mit Lochwand in der Mitte, links ein hoher gelber Schrank und rechts ein hoher grauer Schrank, beide etwa 400 mm tief" />
          <p class="bildtext">Schmale Bank mit mittiger Lochwand, links und rechts hohe schlanke Schränke mit nur ~400 mm Tiefe.</p>
        </div>
      </div>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Vorteile</th><th>Nachteile</th></tr></thead>
          <tbody><tr><td>Geringe Tiefe, alles in Reichweite, Raumhöhe genutzt statt Grundfläche</td><td>Wandverankerung der Hochschränke erforderlich</td></tr></tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Warum dieses Konzept gewinnt:</strong> Es ist das einzige, das die Zonenlogik von
        Seite 5 räumlich exakt abbildet &ndash; Lochwand in der Mitte für Zone A, Schubladen unter
        der Platte für Zone B, Hochschränke seitlich für Zone C. Statt in die Tiefe zu bauen
        (Konzept 1), nutzt es die Höhe: Bei 400 mm Schranktiefe bleibt alles in Reichweite, und
        die Werkstattgrundfläche wird geschont.
      </div>
    </section>

    <section>
      <h2>3️⃣ Konzept 3 &middot; Schlanke Bank + mobiler Wagen</h2>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Konzept 3</span>
          <img src="img/konzept3-bank-wagen.png" alt="Isometrische Darstellung einer offenen, schlanken Werkbank ohne Unterschrank mit Lochwand, daneben ein roter fahrbarer Werkzeugwagen mit vier Schubladen auf Rollen" />
          <p class="bildtext">Offene Bank ohne Unterbau, dafür ein fahrbarer Werkzeugwagen, der zur Maschine mitgeht.</p>
        </div>
      </div>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Vorteile</th><th>Nachteile</th></tr></thead>
          <tbody><tr><td>Werkzeug fährt zur Maschine &ndash; sehr flexibel, kurze Wege am Einsatzort</td><td>Zusatzkosten für den Wagen; erfordert Disziplin, damit alles wieder zurückkommt</td></tr></tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>4️⃣ Konzept 4 &middot; Systemwand über die Länge</h2>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Konzept 4</span>
          <img src="img/konzept4-systemwand.png" alt="Isometrische Darstellung einer offenen Bank vor einer durchgehenden, raumhohen Lochwand mit drei übereinanderliegenden Ablageborden über die volle Länge" />
          <p class="bildtext">Durchgehende Systemwand über die volle Länge &ndash; maximale Sicht und maximaler Zugriff.</p>
        </div>
      </div>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Vorteile</th><th>Nachteile</th></tr></thead>
          <tbody><tr><td>Maximale Sicht und maximaler Zugriff auf alles</td><td>Wenig geschlossener Stauraum &ndash; Zone C hat keinen Platz; alles steht offen im Späneflug</td></tr></tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>⚖️ Die vier Konzepte im Vergleich</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Konzept</th><th>Vorteile</th><th>Nachteile</th><th>Bewertung</th></tr></thead>
          <tbody>
            <tr><td>1 &middot; Tiefe Unterschränke</td><td>Große Fläche, viel Volumen</td><td>Tiefe 700 mm &rarr; weites Greifen</td><td><span class="st-no">❌ verworfen</span></td></tr>
            <tr><td><strong>2 &middot; Lochwand mittig + Hochschränke</strong></td><td>Geringe Tiefe, alles in Reichweite, Höhe genutzt</td><td>Wandverankerung nötig</td><td><span class="st-ok">✅ gewählt</span></td></tr>
            <tr><td>3 &middot; Bank + mobiler Wagen</td><td>Werkzeug fährt zur Maschine, flexibel</td><td>Zusatzkosten, Disziplin nötig</td><td><span class="st-warn">⚠️ als Ergänzung übernommen</span></td></tr>
            <tr><td>4 &middot; Systemwand über die Länge</td><td>Maximale Sicht &amp; Zugriff</td><td>Wenig geschlossener Stauraum</td><td><span class="st-no">❌ verworfen</span></td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Die Entscheidung ist eine Kombination:</strong> Konzept 2 als Basis, ergänzt um den
        mobilen Werkzeugwagen aus Konzept 3 für die Wege zu den Maschinen. Damit ist der
        Hauptnachteil von Konzept 2 aufgehoben &ndash; ein stationärer Platz allein hilft nicht,
        wenn an der Drehmaschine drei Meter weiter ständig Werkzeug gebraucht wird.
      </div>
    </section>

    <section>
      <h2>🖼️ Konzept 2 in 3D &ndash; mit Zonenzuordnung</h2>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Zonen A, B und C am gewählten Konzept</span>
          <img src="img/konzept2-3d-zonen.png" alt="Isometrische 3D-Ansicht des gewählten Konzepts mit Beschriftungen: Zone A an der Lochwand in der Mitte, Zone B am gelben Hochschrank links, Zone C am grauen Hochschrank rechts, auf der Bank ein Maschinenschraubstock" />
          <p class="bildtext">Zone A an der mittigen Lochwand, Zone B im linken, Zone C im rechten Hochschrank &ndash; schmale Schränke mit ~400 mm Tiefe, Bank mit 600 mm. Auf der Platte der fest verschraubte Schraubstock.</p>
        </div>
      </div>
    </section>

    <section>
      <h2>🗺️ Werkstatt-Grundriss</h2>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Maßstäbliche Draufsicht</span>
          <img src="img/werkstatt-grundriss.png" alt="Maßstäblicher Grundriss der Werkstatt in Draufsicht: Raum 6000 mal 4500 mm, Drehmaschine 2000x900 links oben, Fräsmaschine 1600x1200 rechts oben, Werkbank 2000x600 unten mittig, Werkzeugwagen 600x900 rechts unten, dazwischen Wegeflächen" />
          <p class="bildtext">U-Anordnung: Maschinen oben, Werkbank mittig unten, Wagen rechts. Zwischen den Maschinen mindestens 900 mm Freiraum.</p>
        </div>
      </div>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Element</th><th>Maß</th><th>Bemerkung</th></tr></thead>
          <tbody>
            <tr><td>Raum</td><td>6000 × 4500 mm</td><td>Beispielannahme &ndash; vor Umsetzung real aufmessen</td></tr>
            <tr><td>Drehmaschine</td><td>2000 × 900 mm</td><td>links oben</td></tr>
            <tr><td>Fräsmaschine</td><td>1600 × 1200 mm</td><td>rechts oben</td></tr>
            <tr><td>Werkbank (Konzept 2)</td><td>2000 × 600 mm</td><td>mittig unten, Banktiefe 600 mm für kurze Greifwege</td></tr>
            <tr><td>Werkzeugwagen</td><td>600 × 900 mm</td><td>rechts unten, fährt zu den Maschinen</td></tr>
            <tr><td>Freiraum je Maschine</td><td>≥ 800&ndash;1000 mm</td><td>für Bedienung, Sicherheit und Späneabfuhr</td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Zu prüfen vor der Umsetzung:</strong> Raum- und Maschinenmaße im Grundriss sind
        Beispielannahmen. Die tatsächliche Werkstatt ist aufzumessen &ndash; insbesondere, ob die
        2000 mm breite Bank an der vorgesehenen Wand überhaupt Platz findet und ob die Wand die
        Hochschränke tragen kann. Das Entscheidungsblatt legt die Bank deshalb mit ~1800 mm etwas
        schmaler fest als im Grundriss dargestellt.
      </div>
    </section>

{projekt_nav("07-varianten.html", "4 Bauvarianten", "09-nutzwertanalyse.html", "Nutzwertanalyse & Empfehlung")}
  </main>
"""

write_page("08-layout-konzepte.html", "Projekt 7: 4 Layout-Konzepte", body)
