# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt7 import *

CRIT = [("Flexibilität", 20), ("Ergonomie", 15), ("Anschaffungskosten", 20), ("Robustheit", 15),
        ("Aufwand bis einsatzbereit", 10), ("5S-Eignung", 15), ("Optik / Wertigkeit", 5)]
VARS = [("V1 item-Profil", [5, 5, 2, 4, 4, 5, 5]),
        ("V2 Stahl-Standard", [2, 3, 5, 4, 5, 3, 3]),
        ("V3 Systemmodule", [4, 4, 3, 4, 4, 5, 4]),
        ("V4 Eigenbau", [3, 2, 5, 5, 2, 3, 2])]
GEW_SUM = sum(g for _, g in CRIT)

def nutzwert(punkte):
    return sum(CRIT[i][1] / GEW_SUM * punkte[i] for i in range(len(CRIT)))

erg = [(n, p, nutzwert(p)) for n, p in VARS]
rang = {n: i + 1 for i, (n, _, _) in enumerate(sorted(erg, key=lambda x: -x[2]))}

kopf = "".join(f"<th>{n}</th>" for n, _ in VARS)
zeilen = ""
for i, (krit, gew) in enumerate(CRIT):
    zellen = ""
    best = max(v[1][i] for v in VARS)
    for n, p in VARS:
        cls = ' class="st-ok"' if p[i] == best else ""
        zellen += f"<td><span{cls}>{p[i]}</span></td>" if cls else f"<td>{p[i]}</td>"
    zeilen += f"<tr><td>{krit}</td><td>{gew} %</td>{zellen}</tr>\n            "
zeilen += '<tr class="total-row"><td>Nutzwert (gewichtet)</td><td>100 %</td>'
for n, p, v in erg:
    zeilen += f"<td><strong>{v:.2f}</strong>".replace(".", ",") + "</td>"
zeilen += "</tr>\n            <tr class=\"total-row\"><td>Rangfolge</td><td>&nbsp;</td>"
for n, p, v in erg:
    zeilen += f"<td>Platz {rang[n]}</td>"
zeilen += "</tr>"

body = seiten_kopf(9, "Nutzwertanalyse &amp; Empfehlung",
    "Teilaufgabe E: Sieben gewichtete Kriterien, vier Varianten, eine nachvollziehbare Rechnung "
    "&ndash; und die Empfehlung, die daraus folgt.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>⚖️ Die sieben Kriterien und ihre Gewichtung</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Kriterium</th><th>Gewicht</th><th>Warum dieses Gewicht</th></tr></thead>
          <tbody>
            <tr><td>Flexibilität</td><td>20 %</td><td>Höchstes Gewicht &ndash; ein 5S-Platz wird nach jedem Audit nachjustiert. Was sich nicht ändern lässt, blockiert die Verbesserung.</td></tr>
            <tr><td>Anschaffungskosten</td><td>20 %</td><td>Ebenso hoch: Ohne festes Budget muss der Preis trotzdem begründbar bleiben.</td></tr>
            <tr><td>Ergonomie</td><td>15 %</td><td>Drei Personen unterschiedlicher Größe nutzen denselben Platz &ndash; eine feste Höhe passt nie allen.</td></tr>
            <tr><td>Robustheit</td><td>15 %</td><td>Zerspanumgebung: Späne, KSS, schwere Werkstücke, gespannter Schraubstock.</td></tr>
            <tr><td>5S-Eignung</td><td>15 %</td><td>Kernziel des ganzen Projekts &ndash; wie gut lassen sich feste Plätze und Shadow-Boards umsetzen?</td></tr>
            <tr><td>Aufwand bis einsatzbereit</td><td>10 %</td><td>Wichtig, aber einmalig &ndash; ein langer Aufbau ärgert nur am Anfang.</td></tr>
            <tr><td>Optik / Wertigkeit</td><td>5 %</td><td>Geringstes Gewicht &ndash; nicht irrelevant (Ordnung wirkt ansteckend), aber nachrangig.</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Zur Methodik:</strong> Jede Variante wird je Kriterium mit 1 bis 5 Punkten bewertet
        (5 = am besten). Der Nutzwert ist die gewichtete Summe: Punktzahl × Gewicht, aufsummiert
        und auf 100 % normiert. Der Höchstwert wäre 5,00.
      </div>
    </section>

    <section>
      <h2>📊 Die vollständige Bewertungsmatrix</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Kriterium</th><th>Gew.</th>{kopf}</tr></thead>
          <tbody>
            {zeilen}
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">
        Hervorgehoben ist jeweils die beste Bewertung je Kriterium. Gut ablesbar: item-Profil
        gewinnt in vier von sieben Kriterien, verliert aber deutlich beim Preis &ndash; genau das
        macht die Entscheidung interessant.
      </p>
    </section>

    <section>
      <h2>🏁 Ergebnis der Rechnung</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Platz</th><th>Variante</th><th>Nutzwert</th><th>Erreichter Anteil</th></tr></thead>
          <tbody>
            <tr><td><span class="prio prio--hoch">1</span></td><td>V1 item-Profil</td><td><strong>4,15</strong></td><td>83 % der Maximalpunktzahl</td></tr>
            <tr><td><span class="prio prio--mittel">2</span></td><td>V3 Systemmodule</td><td><strong>3,95</strong></td><td>79 %</td></tr>
            <tr><td><span class="prio prio--niedrig">3</span></td><td>V2 Stahl-Standard</td><td><strong>3,55</strong></td><td>71 %</td></tr>
            <tr><td><span class="prio prio--niedrig">4</span></td><td>V4 Eigenbau</td><td><strong>3,40</strong></td><td>68 %</td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Der Abstand ist klein &ndash; und das ist die eigentliche Erkenntnis:</strong>
        Zwischen Platz 1 und Platz 2 liegen 0,20 Punkte, also 4 % der Skala. Bei einer
        Bewertung, die auf geschätzten Einzelnoten beruht, ist das kein belastbarer Vorsprung. Die
        Nutzwertanalyse sagt hier ehrlicherweise nicht „item-Profil ist die richtige Wahl", sondern
        „item-Profil und Systemmodule sind gleichwertig, Stahl-Standard und Eigenbau fallen ab".
      </div>
    </section>

    <section>
      <h2>💰 Kostenschätzung je Variante</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Variante</th><th>Anschaffung</th><th>Zusatzaufwand</th><th>Rechenwert</th></tr></thead>
          <tbody>
            <tr><td>V1 item-Profil</td><td>4.000&ndash;7.000 €</td><td>gering (montieren)</td><td>5.500 €</td></tr>
            <tr><td>V2 Stahl-Standard</td><td>1.500&ndash;3.000 €</td><td>sehr gering</td><td>2.250 €</td></tr>
            <tr><td>V3 Systemmodule</td><td>2.500&ndash;4.500 €</td><td>gering</td><td>3.500 €</td></tr>
            <tr><td>V4 Eigenbau</td><td>~800&ndash;1.500 € Material</td><td><span class="st-warn">hoch (Bauzeit)</span></td><td>1.150 €</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">
        Der Rechenwert ist jeweils die Mitte der Spanne und geht so in die Amortisationsrechnung
        auf Seite 10 ein. Beim Eigenbau ist der Materialpreis irreführend niedrig: Die Bauzeit ist
        nirgends in Euro bewertet, macht aber den größten Teil der wirklichen Kosten aus. Genau
        deshalb erhält V4 im Kriterium „Aufwand bis einsatzbereit" nur 2 von 5 Punkten.
      </p>
    </section>

    <section>
      <h2>✅ Empfehlung</h2>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>🥇 1. Wahl: item-Profil</h4><p>Nutzwert 4,15 &ndash; beste Flexibilität, Ergonomie und 5S-Eignung. Die richtige Wahl, wenn der Platz sich weiterentwickeln soll.</p></div>
        <div class="mini-karte"><h4>💡 Alternative: Systemmodule</h4><p>Nutzwert 3,95 &ndash; praktisch gleichwertig, aber rund 2.000 € günstiger. Die vernünftige Wahl, wenn der Preis zählt.</p></div>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Praktische Lesart für die Entscheidung im Betrieb:</strong> Die Nutzwertanalyse
        allein trägt die Entscheidung nicht &ndash; dafür ist der Abstand zu gering. Sie schließt
        aber zwei Varianten belastbar aus und stellt zwei zur Wahl. Welche der beiden es wird,
        sollte die Wirtschaftlichkeitsrechnung auf Seite 10 mitentscheiden: dort schlägt der
        Preisunterschied direkt auf die Amortisationsdauer durch.
      </div>
    </section>

{projekt_nav("08-layout-konzepte.html", "4 Layout-Konzepte", "10-wirtschaftlichkeit.html", "Wirtschaftlichkeit & Amortisation")}
  </main>
"""

write_page("09-nutzwertanalyse.html", "Projekt 7: Nutzwertanalyse & Empfehlung", body)
