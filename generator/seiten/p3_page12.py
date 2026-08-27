# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt3 import *

code_zeile = """class _Zeile(dict):
    def __init__(self, mapping):
        self._werte = list(mapping.values())
        super().__init__(
            (_SCHEMA_SPALTEN.get(k.lower(), k), v) for k, v in mapping.items()
        )

    def __getitem__(self, schluessel):
        if isinstance(schluessel, int):
            return self._werte[schluessel]
        return super().__getitem__(schluessel)"""

code_lock = """# Schützt &quot;Höchste Nummer suchen + neuen Barcode einfügen&quot; vor Race-Conditions,
# wenn mehrere Nutzer im Netzwerk gleichzeitig auf denselben Streamlit-Prozess zugreifen.
_SCHREIB_LOCK = threading.Lock()

def create_artikel_gruppe(profil: str, mass: str, material: str) -&gt; str:
    bezeichnung = f&quot;{profil}-{mass}-{material}&quot;
    with _SCHREIB_LOCK:
        if db.value_exists(&quot;Artikel_Gruppe&quot;, &quot;Bezeichnung&quot;, bezeichnung):
            raise LagerFehler(f&quot;Dieser Artikel existiert bereits: {bezeichnung}&quot;)
        barcode = make_barcode_ag(profil, mass, material)
        db.execute(
            &quot;INSERT INTO Artikel_Gruppe (Barcode, Bezeichnung, Profil, Mass, Material) &quot;
            &quot;VALUES (?, ?, ?, ?, ?)&quot;,
            (barcode, bezeichnung, profil, mass, material),
        )
    return barcode"""

code_migrate = """for tabelle in TABELLEN:
    zeilen = quelle.execute(f&quot;SELECT * FROM {tabelle}&quot;).fetchall()
    cur.execute(f&quot;DELETE FROM {tabelle}&quot;)
    ...
    for zeile in zeilen:
        werte = [zeile[s] for s in spalten]
        cur.execute(f&quot;INSERT INTO {tabelle} ({spalten_liste}) VALUES ({platzhalter})&quot;, werte)

    if tabelle in SERIAL_PKS:
        pk = SERIAL_PKS[tabelle]
        # pg_get_serial_sequence() erwartet Tabellen-/Spaltennamen als Text-Literal
        cur.execute(
            f&quot;SELECT setval(pg_get_serial_sequence('{tabelle.lower()}', '{pk.lower()}'), &quot;
            f&quot;COALESCE((SELECT MAX({pk}) FROM {tabelle}), 1))&quot;
        )"""

body = seiten_kopf(12, "Code-Vertiefung",
    "Drei Ausschnitte aus dem echten Quellcode, die zeigen, wie robust statt notdürftig auf "
    "die in dieser Dokumentation beschriebenen Probleme reagiert wurde.") + f"""
  <main class="projekt-detail">

    <section>
      <div class="info-box">
        <strong>Quelle</strong>
        Vollständige Code-Dokumentation der Anwendung (db.py, logic.py, app.py, Migrations- und
        Betriebs-Skripte) &ndash; Repository <code>github.com/houcinehassine/lagersystem</code> (privat).
      </div>
    </section>

    <section>
      <h2>Die <code>_Zeile</code>-Klasse: eine Postgres-Eigenheit robust gelöst</h2>
      <p>
        Postgres faltet unquotierte Bezeichner (Tabellen/Spalten) automatisch auf
        Kleinschreibung &ndash; „LaengeMM“ kommt als „laengemm“ zurück. <code>sqlite3.Row</code>
        erlaubt dagegen Zugriff per Position UND per Name in der im Schema definierten
        Groß-/Kleinschreibung. <code>_Zeile</code> bildet das für Postgres nach &ndash; und zwar,
        indem die Schlüssel schon beim Erstellen umbenannt werden (nicht erst bei
        <code>row["Spalte"]</code>), damit auch <code>dict(row)</code> die richtige Schreibweise
        behält.
      </p>
      <pre class="code-block">{code_zeile}</pre>
    </section>

    <section>
      <h2>Der Schreib-Lock: Barcode-Vergabe ohne Kollisionen</h2>
      <p>
        Jede Stelle, die eine neue Barcode-Nummer vergibt, tut das innerhalb desselben
        <code>threading.Lock</code> &ndash; „höchste vorhandene Nummer suchen“ und „neue Zeile mit
        dieser Nummer einfügen“ laufen dadurch als eine ununterbrechbare Einheit, auch wenn zwei
        Nutzer im selben Moment auf denselben Streamlit-Prozess zugreifen.
      </p>
      <pre class="code-block">{code_lock}</pre>
    </section>

    <section>
      <h2>Das Migrationsskript: wiederholbar statt einmalig gedacht</h2>
      <p>
        <code>migrate_sqlite_to_postgres.py</code> löscht vor jeder Tabelle deren Zieldaten, bevor
        die aktuellen Daten aus SQLite eingespielt werden &ndash; es kann dadurch gefahrlos
        mehrfach ausgeführt werden, falls sich die lokalen Daten vor dem endgültigen Umzug noch
        ändern. Nach dem Kopieren wird für jede Tabelle mit automatisch vergebenen IDs zusätzlich
        die interne Postgres-Sequenz auf den höchsten übertragenen Wert gesetzt.
      </p>
      <pre class="code-block">{code_migrate}</pre>
    </section>

    <section>
      <h2>Betriebs-Skripte im Überblick</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Datei</th><th>Zweck</th></tr></thead>
          <tbody>
            <tr><td><code>backup.sh</code> / <code>windows-setup/backup.py</code></td><td>Täglicher Backup-Job (Mac/Linux per Shell, Windows per Python, da dort kein natives cron existiert).</td></tr>
            <tr><td><code>server.sh</code> / <code>windows-setup/start_server.bat</code></td><td>Startet den Streamlit-Server im Hintergrundbetrieb, ruft vorher das Backup auf.</td></tr>
            <tr><td><code>start.command</code> / <code>windows-setup/start.bat</code></td><td>Doppelklick-Fallback: prüft, ob der Dienst schon läuft (dann nur Browser öffnen), sonst Direktstart.</td></tr>
            <tr><td><code>windows-setup/start_hidden.vbs</code></td><td>Startet den Server unsichtbar im Hintergrund für die Windows-Aufgabenplanung, ohne sichtbares Konsolenfenster.</td></tr>
          </tbody>
        </table>
      </div>
    </section>

{projekt_nav("11-go-live.html", "Go-Live", "13-fazit.html", "Fazit & Ausblick")}
  </main>
"""

write_page("12-code-vertiefung.html", "Projekt 3: Code-Vertiefung", body)
