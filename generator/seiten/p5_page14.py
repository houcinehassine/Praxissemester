# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt5 import *

offene_punkte = """<table class="tabelle"><thead><tr><th>#</th><th>Aufgabe</th><th>Warum</th><th>Priorität</th></tr></thead><tbody>
<tr><td>1</td><td>Bohrungszahl der Lochplatte am CAD-Modell prüfen (40 vs. ca. 64 rechnerisch)</td><td>Rechnerischer Rückschluss aus dem Gewicht weicht vom erwarteten Raster ab</td><td><span class="prio prio--mittel">mittel</span></td></tr>
<tr><td>2</td><td>Verschraubungsmethode für die Lochplatten festlegen</td><td>Baugruppe „Lochplatte + Schrauben" enthält bis heute keine Schrauben in der Stückliste</td><td><span class="prio prio--hoch">hoch</span></td></tr>
<tr><td>3</td><td>Quelle für 4× Sechskantmutter M16 klären</td><td>Weiterhin „Unbekannt" – Teil würde sonst bei der Bestellung fehlen</td><td><span class="prio prio--mittel">mittel</span></td></tr>
<tr><td>4</td><td>Lenkrollen mit mind. 150–200 kg Tragkraft je Rolle beschaffen</td><td>Reales Gewicht liegt bei ca. 320 kg statt der dokumentierten 289 kg</td><td><span class="prio prio--hoch">hoch</span></td></tr>
<tr><td>5</td><td>Fehlerhafte Gewichtsangaben (Oberteil-BG, Untergestell) im CAD korrigieren</td><td>Für zukünftige Auswertungen/Exporte sollen die Schriftfelder stimmen, nicht nur die Handrechnung</td><td><span class="prio prio--mittel">mittel</span></td></tr>
</tbody></table>"""

body = seiten_kopf(14, "Fazit &amp; Ausblick",
    "Vom ersten YouTube-Video als Inspiration bis zum geprüften, fertigungsreifen Endstand &ndash; "
    "und was diese Konstruktionsprüfung für den Tätigkeitsbericht bedeutet.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>Nutzen des Projekts</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>Vollwertiger Schweißarbeitsplatz</strong>1600 × 1000 mm Arbeitsfläche, beidseitig bis 3,1 m ausziehbar, fahrbar auf 4 Lenkrollen.</span></li>
        <li><span><strong>Vollständige Fertigungsunterlagen</strong>15 bemaßte Zeichnungsblätter mit Stückliste, Werkstoffangaben und Toleranzen.</span></li>
        <li><span><strong>Nachvollziehbare Konstruktionsentwicklung</strong>vom ersten Konzept über einen kompletten Zwischenentwurf bis zum geprüften Endstand &ndash; jede Änderung begründet.</span></li>
        <li><span><strong>Eigenständige Qualitätsprüfung</strong>5 belegte Fehler in den eigenen CAD-Daten gefunden, rechnerisch bewiesen und auf ihre Ursache zurückgeführt &ndash; bevor sie in der Fertigung Probleme verursacht hätten.</span></li>
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
          <h4>Ein CAD-Gewicht ist nur so gut wie die Werkstoffzuweisung</h4>
          <p>Drei von fünf Fehlern hatten dieselbe Ursache: fehlende Materialdichte im Modell. Ein einfacher Prüfschritt vor der Zeichnungsausgabe hätte sie verhindert.</p>
        </div>
        <div class="karte">
          <span class="label">Methodisch</span>
          <h4>Plausibilitätsprüfung durch Nachrechnung ist eine eigene Leistung</h4>
          <p>Jeder Fund wurde nicht nur behauptet, sondern per Handrechnung (Querschnitt × Länge × Dichte) bewiesen &ndash; und wo möglich mehrfach unabhängig bestätigt.</p>
        </div>
        <div class="karte">
          <span class="label">Praktisch</span>
          <h4>Konstruktion ist iterativ, auch mit Rückschlägen</h4>
          <p>Zwischen dem ersten fertigen Entwurf (52 Teile) und dem Endstand (40 Teile, komplett andere Aufteilung) liegt eine Woche echter Überarbeitung &ndash; nicht alles war beim ersten Versuch richtig, und das ist normal.</p>
        </div>
      </div>
    </section>

    <section>
      <div class="zitat-box">
        Dieser Schweißtisch ist die konkrete, real gebaute Antwort auf die Frage aus Projekt 4:
        eine Stahl-Lochplatten-Werkbank statt der abstrakt „besten“ Item-Variante &ndash; robust,
        hitzefest, ausziehbar und mit einer selbst durchgeführten Qualitätsprüfung, die auf
        einer geprüften Fertigungszeichnung von MW Schmidt beruht.
      </div>
    </section>

    <nav class="projekt-nav">
      <a href="13-endstand-technische-daten.html">
        <span class="richtung">&larr; Zurück</span>
        Endstand & Technische Daten
      </a>
      <a class="naechste" href="../projekt-6/index.html">
        <span class="richtung">Weiter zu Projekt 6 &rarr;</span>
        Schweißmaschinenwagen
      </a>
    </nav>
  </main>
"""

write_page("14-fazit-ausblick.html", "Projekt 5: Fazit & Ausblick", body)
