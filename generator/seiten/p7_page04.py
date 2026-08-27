# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt7 import *
from collections import OrderedDict

ITEMS = [
 ('Drehen','Drehmeißel-Satz (Schrupp/Schlicht/Stech/Innen)',1,'Satz',180),
 ('Drehen','Wendeschneidplatten + Halter',1,'Sort.',320),
 ('Drehen','Bohrfutter + Bohrersatz HSS',1,'Satz',95),
 ('Drehen','Zentrierbohrer-Satz',1,'Satz',35),
 ('Drehen','Gewindeschneidzeug (Schneideisen)',1,'Satz',120),
 ('Drehen','Mitlaufende Körnerspitze',1,'Stk',65),
 ('Drehen','Drehmeißel-Einstelllehre',1,'Stk',25),
 ('Fräsen','Schaftfräser-Satz HSS/VHM',1,'Sort.',260),
 ('Fräsen','Walzenstirnfräser / Messerkopf',2,'Stk',140),
 ('Fräsen','Bohrersatz + Zentrierbohrer',1,'Satz',90),
 ('Fräsen','Gewindebohrer-Satz + Windeisen',1,'Satz',110),
 ('Fräsen','Spannzangen / Fräsdorne',1,'Satz',240),
 ('Fräsen','Kantentaster / 3D-Taster',1,'Stk',130),
 ('Spannen','Maschinenschraubstock',1,'Stk',280),
 ('Spannen','Spanneisen / Pratzen-Satz',1,'Satz',95),
 ('Spannen','Vierbackenfutter + Futterschlüssel',1,'Stk',210),
 ('Spannen','Parallelunterlagen-Satz',1,'Satz',70),
 ('Spannen','Teilapparat / Rundtisch (optional)',1,'Stk',450),
 ('Messen','Messschieber digital 150 mm',3,'Stk',45),
 ('Messen','Bügelmessschraube (Mikrometer)',2,'Stk',85),
 ('Messen','Messuhr + Magnetstativ',2,'Set',70),
 ('Messen','Anschlagwinkel / Haarwinkel',2,'Stk',30),
 ('Messen','Radien- &amp; Fühlerlehren',2,'Satz',25),
 ('Messen','Gewindelehren / Lehrdorne',1,'Satz',90),
 ('Nacharbeit','Entgratwerkzeug + Klingen',3,'Stk',22),
 ('Nacharbeit','Feilen-Satz',2,'Satz',55),
 ('Nacharbeit','Schleifleinen / Schmirgel',1,'Sort.',40),
 ('Nacharbeit','Handbürste / Drahtbürste',3,'Stk',8),
 ('Nacharbeit','Gewinde-Nachschneider-Satz',1,'Satz',60),
 ('Hilfsmittel','Handwerkzeug-Grundsatz',3,'Satz',120),
 ('Hilfsmittel','Drehmomentschlüssel',1,'Stk',90),
 ('Hilfsmittel','Kühlschmierstoff / Schneidöl',1,'Gebinde',45),
 ('Hilfsmittel','Spänehaken + Handfeger + Schaufel',1,'Set',30),
 ('Hilfsmittel','PSA (Brille, Gehörschutz, Handschuhe)',3,'Satz',40),
 ('Hilfsmittel','Werkstattwagen / Ablage',1,'Stk',180),
]

def eur(n):
    return f"{n:,.0f}".replace(",", ".") + " €"

cat = OrderedDict()
for c, n, q, u, p in ITEMS:
    cat.setdefault(c, [0, 0])
    cat[c][0] += 1
    cat[c][1] += q * p
netto = sum(v[1] for v in cat.values())
mwst = netto * 0.19
brutto = netto + mwst

# Kategorie-Übersicht
kat_rows = ""
for c, (n, s) in cat.items():
    anteil = s / netto * 100
    kat_rows += f'<tr><td>{c}</td><td>{n}</td><td>{eur(s)}</td><td>{anteil:.1f} %</td></tr>\n            '
kat_rows += f'<tr class="total-row"><td>Gesamt</td><td>{len(ITEMS)}</td><td>{eur(netto)}</td><td>100 %</td></tr>'

# Vollständige Liste
rows = ""
last = None
for c, n, q, u, p in ITEMS:
    kat = c if c != last else "&nbsp;"
    last = c
    rows += f'<tr><td>{kat}</td><td>{n}</td><td>{q}</td><td>{u}</td><td>{eur(p)}</td><td>{eur(q*p)}</td></tr>\n            '

# Teuerste Positionen
top = sorted(ITEMS, key=lambda x: -x[2]*x[4])[:6]
top_rows = ""
for c, n, q, u, p in top:
    top_rows += f'<tr><td>{n}</td><td>{c}</td><td>{q} × {eur(p)}</td><td>{eur(q*p)}</td></tr>\n            '

body = seiten_kopf(4, "Bepreiste Werkzeugliste",
    "Dieselben 35 Positionen &ndash; jetzt mit Menge, Einzelpreis und Gesamtsumme. Diese Zahl ist "
    "die Grundlage für die Wirtschaftlichkeitsrechnung auf Seite 10.") + f"""
  <main class="projekt-detail">

    <section>
      <div class="kennzahlen-grid">
        <div class="kennzahl"><strong>{eur(netto)}</strong><span>netto</span></div>
        <div class="kennzahl"><strong>{eur(mwst)}</strong><span>MwSt. 19 %</span></div>
        <div class="kennzahl"><strong>{eur(brutto)}</strong><span>brutto</span></div>
        <div class="kennzahl"><strong>{len(ITEMS)}</strong><span>Positionen</span></div>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Wichtiger Vorbehalt zu allen Preisen:</strong> Es handelt sich um Netto-Richtwerte
        aus einer Marktrecherche des deutschen Handels &ndash; um Größenordnungen, nicht um
        Angebote. Werkbank und Maschinen sind hier nicht enthalten; sie kommen auf Seite 10 dazu.
        Vor einer Beschaffung sind alle Werte durch reale Angebote zu ersetzen.
      </div>
    </section>

    <section>
      <h2>📊 Verteilung nach Kategorien</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Kategorie</th><th>Positionen</th><th>Summe netto</th><th>Anteil</th></tr></thead>
          <tbody>
            {kat_rows}
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Was die Verteilung zeigt:</strong> Fräsen und Spannen machen zusammen knapp die
        Hälfte der Werkzeugkosten aus &ndash; Fräswerkzeuge und Spannmittel sind schlicht teurer als
        Drehmeißel. Die Nacharbeit ist mit 300 € die günstigste Gruppe, obwohl sie im Alltag
        ständig gebraucht wird. Genau diese Gruppe verdient in der 5S-Ordnung besondere
        Aufmerksamkeit: geringe Kosten, hohe Nutzungshäufigkeit &ndash; also konsequent in Zone A.
      </div>
    </section>

    <section>
      <h2>💰 Die sechs teuersten Positionen</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Position</th><th>Kategorie</th><th>Rechnung</th><th>Summe</th></tr></thead>
          <tbody>
            {top_rows}
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">
        Diese sechs Positionen machen zusammen rund ein Drittel der Werkzeugkosten aus. Beim
        Teilapparat (450 €) ist die Anschaffung ausdrücklich als optional gekennzeichnet &ndash;
        er ist der erste Kandidat, wenn das Budget doch begrenzt wird. Der Handwerkzeug-Grundsatz
        (3 × 120 €) ist dagegen nicht kürzbar: Er ist der Grund, warum niemand auf den Satz des
        Kollegen warten muss.
      </p>
    </section>

    <section>
      <h2>🧾 Vollständige Liste &ndash; alle {len(ITEMS)} Positionen</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Kategorie</th><th>Werkzeug</th><th>Menge</th><th>Einh.</th><th>Einzel</th><th>Gesamt</th></tr></thead>
          <tbody>
            {rows}<tr class="total-row"><td colspan="5">Summe netto</td><td>{eur(netto)}</td></tr>
            <tr><td colspan="5">zzgl. 19 % MwSt.</td><td>{eur(mwst)}</td></tr>
            <tr class="total-row"><td colspan="5">Summe brutto</td><td>{eur(brutto)}</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>🔍 Was in dieser Summe noch nicht steckt</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>Die Werkbank selbst</strong>Je nach Variante 1.150 bis 5.500 € &ndash; siehe Kostenschätzung auf Seite 9.</span></li>
        <li><span><strong>Die Maschinen</strong>Dreh- und Fräsmaschine sind vorhanden und nicht Teil der Investition.</span></li>
        <li><span><strong>Verbrauch im laufenden Betrieb</strong>Wendeschneidplatten, Schleifleinen und KSS werden nachgekauft; hier steckt nur die Erstausstattung drin.</span></li>
        <li><span><strong>Montage- und Bauzeit</strong>Bei Variante 4 (Eigenbau) der größte versteckte Posten &ndash; auf Seite 9 als Zusatzaufwand bewertet.</span></li>
        <li><span><strong>Beschriftung und Shadow-Board</strong>Schaumeinlagen, Etiketten und Haken für die 5S-Ordnung &ndash; kleiner Betrag, aber einzuplanen.</span></li>
      </ul>
    </section>

{projekt_nav("03-werkzeugbedarf.html", "Werkzeugbedarf", "05-5s-ordnung.html", "5S-Ordnung & Zonen")}
  </main>
"""

write_page("04-kostenliste.html", "Projekt 7: Bepreiste Werkzeugliste", body)
