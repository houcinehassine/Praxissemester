# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt3 import *

body = seiten_kopf(3, "Erkannte Schwachstellen als Ausgangspunkt",
    "Die detaillierte Durchsicht des Codes machte mehrere strukturelle Schwachpunkte sichtbar, "
    "die die Entscheidung für eine Neuentwicklung zusätzlich untermauerten.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>Sechs konkrete Schwachpunkte</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Schwachpunkt</th><th>Konkret</th></tr></thead>
          <tbody>
            <tr><td><span class="prio prio--hoch">Kein Mehrbenutzerbetrieb</span></td><td>Eine Excel-Datei kann von mehreren Personen nur eingeschränkt gleichzeitig bearbeitet werden &ndash; im Original gar nicht vorgesehen.</td></tr>
            <tr><td><span class="prio prio--mittel">Durchgängige Plattformweichen</span></td><td>Fast jede Datei-, Ordner- und E-Mail-Operation brauchte eigenen Code für Mac (<code>#If Mac</code>, AppleScript) und Windows (FileDialog, Outlook-COM) &ndash; jede Änderung musste zweimal gepflegt werden.</td></tr>
            <tr><td><span class="prio prio--mittel">Gmail nie wirklich unterstützt</span></td><td>Der entsprechende Code-Pfad öffnet im Zweifel nur ein leeres Programmfenster und gibt sonst nichts zurück.</td></tr>
            <tr><td><span class="prio prio--mittel">Unvollständiger Code an zentraler Stelle</span></td><td>Die Validierung der Dashboard-Suche (<code>H1_Suchen_Funktionen</code>) enthielt noch Platzhalter- und auskommentierten Code für eine nie fertiggestellte Zusatzfunktion.</td></tr>
            <tr><td><span class="prio prio--hoch">Sicherheitsschwache Absicherung</span></td><td>Der Blattschutz nutzte ein kurzes, im Klartext im Quellcode hinterlegtes Passwort.</td></tr>
            <tr><td><span class="prio prio--hoch">Fehlende Nachvollziehbarkeit von Löschvorgängen</span></td><td>Ein gelöschtes Artikel-Stück (<code>Del_ArtikelStueck</code>) war sofort und ohne jede Wiederherstellungsmöglichkeit weg.</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>Was direkt in die Anforderungen einfloss</h2>
      <p>
        Diese Beobachtungen wurden nicht nur zur Kenntnis genommen, sondern
        flossen unmittelbar in die Anforderungen an die Neuentwicklung ein:
      </p>
      <ul class="ergebnis-liste">
        <li><span><strong>Mehrbenutzerfähigkeit von Anfang an</strong>statt sie nachträglich zu ergänzen (siehe Seite 5).</span></li>
        <li><span><strong>Eine einzige Codebasis ohne Plattformweichen</strong>Python/Streamlit läuft identisch auf Mac und Windows.</span></li>
        <li><span><strong>Eine bewusst einfach gehaltene E-Mail-Lösung</strong>mailto-Links statt fragiler Client-Automatisierung &ndash; funktioniert dadurch auch mit Gmail zuverlässig.</span></li>
        <li><span><strong>Eine Papierkorb-Funktion mit Wiederherstellungsmöglichkeit</strong>später im Projekt gezielt ergänzt (siehe Seite 8).</span></li>
      </ul>
    </section>

    <section>
      <div class="warn-box">
        <strong>Wichtig für die Einordnung:</strong> Keiner dieser Punkte bedeutet, dass das
        Original-System &bdquo;schlecht&ldquo; war &ndash; es hat seinen Zweck über Monate
        zuverlässig erfüllt (siehe Projekt 2). Es zeigt lediglich die Grenzen von Excel/VBA
        für ein System, das mehrbenutzerfähig, plattformunabhängig und langfristig wartbar
        sein soll.
      </div>
    </section>

{projekt_nav("02-original-system.html", "Das Original-System", "04-architektur.html", "Architektur")}
  </main>
"""

write_page("03-schwachstellen.html", "Projekt 3: Schwachstellen", body)
