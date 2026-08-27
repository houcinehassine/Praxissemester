# -*- coding: utf-8 -*-
import os, sys, re
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
from _k13 import P1, P2, P3
from _k4 import P4
from _k56 import P5, P6
from _k7 import P7

KOEPFE = [
 ("01", "Schraubenlager &ndash; Ordnungssystem", "Lager &amp; Organisation", "M&auml;rz &ndash; April 2026",
  "entscheidungsreif", "warten", P1),
 ("02", "Lagerbestand-System in Excel", "Lager &amp; Organisation", "22.04. &ndash; 14.08.2026",
  "im Einsatz", "fertig", P2),
 ("03", "Lagersystem als Web-Anwendung", "Lager &amp; Organisation", "Stand 16.08.2026",
  "in Betrieb", "fertig", P3),
 ("04", "Schwei&szlig;arbeitsplatz &ndash; Gesamtplanung", "Schwei&szlig;arbeitsplatz", "Verfahren: E-Hand &amp; MAG/MIG",
  "Planung abgeschlossen", "warten", P4),
 ("05", "Schwei&szlig;tisch &ndash; Konstruktion", "Schwei&szlig;arbeitsplatz", "M&auml;rz &ndash; April 2026 &middot; gepr&uuml;ft MW Schmidt",
  "fertigungsreif", "bereit", P5),
 ("06", "Schwei&szlig;maschinenwagen", "Schwei&szlig;arbeitsplatz", "02.03. &ndash; 31.07.2026 &middot; gepr&uuml;ft MW Schmidt",
  "fertigungsreif", "bereit", P6),
 ("07", "Zerspanarbeitsplatz", "Zerspanung", "08.06. &ndash; 11.09.2026",
  "entscheidungsreif", "warten", P7),
]

bloecke = ""
uebersicht = ""
inhalt = ""
for nr, titel, bereich, zeit, status, cls, korpus in KOEPFE:
    aid = f"p{nr}"
    bloecke += f"""  <article class="blatt" id="{aid}">
    <header class="schriftfeld">
      <span class="schriftfeld-nr mono">{nr}</span>
      <div class="schriftfeld-titel">
        <h3>{titel}</h3>
        <p class="mono">{bereich} &middot; {zeit}</p>
      </div>
      <span class="marke marke--{cls}">{status}</span>
    </header>
{korpus}  </article>

"""
    uebersicht += (f'<tr><td class="mono">{nr}</td><td><a href="#{aid}">{titel}</a></td>'
                   f'<td>{bereich}</td><td><span class="marke marke--{cls}">{status}</span></td></tr>\n')
    # Unterabschnitte je Projekt fürs Inhaltsverzeichnis
    unter = re.findall(r'<h4>(?:\d+\s*&middot;\s*)?([^<]+)</h4>', korpus)
    unter = [u for u in unter if u not in ("Aufgabe", "Nutzen f&uuml;r den Betrieb")][:12]
    punkte = "".join(f"<li>{u}</li>" for u in unter)
    inhalt += (f'<div class="iv-block"><a class="iv-kopf" href="#{aid}">'
               f'<span class="mono">{nr}</span> {titel}</a><ul>{punkte}</ul></div>\n')

open(os.path.join(HIER, "_montage.py"), "w", encoding="utf-8").write(
    "BLOECKE = " + repr(bloecke) + "\nUEBERSICHT = " + repr(uebersicht) + "\nINHALT = " + repr(inhalt) + "\n")
print("montiert:", len(bloecke), "| Tabellen gesamt:", bloecke.count("<table>"), "| Bilder:", bloecke.count("<figure"))
