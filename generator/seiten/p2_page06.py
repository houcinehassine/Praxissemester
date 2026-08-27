# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt2 import *

code_filter = """&#39; Universelle Filterfunktion – funktioniert für jede Tabelle
Function TabelleFiltern(SheetName As String, TableName As String, _
    SuchWerte() As String, SpaltenNummern() As Long) As Boolean

    For i = LBound(SuchWerte) To UBound(SuchWerte)
        If Trim(SuchWerte(i)) &lt;&gt; &quot;&quot; Then
            &#39; &quot;*&quot; erlaubt eine Teilsuche (enthält), nicht nur exakte Treffer
            tbl.Range.AutoFilter Field:=SpaltenNummern(i), _
                Criteria1:=&quot;*&quot; &amp; Trim(SuchWerte(i)) &amp; &quot;*&quot;
        End If
    Next i
End Function"""

body = seiten_kopf(6, "Filtern &amp; Speichern",
    "Eine universelle Filterfunktion, die für jede Tabelle wiederverwendet werden "
    "kann, sowie der Export- und Versand-Mechanismus, der Dashboard-Auswahl in "
    "fertige PDF-/Excel-Dateien und E-Mails verwandelt.") + f"""
  <main class="projekt-detail">

    <section>
      <div class="info-box">
        <strong>Quellen</strong>
        0105filternentfiltern.pdf &middot; 0106Speichern.pdf &middot; beide vom 4. Mai 2026
      </div>
    </section>

    <section>
      <h2>Universelle Filter-Funktion</h2>
      <p>
        Statt für jedes Blatt eine eigene Filterfunktion zu schreiben, nimmt
        eine einzige Funktion Blattname, Tabellenname sowie zwei Listen
        entgegen: die Suchbegriffe und die dazugehörigen Spaltennummern. So
        lässt sie sich für „Artikeln Liste“, „Reste“ und „Verlauf“
        gleichermaßen wiederverwenden.
      </p>
      <pre class="code-block">{code_filter}</pre>
      <p style="margin-top:0.75rem">
        Eine zweite Funktion („DynamischFiltern“) liest die Suchfelder direkt
        aus benannten Zellen im Blatt aus – der Button auf dem Blatt „Artikel
        Liste“ ruft dazu nur eine Zeile Code auf:
      </p>
      <pre class="code-block">Call DynamischFiltern(&quot;Artikel Liste&quot;, &quot;Artikel_Liste&quot;, _
    &quot;E2,E4,E6,E8,E10,E12&quot;, &quot;2,4,5,6,8,9&quot;)</pre>
      <p style="margin-top:0.75rem">
        Das Entfiltern läuft spiegelbildlich: AutoFilter zurücksetzen und die
        Eingabefelder wieder leeren.
      </p>
    </section>

    <section>
      <h2>Speichern &amp; Export</h2>
      <p class="section-intro">Ein Button auf dem Dashboard löst den kompletten Export-Vorgang aus.</p>
      <div class="stepper">
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">1</span>
            <span class="schritt-titel">Zielordner &amp; Format prüfen</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Ordnerpfad aus dem Dashboard lesen, prüfen ob mindestens ein Format (Excel und/oder PDF) angehakt ist.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">2</span>
            <span class="schritt-titel">Ausgewählte Blätter sammeln</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Die drei Checkboxen (Artikel/Reste/Verlauf) auf dem Dashboard auslesen und in eine Liste der zu exportierenden Blattnamen umwandeln.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">3</span>
            <span class="schritt-titel">PDF-Layout anwenden</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Papierformat (A3/A4) und Ausrichtung (Hoch/Quer) aus den Dashboard-Optionen übernehmen, Inhalt zwingend auf eine Seitenbreite anpassen.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">4</span>
            <span class="schritt-titel">Export-Schleife ausführen</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Für jedes ausgewählte Blatt: PDF exportieren (falls gewünscht) und/oder als eigene Excel-Datei speichern – Dateiname automatisch mit Zeitstempel versehen.</p></div>
        </div>
      </div>
    </section>

    <section>
      <h2>E-Mail-Versand mit Wahl des Mailprogramms</h2>
      <p class="section-intro">Der Export lässt sich direkt im Anschluss automatisch per E-Mail verschicken – inklusive Anhängen.</p>
      <p>
        Statt sich auf ein einziges Mailprogramm festzulegen, prüft das
        Modul, welcher Client gewünscht ist, und initialisiert das passende
        Objekt:
      </p>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>Outlook</h4><p>Standardfall: Outlook wird per COM-Automatisierung direkt angesteuert (<code>CreateObject("Outlook.Application")</code>).</p></div>
        <div class="mini-karte"><h4>Gmail</h4><p>Als Workaround wird das Gmail-Fenster im Browser aktiviert – im Code selbst als „Hack-Vorschlag“ kommentiert, da VBA Web-Gmail nicht direkt steuern kann.</p></div>
        <div class="mini-karte"><h4>Apple Mail</h4><p>Auf Mac-Rechnern wird stattdessen <code>Mail.Application</code> angesprochen.</p></div>
      </div>
      <p style="margin-top:0.75rem"><strong>Betreff und Text werden automatisch erzeugt</strong> – kein manuelles Tippen nötig:</p>
      <ul class="ergebnis-liste">
        <li><span><strong>Betreff</strong>setzt sich aus den exportierten Blattnamen und dem heutigen Datum zusammen, z. B. „Lager_System - Stand: 05.05.2026“.</span></li>
        <li><span><strong>Text</strong>enthält eine Liste der exportierten Blätter, Erstellungsdatum/-uhrzeit und den Windows-Benutzernamen als Unterschrift.</span></li>
        <li><span><strong>Anhänge</strong>werden automatisch anhand des generierten Dateinamens im Zielordner gesucht und angehängt (PDF und/oder Excel).</span></li>
        <li><span><strong>Entwurf oder Direktversand</strong>eine Checkbox „Check_Direktversand“ entscheidet, ob die Mail nur zur Kontrolle geöffnet (<code>.Display</code>) oder sofort verschickt wird (<code>.Send</code>).</span></li>
      </ul>
    </section>

    <section>
      <h2>Erste funktionierende Version im Einsatz</h2>
      <p class="section-intro">Testdaten vom 23.04.2026 – das Verlaufsblatt beim tatsächlichen Ein- und Ausbuchen.</p>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Screenshot &middot; Verlauf mit echten Testbuchungen</span>
          <img src="img/verlauf-testdaten.jpg" alt="Verlauf-Tabelle mit echten Testbuchungen: Vierkantrohr, Blech, Rolle, Stab und weitere Artikel mit Soll-/Ist-Bestand und Preisen" />
          <p class="bildtext">Reale erste Testläufe: Vierkantrohr 80×80×3 (Baustahl), Blech 500 (Aluminium), Rolle (Kunststoff), Stab D20 (Vergütungsstahl) – jede Buchung mit Zeitstempel, Menge, Soll-/Ist-Bestand und automatisch berechnetem V-Preis.</p>
        </div>
      </div>
    </section>

{projekt_nav("05-artikelgruppe-barcode.html", "Artikelgruppe &amp; Barcode", "07-versionsgeschichte.html", "Versionsgeschichte")}
  </main>
"""

write_page("06-filtern-speichern.html", "Projekt 2: Filtern & Speichern", body)
