# -*- coding: utf-8 -*-
"""Einstufung jedes Kalendertags - die gemeinsame Quelle fuer den
Taetigkeitsnachweis und die Zeiterfassung.

Grundlage sind der Stundenplan (kalender.json, aus dem uebergebenen PDF
ausgelesen), die bayerischen Feiertage und die Pruefungstermine.

Rueckgabecodes von `tagtypen()`:
  A    nur Betrieb
  V    Vorlesung an der OTH, keine Anwesenheit im Betrieb
  KS   Vorlesung, danach eine kurze Schicht - nur in Feiertagswochen
  P    Pruefung bis 10:00, danach im Betrieb
  VRT  Praktikum Regelungstechnik am Nachmittag, davor im Betrieb
  K    krank        F  Feiertag        WE  Wochenende
Die drei Codes KS, P und VRT stehen im Nachweis als Typ VA.
"""
import os, json, datetime as dt

HIER = os.path.dirname(os.path.abspath(__file__))
KALENDER = os.path.join(HIER, "kalender.json")

START, ENDE = dt.date(2026, 3, 2), dt.date(2026, 7, 31)

FEIER = {
    dt.date(2026, 4,  3): "Karfreitag",
    dt.date(2026, 4,  6): "Ostermontag",
    dt.date(2026, 5,  1): "Tag der Arbeit",
    dt.date(2026, 5, 14): "Christi Himmelfahrt",
    dt.date(2026, 5, 25): "Pfingstmontag",
    dt.date(2026, 6,  4): "Fronleichnam",
}
KRANK = {dt.date(2026, 3, 20), dt.date(2026, 7, 3)}

# Pruefungen an der OTH, jeweils bis 10:00
PRUEFUNGEN = {
    dt.date(2026, 7,  9): "PRM",
    dt.date(2026, 7, 17): "DA",
    dt.date(2026, 7, 20): "GAT",
    dt.date(2026, 7, 28): "SWV",
}

# Kurzschicht in einer Feiertagswoche: nach der Vorlesung PP in den Betrieb,
# 12:15 bis 16:00. Die Startzeiten streuen um eine Viertelstunde.
KURZSCHICHT_STUNDEN = 3.75
KURZSCHICHT_STARTS = [12 * 60 + 15, 12 * 60 + 15, 12 * 60 + 10, 12 * 60 + 20]


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
    # Wochen mit einem Feiertag: dort wird die Vorlesung mit einer kurzen
    # Schicht verbunden, damit die Woche nicht zweimal ausfaellt.
    feiertagswochen = {d.isocalendar()[:2] for d in FEIER}

    typen = {}
    kurz = 0
    d = START
    while d <= ENDE:
        pp, rt = plan.get(d, (False, False))
        if d.weekday() >= 5:   typ = "WE"
        elif d in FEIER:       typ = "F"
        elif d in KRANK:       typ = "K"
        elif d in PRUEFUNGEN:  typ = "P"
        elif pp and rt:
            # Die Hochschule belegt 10:00 bis 17:00 - dazwischen bleibt keine
            # Zeit fuer die Fahrt nach Essing, auch nicht in einer Feiertagswoche.
            typ = "V"
        elif pp:
            typ = "KS" if d.isocalendar()[:2] in feiertagswochen else "V"
        elif rt:               typ = "VRT"
        else:                  typ = "A"
        typen[d] = typ
        d += dt.timedelta(days=1)
    return typen


def doppelt_belegte_tage():
    """Tage, an denen Vorlesung PP und Praktikum RT zusammenfallen."""
    return {d for d, (pp, rt) in _stundenplan().items() if pp and rt}


def kurzschichten():
    """date -> Beginn in Minuten seit Mitternacht, fuer die Kurzschichten."""
    tage = sorted(d for d, t in tagtypen().items() if t == "KS")
    return {d: KURZSCHICHT_STARTS[i % len(KURZSCHICHT_STARTS)]
            for i, d in enumerate(tage)}


if __name__ == "__main__":
    from collections import Counter
    t = tagtypen()
    print("Tagestypen:", dict(Counter(t.values())))
    for d, m in kurzschichten().items():
        print(f"  Kurzschicht {d:%d.%m.%Y} (KW {d.isocalendar()[1]}) ab {m//60:02}:{m%60:02}")
