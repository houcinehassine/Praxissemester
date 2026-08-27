# Hochschulunterlagen — Pflichtabgabe Praxissemester

Zwei Dateien für die Abgabe über GRIPS, erzeugt in der Form der OTH-Vorlagen.

| Datei | Inhalt |
|---|---|
| `Hassine_3399727_Tätigkeitsnachweis.xlsx` | Täglicher Nachweis, 02.03.–31.07.2026 |
| `Hassine_3399727_Bericht.docx` | Die fünf Tätigkeitsberichte |
| `Hassine_3399727_Bericht.pdf` | Nur zur Ansicht — abgegeben wird die .docx |

Die Dateinamen entsprechen der Vorgabe aus dem Reiter „Anleitung" der Excel-Vorlage
(`NAME_MATRIKELNUMMER_…`). Bitte nicht umbenennen.

## Noch einzutragen

Drei Felder konnte ich nicht füllen. Sie stehen in beiden Dateien als `⟨…⟩`:

- Position bzw. Funktion von Amine Halloul im Unternehmen
- E-Mail des Betreuers
- Telefonnummer des Betreuers

Im Excel stehen sie auf dem Blatt **Stammdaten** in `I17`, `I20` und `I23` — von dort
ziehen alle Kopfzeilen des Nachweises automatisch nach. Im Word stehen sie im Block
„Angaben Ausbildungsbetrieb".

## Grundlage der Tagesdaten

Der Nachweis folgt dem Schichtkalender (`generator/kalender.json`, aus dem übergebenen
PDF ausgelesen):

- **86 Tage** Typ `A` (anwesend), 7,5–9,5 h
- **16 Tage** Typ `VA` (Vorlesung und anwesend) — alle Mittwoch, 5–6,5 h Betrieb,
  Vorlesung „PP" 10:00–11:30. Die ersten beiden Mittwoche (04.03., 11.03.) sind `A`,
  da die Vorlesungen erst am 18.03. beginnen.
- **2 Tage** Typ `K` — 20.03. und 03.07.
- **6 Tage** Typ `F` — Karfreitag, Ostermontag, Tag der Arbeit, Christi Himmelfahrt,
  Pfingstmontag, Fronleichnam

Summe **831,8 h** auf 21,7 Wochen = **38,3 h/Woche**, stimmig zu den 38 h in den Stammdaten.

Die erste Woche (02.–06.03.) ist bewusst Einarbeitung: Sicherheitsunterweisung,
Betriebsrundgang, Maschinen und Abläufe kennenlernen, Arbeitsplatz einrichten. Die
Projektarbeit beginnt am 09.03.

## Zeitliche Zuordnung der Projekte

Der **Tagesnachweis dokumentiert alle Projekte**, der Word-Bericht nur fünf davon.

| Thema | Zeitraum | Tage | im Word-Bericht |
|---|---|---|---|
| Einarbeitung | 02.03. – 06.03. | 5 | — |
| Material- und Schraubenlager (5S) | 02.03. – 10.04. | 25 | Bericht 1 |
| Lagerbestand-System in Excel/VBA | ab 22.04., parallel | 15 | — |
| Schweißarbeitsplatz | 13.04. – 08.05. | 16 | Bericht 2 |
| Schweißtisch-Konstruktion | 11.05. – 05.06. | 13 | Bericht 3 |
| Schweißmaschinen-Wagen nach 5S | 08.06. – 26.06. | 10 | Bericht 4 |
| Lagersystem als Web-Anwendung | ab 22.06., parallel | 10 | — |
| Zerspanarbeitsplatz | 29.06. – 17.07. | 9 | Bericht 5 |
| Rostschutz-Konzept Schienenprofile | 20.07. – 31.07. | 7 | — |

Die beiden Software-Projekte liefen laut Projektdokumentation neben den
Werkstattprojekten her. Im Nachweis bekommt deshalb ab dem jeweiligen Startdatum
**jeder dritte Arbeitstag** ein Software-Thema (`EXCEL_AB`, `CLOUD_AB` und
`SOFTWARE_TAKT` in `generator/bau_nachweis.py`). Zusammen sind das 25 Tage –
genauso viele wie für das Schraubenlager.

Die Arbeitsanweisungen laufen ebenfalls parallel als einzelne Tageseinträge mit.

## Neu erzeugen

    python3 generator/bau_nachweis.py        # Excel
    python3 generator/bau_berichtsdaten.py   # Daten für das Word
    node    generator/bau_bericht.js         # Word

`generator/tagestexte.py` enthält die Tagesbeschreibungen nach Phasen,
`generator/berichtstexte.py` die fünf Berichtstexte. Beides ist reiner Text und
lässt sich direkt bearbeiten; danach das jeweilige Skript erneut laufen lassen.

Der Nachweis wird mit `fullCalcOnLoad` gespeichert — Excel rechnet die Formeln beim
Öffnen selbst neu. Die Vorlage in `generator/vorlage_taetigkeitsnachweis.xlsx` bleibt
dabei unverändert; alle Formeln und benannten Bereiche der Hochschule sind erhalten.

## Vor der Abgabe

1. Die drei Betreuer-Felder ausfüllen
2. In den Word-Bericht die Abbildungen einsetzen — die Plätze sind mit
   `[ Hier Abbildung einfügen: … ]` und fertiger Bildunterschrift markiert
3. Nachweis ausdrucken, vom Betrieb unterschreiben und stempeln lassen, scannen
4. Hochladen: Zeugnis (PDF), Nachweis (xlsx), unterschriebener Nachweis (PDF), Bericht (docx)
