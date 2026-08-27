# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt2 import *

v22_module = """<table class="tabelle"><thead><tr><th>Modul</th><th>Aufgabe</th></tr></thead><tbody>
<tr><td>APP_Modus</td><td>Ribbon/Gitterlinien für den App-artigen Look ein-/ausblenden</td></tr>
<tr><td>Auf_Entsperen</td><td>Blätter zum Bearbeiten entsperren</td></tr>
<tr><td>Einbuchen / Ausbuchen</td><td>Kernlogik für Zu- und Abgänge</td></tr>
<tr><td>Markieren</td><td>Zeilen farblich hervorheben</td></tr>
<tr><td>Filter</td><td>Tabellen nach Kriterien filtern</td></tr>
<tr><td>Hinzufügen_löschen</td><td>Neue Artikel anlegen bzw. entfernen</td></tr>
<tr><td>Exportieren_Email</td><td>PDF/Excel-Export und Mailversand</td></tr>
<tr><td>Navigation</td><td>Zwischen den Blättern springen</td></tr>
</tbody></table>"""

module_karten = [
    ("A", "Sheets/Excel bearbeiten", "Sicherheit (sperren/entsperren), Navigation zwischen Blättern, Tablet-/Entwickler-Modus umschalten, Ansichtsbereich einstellen."),
    ("B", "Exportieren", "Datentypen für den Export, Hilfsfunktionen und die eigentliche Export-Logik nach PDF/Excel."),
    ("C", "E-Mail senden", "Datentypen, Hilfsfunktionen und der eigentliche Versand von Exporten als E-Mail-Anhang."),
    ("D", "Universelle Funktionen", "Barcode-Erzeugung, Tabellen durchsuchen, Filtern/Entfiltern – von allen anderen Modulen wiederverwendet."),
    ("E", "Einstellungen", "Profil- und Material-Nachschlagetabellen zentral verwalten."),
    ("F", "Artikelgruppe", "Datentyp, Hilfsfunktionen sowie Erstellen sind Auslesen von Artikelgruppen."),
    ("G", "Artikelstück", "Datentyp, Hilfsfunktionen, Hinzufügen/Löschen/Bearbeiten einzelner Stücke, Buttons und die Material-Entnahme-Logik."),
    ("H", "Suchen (neu im Endstand)", "Durchsucht Artikel- und Restebestand gleichzeitig nach Barcode oder Bezeichnung und listet Treffer inkl. Summen im Dashboard – die Konfliktprüfung bei widersprüchlichen Eingaben ist noch als Platzhalter angelegt."),
]

module_html = ""
for letter, titel, text in module_karten:
    module_html += f'<div class="mini-karte"><h4>{letter}-Module &middot; {titel}</h4><p>{text}</p></div>\n'

body = seiten_kopf(7, "Versionsgeschichte: von V2.2 zu V3.3",
    "Aus einer einzigen, langen Codedatei wurde eine saubere Modul-Architektur "
    "mit acht klar abgegrenzten Verantwortungsbereichen.") + f"""
  <main class="projekt-detail">

    <section>
      <div class="info-box">
        <strong>Quellen</strong>
        02LagerSystem_Version_2.2.pdf (5. Mai 2026) &middot; 0300Lager_System_V3.3_.pdf und Modul-Dateien 0302–0308 (ab 5./7. Mai 2026)
      </div>
    </section>

    <section>
      <h2>Version 2.2 – alles in einer Datei</h2>
      <p>
        Die erste vollständige Version bündelt Dashboard, Artikeln Liste,
        Verlauf und Einstellungen samt aller Makros in einer Arbeitsmappe.
        Beim Öffnen wird automatisch das Dashboard aktiviert und die
        Excel-Oberfläche (Spaltenköpfe, Formelleiste, Ribbon, Gitterlinien)
        ausgeblendet – beim Schließen wieder eingeblendet, damit andere
        Excel-Dateien nicht betroffen sind.
      </p>
      <div class="tabelle-wrapper">{v22_module}</div>
    </section>

    <section>
      <h2>Version 3.3 – Modul-Übersicht A–G</h2>
      <p class="section-intro">
        Statt weniger, großer Module folgt V3.3 einer klaren Trennung nach
        Verantwortlichkeit – jede Buchstabengruppe kümmert sich um genau
        einen Bereich.
      </p>
      <div class="karten-grid-4">
        {module_html}
      </div>
    </section>

    <section>
      <h2>Was sich strukturell ändert</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>Von 9 auf über 20 Module</strong>jede Verantwortlichkeit bekommt ihr eigenes, klar benanntes Modul statt eines Sammelmoduls.</span></li>
        <li><span><strong>Wiederverwendbare Universalfunktionen (D)</strong>Barcode-Suche und Filterlogik werden zentral einmal geschrieben und von A/F/G aus aufgerufen.</span></li>
        <li><span><strong>Eigene Datentyp-Module</strong>„TabelleDaten“ und „ArtikelGruppe“ bündeln zusammengehörige Felder statt einzelner loser Variablen.</span></li>
        <li><span><strong>Neues Modul H</strong>im Endstand kommt eine eigenständige Suchfunktion nach Barcode oder Bezeichnung dazu, inklusive Konfliktprüfung.</span></li>
      </ul>
    </section>

{projekt_nav("06-filtern-speichern.html", "Filtern &amp; Speichern", "08-aktueller-stand.html", "Aktueller Stand")}
  </main>
"""

write_page("07-versionsgeschichte.html", "Projekt 2: Versionsgeschichte", body)
