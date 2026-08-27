# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt3 import *

body = seiten_kopf(7, "Iterative Weiterentwicklung der Oberfläche",
    "Im Anschluss an das Grundsystem folgte eine längere Phase kleinteiliger, "
    "nutzerzentrierter Verbesserungen &ndash; jede einzeln umgesetzt und im Browser "
    "getestet, bevor die nächste angegangen wurde.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>Export- und Downloadfunktionen</h2>
      <p>
        Zu jeder Tabellenansicht wurde neben dem eingebauten CSV-Download ein zusätzlicher
        PDF-Download-Button ergänzt, direkt neben dem nativen Symbol-Menü platziert. Später
        wurde diese Position bei gefilterten/gesuchten Tabellen vereinheitlicht: der PDF-Button
        steht seither immer oben neben der Ergebnis-Überschrift, nicht darunter.
      </p>
    </section>

    <section>
      <h2>Modale Dialoge statt Seitenwechsel</h2>
      <p>
        Die häufigsten Aktionen (Hinzufügen, Material entnehmen, Bearbeiten/Löschen, Artikelgruppe
        anlegen, Materialgruppe anlegen) wurden von eigenen Unterseiten auf modale Popup-Fenster
        (<code>st.dialog</code>) umgestellt, die sich per Knopfdruck öffnen, ohne die Seite zu
        wechseln. Die Fenster wurden vertikal mittig zentriert, alle Eingabefelder untereinander
        statt nebeneinander angeordnet, und Bestätigungs-Buttons konsequent rechts platziert
        (Löschen links, Speichern/Hinzufügen rechts).
      </p>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Sechs Buttons wurden zu drei:</strong> Die ursprünglich getrennten Buttons für
        „Artikel“ und „Reste“ wurden zusammengeführt. Beim Hinzufügen entscheidet seither die
        eingegebene Länge automatisch, ob ein Stück als voller Artikel oder als Rest gespeichert
        wird &ndash; mit Live-Hinweistext und manueller Überschreibungs-Möglichkeit.
      </div>
    </section>

    <section>
      <h2>Layout- und Bedienbarkeits-Feinschliff</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>Tabellen ohne inneren Scrollbalken</strong>zeigen seither ihre volle Höhe &ndash; die Seite selbst scrollt.</span></li>
        <li><span><strong>Tipp- und scanfähige Kombobox</strong>statt einfacher Textsuche, ergänzt um „Erweiterte Filter“ mit Mehrfachkriterien (Profil, Barcode, Bezeichnung, Lagerort, Material, Maß, Länge von/bis).</span></li>
        <li><span><strong>Eine gemeinsame Schrott-/Rest-Grenze</strong>statt zwei getrennter, fest im Code verankerter Schwellenwerte &ndash; jetzt über eine Konfigurationstabelle einstellbar.</span></li>
        <li><span><strong>Schnellzugriff zentral in der Seitenleiste</strong>statt auf allen Einzelseiten dupliziert &ndash; von jeder Seite aus verfügbar, ohne redundante Pflege.</span></li>
        <li><span><strong>Zahlreiche Feinjustierungen</strong>Überschriftengrößen, Spaltenanzahl in Formularen, einheitliche Button-Breiten sowie eigene Filterleisten direkt auf „Artikel Liste“ und „Reste“.</span></li>
      </ul>
    </section>

    <section>
      <h2>Automatische Voll/Rest-Zuordnung in der Praxis</h2>
      <p>
        Ein konkretes Beispiel für den iterativen Feinschliff: Beim Hinzufügen eines neuen Stücks
        zeigt die App live einen Hinweis, sobald eine Länge eingegeben wird &ndash; liegt sie
        unter der Schrott-/Rest-Grenze, erscheint eine Warnung, dass automatisch als „Rest“
        gespeichert wird, sonst eine Info, dass es ein voller Artikel wird. Eine Checkbox
        erlaubt es, diese automatische Zuordnung im Einzelfall zu überschreiben.
      </p>
    </section>

{projekt_nav("06-datenmodell.html", "Datenmodell & Import", "08-papierkorb.html", "Papierkorb")}
  </main>
"""

write_page("07-oberflaeche.html", "Projekt 3: Oberfläche", body)
