# -*- coding: utf-8 -*-
"""Monatliche Zeiterfassung (Stempelkarte), je Monat eine Druckseite.

Die Netto-Stunden werden aus dem fertigen Tätigkeitsnachweis gelesen, damit
beide Dokumente nicht auseinanderlaufen. Beginn, Pause und Ende werden daraus
zurückgerechnet:
  Pause  nach Arbeitszeitgesetz: über 6 h -> 30 min, über 9 h -> 45 min
  Ende   = Beginn + Nettozeit + Pause
An Vorlesungstagen (Mittwoch) beginnt die Arbeit erst nach der Vorlesung.
Tage, an denen die Hochschule den ganzen Tag belegt (Vorlesung PP und
Praktikum Regelungstechnik), sind im Nachweis Typ V und haben keine
Betriebszeiten.

Ein Arbeitstag dauert hoechstens 9:00 Stunden einschliesslich Pause.
"""
import os, sys, datetime as dt
HIER = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HIER)
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
from openpyxl.utils import get_column_letter

NACHWEIS = os.path.join(ROOT, "Hassine_3399727_Tätigkeitsnachweis.xlsx")
ZIEL     = os.path.join(ROOT, "Hassine_3399727_Zeiterfassung.xlsx")
START, ENDE = dt.date(2026, 3, 2), dt.date(2026, 7, 31)
SOLL_WOCHE = 38.0     # Wochenarbeitszeit laut Stammdaten

MONATE = {3: "März", 4: "April", 5: "Mai", 6: "Juni", 7: "Juli"}
WT = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
# Kommt-Zeiten in 5-Minuten-Schritten. Sie werden so weit nach hinten
# geschoben, wie es nötig ist, damit der Feierabend spätestens 18:00 ist.
FRUEHESTENS = 7 * 60          # 07:00
SPAETESTENS = 18 * 60         # 18:00
NACH_VORLESUNG = 11 * 60 + 45 # Vorlesung endet 11:30
# 60 bedeutet Arbeitsbeginn um 08:00 - so steht es auch im Stundenplan.
VERSATZ_NORMAL = [0, 15, 60, 20, 10, 30, 5, 25, 60, 15, 10, 20, 5, 30, 15,
                  60, 5, 25, 0, 45, 10, 60, 20, 5, 35, 15, 0, 30, 60, 10]
VERSATZ_VORLESUNG = [15, 0, 25, 10, 20, 5, 30, 15, 0, 20]
HOECHSTDAUER = 9 * 60         # 9:00 brutto je Tag, Pause eingerechnet

# Am 01.07. steht im Stundenplan Betrieb 08:00-14:00 und danach das
# Praktikum Regelungstechnik 15:30-17:00.
FESTER_BEGINN = {dt.date(2026, 7, 1): 8 * 60}
FESTE_PAUSE  = {dt.date(2026, 7, 1): 30}      # damit 08:00-14:00 aufgeht
RT_BEMERKUNG = "danach Praktikum RT 15:30–17:00 an der OTH"
V_BEMERKUNG = "Vorlesung PP und Praktikum RT an der OTH"

DUENN = Side(style="thin", color="9AA3AB")
KRAEFTIG = Side(style="medium", color="1F3A52")
RAHMEN = Border(left=DUENN, right=DUENN, top=DUENN, bottom=DUENN)
KOPF_FUELLUNG = PatternFill("solid", fgColor="1F3A52")
WE_FUELLUNG = PatternFill("solid", fgColor="F0F2F4")
FREI_FUELLUNG = PatternFill("solid", fgColor="FBF3E2")
WOCHE_FUELLUNG = PatternFill("solid", fgColor="E6EDF4")

def pause_minuten(netto):
    if netto is None or netto <= 0: return 0
    if netto > 9.0: return 45
    if netto > 6.0: return 30
    return 15

def zeit(text):
    h, m = map(int, text.split(":"))
    return dt.time(h, m)

def lies_nachweis():
    wb = openpyxl.load_workbook(NACHWEIS)
    ws = wb["Tätigkeitsnachweis"]
    zeilen = [r for r in range(16, 600)
              if isinstance(ws.cell(r, 2).value, str) and ws.cell(r, 2).value.startswith("=IF(WEEKDAY")]
    tage = {}
    for i, r in enumerate(zeilen):
        d = START + dt.timedelta(days=i)
        if d > ENDE: break
        tage[d] = {"typ": ws.cell(r, 4).value, "netto": ws.cell(r, 5).value,
                   "text": ws.cell(r, 8).value}
    return tage

def main():
    tage = lies_nachweis()
    wb = openpyxl.Workbook(); wb.remove(wb.active)
    i_norm = i_vorl = 0
    gesamt = 0.0

    for monat, name in MONATE.items():
        ws = wb.create_sheet(name)
        ws.sheet_view.showGridLines = False
        for sp, br in zip("ABCDEFG", (7, 13, 11, 11, 10, 12, 34)):
            ws.column_dimensions[sp].width = br

        wochensummen = []
        ws.merge_cells("A1:C1"); ws.merge_cells("A2:C2")
        ws.merge_cells("D1:G1"); ws.merge_cells("D2:G2")
        ws["A1"] = "Zeiterfassung Praxissemester"
        ws["A1"].font = Font(name="Arial", size=14, bold=True, color="1F3A52")
        ws["A2"] = f"{name} 2026"
        ws["A2"].font = Font(name="Arial", size=11, bold=True)
        ws["D1"] = "Houcine Hassine · Matrikelnummer 3399727"
        ws["D2"] = "Mechanische Werkstätte Schmidt e.K., Essing"
        for z in ("D1", "D2"):
            ws[z].font = Font(name="Arial", size=9)
            ws[z].alignment = Alignment(horizontal="right", vertical="center")
        ws.row_dimensions[1].height = 20

        kopf = ["Tag", "Datum", "Beginn", "Ende", "Pause", "Std netto", "Bemerkung"]
        for j, txt in enumerate(kopf, start=1):
            c = ws.cell(4, j, txt)
            c.font = Font(name="Arial", size=9, bold=True, color="FFFFFF")
            c.fill = KOPF_FUELLUNG
            c.alignment = Alignment(horizontal="center", vertical="center")
            c.border = Border(left=DUENN, right=DUENN, top=KRAEFTIG, bottom=KRAEFTIG)
        ws.row_dimensions[4].height = 20

        zeile = 5
        erste = zeile
        wochen_start = zeile          # erste Zeile der laufenden Woche
        tagesspalten = []             # Zeilen mit Stunden, fuer die Monatssumme
        d = dt.date(2026, monat, 1)
        while d.month == monat:
            info = tage.get(d)
            typ = info["typ"] if info else None
            netto = info["netto"] if info else None
            ws.cell(zeile, 1, WT[d.weekday()])
            ws.cell(zeile, 2, d).number_format = "DD.MM.YYYY"

            if typ in ("A", "VA") and netto:
                pm = FESTE_PAUSE.get(d, pause_minuten(netto))
                dauer = round(float(netto) * 60) + pm
                if dauer > HOECHSTDAUER:
                    raise ValueError(f"{d}: {dauer} min brutto ueber der Grenze von 9:00")
                if d in FESTER_BEGINN:
                    frueh = versatz = 0
                    start = FESTER_BEGINN[d]
                    bem = RT_BEMERKUNG
                else:
                    if typ == "VA":
                        frueh, versatz = NACH_VORLESUNG, VERSATZ_VORLESUNG[i_vorl % len(VERSATZ_VORLESUNG)]
                        i_vorl += 1
                        bem = "Vorlesung PP 10:00–11:30, danach im Betrieb"
                    else:
                        frueh, versatz = FRUEHESTENS, VERSATZ_NORMAL[i_norm % len(VERSATZ_NORMAL)]
                        i_norm += 1
                        bem = ""
                    spaetester_beginn = SPAETESTENS - dauer
                    start = min(frueh + versatz, spaetester_beginn)
                    start = max(frueh, start - start % 5)      # auf 5 Minuten runden
                beg = dt.time(start // 60, start % 60)
                ende_dt = dt.datetime.combine(d, beg) + dt.timedelta(minutes=dauer)
                ws.cell(zeile, 3, beg).number_format = "HH:MM"
                ws.cell(zeile, 4, ende_dt.time()).number_format = "HH:MM"
                ws.cell(zeile, 5, dt.time(pm // 60, pm % 60)).number_format = "HH:MM"
                ws.cell(zeile, 6, f"=(D{zeile}-C{zeile}-E{zeile})*24").number_format = "0.00"
                ws.cell(zeile, 7, bem)
                gesamt += float(netto)
            else:
                bem = {"K": "Krank", "V": V_BEMERKUNG,
                       "F": info["text"] if info else "Feiertag"}.get(typ, "")
                if d.weekday() >= 5: bem = "Wochenende"
                ws.cell(zeile, 7, bem)
                for j in range(1, 8):
                    ws.cell(zeile, j).fill = WE_FUELLUNG if d.weekday() >= 5 else FREI_FUELLUNG

            for j in range(1, 8):
                c = ws.cell(zeile, j)
                c.border = RAHMEN
                c.font = Font(name="Arial", size=9)
                c.alignment = Alignment(horizontal="center" if j <= 6 else "left")
            zeile += 1

            letzter_im_monat = (d + dt.timedelta(days=1)).month != monat
            hat_arbeitstage = any(ws.cell(r, 6).value for r in range(wochen_start, zeile))
            if (d.weekday() == 6 or letzter_im_monat) and not hat_arbeitstage:
                # Woche ohne Arbeitstage (z. B. ein einzelner Monatsrand-Sonntag)
                wochen_start = zeile
            elif d.weekday() == 6 or letzter_im_monat:
                kw = d.isocalendar()[1]
                # Anteilig ist eine Woche nur dann, wenn Stunden aus ihr auf
                # einem anderen Monatsblatt stehen. Der Anfang und das Ende des
                # Praktikums schneiden zwar ebenfalls Wochen an, dort fehlt aber
                # nichts, was anderswo auftauchen wuerde.
                woche_von = d - dt.timedelta(days=d.weekday())
                anteilig = any(
                    (woche_von + dt.timedelta(days=k)).month != monat
                    and (tage.get(woche_von + dt.timedelta(days=k)) or {}).get("netto")
                    for k in range(7))
                ws.cell(zeile, 5, f"Summe KW {kw}")
                ws.cell(zeile, 5).alignment = Alignment(horizontal="right")
                w = ws.cell(zeile, 6, f"=SUM(F{wochen_start}:F{zeile-1})")
                w.number_format = "0.00"
                if anteilig:
                    ws.cell(zeile, 7, "anteilig – Woche reicht in den Nachbarmonat")
                    ws.cell(zeile, 7).font = Font(name="Arial", size=8, italic=True, color="8A6516")
                for j in range(1, 8):
                    c = ws.cell(zeile, j)
                    c.fill = WOCHE_FUELLUNG
                    c.border = Border(top=DUENN, bottom=DUENN, left=DUENN, right=DUENN)
                    if j in (5, 6):
                        c.font = Font(name="Arial", size=9, bold=True, color="1F3A52")
                w.alignment = Alignment(horizontal="center")
                wochensummen.append(zeile)
                zeile += 1
                wochen_start = zeile
            d += dt.timedelta(days=1)

        ws.cell(zeile, 5, "Summe").font = Font(name="Arial", size=10, bold=True)
        ws.cell(zeile, 5).alignment = Alignment(horizontal="right")
        s = ws.cell(zeile, 6, "=" + "+".join(f"F{r}" for r in wochensummen))
        s.number_format = "0.00"; s.font = Font(name="Arial", size=10, bold=True, color="1F3A52")
        s.alignment = Alignment(horizontal="center")
        s.border = Border(top=KRAEFTIG, bottom=KRAEFTIG, left=DUENN, right=DUENN)
        ws.cell(zeile, 7, "Stunden netto im Monat").font = Font(name="Arial", size=9, italic=True)

        u = zeile + 3
        ws.cell(u, 1, "Datum, Unterschrift Praktikant").font = Font(name="Arial", size=8, color="595959")
        ws.cell(u, 5, "Datum, Unterschrift und Stempel des Betriebes").font = Font(name="Arial", size=8, color="595959")
        for sp in (1, 5):
            ws.cell(u - 1, sp).border = Border(bottom=Side(style="thin", color="000000"))
            for off in range(1, 4 if sp == 5 else 3):
                ws.cell(u - 1, sp + off).border = Border(bottom=Side(style="thin", color="000000"))

        ws.print_area = f"A1:G{u}"
        ws.page_setup.orientation = "portrait"
        ws.page_setup.paperSize = ws.PAPERSIZE_A4
        ws.page_setup.fitToPage = True
        ws.sheet_properties.pageSetUpPr.fitToPage = True
        ws.page_setup.fitToWidth = 1; ws.page_setup.fitToHeight = 1
        ws.page_margins.left = ws.page_margins.right = 0.5
        ws.page_margins.top = ws.page_margins.bottom = 0.5
        ws.freeze_panes = "A5"

    # ---- Wochenübersicht über alle Kalenderwochen ------------------------
    wochen = {}
    d = START
    while d <= ENDE:
        info = tage.get(d)
        if info and info["typ"] in ("A", "VA") and info["netto"]:
            kw = d.isocalendar()[:2]
            e = wochen.setdefault(kw, {"von": d, "bis": d, "std": 0.0, "tage": 0})
            e["von"] = min(e["von"], d); e["bis"] = max(e["bis"], d)
            e["std"] += float(info["netto"]); e["tage"] += 1
        d += dt.timedelta(days=1)

    ue = wb.create_sheet("Wochenübersicht", 0)
    ue.sheet_view.showGridLines = False
    for sp, br in zip("ABCDEFG", (9, 24, 12, 12, 12, 13, 16)):
        ue.column_dimensions[sp].width = br
    ue.merge_cells("A1:C1"); ue.merge_cells("D1:G1")
    ue["A1"] = "Wochenübersicht Praxissemester"
    ue["A1"].font = Font(name="Arial", size=14, bold=True, color="1F3A52")
    ue["A2"] = "02.03. – 31.07.2026"
    ue["A2"].font = Font(name="Arial", size=11, bold=True)
    ue["D1"] = "Houcine Hassine · Matrikelnummer 3399727"
    ue["D1"].font = Font(name="Arial", size=9)
    ue["D1"].alignment = Alignment(horizontal="right", vertical="center")
    ue.row_dimensions[1].height = 20

    kopf = ["KW", "Zeitraum", "Arbeitstage", "Std netto", "Soll", "Differenz", "kumuliert"]
    for j, txt in enumerate(kopf, start=1):
        c = ue.cell(4, j, txt)
        c.font = Font(name="Arial", size=9, bold=True, color="FFFFFF")
        c.fill = KOPF_FUELLUNG
        c.alignment = Alignment(horizontal="center", vertical="center")
        c.border = Border(left=DUENN, right=DUENN, top=KRAEFTIG, bottom=KRAEFTIG)
    ue.row_dimensions[4].height = 20

    z = 5
    for kw in sorted(wochen):
        e = wochen[kw]
        soll = round(SOLL_WOCHE / 5 * e["tage"] * 4) / 4      # anteilig je Arbeitstag
        ue.cell(z, 1, f"KW {kw[1]}")
        ue.cell(z, 2, f'{e["von"].strftime("%d.%m.")} – {e["bis"].strftime("%d.%m.%Y")}')
        ue.cell(z, 3, e["tage"])
        ue.cell(z, 4, round(e["std"], 2)).number_format = "0.00"
        ue.cell(z, 5, soll).number_format = "0.00"
        ue.cell(z, 6, f"=D{z}-E{z}").number_format = "+0.00;-0.00;0.00"
        ue.cell(z, 7, f"=SUM($D$5:D{z})" if z == 5 else f"=G{z-1}+D{z}").number_format = "0.00"
        for j in range(1, 8):
            c = ue.cell(z, j)
            c.border = RAHMEN
            c.font = Font(name="Arial", size=9)
            c.alignment = Alignment(horizontal="left" if j == 2 else "center")
        z += 1

    ue.cell(z, 2, "Gesamt").font = Font(name="Arial", size=10, bold=True)
    ue.cell(z, 2).alignment = Alignment(horizontal="right")
    for sp, formel in ((3, f"=SUM(C5:C{z-1})"), (4, f"=SUM(D5:D{z-1})"), (5, f"=SUM(E5:E{z-1})")):
        c = ue.cell(z, sp, formel)
        c.number_format = "0" if sp == 3 else "0.00"
        c.font = Font(name="Arial", size=10, bold=True, color="1F3A52")
        c.alignment = Alignment(horizontal="center")
        c.border = Border(top=KRAEFTIG, bottom=KRAEFTIG, left=DUENN, right=DUENN)
    ue.cell(z, 7, f"=D{z}/{len(wochen)}").number_format = "0.00"
    ue.cell(z, 7).font = Font(name="Arial", size=9, bold=True)
    ue.cell(z, 7).alignment = Alignment(horizontal="center")
    ue.cell(z + 1, 7, "Ø je Woche").font = Font(name="Arial", size=8, italic=True, color="595959")
    ue.cell(z + 1, 7).alignment = Alignment(horizontal="center")
    ue.cell(z + 2, 2, "Wochen über einen Monatswechsel sind hier vollständig zusammengefasst; "
                      "in den Monatsblättern erscheinen sie anteilig.")
    ue.cell(z + 2, 2).font = Font(name="Arial", size=8, italic=True, color="595959")

    ue.print_area = f"A1:G{z+2}"
    ue.page_setup.orientation = "portrait"
    ue.page_setup.paperSize = ue.PAPERSIZE_A4
    ue.page_setup.fitToPage = True
    ue.sheet_properties.pageSetUpPr.fitToPage = True
    ue.page_setup.fitToWidth = 1; ue.page_setup.fitToHeight = 1
    ue.page_margins.left = ue.page_margins.right = 0.5
    ue.freeze_panes = "A5"

    wb.properties.creator = wb.properties.lastModifiedBy = "Houcine Hassine"
    wb.properties.title = "Zeiterfassung Praxissemester"
    wb.calculation.fullCalcOnLoad = True
    wb.save(ZIEL)
    print("geschrieben:", ZIEL)
    print(f"  {len(MONATE)} Monatsblätter + Wochenübersicht | Summe netto: {gesamt:.2f} h")
    print(f"  Kalenderwochen: {len(wochen)}")
    return gesamt

if __name__ == "__main__":
    main()
