# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt2 import *

code_open = """&#39; Wird automatisch beim Öffnen der Datei ausgeführt
Private Sub Workbook_Open()
    Call SheetsEntsperren

    &#39; Nur die wirklich nötigen Zellen editierbar lassen
    Call ZellenOeffnen(Sheets(&quot;Dashboard&quot;), &quot;C23&quot;, &quot;C28&quot;, &quot;G13&quot;, &quot;L13&quot;)
    Call ZellenOeffnen(Sheets(&quot;Artikel Liste&quot;), &quot;A:Q&quot;)
    Call ZellenOeffnen(Sheets(&quot;Reste&quot;), &quot;A:Q&quot;)
    Call ZellenOeffnen(Sheets(&quot;Verlauf&quot;), &quot;A:Q&quot;)
    Call ZellenOeffnen(Sheets(&quot;Artikel Gruppe&quot;), &quot;A:G&quot;)

    Call SheetsSperren          &#39; alle Blätter wieder schützen
    Call APP_ModusAktivieren    &#39; Tablet-Modus aktivieren
End Sub"""

body = seiten_kopf(8, "Aktueller Stand (14.08.2026)",
    "Der bisher reifste Stand: fünf Blätter, vier eigene Formulare, "
    "automatischer Zellschutz beim Öffnen und ein Umschalter zwischen "
    "Tablet- und Entwickler-Modus.") + f"""
  <main class="projekt-detail">

    <section>
      <div class="info-box">
        <strong>Quelle</strong>
        05Lagerbestand_Excel_Datei_Stand_14.08.26.pdf
      </div>
      <div class="kennzahlen-grid" style="background:var(--karte);padding:1rem;border-radius:var(--radius);border:1px solid var(--rand);margin-top:1rem">
        <div class="kennzahl" style="background:var(--hintergrund);border-color:var(--rand)"><strong style="color:var(--akzent)">5</strong><span style="color:var(--text-hell)">Blätter (inkl. Reste)</span></div>
        <div class="kennzahl" style="background:var(--hintergrund);border-color:var(--rand)"><strong style="color:var(--akzent)">4</strong><span style="color:var(--text-hell)">Formulare (UserForms)</span></div>
        <div class="kennzahl" style="background:var(--hintergrund);border-color:var(--rand)"><strong style="color:var(--akzent)">2</strong><span style="color:var(--text-hell)">Ansichtsmodi</span></div>
      </div>
    </section>

    <section>
      <h2>Tablet-Modus</h2>
      <p class="section-intro">Für den Einsatz direkt in der Werkstatt: reduzierte Oberfläche ohne Excel-Chrome.</p>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Screenshot &middot; Tablet-Modus</span>
          <img src="img/tablet-modus.jpg" alt="Tablet-Modus des Lager Systems V3.3 mit seitlicher Icon-Navigation, Filtern/Entfiltern und farbigen Buttons für Artikel und Reste" />
          <p class="bildtext">Ribbon, Formelleiste und Blattreiter sind ausgeblendet, stattdessen eine schmale Icon-Leiste links zur Navigation zwischen den Blättern – wirkt wie eine eigenständige App statt einer Excel-Tabelle.</p>
        </div>
      </div>
    </section>

    <section>
      <h2>Entwickler-Modus</h2>
      <p class="section-intro">Für die Bearbeitung: volle Excel-Oberfläche inklusive aller Blattreiter.</p>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Screenshot &middot; Entwickler-Modus</span>
          <img src="img/entwickler-modus.jpg" alt="Entwickler-Modus mit vollem Excel-Ribbon und farbig markierten Blattreitern: Dashboard, Artikel Liste, Reste, Verlauf, Artikel Gruppe, Einstellung" />
          <p class="bildtext">Mit sichtbarem Ribbon und farbcodierten Blattreitern (Dashboard gelb, Artikel Liste grün, Reste weiß, Verlauf blau, Artikel Gruppe magenta, Einstellung rot) – hier zu sehen: das Blatt „Reste“ für Restlängen und Verschnitt.</p>
        </div>
      </div>
      <p style="margin-top:0.75rem">
        Ein Klick auf denselben Button schaltet zwischen beiden Modi um –
        <code>APPModus_Umschalten()</code> prüft einfach, ob die Formelleiste
        gerade sichtbar ist, und ruft je nachdem
        <code>Entwickler_ModusAktivieren</code> oder
        <code>APP_ModusAktivieren</code> auf.
      </p>
    </section>

    <section>
      <h2>Automatischer Zellschutz beim Öffnen</h2>
      <p>
        Neu im Endstand: Beim Öffnen der Datei werden zunächst gezielt nur
        die wirklich benötigten Zellen/Spalten freigegeben, danach werden
        <strong>alle</strong> Blätter gesperrt. So lässt sich nichts aus
        Versehen überschreiben – bedient wird ausschließlich über Buttons,
        Formulare und die freigegebenen Eingabefelder.
      </p>
      <pre class="code-block">{code_open}</pre>
    </section>

    <section>
      <h2>Die vier Formulare (UserForms)</h2>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>frmArtikelDetails</h4><p>Details eines neuen Artikelstücks erfassen: Ort/Regal, Type (Voll/Rest), Länge, Menge, E-Preis – mit Eingabeprüfung.</p></div>
        <div class="mini-karte"><h4>frmArtikelGruppe</h4><p>Neue Artikelgruppe anlegen: Profil, Maß, Material auswählen bzw. eingeben.</p></div>
        <div class="mini-karte"><h4>frmBarcodeEingabe</h4><p>Barcode manuell eingeben, wenn kein Scanner zur Hand ist.</p></div>
        <div class="mini-karte"><h4>frmMaterialEntnahme</h4><p>Restentnahme aus einem vorhandenen Stück, inklusive Auswahl passender Reststücke per ComboBox.</p></div>
      </div>
    </section>

    <section>
      <h2>Neu: das Blatt „Reste“</h2>
      <div class="info-box">
        Ein eigenständiges Blatt für Verschnitt und Restlängen – getrennt von
        den vollständigen Artikeln, aber mit denselben Spalten (Barcode,
        Profil, Maß, Länge, Material, Ort, Menge, Preis). Direkter Bezug zur
        Praxissemester-Aufgabe „Reste besser nutzen“: Restlängen bekommen
        damit erstmals einen eigenen, durchsuchbaren Platz im System statt
        irgendwo notiert zu werden.
      </div>
    </section>

{projekt_nav("07-versionsgeschichte.html", "Versionsgeschichte", "09-material-entnahme.html", "Material-Entnahme &amp; Reste")}
  </main>
"""

write_page("08-aktueller-stand.html", "Projekt 2: Aktueller Stand (14.08.2026)", body)
