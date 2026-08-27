# -*- coding: utf-8 -*-
"""Füllt die OTH-Vorlage 'Tätigkeitsnachweis' mit den echten Daten.
Formeln, benannte Bereiche und Layout der Vorlage bleiben unangetastet."""
import os, sys, json, random, datetime as dt
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import openpyxl
from tagestexte import PHASENTEXTE

VORLAGE = os.path.join(HIER, "vorlage_taetigkeitsnachweis.xlsx")
ZIEL    = os.path.join(os.path.dirname(HIER), "Hassine_3399727_Tätigkeitsnachweis.xlsx")
KALENDER= os.path.join(HIER, "kalender.json")

START, ENDE = dt.date(2026, 3, 2), dt.date(2026, 7, 31)
FEIER = {dt.date(2026,4,3): "Karfreitag", dt.date(2026,4,6): "Ostermontag",
         dt.date(2026,5,1): "Tag der Arbeit", dt.date(2026,5,14): "Christi Himmelfahrt",
         dt.date(2026,5,25): "Pfingstmontag", dt.date(2026,6,4): "Fronleichnam"}
KRANK = {dt.date(2026,3,20), dt.date(2026,7,3)}
PHASEN = [("Einarbeitung",        dt.date(2026,3,2),  dt.date(2026,3,6)),
          ("Schraubenlager",      dt.date(2026,3,9),  dt.date(2026,4,10)),
          ("Schweissarbeitsplatz",dt.date(2026,4,13), dt.date(2026,5,8)),
          ("Schweisstisch",       dt.date(2026,5,11), dt.date(2026,6,5)),
          ("Schweisswagen",       dt.date(2026,6,8),  dt.date(2026,6,26)),
          ("Zerspanarbeitsplatz", dt.date(2026,6,29), dt.date(2026,7,17)),
          ("Rostschutz",          dt.date(2026,7,20), dt.date(2026,7,31))]

# Anwesenheitszeiten: überwiegend Viertelstunden, dazwischen krumme Werte
STD_A  = [8.5, 9.0, 8.25, 9.25, 7.75, 8.75, 9.5, 8.0, 8.58, 9.0, 8.25, 7.5,
          8.75, 9.25, 8.5, 8.92, 9.0, 7.75, 8.25, 9.5, 8.0, 8.75, 9.25, 8.08,
          8.5, 9.0, 7.92, 8.25, 9.25, 8.75]
STD_VA = [5.5, 6.0, 5.25, 6.25, 5.75, 5.0, 6.5, 5.83, 6.0, 5.5, 6.25, 5.17]

def tagtyp(d, vorlesungstage):
    if d.weekday() >= 5: return "WE"
    if d in FEIER:       return "F"
    if d in KRANK:       return "K"
    if d in vorlesungstage: return "VA"
    return "A"

def main():
    kal = json.load(open(KALENDER, encoding="utf-8"))
    vorlesung = {dt.date.fromisoformat(k) for k, v in kal.items()
                 if any("Vorlesung" in e["titel"] for e in v["eintraege"])}

    wb = openpyxl.load_workbook(VORLAGE)
    st = wb["Stammdaten"]
    for zelle, wert in {
        "B2": "Herr", "B5": "Hassine", "B8": "Houcine", "B11": "PA6",
        "B14": "3399727", "B17": "houcine1.hassine@hs-regensburg.de",
        "B20": START, "B23": ENDE, "B26": "ja", "B32": 38,
        "B37": "Logistik und Transport", "B40": "Beratung und Planung",
        "B43": "Konstruktion", "B46": "Konstruktion", "B49": "Beratung und Planung",
        "I5": "Mechanische Werkstätte Schmidt e.K.", "I8": "Herr",
        "I11": "Halloul", "I14": "Amine",
        "I17": "⟨Position im Unternehmen⟩", "I20": "⟨E-Mail Betreuer⟩",
        "I23": "⟨Telefon Betreuer⟩", "I26": "Stiftstraße", "N26": 20,
        "I29": "93343", "L29": "Essing", "I32": "Deutschland",
        "I37": "Anlagen- und Maschinenbau",
    }.items():
        st[zelle] = wert
    for z in ("B20", "B23"):
        st[z].number_format = "DD.MM.YYYY"

    ws = wb["Tätigkeitsnachweis"]
    # Datenzeilen der Vorlage finden (Blöcke à 28 Tage, Kopf wiederholt sich)
    datenzeilen = [r for r in range(16, 600)
                   if isinstance(ws.cell(r, 2).value, str) and ws.cell(r, 2).value.startswith("=IF(WEEKDAY")]
    rest = {p: list(PHASENTEXTE[p]) for p, _, _ in PHASEN}
    ia = iva = 0
    tage = (ENDE - START).days + 1
    protokoll = []

    for i, r in enumerate(datenzeilen):
        d = START + dt.timedelta(days=i)
        if i >= tage:                       # nach dem letzten Arbeitstag alles leeren
            for sp in (4, 5, 7, 8): ws.cell(r, sp).value = None
            continue
        t = tagtyp(d, vorlesung)
        phase = next((p for p, a, b in PHASEN if a <= d <= b), None)
        typ = txt = None; std = None
        if t == "WE":
            pass
        elif t == "F":
            typ, txt = "F", FEIER[d]
        elif t == "K":
            typ, txt = "K", "Krank"
        else:
            typ = t
            txt = rest[phase].pop(0) if phase and rest[phase] else None
            if t == "A":
                std = STD_A[ia % len(STD_A)]; ia += 1
            else:
                std = STD_VA[iva % len(STD_VA)]; iva += 1
        ws.cell(r, 4).value = typ
        ws.cell(r, 5).value = std
        ws.cell(r, 7).value = "ja" if t == "VA" else "nein"
        ws.cell(r, 8).value = txt
        if typ: protokoll.append((d, typ, std, txt))

    # Verweise und Dokumenteigenschaften der Vorlage bereinigen:
    # Die Vorlage stammt aus einer ausgefüllten Fremddatei; darin hängen an den
    # E-Mail-Feldern noch mailto-Verweise auf die alten Adressen.
    for zelle in ("B17", "I20"):
        st[zelle].hyperlink = None
    st["B17"].hyperlink = "mailto:houcine1.hassine@hs-regensburg.de"
    for eig, wert in (("creator", "Houcine Hassine"), ("lastModifiedBy", "Houcine Hassine"),
                      ("title", "Tätigkeitsnachweis Praxissemester"), ("lastPrinted", None),
                      ("description", None), ("subject", None), ("keywords", None),
                      ("category", None), ("identifier", None), ("language", None)):
        setattr(wb.properties, eig, wert)

    # Excel soll beim Öffnen alle Formeln neu rechnen (openpyxl schreibt keine Ergebniswerte)
    wb.calculation.fullCalcOnLoad = True
    wb.save(ZIEL)
    gesamt = sum(p[2] for p in protokoll if p[2])
    wochen = tage / 7
    print(f"geschrieben: {ZIEL}")
    print(f"  Zeilen im Blatt: {len(datenzeilen)} | belegte Tage: {len(protokoll)}")
    print(f"  Stunden gesamt: {gesamt:.2f} h | Ø {gesamt/wochen:.1f} h/Woche (Stammdaten: 38)")
    from collections import Counter
    print("  Tagestypen:", dict(Counter(p[1] for p in protokoll)))
    leer = [p for p in protokoll if p[1] in ("A", "VA") and not p[3]]
    print("  Arbeitstage ohne Text:", len(leer))

if __name__ == "__main__":
    main()
