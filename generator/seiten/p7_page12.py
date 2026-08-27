# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt7 import *

AUDIT = [
    ("Seiri", "Nur benötigte Werkzeuge, nichts Überflüssiges oder Defektes"),
    ("Seiri", "Kein fremdes Material auf der Bank"),
    ("Seiton", "Jedes Werkzeug am markierten Platz (Shadow-Board)"),
    ("Seiton", "Zonen A/B/C korrekt genutzt, Beschriftung lesbar"),
    ("Seiso", "Fläche und Maschinen sauber, keine Späne"),
    ("Seiso", "Messmittel sauber, geölt, geschützt"),
    ("Seiketsu", "Standard (Foto / Regeln) sichtbar und aktuell"),
    ("Seiketsu", "PSA vorhanden und einsatzbereit"),
    ("Shitsuke", "Schichtende-Check durchgeführt"),
    ("Shitsuke", "Maßnahmen aus letztem Audit umgesetzt"),
]
audit_rows = ""
last = None
for i, (s, text) in enumerate(AUDIT, start=1):
    kat = s if s != last else "&nbsp;"
    last = s
    audit_rows += f'<tr><td>{i}</td><td>{kat}</td><td>{text}</td><td>0 &middot; 1 &middot; 2</td></tr>\n            '

PHASEN = [
    ("1 · Analyse &amp; Werkzeuge", 2, "19.06.2026", "Analyse &amp; Werkzeugliste fertig"),
    ("2 · 5S-Konzept", 1, "26.06.2026", "5S-Konzept fertig"),
    ("3 · Layout &amp; Varianten", 2, "10.07.2026", "Varianten &amp; Layout fertig"),
    ("4 · Angebote &amp; Wirtschaftlichkeit", 1, "17.07.2026", "Angebote &amp; Wirtschaftlichkeit fertig"),
    ("5 · Entscheidung / Beschaffung", 1, "28.08.2026", "Entscheidung / Beschaffung angestoßen"),
    ("6 · Aufbau &amp; Bestückung", 2, "11.09.2026", "Arbeitsplatz aufgebaut &amp; bestückt"),
    ("7 · Einweisung &amp; Audit", 1, "18.09.2026", "Einweisung, 1. 5S-Audit"),
]
phasen_rows = ""
for name, dur, datum, ms in PHASEN:
    phasen_rows += f'<tr><td>{name}</td><td>{dur} Woche{"n" if dur > 1 else ""}</td><td>{datum}</td><td>{ms}</td></tr>\n            '
phasen_rows += f'<tr class="total-row"><td>Summe</td><td>{sum(p[1] for p in PHASEN)} Arbeitswochen</td><td colspan="2">zzgl. 4 Wochen Urlaub (23.07.&ndash;21.08.2026)</td></tr>'

body = seiten_kopf(12, "Umsetzung, Zeitplan &amp; Audit",
    "Wie aus dem Konzept ein fertiger Arbeitsplatz wird: sieben Phasen mit Meilensteinen, die "
    "5S-Audit-Checkliste als Messinstrument und das finale Entscheidungsblatt.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>📅 Zeitplan &ndash; sieben Phasen</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Phase</th><th>Dauer</th><th>Meilenstein am</th><th>Ergebnis</th></tr></thead>
          <tbody>
            {phasen_rows}
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Struktur des Plans:</strong> Phasen 1&ndash;4 sind reine Planung (6 Wochen),
        Phase 5 ist die Entscheidung, Phasen 6&ndash;7 sind Umsetzung (3 Wochen). Auffällig ist
        der lange Sprung zwischen Phase 4 und 5: Dort liegt der vierwöchige Urlaub vom 23.07. bis
        21.08.2026. Das ist bewusst so gelegt &ndash; die Entscheidung über eine mehrere tausend
        Euro teure Beschaffung soll nicht kurz vor einer Abwesenheit fallen, sondern danach, wenn
        die Umsetzung durchgehend begleitet werden kann.
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Kleine Unschärfe im Zeitraum:</strong> Das Entscheidungsblatt nennt als Zeitraum
        08.06.&ndash;11.09.2026. Dieses Datum entspricht dem Ende von Phase 6 (Arbeitsplatz
        aufgebaut und bestückt). Phase 7 mit Einweisung und erstem Audit liegt rechnerisch eine
        Woche später, am 18.09.2026. Für die Abgabe ist zu klären, ob das erste Audit noch in den
        Projektzeitraum fällt oder als Nachlauf dokumentiert wird.
      </div>
    </section>

    <section>
      <h2>✅ 5S-Audit-Checkliste</h2>
      <p>
        Zehn Prüfpunkte, je 0 bis 2 Punkte &ndash; <strong>maximal 20 Punkte</strong>. Die
        Checkliste ist das Instrument für das fünfte S (Selbstdisziplin): Sie macht den Zustand des
        Platzes messbar und damit über die Zeit vergleichbar.
      </p>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>#</th><th>S</th><th>Prüfpunkt</th><th>Bewertung</th></tr></thead>
          <tbody>
            {audit_rows}
          </tbody>
        </table>
      </div>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Punktzahl</th><th>Bewertung</th><th>Konsequenz</th></tr></thead>
          <tbody>
            <tr><td>16&ndash;20</td><td><span class="st-ok">sehr gut</span></td><td>Zustand halten, nächstes Audit planmäßig</td></tr>
            <tr><td>10&ndash;15</td><td><span class="st-warn">nachbessern</span></td><td>Schwachpunkte benennen, Maßnahmen bis zum nächsten Audit</td></tr>
            <tr><td>unter 10</td><td><span class="st-no">Sofortmaßnahmen</span></td><td>Platz gemeinsam neu aufräumen, Ursachen klären</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Warum 0/1/2 statt Ja/Nein:</strong> Eine Ja-Nein-Bewertung führt dazu, dass
        „fast in Ordnung" als erfüllt durchgeht. Die Zwischenstufe zwingt dazu, teilweise erfüllte
        Punkte auch als solche zu benennen &ndash; und macht Verbesserungen zwischen zwei Audits
        überhaupt erst sichtbar.
      </div>
    </section>

    <section>
      <h2>👍 Entscheidungsblatt (final)</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Punkt</th><th>Festlegung</th></tr></thead>
          <tbody>
            <tr><td>Layout</td><td><strong>Konzept 2</strong> &ndash; Lochwand mittig, hohe schmale Seitenschränke</td></tr>
            <tr><td>Werkbank</td><td>B ~1800 · T 600 · H 850&ndash;950 mm, Schraubstock fest verschraubt</td></tr>
            <tr><td>Seitenschränke</td><td>Tiefe ~400 mm, wandverankert</td></tr>
            <tr><td>Ergänzung</td><td>Mobiler Werkzeugwagen (aus Konzept 3)</td></tr>
            <tr><td>Ordnung</td><td>5S mit Farbcode und wöchentlichem Audit</td></tr>
            <tr><td>Werkzeugkosten</td><td>~5.742 € brutto</td></tr>
            <tr><td>Zeitraum</td><td>08.06. &ndash; 11.09.2026 (Urlaub 23.07. &ndash; 21.08.)</td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Was das Entscheidungsblatt bewusst offenlässt:</strong> Es legt Layout, Maße,
        Ordnung und Kosten fest &ndash; aber <em>nicht</em> die Bauvariante. Ob die Bank aus
        item-Profil, Systemmodulen oder Stahl entsteht, ist damit weiterhin offen. Das ist
        konsequent, weil die Nutzwertanalyse zwischen item-Profil (4,15) und Systemmodulen (3,95)
        keinen belastbaren Abstand ergibt &ndash; diese Entscheidung braucht reale Angebote, keine
        weitere Bewertung.
      </div>
    </section>

    <section>
      <h2>📋 Was für die Umsetzung noch zu tun ist</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Prio</th><th>Aufgabe</th><th>Warum</th></tr></thead>
          <tbody>
            <tr><td><span class="prio prio--hoch">hoch</span></td><td>Angebote für item-Profil und Systemmodule einholen</td><td>Entscheidet die offene Variantenfrage &ndash; die Nutzwertanalyse allein kann es nicht</td></tr>
            <tr><td><span class="prio prio--hoch">hoch</span></td><td>Werkstatt real aufmessen</td><td>Grundriss-Maße sind Beispielannahmen; die 1800-mm-Bank braucht eine geprüfte Wandfläche</td></tr>
            <tr><td><span class="prio prio--hoch">hoch</span></td><td>Wandverankerung der Hochschränke klären</td><td>Einziger Nachteil von Konzept 2 &ndash; Wandaufbau und Tragfähigkeit prüfen</td></tr>
            <tr><td><span class="prio prio--mittel">mittel</span></td><td>Belegungsplan der Lochwand zeichnen</td><td>Zone A ist inhaltlich definiert, aber die Anordnung am Board fehlt noch</td></tr>
            <tr><td><span class="prio prio--mittel">mittel</span></td><td>Traglast des gewählten Fabrikats gegen 500 kg prüfen</td><td>Anforderung aus Seite 6, bisher nicht gegen ein konkretes Produkt geprüft</td></tr>
            <tr><td><span class="prio prio--mittel">mittel</span></td><td>Beleuchtung am Platz messen</td><td>500 lx sind gefordert &ndash; ob sie erreicht werden, ist ungeprüft</td></tr>
            <tr><td><span class="prio prio--niedrig">niedrig</span></td><td>Foto-Standard des Sollzustands anlegen</td><td>Grundlage für Seiketsu und für jedes spätere Audit</td></tr>
            <tr><td><span class="prio prio--niedrig">niedrig</span></td><td>Beschriftung und Schaumeinlagen beschaffen</td><td>Kleiner Betrag, in der Kostenliste noch nicht enthalten</td></tr>
          </tbody>
        </table>
      </div>
    </section>

{projekt_nav("11-arbeitssicherheit.html", "Arbeitssicherheit", "13-fazit-quellen.html", "Fazit, Quellen & Normen")}
  </main>
"""

write_page("12-umsetzung-audit.html", "Projekt 7: Umsetzung, Zeitplan & Audit", body)
