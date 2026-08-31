# -*- coding: utf-8 -*-
"""Nettostunden je Tag.

Alle Werte sind Vielfache von 0,25 h. Nur so ist beides zugleich glatt:
der Dezimalwert (8,25) und die Uhrzeit (8:15). Bei 5-Minuten-Schritten wie
8:05 waere der Dezimalwert 8,0833 und liesse sich nicht sauber anzeigen.

Die reinen Betriebstage (Typ A) folgen den drei Abschnitten aus
hochschultage.py:

  Startphase 02.03.-13.03.
      Einarbeitung, jeden Tag 9 bis 10 Stunden.

  Sammelphase 16.03.-12.06.
      Grundlast 7,25 bis 7,75 h. Dazu bekommt jeder Monat vier laengere
      Tage, um Stunden vorzuarbeiten: zweimal 8,00 h und zweimal zwischen
      9 und 10 h. Sie liegen ueber den Monat verteilt.

  Pruefungsphase ab 15.06.
      Feierabend spaetestens 15:00, also hoechstens 7,50 h netto. Der Rest
      des Tages geht in die Pruefungsvorbereitung.

Die Tage mit Vorlesung, Praktikum oder Pruefung haben feste Zeitfenster;
ihre Stunden stehen in hochschultage.FENSTER.

Obergrenze: 10,00 h netto am Tag - mehr laesst das Arbeitszeitgesetz auch
im Ausnahmefall nicht zu (§ 3 ArbZG).
"""
import os, sys, datetime as dt
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hochschultage import (STARTPHASE_ENDE, PRUEFUNGSPHASE_START,
                           abschnitt, tagtypen, zeitfenster)

HOECHSTNETTO = 10.00

# Startphase: zehn Arbeitstage, 9 bis 10 Stunden
STARTPHASE = [9.50, 9.75, 9.25, 10.00, 9.50, 9.25, 9.75, 9.00, 9.50, 9.75]

# Sammelphase: Grundlast und die vier laengeren Tage je Monat
SAMMEL_GRUND = [7.25, 7.50, 7.75, 7.50]
SAMMEL_EXTRA = [8.00, 9.75, 8.00, 9.25]
SAMMEL_LAGE  = (0.15, 0.35, 0.60, 0.85)   # relative Lage im Monat

# Pruefungsphase: hoechstens 7,50 h, damit um 15:00 Schluss ist
PRUEFUNGSPHASE = [7.50, 7.25, 7.00, 7.50, 6.75, 7.25, 7.50, 7.00]


def _reihe(werte, muster):
    return {d: muster[i % len(muster)] for i, d in enumerate(sorted(werte))}


def stunden_je_tag():
    """date -> Nettostunden, fuer jeden Tag mit Anwesenheit im Betrieb."""
    typen = tagtypen()
    aus = {}

    # Tage mit festem Zeitfenster (Vorlesung, Praktikum, Pruefung)
    for d, (beginn, ende, pause) in zeitfenster().items():
        aus[d] = (ende - beginn - pause) / 60

    a_tage = sorted(d for d, c in typen.items() if c == "A")
    aus.update(_reihe([d for d in a_tage if abschnitt(d) == "Start"], STARTPHASE))
    aus.update(_reihe([d for d in a_tage if abschnitt(d) == "Pruefung"], PRUEFUNGSPHASE))

    # Sammelphase monatsweise, damit jeder Monat seine vier langen Tage bekommt
    for monat in sorted({d.month for d in a_tage if abschnitt(d) == "Sammel"}):
        tage = [d for d in a_tage if abschnitt(d) == "Sammel" and d.month == monat]
        lage = {int(len(tage) * f): v for f, v in zip(SAMMEL_LAGE, SAMMEL_EXTRA)}
        grund = 0
        for i, d in enumerate(tage):
            if i in lage:
                aus[d] = lage[i]
            else:
                aus[d] = SAMMEL_GRUND[grund % len(SAMMEL_GRUND)]
                grund += 1

    zuviel = {d: h for d, h in aus.items() if h > HOECHSTNETTO}
    if zuviel:
        raise ValueError(f"ueber der Grenze von {HOECHSTNETTO} h: {zuviel}")
    return aus


def stunden(datum):
    return stunden_je_tag()[datum]


if __name__ == "__main__":
    import collections
    werte = stunden_je_tag()
    typen = tagtypen()
    MON = {3: "März", 4: "April", 5: "Mai", 6: "Juni", 7: "Juli"}
    mon = collections.defaultdict(list)
    for d, h in werte.items():
        mon[d.month].append(h)
    print(f"{'Monat':7} {'Tage':>5} {'Summe':>8} {'Ø':>6}")
    for m in sorted(mon):
        a = mon[m]
        print(f"{MON[m]:7} {len(a):5} {sum(a):8.2f} {sum(a)/len(a):6.2f}")
    ges = sum(werte.values())
    print(f"{'Gesamt':7} {len(werte):5} {ges:8.2f} {ges/len(werte):6.2f}"
          f"   -> Ø {ges/22:.2f} h je Kalenderwoche")
    for name in ("Start", "Sammel", "Pruefung"):
        a = [werte[d] for d, c in typen.items() if c == "A" and abschnitt(d) == name]
        print(f"  A-Tage {name:9} {len(a):3} Tage  {min(a):.2f}–{max(a):.2f}  Ø {sum(a)/len(a):.2f}")
