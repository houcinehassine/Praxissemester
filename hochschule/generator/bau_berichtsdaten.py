# -*- coding: utf-8 -*-
"""Stellt die Daten für bau_bericht.js als JSON bereit."""
import os, sys, json
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
from berichtstexte import BERICHTE

# Der Zeitraum je Bericht wird aus den tatsaechlichen Phasengrenzen gelesen
# (bau_nachweis.py schreibt sie nach zeitraeume.json), damit Bericht und
# Taetigkeitsnachweis nicht auseinanderlaufen.
PHASEN_JE_BERICHT = {
 1: ["ExcelLagersystem", "CloudAnwendung"],
 2: ["Schweissarbeitsplatz"],
 3: ["Schweisstisch"],
 4: ["Schweisswagen"],
 5: ["Zerspanarbeitsplatz"],
}
_spanne = json.load(open(os.path.join(HIER, "zeitraeume.json"), encoding="utf-8"))

def zeitraum(nr):
    tage = [t for name in PHASEN_JE_BERICHT[nr] for t in _spanne[name]]
    von, bis = min(tage), max(tage)
    d = lambda x: f"{x[8:10]}.{x[5:7]}.{x[0:4]}"
    return f"{d(von)} – {d(bis)}"

# Bildunterschrift, Datei (repo-relativ) - nur echte, vorhandene Bilder aus den
# Projektordnern bzw. dem Montage-Ordner. Projekt 3 (Web-Anwendung) und Projekt 4
# (Schweißarbeitsplatz) haben keine Bilder in der Website hinterlegt und bleiben
# deshalb ohne Abbildungen - besser keine als erfundene.
ABBILDUNGEN = {
 1: [("Dashboard des Lagerbestand-Systems mit Barcode-Eingabe, Suchergebnis und Exportbereich",
      "projekte/projekt-2/img/design-dashboard.jpg"),
     ("Tablet-Modus für die Bedienung an der Maschine",
      "projekte/projekt-2/img/tablet-modus.jpg"),
     ("Verlaufsprotokoll mit Zeitstempel und Mengenänderung",
      "projekte/projekt-2/img/verlauf-testdaten.jpg")],
 2: [],
 3: [("3D-Modell des Schweißtisches im Gesamtzusammenbau",
      "projekte/projekt-5/img/grundkonzept-3d-modell.png"),
     ("Lochplatten-Spannsystem auf dem Tischrahmen",
      "projekte/projekt-5/img/lochplatten-auf-rahmen.png"),
     ("Zeichnungsblatt des Endstands mit Schriftfeld",
      "projekte/projekt-5/img/endstand-blatt1-15-17april.jpg")],
 4: [("Vorhandener Schweißwagen im Betrieb",
      "projekte/projekt-6/img/ist-wagen-foto1.jpg"),
     ("Handskizze mit dem Aufmaß von Gerät und Gasflasche",
      "projekte/projekt-6/img/ist-handskizze-aufmass.jpg"),
     ("Gewähltes Wagenkonzept mit Gasflaschenhalterung und mehreren Ablagen",
      "projekte/projekt-6/img/zusatzwagen-v2-mit-bestandswagen.jpg"),
     ("Zeichnungsblatt der Gesamtbaugruppe mit Stückliste",
      "projekte/projekt-6/img/zeichnung-blatt21-gesamtbaugruppe.jpg")],
 5: [("Vier untersuchte Bauvarianten der Werkbank im Vergleich",
      "hochschule/generator/berichtsbilder/zerspan-vier-varianten.png"),
     ("Gewähltes Layout-Konzept mit den Zonen A, B und C",
      "projekte/projekt-7/img/konzept2-3d-zonen.png"),
     ("Maßstäblicher Werkstatt-Grundriss",
      "projekte/projekt-7/img/werkstatt-grundriss.png")],
}

daten = {
 "dateiname": "Hassine_3399727_Bericht",
 "student": {"anrede": "Herr", "vorname": "Houcine", "name": "Hassine",
             "studiengruppe": "PA6", "matrikelnummer": "3399727",
             "email": "houcine1.hassine@hs-regensburg.de"},
 "betrieb": {"name": "Mechanische Werkstätte Schmidt e.K.",
             "anschrift": "Stiftstraße 20, 93343 Essing"},
 "betreuer": {"anrede": "Herr", "vorname": "Amin", "name": "Halloul",
              "email": "⟨E-Mail Betreuer eintragen⟩", "telefon": "⟨Telefon Betreuer eintragen⟩"},
 "berichte": [
   {"titel": b["titel"], "zeitraum": zeitraum(i + 1), "absaetze": b["absaetze"],
    "abbildungen": [{"nr": j + 1, "text": txt, "datei": datei}
                    for j, (txt, datei) in enumerate(ABBILDUNGEN[i + 1])]}
   for i, b in enumerate(BERICHTE)],
}
ziel = os.path.join(HIER, "berichtsdaten.json")
json.dump(daten, open(ziel, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("geschrieben:", ziel, "|", len(daten["berichte"]), "Berichte,",
      sum(len(b["abbildungen"]) for b in daten["berichte"]), "Abbildungsplätze")
