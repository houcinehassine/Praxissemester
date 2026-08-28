# Hochschulunterlagen — Pflichtabgabe Praxissemester

Zwei Dateien für die Abgabe über GRIPS, erzeugt in der Form der OTH-Vorlagen.

| Datei | Inhalt |
|---|---|
| `Hassine_3399727_Tätigkeitsnachweis.xlsx` | Täglicher Nachweis, 02.03.–31.07.2026 |
| `Hassine_3399727_Bericht.docx` | Die fünf Tätigkeitsberichte |
| `Hassine_3399727_Zeiterfassung.xlsx` | Stempelkarte, je Monat ein Blatt, plus Wochenübersicht |
| `…_Bericht.pdf`, `…_Zeiterfassung.pdf` | Nur zur Ansicht und zum Drucken |

## Zeiterfassung

Fünf Monatsblätter mit den Spalten Tag, Datum, Beginn, Ende, Pause, Std netto
und Bemerkung, je Blatt eine A4-Seite mit Monatssumme und Unterschriftszeilen
für Praktikant und Betrieb. Innerhalb der Monatsblätter steht nach jedem Sonntag
eine hinterlegte Zeile **Summe KW nn**; die Monatssumme addiert genau diese
Wochenzeilen.

### Wochenübersicht

Das erste Blatt fasst alle **22 Kalenderwochen** zusammen: KW, Zeitraum,
Arbeitstage, Std netto, Soll, Differenz und kumulierter Stand. Das Soll ist die
Wochenarbeitszeit von 38,0 h, je Arbeitstag anteilig gerechnet — eine Woche mit
einem Feiertag hat also 30,50 h Soll statt 38,00 h.

| | |
|---|---|
| Ist | **824,75 h** |
| Soll (anteilig) | 776,00 h |
| Differenz | **+48,75 h** |
| Spanne | 33,50 h (KW 30) bis 47,75 h (KW 10) |
| Ø je Woche | 37,49 h |

Der Vorlauf entsteht zwangsläufig aus zwei Vorgaben: Juli und Juni sollen die
kleinsten Monatssummen haben, und kein Arbeitstag darf unter 6,50 h liegen.
Die frühen Monate müssen die Stunden also vorziehen. Wer das flacher haben
möchte, ändert die Monatsziele in `generator/stundenplan.py` und baut Nachweis
und Zeiterfassung neu.

Wochen über einen Monatswechsel (KW 14 und KW 27) stehen in der Übersicht
vollständig, in den Monatsblättern anteilig; die betroffenen Wochenzeilen sind
dort entsprechend beschriftet.

Die Netto-Stunden werden **aus dem fertigen Tätigkeitsnachweis gelesen**;
Beginn, Pause und Ende sind daraus zurückgerechnet. Beide Dateien können damit
nicht auseinanderlaufen. Die Pause folgt dem Arbeitszeitgesetz: über 6 h → 30 min,
über 9 h → 45 min, darunter 15 min. An Vorlesungstagen beginnt die Arbeit erst
nach der Vorlesung, frühestens 11:55.

Regeln für die Zeiten (alle geprüft, siehe unten):

- Beginn, Ende und Pause nur in **5-Minuten-Schritten** — die Karte wird von Hand
  ausgefüllt, nicht automatisch gestempelt
- Beginn frühestens **07:00**, Ende spätestens **18:00**
- Arbeitstage mindestens **6,50 h**; nur Vorlesungstage dürfen darunter liegen
- Nettostunden in **Viertelstundenschritten**. Nur so sind Dezimalwert *und*
  Uhrzeit zugleich glatt: 8,25 h = 8:15. Bei 5-Minuten-Schritten wäre der
  Dezimalwert 8,0833 und ließe sich nicht sauber anzeigen.

Die Nettostunden je Monat stehen in `generator/stundenplan.py`. Dort ist auch
festgelegt, dass **Juli die kleinste und Juni die zweitkleinste** Monatssumme
bekommt:

| Monat | Arbeitstage | Std netto |
|---|---|---|
| Juli | 21 A + 1 VA | 147,25 |
| Juni | 17 A + 4 VA | 153,75 |
| Mai | 14 A + 4 VA | 158,50 |
| April | 15 A + 5 VA | 173,75 |
| März | 19 A + 2 VA | 191,50 |
| **Gesamt** | | **824,75** = 38,0 h/Woche |

Juli hat die meisten Arbeitstage, deshalb liegen seine Tage nahe an der
Untergrenze von 6,50 h — anders wäre die kleinste Monatssumme nicht erreichbar.

Reihenfolge beim Bauen: erst `bau_nachweis.py`, dann `bau_zeiterfassung.py`.

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

Summe **824,75 h** auf 21,7 Wochen = **38,0 h/Woche**, stimmig zu den 38 h in den Stammdaten.

Die erste Woche (02.–06.03.) ist bewusst Einarbeitung: Sicherheitsunterweisung,
Betriebsrundgang, Maschinen und Abläufe kennenlernen, Arbeitsplatz einrichten. Die
Projektarbeit beginnt am 09.03.

## Zeitliche Zuordnung der Projekte

Die Phasen laufen **nacheinander**, festgelegt über die Anzahl der Arbeitstage
(`PHASEN` in `generator/bau_nachweis.py`). Die Datumsgrenzen ergeben sich daraus.
Der **Tagesnachweis dokumentiert alle Projekte**, der Word-Bericht nur fünf davon.

| Thema | Zeitraum | Tage | im Word-Bericht |
|---|---|---|---|
| Einarbeitung | 02.03. – 04.03. | 3 | — |
| Material- und Schraubenlager (5S) | 05.03. – 18.03. | 10 | — |
| Lagerbestand-System in Excel/VBA | 19.03. – 20.04. | 20 | Bericht 1 |
| Lagersystem als Web-Anwendung | 21.04. – 23.04. | 3 | in Bericht 1 |
| Schweißarbeitsplatz | 24.04. – 18.05. | 15 | Bericht 2 |
| Schweißtisch-Konstruktion | 19.05. – 10.06. | 15 | Bericht 3 |
| Schweißmaschinen-Wagen nach 5S | 11.06. – 29.06. | 13 | Bericht 4 |
| Zerspanarbeitsplatz | 30.06. – 20.07. | 14 | Bericht 5 |
| Rostschutz-Konzept Schienenprofile | 21.07. – 31.07. | 9 | — |

Das Schraubenlager hat bewusst weniger Tage als die übrigen Projekte. Die
Web-Anwendung entstand mit KI-Unterstützung und beansprucht deshalb nur drei Tage;
sie ist im Word-Bericht als Abschluss von Bericht 1 beschrieben.

Die Arbeitsanweisungen laufen als einzelne Tageseinträge in den jeweiligen
Projektphasen mit.

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
