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

ABBILDUNGEN = {
 1: [("Dashboard des Lagerbestand-Systems mit Barcode-Eingabe, Suchergebnis und Exportbereich", "Screenshot aus Excel"),
     ("Tablet-Modus für die Bedienung an der Maschine", "Screenshot aus Excel"),
     ("Verlaufsprotokoll mit Zeitstempel und Mengenänderung", "Screenshot aus Excel"),
     ("Oberfläche der Web-Anwendung", "Screenshot der Anwendung")],
 2: [("Bestehender Schweißarbeitsplatz vor der Planung", "Foto aus der Werkstatt"),
     ("Gewähltes Layout-Konzept des Schweißarbeitsplatzes", "Skizze oder CAD-Ansicht"),
     ("Werkzeugwand mit Schattenbrett", "Foto oder Entwurf")],
 3: [("3D-Modell des Schweißtisches im Gesamtzusammenbau", "Screenshot aus dem CAD"),
     ("Lochplatten-Spannsystem auf dem Tischrahmen", "Screenshot aus dem CAD"),
     ("Zeichnungsblatt des Endstands mit Schriftfeld", "Ausschnitt aus dem Zeichnungssatz")],
 4: [("Vorhandener Schweißwagen im Betrieb", "Foto aus der Werkstatt"),
     ("Handskizze mit dem Aufmaß von Gerät und Gasflasche", "Foto der Skizze"),
     ("Gewähltes Konzept: modularer Aufbau in vier Etagen", "Screenshot aus dem CAD"),
     ("Zeichnungsblatt der Gesamtbaugruppe mit Stückliste", "Ausschnitt aus dem Zeichnungssatz")],
 5: [("Vier Bauvarianten der Werkbank im Vergleich", "3D-Darstellungen"),
     ("Gewähltes Layout-Konzept mit den Zonen A, B und C", "3D-Darstellung"),
     ("Maßstäblicher Werkstatt-Grundriss", "Zeichnung der Draufsicht")],
}

daten = {
 "dateiname": "Hassine_3399727_Bericht",
 "student": {"anrede": "Herr", "vorname": "Houcine", "name": "Hassine",
             "studiengruppe": "PA6", "matrikelnummer": "3399727",
             "email": "houcine1.hassine@hs-regensburg.de"},
 "betrieb": {"name": "Mechanische Werkstätte Schmidt e.K.",
             "anschrift": "Stiftstraße 20, 93343 Essing"},
 "betreuer": {"anrede": "Herr", "vorname": "Amine", "name": "Halloul",
              "email": "⟨E-Mail Betreuer eintragen⟩", "telefon": "⟨Telefon Betreuer eintragen⟩"},
 "berichte": [
   {"titel": b["titel"], "zeitraum": zeitraum(i + 1), "absaetze": b["absaetze"],
    "abbildungen": [{"nr": j + 1, "text": txt, "hinweis": hin}
                    for j, (txt, hin) in enumerate(ABBILDUNGEN[i + 1])]}
   for i, b in enumerate(BERICHTE)],
}
ziel = os.path.join(HIER, "berichtsdaten.json")
json.dump(daten, open(ziel, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("geschrieben:", ziel, "|", len(daten["berichte"]), "Berichte,",
      sum(len(b["abbildungen"]) for b in daten["berichte"]), "Abbildungsplätze")
