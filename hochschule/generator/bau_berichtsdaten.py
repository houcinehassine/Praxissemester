# -*- coding: utf-8 -*-
"""Stellt die Daten für bau_bericht.js als JSON bereit."""
import os, sys, json
HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
from berichtstexte import BERICHTE

ABBILDUNGEN = {
 1: [("Ausgangszustand des Schraubenlagers vor der Neuordnung", "Foto aus der Werkstatt"),
     ("CAD-Konstruktion der Sichtlagerkästen in den Größen S, M und L", "Screenshot aus dem CAD"),
     ("Belegungsplan der Regalfächer", "Scan oder Foto des Belegungsplans")],
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
   {"titel": b["titel"], "zeitraum": b["zeitraum"], "absaetze": b["absaetze"],
    "abbildungen": [{"nr": j + 1, "text": txt, "hinweis": hin}
                    for j, (txt, hin) in enumerate(ABBILDUNGEN[i + 1])]}
   for i, b in enumerate(BERICHTE)],
}
ziel = os.path.join(HIER, "berichtsdaten.json")
json.dump(daten, open(ziel, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("geschrieben:", ziel, "|", len(daten["berichte"]), "Berichte,",
      sum(len(b["abbildungen"]) for b in daten["berichte"]), "Abbildungsplätze")
