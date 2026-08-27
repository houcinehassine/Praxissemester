# -*- coding: utf-8 -*-
import re

# Verweise auf Seitenzahlen der Website in Verweise auf Abschnitte dieses Berichts umschreiben
ERSATZ = [
  # Projekt 3
  ("</code>, siehe Seite 12) sorgt seither", "</code>) sorgt seither"),
  # Projekt 4
  ("Lochwand + Schränke, voller Werkzeugsatz (5S)</td><td>Seiten 7&ndash;10",
   "Lochwand + Schränke, voller Werkzeugsatz (5S)</td><td>Abschnitt 5"),
  ("Rohmaterial &amp; Reste, getrennt</td><td>Seite 10",
   "Rohmaterial &amp; Reste, getrennt</td><td>Abschnitt 5"),
  ("Feuerlöscher, Erste Hilfe, Beleuchtung</td><td>Seite 11",
   "Feuerlöscher, Erste Hilfe, Beleuchtung</td><td>Abschnitt 7"),
  ("Kaufteile-Station (Seiten 7&ndash;10)",
   "Kaufteile-Station (Abschnitt 5)"),
  ("Werkzeuge &amp; Ausrüstung (Konzeptphase, Seite 4)",
   "Werkzeuge &amp; Ausrüstung (Konzeptphase, Abschnitt 2)"),
  # Projekt 7 – Spalte „Bearbeitet auf“ der Teilaufgaben-Tabelle
  ("<th>Bearbeitet auf</th>", ""),
  ("<td>Seiten 3&ndash;4</td>", ""),
  ("<td>Seiten 6, 8</td>", ""),
  ("<td>Seiten 5, 12</td>", ""),
  ("<td>Seite 7</td>", ""),
  ("<td>Seiten 9&ndash;10</td>", ""),
  # Projekt 7 – Fließtext in Tabellen
  ("Deshalb die Nutzwertanalyse (Seite 9) und die Amortisationsrechnung (Seite 10):",
   "Deshalb die Nutzwertanalyse (Abschnitt 7) und die Amortisationsrechnung (Abschnitt 8):"),
  ("regelmäßiges Audit (Checkliste auf Seite 12)",
   "regelmäßiges Audit (Checkliste in Abschnitt 10)"),
  ("Gefährdungsbeurteilung auf Seite 11 ist unmittelbar.",
   "Gefährdungsbeurteilung in Abschnitt 9 ist unmittelbar."),
  ("aus den Rahmenbedingungen (Seite 2)", "aus den Rahmenbedingungen dieses Projekts"),
  ("bepreiste Werkzeugliste, Seite 4", "bepreiste Werkzeugliste, Abschnitt 2"),
  ("Kostenschätzung, Seite 9", "Kostenschätzung, Abschnitt 7"),
  ("Lasten trägt (≥ 500 kg, Seite 6)", "Lasten trägt (≥ 500 kg, Abschnitt 4)"),
  ("Anforderung aus Seite 6, bisher", "Anforderung aus Abschnitt 4, bisher"),
]

def umschreiben(html):
    offen = []
    for alt, neu in ERSATZ:
        if alt in html:
            html = html.replace(alt, neu)
        else:
            offen.append(alt[:55])
    rest = re.findall(r'[^<>]{0,25}Seite[n]?\s*\d[^<]{0,25}', re.sub(r'<[^>]+>', ' ', html))
    return html, offen, rest
