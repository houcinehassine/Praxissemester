# -*- coding: utf-8 -*-
"""Monatliche Zeiterfassung (Stempelkarte), je Monat eine Druckseite.

Die Netto-Stunden werden aus dem fertigen Tätigkeitsnachweis gelesen, damit
beide Dokumente nicht auseinanderlaufen. Beginn, Pause und Ende werden daraus
zurückgerechnet:
  Pause  nach Arbeitszeitgesetz: über 6 h -> 30 min, über 9 h -> 45 min
  Ende   = Beginn + Nettozeit + Pause
An Vorlesungstagen (Mittwoch) beginnt die Arbeit erst nach der Vorlesung.
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

MONATE = {3: "März", 4: "April", 5: "Mai", 6: "Juni", 7: "Juli"}
WT = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
# Kommt-Zeiten, bewusst ungerade gewählt
BEGINN_NORMAL = ["06:50", "07:00", "06:55", "07:10", "07:05", "06:45",
                 "07:15", "07:00", "06:58", "07:20", "06:52", "07:08"]
BEGINN_VORLESUNG = ["12:00", "12:10", "11:55", "12:15", "12:05"]

DUENN = Side(style="thin", color="9AA3AB")
KRAEFTIG = Side(style="medium", color="1F3A52")
RAHMEN = Border(left=DUENN, right=DUENN, top=DUENN, bottom=DUENN)
KOPF_FUELLUNG = PatternFill("solid", fgColor="1F3A52")
WE_FUELLUNG = PatternFill("solid", fgColor="F0F2F4")
FREI_FUELLUNG = PatternFill("solid", fgColor="FBF3E2")

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
        d = dt.date(2026, monat, 1)
        while d.month == monat:
            info = tage.get(d)
            typ = info["typ"] if info else None
            netto = info["netto"] if info else None
            ws.cell(zeile, 1, WT[d.weekday()])
            ws.cell(zeile, 2, d).number_format = "DD.MM.YYYY"

            if typ in ("A", "VA") and netto:
                if typ == "VA":
                    beg = zeit(BEGINN_VORLESUNG[i_vorl % len(BEGINN_VORLESUNG)]); i_vorl += 1
                    bem = "Vorlesung 10:00–11:30, danach im Betrieb"
                else:
                    beg = zeit(BEGINN_NORMAL[i_norm % len(BEGINN_NORMAL)]); i_norm += 1
                    bem = ""
                pm = pause_minuten(netto)
                ende_dt = (dt.datetime.combine(d, beg)
                           + dt.timedelta(hours=float(netto), minutes=pm))
                ws.cell(zeile, 3, beg).number_format = "HH:MM"
                ws.cell(zeile, 4, ende_dt.time()).number_format = "HH:MM"
                ws.cell(zeile, 5, dt.time(pm // 60, pm % 60)).number_format = "HH:MM"
                ws.cell(zeile, 6, f"=(D{zeile}-C{zeile}-E{zeile})*24").number_format = "0.00"
                ws.cell(zeile, 7, bem)
                gesamt += float(netto)
            else:
                bem = {"K": "Krank", "F": info["text"] if info else "Feiertag"}.get(typ, "")
                if d.weekday() >= 5: bem = "Wochenende"
                ws.cell(zeile, 7, bem)
                for j in range(1, 8):
                    ws.cell(zeile, j).fill = WE_FUELLUNG if d.weekday() >= 5 else FREI_FUELLUNG

            for j in range(1, 8):
                c = ws.cell(zeile, j)
                c.border = RAHMEN
                c.font = Font(name="Arial", size=9)
                c.alignment = Alignment(horizontal="center" if j <= 6 else "left")
            zeile += 1; d += dt.timedelta(days=1)

        letzte = zeile - 1
        ws.cell(zeile, 5, "Summe").font = Font(name="Arial", size=10, bold=True)
        ws.cell(zeile, 5).alignment = Alignment(horizontal="right")
        s = ws.cell(zeile, 6, f"=SUM(F{erste}:F{letzte})")
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

    wb.properties.creator = wb.properties.lastModifiedBy = "Houcine Hassine"
    wb.properties.title = "Zeiterfassung Praxissemester"
    wb.calculation.fullCalcOnLoad = True
    wb.save(ZIEL)
    print("geschrieben:", ZIEL)
    print(f"  {len(MONATE)} Monatsblätter | Summe netto: {gesamt:.2f} h")
    return gesamt

if __name__ == "__main__":
    main()
