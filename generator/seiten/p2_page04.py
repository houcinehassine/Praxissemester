# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt2 import *

code_ausbuchen = """&#39; Ausschnitt aus dem Ausbuchen-Makro
&#39; 6. Artikelliste aktualisieren
Ist_Bestand = Ist_Bestand - Menge

&#39; Vergleich Ist-Bestand mit Soll-Bestand
If Ist_Bestand &lt; 1.25 * Soll_Bestand Then
    Zelle.Interior.Color = RGB(204, 153, 0)   &#39; Dunkles Gelb
ElseIf Ist_Bestand &lt; 1.5 * Soll_Bestand Then
    Zelle.Interior.Color = RGB(255, 230, 100) &#39; Helles Gelb
Else
    Zelle.Interior.ColorIndex = xlNone         &#39; Keine Färbung
End If"""

body = seiten_kopf(4, "Kernfunktionen: Einbuchen, Ausbuchen, Markieren",
    "Die drei zentralen Makros, auf denen das ganze System aufbaut – inklusive "
    "automatischer Farblogik für den Lagerbestand und einem cleveren "
    "Auto-Reset für Markierungen.") + f"""
  <main class="projekt-detail">

    <section>
      <div class="info-box">
        <strong>Quelle</strong>
        0101Funktionen_Algoritmus.pdf &middot; Beginn 24. April 2026
      </div>
    </section>

    <section>
      <h2>&#9662; Ausbuchen</h2>
      <p class="section-intro">Nimmt einen gescannten Barcode entgegen und bucht die gewünschte Menge aus.</p>
      <div class="stepper">
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">1</span>
            <span class="schritt-titel">Artikel suchen</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Barcode in der Spalte EAN/Barcode der Tabelle „Artikeln Liste“ suchen. Kein Treffer → Fehlermeldung.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">2</span>
            <span class="schritt-titel">Artikeldaten einlesen &amp; V-Preis berechnen</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Bezeichnung, Form, Material, Einheit, Soll-/Ist-Bestand und E-Preis auslesen. V-Preis = E-Preis × 1,2 × 1,19.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">3</span>
            <span class="schritt-titel">Details anzeigen &amp; bestätigen</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Alle Daten in einer MsgBox zeigen, Rückfrage „Möchten Sie diesen Artikel ausbuchen?“ – bei „Nein“ Abbruch.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">4</span>
            <span class="schritt-titel">Menge abfragen &amp; Bestand prüfen</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>InputBox mit Vorschlag „1“, muss eine Zahl &gt; 0 sein. Reicht der Ist-Bestand nicht aus → Fehlermeldung und Abbruch.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">5</span>
            <span class="schritt-titel">Bestand aktualisieren &amp; einfärben</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Ist-Bestand verringern und je nach Abstand zum Soll-Bestand automatisch gelb einfärben (siehe Farblogik unten).</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">6</span>
            <span class="schritt-titel">Verlauf protokollieren</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Neue Zeile in „Verlauf“ mit Zeitstempel, Barcode, allen Stammdaten und der Menge als negativem Wert (Konvention: Ausbuchung = negativ).</p></div>
        </div>
      </div>
      <p style="margin-top:0.75rem"><strong>Einbuchen läuft nach demselben Schema</strong> – nur wird die Menge addiert statt subtrahiert und im Verlauf positiv eingetragen.</p>
    </section>

    <section>
      <h2>Farblogik des Bestands</h2>
      <p class="section-intro">Nach jeder Ein- oder Ausbuchung wird die Ist-Bestand-Zelle automatisch bewertet.</p>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>Ist &lt; 125 % Soll</h4><p>Zelle wird dunkles Gelb eingefärbt – Bestand wird knapp.</p></div>
        <div class="mini-karte"><h4>125 %–150 % Soll</h4><p>Zelle wird helleres Gelb eingefärbt – Vorwarnstufe.</p></div>
        <div class="mini-karte"><h4>&gt; 150 % Soll</h4><p>Keine Färbung – Bestand ist komfortabel.</p></div>
      </div>
      <pre class="code-block">{code_ausbuchen}</pre>
    </section>

    <section>
      <h2>&#9662; markieren</h2>
      <p class="section-intro">Hebt alle Zeilen eines gescannten Artikels farblich hervor – praktisch zum schnellen Wiederfinden.</p>
      <ul class="ergebnis-liste">
        <li><span><strong>Aktives Blatt erkennen</strong>arbeitet automatisch auf dem gerade geöffneten Sheet (Verlauf oder Artikeln Liste).</span></li>
        <li><span><strong>Alle Treffer sammeln</strong>durchläuft die komplette Barcode-Spalte und sammelt alle passenden Zeilennummern.</span></li>
        <li><span><strong>Hellgrün einfärben</strong>alle gefundenen Zeilen werden mit RGB(200, 255, 200) markiert.</span></li>
        <li><span><strong>Auto-Reset anbieten</strong>Rückfrage, ob die Markierung nach 30 Sekunden automatisch verschwinden soll.</span></li>
      </ul>
    </section>

    <section>
      <h2>Zusammenspiel der drei Makros</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Schritt</th><th>Was passiert</th></tr></thead>
          <tbody>
            <tr><td>Markieren()</td><td>Zeilen grün einfärben</td></tr>
            <tr><td>→ Ja, Auto-Reset</td><td>Timer läuft 30 s → EntferneMarkierung() setzt Farbe automatisch zurück</td></tr>
            <tr><td>→ Nein, kein Auto-Reset</td><td>Markierung bleibt, bis der Button „Färben entfernen“ (FaerbenEntfernen()) gedrückt wird</td></tr>
            <tr><td>FaerbenEntfernen()</td><td>Entfernt alle Färbungen sofort und bricht einen laufenden Timer ab</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">
        Praktischer Kniff: Für den Auto-Reset speichert das Makro Sheet-Name
        und Zeilennummern als benannte Bereiche in der Arbeitsmappe – so
        „merkt“ sich der Timer auch nach 30 Sekunden noch, welche Zeilen
        zurückgesetzt werden müssen.
      </p>
    </section>

{projekt_nav("03-design.html", "Design der Oberfläche", "05-artikelgruppe-barcode.html", "Artikelgruppe &amp; Barcode")}
  </main>
"""

write_page("04-kernfunktionen.html", "Projekt 2: Kernfunktionen", body)
