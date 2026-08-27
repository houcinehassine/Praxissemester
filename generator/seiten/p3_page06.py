# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt3 import *

body = seiten_kopf(6, "Datenmodell &amp; Import",
    "Das Datenbankschema wurde bewusst nah an der Struktur der ursprünglichen Excel-Tabellen "
    "gehalten &ndash; und die realen Lagerbestände wurden erst nach einer eigenen Kontrollrunde "
    "übernommen.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>Das Datenbankschema</h2>
      <p>
        <strong>Lager</strong> (Lagerorte), <strong>Typ</strong>, <strong>Einheit</strong>,
        <strong>Profil_Abk</strong> und <strong>Material_Gruppe</strong> als Stammdaten,
        <strong>Artikel_Gruppe</strong> als Artikel-Stammsatz (erzeugt den Haupt-Barcode), sowie
        die drei identisch aufgebauten Tabellen <strong>Artikel_Liste</strong> (volle Stücke),
        <strong>Reste</strong> (kurze Stücke) und <strong>Verlauf</strong> (unveränderliches
        Buchungsprotokoll) &ndash; plus eine neu hinzugekommene <strong>Papierkorb</strong>-Tabelle
        (siehe Seite 8) und eine <strong>Konfiguration</strong>-Tabelle für einstellbare
        Schwellenwerte wie die Schrott-Grenze.
      </p>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Zwei Schema-Dateien, ein Inhalt:</strong> <code>schema.sql</code> (SQLite) und
        <code>schema_postgres.sql</code> (Postgres/Cloud) sind inhaltlich identisch &ndash; gleiche
        Tabellen, gleiche Spalten, gleiche Reihenfolge &ndash; und unterscheiden sich nur in
        Postgres-spezifischer Syntax (<code>SERIAL</code> statt <code>AUTOINCREMENT</code>, keine
        <code>PRAGMA</code>-Zeilen). <code>db.py</code> wählt beim Start automatisch die passende
        Datei, abhängig davon, ob eine <code>DATABASE_URL</code> konfiguriert ist.
      </div>
    </section>

    <section>
      <h2>Das Barcode-Schema &ndash; unverändert übernommen</h2>
      <p>
        Das Barcode-Schema unterscheidet zwischen dem <strong>Haupt-Barcode</strong> einer
        Artikelgruppe (z. B. „FLS370001“, zusammengesetzt aus Profil- und Material-Kürzel plus
        laufender Nummer) und dem <strong>Stück-Barcode</strong> eines einzelnen physischen
        Stücks (z. B. „FLS370001-2“). Damit lässt sich sowohl ein gescannter Gruppen-Code als
        auch ein gescannter Stück-Code eindeutig zuordnen &ndash; genau wie im VBA-Original.
      </p>
    </section>

    <section>
      <h2>Digitalisierung der Bestandsdaten</h2>
      <p class="section-intro">Vier Fotos handbeschriebener Listen &ndash; und der bewusst vorsichtige Weg von dort in die Produktivdatenbank.</p>
      <div class="stepper">
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">1</span>
            <span class="schritt-titel">Fotos handschriftlicher Listen</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Die realen Lagerbestände lagen zunächst nur als vier Fotos handbeschriebener Listen vor.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">2</span>
            <span class="schritt-titel">Kontroll-Tabelle statt direkter Übernahme</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Um Fehler bei der Übertragung zu vermeiden, wurde keine direkte Übernahme in die Produktivdatenbank vorgenommen. Stattdessen entstand eine Kontroll-Tabelle „Bestandsaufnahme_Kontrolle.xlsx“ mit allen erkannten Werten samt unsicherer/unleserlicher Stellen.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">3</span>
            <span class="schritt-titel">Bestätigung durch den Auftraggeber</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Diese Kontroll-Tabelle wurde vollständig durchgesehen und korrigiert &ndash; inklusive expliziter Kennzeichnung unbekannter Materialangaben mit „---“.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">4</span>
            <span class="schritt-titel">Import per Skript</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Erst auf Basis der final bestätigten Tabelle wurden die Daten per <code>import_bestand.py</code> in die echte Datenbank übernommen.</p></div>
        </div>
      </div>
      <div class="kennzahlen-grid" style="margin-top:1rem">
        <div class="kennzahl"><strong>86</strong><span>Artikel-Datensätze importiert</span></div>
        <div class="kennzahl"><strong>50</strong><span>Artikelgruppen</span></div>
        <div class="kennzahl"><strong>4</strong><span>Fotos als Ausgangsmaterial</span></div>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        Diese 86 Datensätze bildeten von diesem Zeitpunkt an durchgehend die reale
        Produktivgrundlage, gegen die jede weitere Änderung getestet wurde.
      </div>
    </section>

{projekt_nav("05-vba-python-portierung.html", "VBA → Python", "07-oberflaeche.html", "Oberfläche")}
  </main>
"""

write_page("06-datenmodell.html", "Projekt 3: Datenmodell & Import", body)
