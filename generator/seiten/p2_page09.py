# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt2 import *

offene_punkte = """<table class="tabelle"><thead><tr><th>#</th><th>Aufgabe</th><th>Warum</th><th>Priorität</th></tr></thead><tbody>
<tr><td>1</td><td>Barcode/Bezeichnung-Konfliktprüfung fertigstellen</td><td>Der Suchbutton selbst funktioniert bereits; nur die Prüfung „passt der eingegebene Barcode zur eingegebenen Bezeichnung?“ ist noch eine Platzhalterfunktion</td><td><span class="prio prio--mittel">mittel</span></td></tr>
<tr><td>2</td><td>Schrott-Grenze (1000 mm) konfigurierbar machen</td><td>Aktuell fest im Code verankert statt in den Einstellungen editierbar</td><td><span class="prio prio--mittel">mittel</span></td></tr>
<tr><td>3</td><td>Gmail-Anbindung echt umsetzen</td><td>Aktuell nur ein Browser-Workaround, im Code selbst als „Hack“ kommentiert</td><td><span class="prio prio--mittel">mittel</span></td></tr>
<tr><td>4</td><td>Reste-Workflow in der Praxis testen</td><td>Neuestes Feature, bisher kaum im echten Betrieb erprobt</td><td><span class="prio prio--hoch">hoch</span></td></tr>
<tr><td>5</td><td>Fehlerbehandlung vereinheitlichen</td><td>Manche älteren Module (V2.2) haben noch keine strukturierte Fehlerbehandlung</td><td><span class="prio prio--mittel">mittel</span></td></tr>
<tr><td>6</td><td>Passwortschutz absichern</td><td>Aktuelles Passwort steht als Klartext im Code</td><td><span class="prio prio--mittel">mittel</span></td></tr>
<tr><td>7</td><td>Mehrbenutzer-Betrieb prüfen</td><td>Bisher für Einzelplatz-Nutzung gedacht</td><td><span class="prio prio--niedrig">niedrig</span></td></tr>
</tbody></table>"""

body = seiten_kopf(10, "Fazit &amp; Ausblick",
    "Was das Projekt für den Betrieb bringt, was noch offen ist und was ich "
    "persönlich aus der Entwicklung mitnehme.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>Nutzen im Betrieb</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>Strukturierte Bestandsführung</strong>statt loser Notizen oder Zettelwirtschaft gibt es eine durchsuchbare, zentrale Lagerliste.</span></li>
        <li><span><strong>Schnelle Buchung per Barcode</strong>Scannen statt manuellem Tippen reduziert Erfassungsfehler.</span></li>
        <li><span><strong>Automatische Warnfarben</strong>knapper werdender Bestand fällt sofort optisch auf, statt erst beim Nachzählen entdeckt zu werden.</span></li>
        <li><span><strong>Lückenloser Verlauf</strong>jede Bewegung ist mit Zeitstempel nachvollziehbar – nützlich bei Rückfragen oder Inventur.</span></li>
        <li><span><strong>Reste automatisch erfasst statt nur „sichtbar gemacht“</strong>die Material-Entnahme-Logik (Seite 9) bucht Restlängen beim Zuschnitt selbstständig ein oder fasst sie mit vorhandenen gleich langen Resten zusammen – direkter Bezug zur Aufgabe „Reste besser nutzen“.</span></li>
        <li><span><strong>Fertige Suchmaske</strong>ein Klick durchsucht Artikel- und Restebestand gleichzeitig und zeigt Treffer inkl. Summen direkt im Dashboard.</span></li>
      </ul>
    </section>

    <section>
      <h2>Offene Punkte &amp; nächste Schritte</h2>
      <div class="tabelle-wrapper">{offene_punkte}</div>
    </section>

    <section>
      <h2>Was ich aus dem Projekt mitnehme</h2>
      <div class="fazit-grid">
        <div class="karte">
          <span class="label">Fachlich</span>
          <h4>VBA kann mehr als Makros aufzeichnen</h4>
          <p>Eigene Datentypen, UserForms und modulare Funktionen machen aus ein paar Buttons ein richtiges kleines Programm – bis hin zu einer eigenen Entscheidungslogik für Restlängen.</p>
        </div>
        <div class="karte">
          <span class="label">Methodisch</span>
          <h4>Trennen, bevor es unübersichtlich wird</h4>
          <p>Der Umbau von einer Datei (V2.2) zu Modulen A–H hat gezeigt, wie viel leichter sich Code warten lässt, wenn jede Aufgabe ihren eigenen Platz hat und Hilfsfunktionen (wie die Barcode-Suche) wiederverwendet statt kopiert werden.</p>
        </div>
        <div class="karte">
          <span class="label">Praktisch</span>
          <h4>Iterativ entwickeln statt einmal „fertig“ bauen</h4>
          <p>Zwischen dem ersten Testlauf (23.04.) und dem aktuellen Stand (14.08.) liegen mehrere komplette Überarbeitungen – jede hat reale Schwächen der vorherigen behoben.</p>
        </div>
      </div>
    </section>

    <section>
      <div class="zitat-box">
        Diese Dokumentation fasst den Weg vom ersten Konzept bis zur aktuellen
        Version des Lagerbestand-Systems zusammen. Als Nächstes: die
        Konfliktprüfung im Suchmodul fertigstellen, den Reste-Workflow im
        echten Betrieb testen und die offenen Punkte oben Schritt für Schritt
        abarbeiten.
      </div>
    </section>

    <nav class="projekt-nav">
      <a href="09-material-entnahme.html">
        <span class="richtung">&larr; Zurück</span>
        Material-Entnahme &amp; Reste
      </a>
      <a class="naechste" href="../projekt-3/index.html">
        <span class="richtung">Nächstes Projekt &rarr;</span>
        Lagersystem als Webseite
      </a>
    </nav>
  </main>
"""

write_page("10-fazit.html", "Projekt 2: Fazit & Ausblick", body)
