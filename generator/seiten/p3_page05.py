# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt3 import *

code_entnahme = """def process_material_entnahme(
    source_table: str,
    urspungs_barcode2: str,
    genutzte_laenge: float,
    ist_schrott: bool,
) -&gt; str:
    &quot;&quot;&quot;Entspricht ProzessMaterialEntnahme: bucht eine Entnahme, reduziert/löscht
    das Ursprungsstück, legt bei Bedarf ein Reststück an.&quot;&quot;&quot;
    with _SCHREIB_LOCK:
        orig = db.fetch_one(f&quot;SELECT * FROM {source_table} WHERE Barcode2 = ?&quot;, (urspungs_barcode2,))
        initiale_laenge = orig[&quot;LaengeMM&quot;] or 0
        restlaenge = berechne_restlaenge(initiale_laenge, genutzte_laenge)

        # 1. Verlauf-Eintrag VOR dem Reduzieren (negative Länge = Verbrauch)
        _schreibe_verlauf(orig[&quot;Barcode&quot;], orig[&quot;Barcode2&quot;], ..., -genutzte_laenge, ..., &quot;Verbrauch&quot;, 1, ...)

        # 2. Ursprungsstück reduzieren oder löschen
        if (orig[&quot;MengeStueck&quot;] or 1) &gt; 1:
            db.execute(f&quot;UPDATE {source_table} SET MengeStueck = MengeStueck - 1 WHERE Barcode2 = ?&quot;, (urspungs_barcode2,))
        else:
            db.execute(f&quot;DELETE FROM {source_table} WHERE Barcode2 = ?&quot;, (urspungs_barcode2,))

        # 3. Reststück einbuchen, falls vorhanden und kein Schrott
        if restlaenge &gt; 0 and not ist_schrott:
            ziel_table = &quot;Reste&quot; if restlaenge &lt; schrott_grenze_mm() else &quot;Artikel_Liste&quot;
            _buche_reststueck_ein(ziel_table, orig, restlaenge)"""

body = seiten_kopf(5, "VBA-Funktion vs. Python-Funktion",
    "Wie zentrale VBA-Funktionen des Originalsystems in der neuen Anwendung wiederzufinden sind "
    "&ndash; und wie der Mehrbenutzerbetrieb, den es im Original gar nicht gab, umgesetzt wurde.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>Die Gegenüberstellung</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>VBA (Original)</th><th>Python (Neu)</th><th>Zweck</th></tr></thead>
          <tbody>
            <tr><td><code>FindeMaxBarcodeNummer</code></td><td><code>make_barcode_ag / _naechste_stueck_nummer</code></td><td>Nächste freie Barcode-Nummer ermitteln</td></tr>
            <tr><td><code>Rowsuchen / WertExistiertInTabelle</code></td><td><code>db.value_exists</code> / SQL <code>WHERE</code></td><td>Datensatz-Suche / Duplikatprüfung</td></tr>
            <tr><td><code>MakeNew_ArtikelStueck</code></td><td><code>logic.add_artikel_stueck</code></td><td>Neues Artikel-Stück einbuchen</td></tr>
            <tr><td><code>ProzessMaterialEntnahme</code></td><td><code>logic.process_material_entnahme</code></td><td>Materialentnahme mit Schrott-/Rest-Logik</td></tr>
            <tr><td><code>Del_ArtikelStueck</code></td><td><code>logic.soft_delete_artikel_stueck</code> + Papierkorb</td><td>Löschen (im Original endgültig, jetzt wiederherstellbar)</td></tr>
            <tr><td><code>edit_ArtikelStueck</code></td><td><code>logic.edit_artikel_stueck</code></td><td>Bestehendes Stück bearbeiten</td></tr>
            <tr><td><code>MakeArtikelGruppe</code></td><td><code>logic.create_artikel_gruppe</code></td><td>Neue Artikelgruppe anlegen</td></tr>
            <tr><td><code>DashboardExport / B3_Exportieren</code></td><td><code>logic.export_excel_bytes / export_pdf_bytes</code></td><td>Excel-/PDF-Export</td></tr>
            <tr><td><code>VerschickeExportPerEmail</code></td><td><code>logic.hole_email_betreff/-text</code> + mailto-Link</td><td>E-Mail-Entwurf</td></tr>
            <tr><td><code>BtnSuche_Click</code></td><td><code>logic.suche / erweiterte_suche</code></td><td>Dashboard-Suche</td></tr>
            <tr><td><code>SheetsSperren / SheetsEntsperren</code></td><td><em>entfällt</em></td><td>Zugriffsschutz &ndash; kein Blattschutz-Konzept mehr nötig</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>Die Materialentnahme-Logik &ndash; fast 1:1 übertragen</h2>
      <p>
        Die Kernlogik aus <code>G7_MaterialEntnahme_Logik</code> wurde nahezu 1:1 in
        <code>logic.process_material_entnahme()</code> übertragen: Verlauf-Eintrag vor der
        Reduktion, Reduktion/Löschung des Ursprungsstücks, anschließend bedingtes Einbuchen des
        Reststücks (mit Zusammenführung bei identischer Länge). Neu hinzugekommen ist die später
        eingeführte, über die Oberfläche einstellbare Schrott-/Rest-Schwelle &ndash; im Original
        war „1000&nbsp;mm“ fest im Code verankert.
      </p>
      <pre class="code-block">{code_entnahme}</pre>
    </section>

    <section>
      <h2>Mehrbenutzerbetrieb &ndash; existierte im Original gar nicht</h2>
      <p>
        Da mehrere Personen im selben Netzwerk gleichzeitig zugreifen sollten, wurde die
        SQLite-Datenbank im <strong>WAL-Modus</strong> (Write-Ahead-Logging) betrieben, wodurch
        sich lesende und schreibende Zugriffe nicht gegenseitig blockieren. Die Vergabe neuer
        Barcodes wurde zusätzlich durch einen anwendungsinternen <code>threading.Lock</code>
        abgesichert, damit zwei gleichzeitige Nutzer nicht denselben Barcode erzeugen können.
      </p>
      <div class="kennzahlen-grid" style="margin-top:0.75rem">
        <div class="kennzahl"><strong>100</strong><span>gleichzeitige Schreibzugriffe im Lasttest</span></div>
        <div class="kennzahl"><strong>5</strong><span>parallele simulierte Nutzer</span></div>
        <div class="kennzahl"><strong>0</strong><span>Konflikte oder doppelte Barcodes</span></div>
      </div>
      <p style="margin-top:0.75rem">
        Dieser gesamte Themenbereich existierte im Original überhaupt nicht &ndash; eine
        Excel-Datei kann von mehreren Personen nur eingeschränkt gleichzeitig bearbeitet werden.
      </p>
    </section>

    <section>
      <h2>Export &amp; Kommunikation &ndash; bewusst vereinfacht</h2>
      <p>
        Statt der plattformabhängigen Ordnerdialoge und Mail-Client-Automatisierung aus den B-
        und C-Modulen setzt die neue Anwendung auf Streamlits eingebauten Datei-Download (der
        Browser wählt den Speicherort) sowie auf einen einfachen <code>mailto</code>-Link für den
        E-Mail-Entwurf &ndash; bewusst ohne SMTP-Zugangsdaten, dafür aber garantiert auf jeder
        Plattform und mit jedem Mail-Anbieter (inklusive Gmail) gleich funktionierend.
      </p>
    </section>

{projekt_nav("04-architektur.html", "Architektur", "06-datenmodell.html", "Datenmodell & Import")}
  </main>
"""

write_page("05-vba-python-portierung.html", "Projekt 3: VBA → Python", body)
