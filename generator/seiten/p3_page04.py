# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt3 import *

body = seiten_kopf(4, "Architekturentscheidung: Weg von Excel",
    "Nach der vollständigen Analyse des Originalsystems fiel die bewusste Entscheidung, die "
    "Lösung als eigenständige Web-Anwendung neu aufzubauen &ndash; unter der ausdrücklichen "
    "Vorgabe, sie so einfach wie möglich zu halten.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>Die Entscheidung</h2>
      <p>
        Über Alternativen zur Weiternutzung von Excel wurde diskutiert. Nach
        Abwägung verschiedener Optionen fiel die bewusste Entscheidung,
        <strong>nicht</strong> bei Excel zu bleiben, sondern das System als
        eigenständige Web-Anwendung mit einer robusteren Datenbank im
        Hintergrund neu aufzubauen &ndash; unter der ausdrücklichen Vorgabe,
        die Lösung <strong>so einfach wie möglich</strong> zu halten und das
        Projekt <strong>Schritt für Schritt</strong> gemeinsam zu entwickeln.
      </p>
    </section>

    <section>
      <h2>Die Zielarchitektur: Python + Streamlit + SQLite</h2>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>Streamlit</h4><p>Erzeugt aus reinem Python-Code eine vollständige, plattformunabhängige Web-Oberfläche &ndash; kein Frontend-Framework, kein manuelles HTML/CSS/JavaScript, keine Mac/Windows-Verzweigungen mehr nötig.</p></div>
        <div class="mini-karte"><h4>SQLite</h4><p>Speichert die gesamte Datenbank in einer einzigen Datei, läuft aber &ndash; anders als Excel &ndash; mehrbenutzerfähig im WAL-Modus.</p></div>
        <div class="mini-karte"><h4>Lokaler Webserver</h4><p>Von jedem Gerät im selben Netzwerk per Browser erreichbar, ohne dass irgendetwas installiert werden muss.</p></div>
        <div class="mini-karte"><h4>Einfachheit als Leitprinzip</h4><p>Bewusst gegen zusätzliche Komplexität (eigenes Frontend, Login-System, externe Services) entschieden, solange sie nicht nötig war.</p></div>
      </div>
    </section>

    <section>
      <h2>Drei klar getrennte Schichten</h2>
      <p class="section-intro">Diese Aufteilung hat sich durch das gesamte Projekt hindurch bewährt.</p>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Datei</th><th>Verantwortung</th></tr></thead>
          <tbody>
            <tr><td><code>app.py</code></td><td>Streamlit-Oberfläche: alle Seiten, Formulare, Dialoge und die Navigation. Ersetzt die Excel-Blätter + UserForms.</td></tr>
            <tr><td><code>logic.py</code></td><td>Fachliche Geschäftslogik: Barcode-Vergabe, Materialentnahme-Logik, Suche, Export. Portierung der VBA-Module E/F/G/H/B/C.</td></tr>
            <tr><td><code>db.py</code></td><td>Datenzugriffsschicht: kapselt sämtliche SQL-Zugriffe hinter generischen Funktionen, verbindet wahlweise mit SQLite oder Postgres.</td></tr>
            <tr><td><code>schema.sql</code> / <code>schema_postgres.sql</code></td><td>Das Datenbankschema, 1:1 an die ursprünglichen Excel-Tabellen angelehnt.</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Klarer Schnitt als im VBA-System:</strong> Im Original waren UserForm-Code,
        Fachlogik und Tabellenzugriff oft im selben Modul vermischt. Hier ruft <code>app.py</code>
        ausschließlich Funktionen aus <code>logic.py</code> auf, diese wiederum liest/schreibt
        über <code>db.py</code> &ndash; nie direktes SQL an der Datenbank vorbei. So bleibt jede
        Schicht unabhängig testbar und austauschbar (z. B. SQLite lokal, Postgres in der Cloud),
        ohne dass die anderen beiden Schichten etwas davon merken.
      </div>
    </section>

{projekt_nav("03-schwachstellen.html", "Schwachstellen", "05-vba-python-portierung.html", "VBA → Python")}
  </main>
"""

write_page("04-architektur.html", "Projekt 3: Architektur", body)
