# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt3 import *

body = seiten_kopf(9, "Produktionsreife auf dem lokalen Rechner",
    "Vor der Übergabe an den Vorgesetzten wurde die Betriebssicherheit systematisch verbessert "
    "&ndash; auf die Frage „was sollte vor der offiziellen Nutzung noch passieren?“ wurden vier "
    "Punkte identifiziert und umgesetzt.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>Automatisches Backup</h2>
      <p>
        Ein Backup-Skript sichert die Datenbank über SQLites <code>VACUUM INTO</code>-Befehl in
        eine eigenständige, in sich konsistente Kopie. Zunächst lief dieses Backup nur beim Start
        der Anwendung &ndash; bei einem durchgehend laufenden Hintergrunddienst wäre das Backup
        dadurch aber nie aktualisiert worden. Diese Lücke wurde später durch einen zusätzlichen,
        täglich zu fester Uhrzeit ausgelösten Backup-Zeitplan geschlossen, unabhängig von
        Neustarts. Es werden automatisch die letzten 30 Tage aufbewahrt.
      </p>
    </section>

    <section>
      <h2>Automatischer Hintergrunddienst</h2>
      <p>
        Um die Abhängigkeit von einem ständig geöffneten Terminal-Fenster zu beseitigen, wurde
        ein macOS-<strong>LaunchAgent</strong> eingerichtet: Die Anwendung startet seither
        automatisch beim Anmelden am Rechner und startet sich bei einem Absturz selbstständig
        neu &ndash; verifiziert durch gezieltes Beenden des Prozesses im laufenden Betrieb.
      </p>
    </section>

    <section>
      <h2>Umzug aus iCloud Drive</h2>
      <p>
        Dabei zeigte sich ein grundlegendes Problem: Der Projektordner lag ursprünglich in
        iCloud Drive, und macOS verweigert Hintergrunddiensten dort systembedingt den
        Dateizugriff. Nach Rücksprache wurde das gesamte Projekt in einen lokalen, nicht
        synchronisierten Ordner verschoben (die ursprüngliche Kopie blieb dabei &ndash; nur
        umbenannt &ndash; als Sicherheitsnetz erhalten), die virtuelle Python-Umgebung an der
        neuen Stelle neu aufgebaut und der Hintergrunddienst entsprechend umkonfiguriert.
      </p>
    </section>

    <section>
      <h2>Kurzanleitung für den Vorgesetzten</h2>
      <p>
        Ergänzend zur technischen README wurde eine kurze, nicht-technische Anleitung für die
        tägliche Nutzung erstellt: Öffnen der App, Übersicht der Seiten, die wichtigsten Aktionen
        im Schnellzugriff sowie das Vorgehen bei versehentlichem Löschen.
      </p>
    </section>

    <section>
      <h2>Mehrgeräte-Zugriff und Windows-Vorbereitung</h2>
      <p class="section-intro">Für den Zugriff weiterer Mitarbeitender &ndash; und für den Fall, dass der Betrieb irgendwann auf einen Firmenrechner umzieht.</p>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>macOS</h4><p>Eine <code>.webloc</code>-Datei, die direkt auf die Netzwerkadresse der laufenden Anwendung zeigt &ndash; kein Installationsschritt nötig.</p></div>
        <div class="mini-karte"><h4>Windows</h4><p>Das entsprechende Pendant als <code>.url</code>-Datei.</p></div>
        <div class="mini-karte"><h4>iOS/Android</h4><p>Die Vorgehensweise „Zum Home-Bildschirm hinzufügen“ dokumentiert.</p></div>
        <div class="mini-karte"><h4>Windows-Setup-Paket</h4><p>Ein plattformunabhängiges Backup-Skript (Python statt Bash), ein Start-Skript per Windows-Aufgabenplanung (unsichtbar über ein VBS-Wrapper-Skript gestartet), ein manueller Doppelklick-Fallback sowie eine ausführliche Schritt-für-Schritt-Anleitung.</p></div>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Warum das Windows-Paket wichtig war:</strong> Die ursprüngliche Lösung war an den
        privaten Rechner des Praktikanten gebunden. Ein vollständiges Windows-Setup-Paket wurde
        deshalb vorbereitet, damit der Betrieb bei Bedarf auf einen Firmenrechner (z. B. den PC
        des Vorgesetzten) umziehen kann &ndash; unabhängig davon, ob am Ende der lokale Weg oder
        die Cloud-Variante (Seite 10) genutzt wird.
      </div>
    </section>

{projekt_nav("08-papierkorb.html", "Papierkorb", "10-cloud-migration.html", "Cloud-Migration")}
  </main>
"""

write_page("09-produktionsreife.html", "Projekt 3: Produktionsreife", body)
