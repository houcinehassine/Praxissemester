# -*- coding: utf-8 -*-
"""Einstufung jedes Kalendertags - die gemeinsame Quelle fuer den
Taetigkeitsnachweis und die Zeiterfassung.

Grundlage sind der Stundenplan (kalender.json, aus dem uebergebenen PDF
ausgelesen), die bayerischen Feiertage und die Pruefungstermine.

Rueckgabecodes von `tagtypen()`:
  A     nur Betrieb
  PP    Vormittags im Betrieb, ab 10:00 Vorlesung PP bis 13:15 an der OTH,
        danach keine Rueckkehr mehr in den Betrieb
  PPRT  Vorlesung PP und Praktikum RT - nur der Vormittag im Betrieb
  VRT   nur Praktikum RT am Nachmittag, davor im Betrieb (01.07.)
  P     Pruefung bis 10:00, danach im Betrieb
  K     krank        F  Feiertag        WE  Wochenende
Die vier Codes PP, PPRT, VRT und P stehen im Nachweis als Typ VA.

Der Zeitraum zerfaellt in drei Abschnitte:
  Startphase     02.03.-13.03.  lange Tage zum Einarbeiten (9 bis 10 h)
  Sammelphase    16.03.-12.06.  Grundlast, dazu je Monat vier laengere Tage
  Pruefungsphase ab 15.06.      Feierabend spaetestens 15:00, Zeit zum Lernen
"""
import os, json, datetime as dt

HIER = os.path.dirname(os.path.abspath(__file__))
KALENDER = os.path.join(HIER, "kalender.json")

START, ENDE = dt.date(2026, 3, 2), dt.date(2026, 7, 31)
STARTPHASE_ENDE      = dt.date(2026, 3, 13)   # Ende der ersten zwei Wochen
PRUEFUNGSPHASE_START = dt.date(2026, 6, 15)   # zweite Junihaelfte und Juli
PRUEFUNGSPHASE_ENDE  = 15 * 60                # ab dann taeglich um 15:00 Schluss

FEIER = {
    dt.date(2026, 4,  3): "Karfreitag",
    dt.date(2026, 4,  6): "Ostermontag",
    dt.date(2026, 5,  1): "Tag der Arbeit",
    dt.date(2026, 5, 14): "Christi Himmelfahrt",
    dt.date(2026, 5, 25): "Pfingstmontag",
    dt.date(2026, 6,  4): "Fronleichnam",
}
KRANK = {dt.date(2026, 3, 20), dt.date(2026, 7, 3)}

# Vorlesungsfreie Tage laut Semesterkalender der OTH Regensburg (SoSe 2026),
# die im ausgelesenen Stundenplan (kalender.json) faelschlich noch einen
# Vorlesungstermin fuehren. An diesen Tagen entfaellt die Vorlesung, es wird
# ganz normal im Betrieb gearbeitet (Typ A statt PP/PPRT/VRT).
VORLESUNGSFREI = {
    dt.date(2026, 4, 8),   # Mittwoch der Osterwoche, laut Semesterkalender vorlesungsfrei
}

# Einzelne ausgefallene Vorlesungstermine - kein amtlicher vorlesungsfreier
# Tag, sondern eine einzelne abgesagte Veranstaltung (durchgestrichener
# Termin im Stundenplan der App). An diesen Tagen wurde ganz normal im
# Betrieb gearbeitet (Typ A statt PP/PPRT/VRT).
ENTFALLENE_VORLESUNGEN = {
    dt.date(2026, 3, 18),   # Vorlesung PP ausgefallen, laut Screenshot der Stundenplan-App
}

# Pruefungen an der OTH, jeweils bis 10:00
PRUEFUNGEN = {
    dt.date(2026, 7,  9): "PRM",
    dt.date(2026, 7, 17): "DA",
    dt.date(2026, 7, 20): "GAT",
    dt.date(2026, 7, 28): "SWV",
}

# Feste Zeitfenster (Beginn, Ende, Pause) in Minuten seit Mitternacht.
# An PP-Tagen wird nur vormittags gearbeitet: Beginn 07:00, um 09:30 Feierabend
# im Betrieb fuer die Fahrt zur Vorlesung PP (10:00-13:15 an der OTH); danach
# keine Rueckkehr mehr in den Betrieb (Angabe des Studierenden).
FENSTER = {
    "PP":      (7 * 60,  9 * 60 + 30, 0),       # 07:00-09:30, dann zur Vorlesung
    "PPRT":    (7 * 60,  9 * 60 + 30, 0),       # nur der Vormittag
    "VRT":     (8 * 60, 14 * 60, 0),            # laut Stundenplan 08:00-14:00
    "P":      (11 * 60, 15 * 60, 0),            # nach der Pruefung
}


def _stundenplan():
    """date -> (Vorlesung PP?, Praktikum RT?) aus kalender.json."""
    kal = json.load(open(KALENDER, encoding="utf-8"))
    plan = {}
    for k, v in kal.items():
        titel = [e["titel"] for e in v["eintraege"]]
        pp = any("PP" in t for t in titel)
        rt = any("RT" in t for t in titel)
        if pp or rt:
            plan[dt.date.fromisoformat(k)] = (pp, rt)
    return plan


def tagtypen():
    """date -> Code, fuer jeden Tag des Praktikumszeitraums."""
    plan = _stundenplan()
    typen = {}
    d = START
    while d <= ENDE:
        pp, rt = plan.get(d, (False, False))
        if d in VORLESUNGSFREI or d in ENTFALLENE_VORLESUNGEN:
            pp, rt = False, False
        if d.weekday() >= 5:   typ = "WE"
        elif d in FEIER:       typ = "F"
        elif d in KRANK:       typ = "K"
        elif d in PRUEFUNGEN:  typ = "P"
        elif pp and rt:        typ = "PPRT"
        elif pp:               typ = "PP"
        elif rt:               typ = "VRT"
        else:                  typ = "A"
        typen[d] = typ
        d += dt.timedelta(days=1)
    return typen


def zeitfenster():
    """date -> (Beginn, Ende, Pause) in Minuten, fuer alle Tage mit festem Ablauf."""
    aus = {}
    for d, typ in tagtypen().items():
        if typ in FENSTER:
            aus[d] = FENSTER[typ]
    return aus


def abschnitt(d):
    """Start-, Sammel- oder Pruefungsphase."""
    if d <= STARTPHASE_ENDE:          return "Start"
    if d < PRUEFUNGSPHASE_START:      return "Sammel"
    return "Pruefung"


if __name__ == "__main__":
    from collections import Counter
    t = tagtypen()
    print("Tagestypen:", dict(Counter(t.values())))
    print("A-Tage je Abschnitt:",
          dict(Counter(abschnitt(d) for d, c in t.items() if c == "A")))
    for d, (b, e, p) in sorted(zeitfenster().items()):
        print(f"  {d:%d.%m.%Y} {t[d]:5} {b//60:02}:{b%60:02}-{e//60:02}:{e%60:02} "
              f"Pause {p:3} min -> {(e-b-p)/60:.2f} h")
