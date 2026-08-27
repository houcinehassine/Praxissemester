# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt3 import *

body = seiten_kopf(11, "Go-Live &amp; Fehlerbehebung",
    "Die eigentliche Veröffentlichung über GitHub, Neon und Streamlit Community Cloud &ndash; "
    "und zwei Fehler, die kurz danach gemeldet und grundlegend statt nur symptomatisch behoben "
    "wurden.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>Die Go-Live-Schritte</h2>
      <div class="stepper">
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">1</span>
            <span class="schritt-titel">Privates GitHub-Repository</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Anlegen eines privaten Repositorys, Hochladen des Quellcodes &ndash; die lokale Datenbankdatei, Backups sowie Zugangsdaten wurden über eine <code>.gitignore</code>-Konfiguration bewusst ausgeschlossen.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">2</span>
            <span class="schritt-titel">Neon-Postgres-Datenbank</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Einrichten einer kostenlosen Neon-Postgres-Datenbank und Übertragung der 86 echten Artikel-Datensätze samt aller Stammdaten mittels des vorbereiteten Migrationsskripts.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">3</span>
            <span class="schritt-titel">Deployment auf Streamlit Community Cloud</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Verbunden mit dem GitHub-Repository, die Datenbankverbindung als geschütztes Secret hinterlegt.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">4</span>
            <span class="schritt-titel">Zugriff einschränken</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Einschränkung der Sichtbarkeit auf ausgewählte, eingeladene Personen („Only specific people can view this app“) &ndash; der Link ist nicht öffentlich zugänglich.</p></div>
        </div>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        Nach dem Deployment wurde die Live-Anwendung direkt im Browser gegen die echten Daten
        getestet: Anzeige der 86 Artikel und 50 Artikelgruppen, Anlegen, Bearbeiten, Entnehmen und
        Löschen eines Artikels sowie die Papierkorb-Funktion &ndash; bei laufender Verifikation,
        dass der weiterhin parallel aktive lokale Mac-Betrieb davon unberührt blieb.
      </div>
    </section>

    <section>
      <h2>Fehlerbehebung nach dem Go-Live</h2>
      <p>
        Kurz nach der ersten Veröffentlichung meldete der Auftraggeber Fehlermeldungen beim
        Aufrufen der Seiten „Artikel Liste“ und „Reste“ sowie beim Anlegen eines neuen Artikels
        über den „Hinzufügen“-Dialog.
      </p>
      <p style="margin-top:0.75rem">
        Beide Fehler ließen sich auf dieselbe Grundursache zurückführen &ndash; die
        Postgres-Eigenheiten bei der Groß-/Kleinschreibung aus Seite 10 &ndash; traten jedoch an
        Stellen auf, die von den ursprünglichen Tests nicht abgedeckt waren: ein positionaler
        Listenzugriff sowie eine zufällige Namensüberschneidung eines Abfrage-Alias mit einer
        echten Spalte.
      </p>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Grundlegend statt symptomatisch behoben:</strong> Das interne Zeilen-Objekt
        (<code>_Zeile</code>) benennt Spalten seither bereits beim Erzeugen der Zeile korrekt um,
        sodass sowohl der direkte Feldzugriff als auch eine Umwandlung in ein gewöhnliches
        Python-Dictionary zuverlässig die richtige Schreibweise liefert &ndash; statt nur die zwei
        gemeldeten Symptome einzeln zu flicken.
      </div>
      <p style="margin-top:0.75rem">
        Die Korrektur wurde erneut vollständig lokal nachgestellt (inklusive Nachstellen des
        exakt gemeldeten Ablaufs), vor der Veröffentlichung durch einen kompletten Klick-Test
        aller Seiten und Dialoge bestätigt und anschließend live verifiziert, bevor der Vorgang
        als abgeschlossen gemeldet wurde.
      </p>
    </section>

{projekt_nav("10-cloud-migration.html", "Cloud-Migration", "12-code-vertiefung.html", "Code-Vertiefung")}
  </main>
"""

write_page("11-go-live.html", "Projekt 3: Go-Live & Fehlerbehebung", body)
