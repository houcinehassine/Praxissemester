# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt3 import *

einschraenkungen = """<table class="tabelle"><thead><tr><th>Einschränkung</th><th>Details</th></tr></thead><tbody>
<tr><td>Neon pausiert bei Inaktivität</td><td>Die kostenlose Neon-Datenbank pausiert nach ca. 5 Minuten Inaktivität und braucht beim nächsten Zugriff einen kurzen Moment zum Aufwachen &ndash; im normalen Betrieb kaum spürbar.</td></tr>
<tr><td>Cloud-Backup ersetzt lokales Skript</td><td>Automatische Datensicherung erfolgt in der Cloud-Variante durch Neon selbst (Point-in-Time-Recovery, im kostenlosen Plan für die letzten 6 Stunden).</td></tr>
<tr><td>Netzwerkadresse nicht fest</td><td>Die Netzwerkadresse des lokalen Mac-Betriebs ist nicht als feste IP im Router hinterlegt und könnte sich theoretisch ändern.</td></tr>
</tbody></table>"""

body = seiten_kopf(13, "Fazit &amp; Ausblick",
    "Vom vollständigen Verstehen eines gewachsenen Excel/VBA-Systems bis zu einer eigenständigen, "
    "mehrfach abgesicherten und privat erreichbaren Cloud-Anwendung.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>Was heute funktioniert</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>Vollständige Funktionsabbildung</strong>alle Funktionen des Originalsystems &ndash; jetzt plattformunabhängig, mehrbenutzerfähig und ohne Code-Duplizierung für Mac/Windows.</span></li>
        <li><span><strong>Papierkorb-Funktion</strong>und Lösch-Sicherheitsabfrage als Schutz vor Bedienfehlern &ndash; eine direkte Antwort auf eine Schwachstelle des Originals.</span></li>
        <li><span><strong>Lokaler Betrieb auf dem Mac</strong>läuft weiterhin unverändert als Hintergrunddienst mit automatischem täglichem Backup.</span></li>
        <li><span><strong>Cloud-Version</strong>unter einer privaten, einladungsbasierten Adresse erreichbar &ndash; unabhängig von jedem einzelnen Gerät oder jeder einzelnen Person, mit denselben 86 realen Artikel-Datensätzen.</span></li>
        <li><span><strong>Fertig vorbereitetes Windows-Setup-Paket</strong>als Alternative bzw. Rückfalloption, falls der Betrieb auf einen Firmenrechner umzieht.</span></li>
      </ul>
    </section>

    <section>
      <h2>Bekannte Einschränkungen</h2>
      <div class="tabelle-wrapper">{einschraenkungen}</div>
    </section>

    <section>
      <h2>Was ich aus dem Projekt mitnehme</h2>
      <div class="fazit-grid">
        <div class="karte">
          <span class="label">Fachlich</span>
          <h4>Eine Migration ist mehr als eine Übersetzung</h4>
          <p>Die Materialentnahme-Logik ließ sich fast 1:1 übertragen &ndash; aber erst nachdem ich das VBA-Original vollständig verstanden hatte, nicht nur seinen Code kopiert.</p>
        </div>
        <div class="karte">
          <span class="label">Methodisch</span>
          <h4>Schichten trennen zahlt sich bei jeder Änderung aus</h4>
          <p>Die Drei-Schichten-Architektur (app/logic/db) hat den Cloud-Umzug erst möglich gemacht, ohne app.py oder logic.py überhaupt anfassen zu müssen &ndash; nur db.py wurde erweitert.</p>
        </div>
        <div class="karte">
          <span class="label">Praktisch</span>
          <h4>Echte Daten von Anfang an ernst nehmen</h4>
          <p>86 reale Datensätze wurden bei jeder Änderung mitgetestet &ndash; das hat mehrere Postgres-Fallstricke schon vor dem Go-Live sichtbar gemacht statt erst danach.</p>
        </div>
      </div>
    </section>

    <section>
      <div class="zitat-box">
        Aus einer Excel-Datei, die an einen einzelnen Rechner gebunden war, ist eine
        Anwendung geworden, die unabhängig von jedem einzelnen Gerät oder jeder einzelnen
        Person läuft &ndash; mit denselben echten Daten, aber ohne deren größte Schwäche:
        die Abhängigkeit von einer einzelnen Person.
      </div>
    </section>

    <nav class="projekt-nav">
      <a href="12-code-vertiefung.html">
        <span class="richtung">&larr; Zurück</span>
        Code-Vertiefung
      </a>
      <a class="naechste" href="../../index.html#projekte">
        <span class="richtung">Zur Übersicht &rarr;</span>
        Alle Projekte
      </a>
    </nav>
  </main>
"""

write_page("13-fazit.html", "Projekt 3: Fazit & Ausblick", body)
