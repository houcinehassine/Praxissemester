# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt2 import *

liste_tabelle = """<table class="tabelle"><thead><tr><th>#</th><th>Spalte</th></tr></thead><tbody>
<tr><td>1</td><td>EAN/Barcode</td></tr>
<tr><td>2</td><td>Bezeichnung</td></tr>
<tr><td>3</td><td>Artikelform</td></tr>
<tr><td>4</td><td>Material-Gruppe</td></tr>
<tr><td>5</td><td>Artikelmaterial</td></tr>
<tr><td>6</td><td>Einheit</td></tr>
<tr><td>7</td><td>Soll (Bestand)</td></tr>
<tr><td>8</td><td>Ist (Bestand)</td></tr>
<tr><td>9</td><td>E-Preis (Einkaufspreis)</td></tr>
<tr><td>10</td><td>V-Preis (Verkaufspreis)</td></tr>
</tbody></table>"""

verlauf_tabelle = """<table class="tabelle"><thead><tr><th>#</th><th>Spalte</th></tr></thead><tbody>
<tr><td>1</td><td>Datum + Uhrzeit</td></tr>
<tr><td>2</td><td>EAN/Barcode</td></tr>
<tr><td>3</td><td>Bezeichnung</td></tr>
<tr><td>4</td><td>Artikelform</td></tr>
<tr><td>5</td><td>Material-Gruppe</td></tr>
<tr><td>6</td><td>Artikelmaterial</td></tr>
<tr><td>7</td><td>Einheit</td></tr>
<tr><td>8</td><td>Soll (Bestand)</td></tr>
<tr><td>9</td><td>Ist (Bestand)</td></tr>
<tr><td>10</td><td>E-Preis (Einkaufspreis)</td></tr>
<tr><td>11</td><td>V-Preis (Verkaufspreis)</td></tr>
</tbody></table>"""

body = seiten_kopf(2, "Ausgangslage &amp; Zielbild",
    "Der Startpunkt des Projekts: eine Beschreibung, wie sich die fertige Excel-Datei "
    "am Ende bedienen lassen soll – komplett über Buttons und Barcode-Scan, ohne "
    "direkte Zelleingabe.") + f"""
  <main class="projekt-detail">

    <section>
      <div class="info-box">
        <strong>Quelle</strong>
        01Grundidee.pdf &middot; Beginn 22. April 2026
      </div>
    </section>

    <section>
      <h2>Ausgangslage</h2>
      <div class="zitat-box">
        „Ich arbeite aktuell an einer Excel-Datei, die sollte nur mit Buttons
        bearbeitbar sein. Mein aktueller Stand fehlt noch die VBA-Codes für
        jeden Befehl – damit brauche ich Hilfe. Anbei ist eine Beschreibung
        von dem, was ich am Ende genau erreichen will. Lass uns zusammen
        arbeiten, um alles zu kriegen.“
        <span class="quelle">Originaltext, 22.04.2026</span>
      </div>
    </section>

    <section>
      <h2>Das Scanfeld – gemeinsames Bauteil beider Seiten</h2>
      <p>
        Sowohl „Artikeln Liste“ als auch „Verlauf“ bekommen dieselbe Bedienlogik:
        eine Zelle, in die gescannt oder eingegeben wird, aktiviert per Taste
        <strong>F12</strong>.
      </p>
      <ul class="ergebnis-liste">
        <li><span><strong>Aktiv (nach F12)</strong>Zelle färbt sich grün, Hinweistext „Code Einscannen/Eingeben“.</span></li>
        <li><span><strong>Inaktiv</strong>Zelle ist weißgrau, Hinweistext „Vorher F12 drücken“.</span></li>
        <li><span><strong>3 Optionen daneben</strong>einbuchen, ausbuchen, nur markieren – als Radio-Auswahl.</span></li>
        <li><span><strong>Speichern-Button</strong>aktuelle Liste unter einem Namen (Standard: „Bestand_&lt;heutiges Datum&gt;“) in einem festen Zielordner ablegen.</span></li>
        <li><span><strong>E-Mail-Versand</strong>Liste als Anhang verschicken, wahlweise als Excel-Tabelle und/oder als PDF-Datei, Zieladresse in den Einstellungen hinterlegt.</span></li>
      </ul>
    </section>

    <section>
      <h2>Seite „Artikeln Liste“</h2>
      <p class="section-intro">Tabelle „Liste“ – ein Artikel pro Zeile.</p>
      <div class="tabelle-wrapper">{liste_tabelle}</div>
      <p style="margin-top:0.75rem"><strong>Barcode-Aufbau:</strong> zwei Buchstaben für das Material
      (z. B. Baustahl = <code>BS</code>, Edelstahl = <code>ES</code>, Kunststoff = <code>KU</code>)
      gefolgt von einer vierstelligen, automatisch hochzählenden Nummer, z. B. <code>BS0044</code>.</p>
      <div class="karten-grid-4" style="margin-top:1rem">
        <div class="mini-karte"><h4>Beim Einbuchen</h4><p>Bezeichnung, Form, Material-Gruppe, Material, Einheit, Soll-Bestand und E-Preis abfragen; V-Preis wird berechnet (E-Preis + 20 % + 19 % USt.).</p></div>
        <div class="mini-karte"><h4>Beim Ausbuchen</h4><p>Gescannten Artikel suchen, Artikeldaten anzeigen, nach Bestätigung ausbuchen.</p></div>
        <div class="mini-karte"><h4>Beim Markieren</h4><p>Gescannten Artikel suchen und farblich hervorheben, Färbung nach 5 Minuten automatisch wieder entfernen.</p></div>
      </div>
    </section>

    <section>
      <h2>Seite „Verlauf“</h2>
      <p class="section-intro">Tabelle „Verlauf“ – jede Bewegung wird protokolliert.</p>
      <div class="tabelle-wrapper">{verlauf_tabelle}</div>
      <div class="karten-grid-4" style="margin-top:1rem">
        <div class="mini-karte"><h4>Beim Einbuchen</h4><p>Menge wird erfragt, neue Zeile im Verlauf angelegt, Ist-Bestand in der Artikelliste um diese Menge erhöht.</p></div>
        <div class="mini-karte"><h4>Beim Ausbuchen</h4><p>Menge wird erfragt und als negativer Wert verbucht, Ist-Bestand entsprechend verringert.</p></div>
        <div class="mini-karte"><h4>Beim Markieren</h4><p>Zeilen des Artikels im Verlauf farblich hervorheben, nach 5 Minuten automatisch zurücksetzen.</p></div>
      </div>
    </section>

{projekt_nav("index.html", "Überblick", "03-design.html", "Design der Oberfläche")}
  </main>
"""

write_page("02-ausgangslage.html", "Projekt 2: Ausgangslage & Zielbild", body)
