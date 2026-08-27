# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt3 import *

body = seiten_kopf(8, "Datensicherheit: Papierkorb und Löschbestätigung",
    "Im Zuge der Vorbereitung auf den produktiven Einsatz wurde ein zentrales Risiko "
    "identifiziert: ein einzelner Klick konnte einen Artikel unwiderruflich entfernen.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>Das Risiko</h2>
      <p>
        Sowohl im VBA-Original (<code>Del_ArtikelStueck</code>) als auch in der ersten Version
        der neuen Anwendung entfernte der „Löschen“-Knopf im Bearbeiten-Dialog einen Artikel nach
        einer einzigen Ja/Nein-Abfrage sofort und endgültig. Bei einer Verwechslung beim Scannen
        wäre das ein potenzieller Datenverlust gewesen &ndash; ohne jede Möglichkeit, den Fehler
        rückgängig zu machen.
      </p>
    </section>

    <section>
      <h2>Zwei Absicherungsstufen</h2>
      <div class="stepper">
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">1</span>
            <span class="schritt-titel">Explizite Sicherheitsabfrage</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Vor jedem Löschvorgang erscheint eine explizite Sicherheitsabfrage („Ja, löschen“ / „Abbrechen“).</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">2</span>
            <span class="schritt-titel">Papierkorb statt Löschen</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Ein gelöschtes Stück landet nicht mehr sofort im Nichts, sondern in einer neuen Papierkorb-Tabelle samt Löschzeitpunkt und der ursprünglichen Quelltabelle (Artikel_Liste oder Reste).</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">3</span>
            <span class="schritt-titel">Wiederherstellen ...</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Von dort kann es mit einem Klick wiederhergestellt werden &ndash; legt es wieder in seiner ursprünglichen Tabelle an (schlägt fehlerhaft ab, falls der Barcode inzwischen erneut vergeben wurde).</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">4</span>
            <span class="schritt-titel">... oder endgültig entfernen</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Nach einer zweiten, eigenen Sicherheitsabfrage kann ein Papierkorb-Eintrag endgültig und unwiderruflich gelöscht werden.</p></div>
        </div>
      </div>
    </section>

    <section>
      <div class="info-box">
        <strong>Direkte Antwort auf eine Schwäche des Originals:</strong> Diese Funktion existierte
        im Excel-System nicht (siehe Seite 3) und wurde bewusst als eigenständige Verbesserung
        ergänzt, nicht nur portiert.
      </div>
    </section>

{projekt_nav("07-oberflaeche.html", "Oberfläche", "09-produktionsreife.html", "Produktionsreife")}
  </main>
"""

write_page("08-papierkorb.html", "Projekt 3: Papierkorb", body)
