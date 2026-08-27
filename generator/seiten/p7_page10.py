# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt7 import *

WERKZEUG = 5742
BANK = [("V1 item-Profil", 5500), ("V3 Systemmodule", 3500), ("V2 Stahl-Standard", 2250), ("V4 Eigenbau", 1150)]
PERS, MIN, TAGE, SATZ = 3, 10, 220, 40
STD = PERS * MIN * TAGE / 60
SPAR = STD * SATZ

def eur(n):
    return f"{n:,.0f}".replace(",", ".") + " €"

var_rows = ""
for name, bank in BANK:
    ges = WERKZEUG + bank
    mon = ges / SPAR * 12
    var_rows += (f"<tr><td>{name}</td><td>{eur(bank)}</td><td>{eur(ges)}</td>"
                 f"<td><strong>{mon:.1f}</strong> Monate</td><td>{mon/12:.1f} Jahre</td></tr>\n            ").replace(".0 Monate", ",0 Monate")
var_rows = var_rows.replace(".", ",").replace("&ndash,", "&ndash;").replace("</td>,", "</td>")
# Punkte in Tausendertrennung wiederherstellen
import re
var_rows = re.sub(r'(\d),(\d{3}) €', r'\1.\2 €', var_rows)
var_rows = var_rows.replace("<td>V1 item-Profil</td>", "<td>V1 item-Profil</td>")

szenarien = [(5, "vorsichtig"), (10, "Standardannahme"), (15, "optimistisch"), (20, "sehr optimistisch")]
sz_rows = ""
for m, label in szenarien:
    h = PERS * m * TAGE / 60
    s = h * SATZ
    mon = 9700 / s * 12
    stark = ' class="total-row"' if m == 10 else ""
    sz_rows += (f'<tr{stark}><td>{m} min <span style="opacity:.7">({label})</span></td><td>{h:.0f} h</td>'
                f'<td>{eur(s)}</td><td>{mon:.1f} Monate</td></tr>\n            ').replace(f"{mon:.1f}", f"{mon:.1f}".replace(".", ","))

body = seiten_kopf(10, "Wirtschaftlichkeit &amp; Amortisation",
    "Lohnt sich die Investition? Die 5S-Ordnung spart täglich Suchzeit &ndash; hier gegen die "
    "Kosten gerechnet, mit allen Annahmen offengelegt.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>🧮 Die Rechenlogik</h2>
      <p>
        Der Nutzen von 5S ist schwer greifbar &ndash; „mehr Ordnung" steht in keiner Bilanz.
        Messbar wird er über die <strong>gesparte Suchzeit</strong>: Wenn jedes Werkzeug einen
        festen, markierten Platz hat, entfällt das Suchen. Diese Zeit lässt sich mit dem
        Stundensatz bewerten und der Investition gegenüberstellen.
      </p>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Größe</th><th>Annahme</th><th>Begründung</th></tr></thead>
          <tbody>
            <tr><td>Personen</td><td>{PERS}</td><td>aus den Rahmenbedingungen (Seite 2)</td></tr>
            <tr><td>Gesparte Suchzeit je Person und Tag</td><td>{MIN} min</td><td>bewusst konservativ &ndash; entspricht knapp 2 % der Arbeitszeit</td></tr>
            <tr><td>Arbeitstage pro Jahr</td><td>{TAGE}</td><td>üblicher Rechenwert nach Urlaub und Feiertagen</td></tr>
            <tr><td>Stundensatz</td><td>{SATZ} €</td><td>Vollkostensatz einer Fachkraft (Richtwert)</td></tr>
            <tr class="total-row"><td>Gesparte Zeit pro Jahr</td><td>{STD:.0f} h</td><td>{PERS} × {MIN} min × {TAGE} Tage ÷ 60</td></tr>
            <tr class="total-row"><td>Ersparnis pro Jahr</td><td>{eur(SPAR)}</td><td>{STD:.0f} h × {SATZ} €</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>💶 Die Investition</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Posten</th><th>Betrag</th><th>Quelle</th></tr></thead>
          <tbody>
            <tr><td>Werkzeuge (brutto)</td><td>~5.742 €</td><td>bepreiste Werkzeugliste, Seite 4</td></tr>
            <tr><td>Werkbank + Hochschränke (Konzept 2)</td><td>~4.000 €</td><td>Kostenschätzung, Seite 9</td></tr>
            <tr class="total-row"><td>Summe (Standardannahme)</td><td>~9.700 €</td><td>&nbsp;</td></tr>
          </tbody>
        </table>
      </div>
      <div class="kennzahlen-grid" style="margin-top:0.75rem">
        <div class="kennzahl"><strong>{STD:.0f} h</strong><span>gesparte Zeit / Jahr</span></div>
        <div class="kennzahl"><strong>{eur(SPAR)}</strong><span>Ersparnis / Jahr</span></div>
        <div class="kennzahl"><strong>26,5</strong><span>Monate bis amortisiert</span></div>
        <div class="kennzahl"><strong>{eur(SPAR*5-9700)}</strong><span>netto nach 5 Jahren</span></div>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Das Ergebnis in einem Satz:</strong> Die Investition von 9.700 € ist nach rund
        26 Monaten bezahlt; danach spart der Arbeitsplatz jährlich 4.400 €.
      </div>
    </section>

    <section>
      <h2>📉 Amortisation je Bauvariante</h2>
      <p>
        Die Werkzeugkosten sind bei allen Varianten gleich &ndash; nur die Werkbank unterscheidet
        sich. Damit lässt sich zeigen, wie stark die Variantenwahl auf die Amortisation
        durchschlägt:
      </p>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Variante</th><th>Werkbank</th><th>Gesamt (+ 5.742 € Werkzeug)</th><th>Amortisation</th><th>entspricht</th></tr></thead>
          <tbody>
            {var_rows}
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Was die Zahlen wirklich sagen:</strong> Zwischen der teuersten und der günstigsten
        Variante liegen rund 12 Monate Amortisationsdauer. Das klingt viel &ndash; ist es aber
        nicht: Alle vier Varianten sind in deutlich unter drei Jahren bezahlt, bei einer
        Nutzungsdauer von 10 bis 20 Jahren. Die Wirtschaftlichkeit trägt damit <em>jede</em>
        Variante; sie ist kein Ausschlusskriterium, sondern bestätigt nur, dass die Investition
        insgesamt sinnvoll ist. Beim Eigenbau kommt hinzu, dass die Bauzeit hier gar nicht
        eingerechnet ist &ndash; die 18,8 Monate sind also zu günstig gerechnet.
      </div>
    </section>

    <section>
      <h2>🎚️ Wie empfindlich ist die Rechnung?</h2>
      <p>
        Die unsicherste Annahme ist die gesparte Suchzeit. Deshalb dieselbe Rechnung mit
        verschiedenen Werten, Investition konstant bei 9.700 €:
      </p>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Gesparte Zeit / Person / Tag</th><th>Stunden / Jahr</th><th>Ersparnis / Jahr</th><th>Amortisation</th></tr></thead>
          <tbody>
            {sz_rows}
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Robustes Ergebnis:</strong> Selbst im vorsichtigsten Fall &ndash; nur 5 Minuten
        gesparte Suchzeit pro Person und Tag &ndash; ist die Investition nach gut vier Jahren
        bezahlt. Die Aussage „lohnt sich" hängt also nicht an einer optimistischen Annahme. Das ist
        wichtiger als der exakte Wert, denn 10 Minuten sind eine Schätzung, keine Messung.
      </div>
    </section>

    <section>
      <h2>➕ Weiterer Nutzen &ndash; nicht in Euro gerechnet</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>Weniger Fehler und Ausschuss</strong>Ordnung und das passende Werkzeug am richtigen Platz senken die Fehlerquote &ndash; jedes vermiedene Ausschussteil spart Material und Maschinenzeit.</span></li>
        <li><span><strong>Weniger Werkzeugverlust und Doppelkäufe</strong>Am Shadow-Board fällt ein fehlendes Teil sofort auf, statt Monate später beim Nachbestellen.</span></li>
        <li><span><strong>Mehr Arbeitssicherheit</strong>Feste Plätze und freie Wege &ndash; der direkte Bezug zur Gefährdungsbeurteilung auf Seite 11.</span></li>
        <li><span><strong>Schnelleres Einarbeiten</strong>Neue Mitarbeiter finden sich in einem beschrifteten Platz ohne Erklärung zurecht.</span></li>
      </ul>
      <p style="margin-top:0.75rem">
        Diese Punkte bewusst nicht in Euro umgerechnet: Jede Zahl dafür wäre frei erfunden. Sie
        gehören trotzdem in die Entscheidung &ndash; sie machen den berechneten Nutzen zur
        Untergrenze, nicht zum Gesamtwert.
      </p>
    </section>

{projekt_nav("09-nutzwertanalyse.html", "Nutzwertanalyse & Empfehlung", "11-arbeitssicherheit.html", "Arbeitssicherheit")}
  </main>
"""

write_page("10-wirtschaftlichkeit.html", "Projekt 7: Wirtschaftlichkeit & Amortisation", body)
