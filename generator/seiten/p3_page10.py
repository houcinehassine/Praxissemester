# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt3 import *

code_zwei_wege = """def get_connection():
    if _ist_postgres():
        # pandas' read_sql_query braucht einen normalen Tupel-Cursor.
        return psycopg2.connect(DATABASE_URL)

    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute(&quot;PRAGMA foreign_keys = ON&quot;)
    conn.execute(&quot;PRAGMA journal_mode = WAL&quot;)
    conn.execute(&quot;PRAGMA busy_timeout = 5000&quot;)
    return conn"""

body = seiten_kopf(10, "Cloud-Migration",
    "Ein System, das an den privaten Rechner einer einzelnen Person gebunden ist, ist nicht "
    "betriebsfähig, sobald diese Person das Unternehmen verlässt &ndash; die Entscheidung für "
    "GitHub, Neon und Streamlit Community Cloud.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>Der strukturelle Schwachpunkt</h2>
      <p>
        Bei der Planung der Übergabe wurde ein entscheidender struktureller Schwachpunkt erkannt:
        Der Praktikant, auf dessen Rechner die Anwendung lief, würde das Unternehmen irgendwann
        wieder verlassen &ndash; ein System, das an eine einzelne Person gebunden ist, wäre dann
        nicht mehr betriebsfähig.
      </p>
    </section>

    <section>
      <h2>Zwei Wege, gegenübergestellt</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Option</th><th>Vorteil</th><th>Nachteil</th></tr></thead>
          <tbody>
            <tr><td>Firmenrechner (z.&nbsp;B. PC des Vorgesetzten)</td><td>Kostenlos, kein zusätzliches Sicherheitsrisiko</td><td>Weiterhin auf das Büro-Netzwerk beschränkt</td></tr>
            <tr><td>Echtes Cloud-Hosting</td><td>Von überall erreichbar</td><td>Echte Kosten, notwendiger Zugriffsschutz (bis dahin kein Login), größerer technischer Umbau (eine einzelne SQLite-Datei passt nicht zu den meisten Cloud-Plattformen)</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Die Entscheidung fiel zugunsten der Cloud:</strong>
        GitHub für die Quellcodeverwaltung, Neon als kostenlose gehostete Postgres-Datenbank und
        Streamlit Community Cloud als Ausführungsumgebung mit privatem,
        einladungsbasiertem Zugriff &ndash; alle drei Dienste in ihrer kostenlosen Stufe für
        diesen Anwendungsfall ausreichend.
      </div>
    </section>

    <section>
      <h2>Die Zwei-Wege-Datenzugriffsschicht</h2>
      <p>
        Statt die lokale SQLite-Lösung zu ersetzen, wurde <code>db.py</code> so erweitert, dass sie
        beide Betriebsarten beherrscht: Ist eine <code>DATABASE_URL</code> konfiguriert (lokal über
        eine Umgebungsvariable, in der Cloud über die Streamlit-Secrets-Verwaltung), verbindet sich
        die Anwendung mit Postgres; andernfalls bleibt sie unverändert beim lokalen SQLite-Betrieb.
        Damit läuft exakt derselbe Anwendungscode wahlweise lokal oder in der Cloud, ohne
        Verzweigungen im restlichen Programm &ndash; eine bewusste Abkehr von der
        Mac/Windows-Verzweigungslogik des Originalsystems.
      </p>
      <pre class="code-block">{code_zwei_wege}</pre>
      <p style="margin-top:0.75rem">
        Für Postgres wurde ein eigenes, syntaktisch angepasstes Schema
        (<code>schema_postgres.sql</code>) erstellt sowie ein Migrationsskript
        (<code>migrate_sqlite_to_postgres.py</code>, siehe Seite 12), das die bestehenden Daten aus
        der lokalen Datenbank vollständig und wiederholbar in die Cloud-Datenbank überträgt.
      </p>
    </section>

    <section>
      <h2>Vier subtile Postgres-Fallstricke</h2>
      <p class="section-intro">Erst durch systematisches Testen gegen eine echte lokale Postgres-Testinstanz aufgedeckt.</p>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Fallstrick</th><th>Was passierte</th></tr></thead>
          <tbody>
            <tr><td><span class="st-warn">Groß-/Kleinschreibung</span></td><td>Anders als SQLite faltet Postgres unquotierte Tabellen- und Spaltennamen automatisch auf Kleinschreibung. Ein eigens gebautes Zeilen-Objekt (<code>_Zeile</code>, siehe Seite 12) sorgt seither dafür, dass Ergebniszeilen unabhängig vom Datenbanktyp exakt die im Schema definierte Schreibweise zeigen.</td></tr>
            <tr><td><span class="st-warn">Cursor-Typ-Konflikt mit pandas</span></td><td>Ein für den eigenen dict-artigen Zeilenzugriff gesetzter Cursor-Typ kollidierte mit der Art, wie pandas Tabellen aus einer Datenbankverbindung einliest &ndash; behoben durch getrennte Cursor-Konfigurationen für beide Anwendungsfälle.</td></tr>
            <tr><td><span class="st-warn">Alias-Kollision</span></td><td>Ein in einer Abfrage verwendeter Kurzname geriet in Konflikt mit einer echten Spalte gleichen Namens in einer anderen Tabelle und lieferte dadurch falsche Werte zurück.</td></tr>
            <tr><td><span class="st-warn">Sequenz-Fortsetzung</span></td><td>Nach dem Übertragen bestehender Datensätze mit bereits vergebenen IDs musste der interne Postgres-Zähler für automatisch vergebene IDs manuell auf den höchsten übertragenen Wert gesetzt werden, um spätere ID-Kollisionen zu vermeiden.</td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        Jede dieser Korrekturen wurde vor der Veröffentlichung lokal gegen eine eigens
        installierte Postgres-Testinstanz mit einer Kopie der echten 86 Datensätze nachgestellt
        und durch einen vollständigen Klick-Test aller Seiten und Dialoge verifiziert, bevor sie
        live geschaltet wurde.
      </div>
    </section>

{projekt_nav("09-produktionsreife.html", "Produktionsreife", "11-go-live.html", "Go-Live")}
  </main>
"""

write_page("10-cloud-migration.html", "Projekt 3: Cloud-Migration", body)
