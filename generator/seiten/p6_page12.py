# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt6 import *

body = seiten_kopf(12, "Fazit &amp; Ausblick",
    "Was der Schweißmaschinenwagen am Ende des Praxissemesters erreicht hat, was das Projekt "
    "methodisch gezeigt hat &ndash; und welche Schritte bis zur Fertigung noch fehlen.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>📊 Stand am Projektende</h2>
      <div class="kennzahlen-grid">
        <div class="kennzahl"><strong>21</strong><span>Zeichnungsblätter A3</span></div>
        <div class="kennzahl"><strong>58</strong><span>Teile, 15 verschiedene</span></div>
        <div class="kennzahl"><strong>91,05</strong><span>kg Konstruktionsgewicht</span></div>
        <div class="kennzahl"><strong>6</strong><span>durchlaufene Entwicklungsstufen</span></div>
      </div>
      <p style="margin-top:0.75rem">
        Aus einem Bestandswagen, einem Zollstock und einer Handskizze auf Karopapier ist ein
        vollständig modellierter, in 21 Blättern dokumentierter Schweißmaschinenwagen geworden.
        Der Weg dorthin führte über zwei verworfene Erstentwürfe, einen kompletten Neubau, einen
        Konzeptwechsel zum Portalgestell und schließlich zum modularen 4-Etagen-Aufbau.
      </p>
    </section>

    <section>
      <h2>✅ Was erreicht wurde</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>IST-Zustand sauber erfasst</strong>Fotos, Aufmaß vor Ort (Gerät 610 × 430 × 520 mm, Flasche Ø220 × 1640 mm) und eine CAD-Vereinfachung als Bauraum-Platzhalter. Damit stand von Anfang an fest, welche Bauräume die Konstruktion aufnehmen muss.</span></li>
        <li><span><strong>Anforderungen nummeriert statt beschrieben</strong>14 prüfbare Anforderungen A-01 bis A-14. Jede Variante konnte danach mit einem konkreten Erfüllungsgrad bewertet werden &ndash; SW-001 mit 12 erfüllt, der Zusatzwagen mit 4.</span></li>
        <li><span><strong>Zwei Varianten wirklich durchkonstruiert</strong>Neubau und Zusatzwagen liegen nicht als Skizze, sondern als CAD-Modell vor. Die geforderte Gegenüberstellung Item-Profil gegen Stahlkonstruktion hat damit eine echte technische Grundlage.</span></li>
        <li><span><strong>Fertigungsreifer Zeichnungssatz</strong>21 Blätter A3 mit Einzelteilen, Baugruppen und vollständiger Stückliste, Werkstoff S235JRH, geprüft durch MW Schmidt. Der Satz ist so weit, dass ein Zuschnitt daraus abgeleitet werden könnte.</span></li>
        <li><span><strong>Eigene Prüfung mit belegten Funden</strong>Gewichtsangaben nachgerechnet, Schriftfelder und Stücklisten kontrolliert: drei Stichproben exakt, zwei fehlerhaft, dazu sieben weitere Befunde. Die Fehler sind benannt, statt unbemerkt in die Fertigung zu gehen.</span></li>
      </ul>
    </section>

    <section>
      <h2>🧠 Was das Projekt methodisch gezeigt hat</h2>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>📏 Messen schlägt Schätzen</h4><p>Der Maßkonflikt beim Gerätefach (430 mm Fach gegen 520 mm Maschine) wurde nur sichtbar, weil vorher real aufgemessen wurde. Ohne das Aufmaß wäre der Fehler erst beim Einschieben aufgefallen.</p></div>
        <div class="mini-karte"><h4>🔁 Varianten sind kein Umweg</h4><p>Jede der sechs Stufen wurde aus einem konkreten Grund verworfen. Der Konzeptwechsel zum Portalgestell war keine Kehrtwende, sondern die Konsequenz aus einem gemessenen Widerspruch.</p></div>
        <div class="mini-karte"><h4>🔍 Nachrechnen lohnt sich</h4><p>3,49 kg/m für Rohr 40×40×3 ist in einer Minute gerechnet &ndash; und deckte zwei falsche Gewichtsangaben im eigenen Zeichnungssatz auf.</p></div>
        <div class="mini-karte"><h4>📄 Dokumentieren erzeugt Fragen</h4><p>Beim Zusammenschreiben fielen vier verschiedene Flaschenhöhen in vier Dokumenten auf. Widersprüche zeigen sich erst, wenn Zahlen nebeneinanderstehen.</p></div>
      </div>
    </section>

    <section>
      <h2>❗ Was ehrlicherweise offen bleibt</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Prio</th><th>Offener Punkt</th><th>Nächster Schritt</th></tr></thead>
          <tbody>
            <tr><td><span class="prio prio--hoch">hoch</span></td><td>Gasflaschenaufnahme fehlt im Zeichnungssatz</td><td>Halterung mit Kette konstruieren und als Baugruppe ergänzen (A-02)</td></tr>
            <tr><td><span class="prio prio--hoch">hoch</span></td><td>Schriftfeld nennt auf allen 21 Blättern „Schweißtisch“</td><td>Projektbezeichnung im CAD-Template korrigieren, Satz neu ausgeben</td></tr>
            <tr><td><span class="prio prio--hoch">hoch</span></td><td>Gewichtsangaben Blatt 1 und Blatt 7 falsch</td><td>Werkstoffzuweisung im Modell prüfen, Blätter neu generieren</td></tr>
            <tr><td><span class="prio prio--mittel">mittel</span></td><td>Kostenkalkulation fehlt</td><td>Stückliste bepreisen &rarr; erst damit ist die geforderte technisch-wirtschaftliche Gegenüberstellung vollständig</td></tr>
            <tr><td><span class="prio prio--mittel">mittel</span></td><td>Standsicherheitsnachweis steht aus</td><td>Mit den nun bekannten 91,05 kg Eigengewicht und ≈265&ndash;320 kg beladen rechnen</td></tr>
            <tr><td><span class="prio prio--mittel">mittel</span></td><td>Maßgebende Flaschengröße nicht festgelegt</td><td>Eine Größe verbindlich festlegen und alle Dokumente darauf vereinheitlichen</td></tr>
            <tr><td><span class="prio prio--niedrig">niedrig</span></td><td>Arbeitsanweisung nicht erstellt</td><td>Aus Belegungsplan und Fotos ableiten &ndash; Unterlagen liegen vor</td></tr>
            <tr><td><span class="prio prio--niedrig">niedrig</span></td><td>Belegungsplan der Lochwand</td><td>5S-Schattenbrett festlegen: welches Werkzeug an welche Position</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Bewusst so dargestellt:</strong> Diese Punkte sind nicht ausgelassen, sondern
        benannt. Ein Konstruktionsstand ohne offene Punkte gibt es in dieser Projektphase nicht
        &ndash; entscheidend ist, dass sie dokumentiert, priorisiert und einem nächsten Schritt
        zugeordnet sind.
      </div>
    </section>

    <section>
      <h2>🔗 Zusammenhang mit den anderen Projekten</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Projekt</th><th>Verbindung zum Schweißmaschinenwagen</th></tr></thead>
          <tbody>
            <tr><td><a href="../projekt-4/index.html">Projekt 4 &ndash; Schweißarbeitsplatz</a></td><td>Liefert die Werkzeugliste und das 5S-Konzept. Der Wagen ist die mobile Ergänzung zur festen Station: was am Platz bleibt, steht dort &ndash; was mitfährt, kommt auf den Wagen.</td></tr>
            <tr><td><a href="../projekt-5/index.html">Projekt 5 &ndash; Schweißtisch</a></td><td>Gleiche Werkstatt, gleiche Konstruktionsmethodik, gleiches Vorgehen bei der Eigenprüfung. Der Wagen fährt an den dort konstruierten Tisch heran.</td></tr>
            <tr><td><a href="../projekt-7/index.html">Projekt 7 &ndash; Zerspanarbeitsplatz</a></td><td>Überträgt dieselbe 5S-Systematik auf den Zerspanungsbereich.</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>💬 Persönliches Fazit</h2>
      <div class="zitat-box">
        Am meisten gelernt habe ich nicht beim Modellieren, sondern beim Nachmessen und
        Nachrechnen. Der Wagen sah im CAD lange fertig aus &ndash; erst der Vergleich zwischen
        Aufmaß, Konzeptmaßen und Zeichnungssatz hat gezeigt, wo er es noch nicht war. Genau dieses
        Prüfen gegen die eigene Arbeit nehme ich als wichtigste Erfahrung aus dem Projekt mit.
      </div>
    </section>

{projekt_nav("11-pruefung-funde.html", "Prüfung & Funde", "../projekt-7/index.html", "Projekt 7: Zerspanarbeitsplatz")}
  </main>
"""

write_page("12-fazit.html", "Projekt 6: Fazit & Ausblick", body)
