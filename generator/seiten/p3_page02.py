# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt3 import *

body = seiten_kopf(2, "Das Original-System verstehen",
    "Bevor irgendetwas neu gebaut wurde, stand die vollständige Analyse des bestehenden "
    "„Lager System V3.3.xlsm“ – Tabellenblätter, Eingabemasken und alle 24 VBA-Module.") + f"""
  <main class="projekt-detail">

    <section>
      <div class="info-box">
        <strong>Hinweis</strong>
        Das Original-Excel/VBA-System selbst wird in <a href="../projekt-2/index.html">Projekt 2</a>
        bereits ausführlich dokumentiert. Diese Seite fasst nur die Punkte zusammen, die für die
        Entscheidung zur Neuentwicklung und für die spätere Portierung nach Python wichtig waren.
      </div>
    </section>

    <section>
      <h2>Tablet-Modus und Entwickler-Modus</h2>
      <p>
        Die Excel-Datei kannte zwei Ansichts-Modi, umschaltbar per Button
        (Modul <code>A3_Tablet_Modus</code>, Sub <code>APPModus_Umschalten</code>):
        Im <strong>Tablet-Modus</strong> (App-Modus) werden Menüband, Bearbeitungsleiste,
        Spalten-/Zeilenköpfe und die Blattregister-Reiter ausgeblendet und alle Blätter
        automatisch auf ihren jeweiligen Datenbereich gezoomt (Modul <code>A4_AnsichtBereich</code>) –
        die Excel-Datei wirkt dadurch wie eine eigenständige App. Der Entwickler-Modus blendet
        alle diese Elemente wieder ein.
      </p>
      <p style="margin-top:0.75rem">
        Bereits beim Öffnen der Datei (<code>Workbook_Open</code>) werden außerdem alle Blätter
        zunächst entsperrt, bestimmte Zellbereiche gezielt für Eingaben freigegeben (z. B. nur
        Spalten A–G auf „Artikel Gruppe“, dagegen A–Q auf „Artikel Liste“) und anschließend
        wieder komplett gesperrt (Blattschutz), damit Endnutzer nur über die vorgesehenen
        Buttons und Eingabefelder arbeiten können.
      </p>
    </section>

    <section>
      <h2>Die sechs Tabellenblätter</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Blatt</th><th>Zweck</th></tr></thead>
          <tbody>
            <tr><td>Dashboard</td><td>Zentrale Startseite: Exportbereich, Artikelsuche (Barcode/Bezeichnung), Schnellzugriff zu allen anderen Bereichen.</td></tr>
            <tr><td>Artikel Liste</td><td>Alle vollen Artikel-Stücke, mit Filter/Entfilter und Hinzufügen/Löschen/Bearbeiten.</td></tr>
            <tr><td>Reste</td><td>Identisch aufgebaut wie Artikel Liste, für Reststücke.</td></tr>
            <tr><td>Verlauf</td><td>Reines, nicht editierbares Buchungsprotokoll.</td></tr>
            <tr><td>Artikel Gruppe</td><td>Stammdaten je Artikelsorte, erzeugt den Haupt-Barcode; bewusst nur A&ndash;G für Eingaben freigegeben.</td></tr>
            <tr><td>Einstellung</td><td>Vier Nachschlage-Tabellen: Profil_Abk, Material_Gruppe, Lager, Einheit.</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>Die vier Eingabemasken (UserForms)</h2>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>frmArtikelDetails</h4><p>Erfasst/bearbeitet ein Stück: Länge, Ort/Regal, Type Voll/Rest, Menge, E-Preis. Validiert Pflichtfelder und negative Preise.</p></div>
        <div class="mini-karte"><h4>frmArtikelGruppe</h4><p>Legt eine neue Artikelgruppe an: Profil und Material je als Dropdown, dazu ein freies Textfeld „Maß“.</p></div>
        <div class="mini-karte"><h4>frmBarcodeEingabe</h4><p>Zentrale Barcode-Eingabe/-Suche, wiederverwendet von mehreren anderen Funktionen (Hinzufügen, Löschen, Bearbeiten, Materialentnahme).</p></div>
        <div class="mini-karte"><h4>frmMaterialEntnahme</h4><p>Kernstück der Entnahme-Logik: Barcode scannen, Restlänge live berechnen, bei &lt; 1000&nbsp;mm per Ja/Nein nachfragen, ob Schrott.</p></div>
      </div>
    </section>

    <section>
      <h2>Die 24 VBA-Module – nach Themenbereich A&ndash;H</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Bereich</th><th>Inhalt</th></tr></thead>
          <tbody>
            <tr><td><strong>A</strong> &middot; Grundgerüst</td><td>Sicherheit (Blattschutz mit hartkodiertem Passwort), Navigation, Tablet-/Entwickler-Modus, Zoom-Logik.</td></tr>
            <tr><td><strong>B</strong> &middot; Export</td><td>Excel-/PDF-Export mit plattformabhängigen Ordnerdialogen (Mac: AppleScript, Windows: FileDialog).</td></tr>
            <tr><td><strong>C</strong> &middot; E-Mail-Versand</td><td>Outlook per COM, Apple Mail per AppleScript &ndash; für Gmail existiert keine echte Automatisierung.</td></tr>
            <tr><td><strong>D</strong> &middot; Universelle Hilfsfunktionen</td><td>Barcode-Suche, Duplikat-Prüfung, generische Filter-Funktionen.</td></tr>
            <tr><td><strong>E</strong> &middot; Profil-/Material-Nachschlage­werke</td><td>Kürzel-Lookup für die Barcode-Bildung.</td></tr>
            <tr><td><strong>F</strong> &middot; Artikelgruppen-Verwaltung</td><td>Neue Gruppe anlegen, Barcode generieren, Duplikat-Prüfung.</td></tr>
            <tr><td><strong>G</strong> &middot; Artikel-Stück-Verwaltung</td><td>Das fachliche Herzstück: Zugang, Bearbeiten, Löschen und die Materialentnahme-Logik (<code>G7_MaterialEntnahme_Logik</code>).</td></tr>
            <tr><td><strong>H</strong> &middot; Dashboard-Suche</td><td>Enthielt noch Platzhalter-Code für eine nie fertig umgesetzte Zusatzfunktion.</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>Datenmodell der Excel-Tabellen</h2>
      <p class="section-intro">Die drei zentralen Tabellen Artikel_Liste, Reste und Verlauf teilen sich denselben 14-spaltigen Aufbau.</p>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>#</th><th>Spalte</th></tr></thead>
          <tbody>
            <tr><td>1</td><td>Datum</td></tr>
            <tr><td>2</td><td>Barcode (Haupt)</td></tr>
            <tr><td>3</td><td>Barcode2 (Stück)</td></tr>
            <tr><td>4</td><td>Bezeichnung</td></tr>
            <tr><td>5</td><td>Profil</td></tr>
            <tr><td>6</td><td>Maß</td></tr>
            <tr><td>7</td><td>Länge/mm</td></tr>
            <tr><td>8</td><td>Material-Gruppe</td></tr>
            <tr><td>9</td><td>Material</td></tr>
            <tr><td>10</td><td>Ort/Regal</td></tr>
            <tr><td>11</td><td>Type (Voll/Rest)</td></tr>
            <tr><td>12</td><td>Menge/Stück</td></tr>
            <tr><td>13</td><td>E-Preis</td></tr>
            <tr><td>14</td><td>E-Preis pro Einheit</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">
        Die Tabelle Artikel_Gruppe ist mit fünf Spalten deutlich schmaler
        (Barcode/Nummer, Bezeichnung, Profil, Maß, Material) – genau dieser
        14- bzw. 5-spaltige Aufbau wurde später praktisch unverändert ins
        neue Datenbankschema übernommen (siehe Seite 6).
      </p>
    </section>

{projekt_nav("index.html", "Überblick", "03-schwachstellen.html", "Schwachstellen")}
  </main>
"""

write_page("02-original-system.html", "Projekt 3: Das Original-System", body)
