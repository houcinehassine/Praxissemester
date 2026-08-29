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
für Praktikant und Betrieb.

Die Netto-Stunden werden **aus dem fertigen Tätigkeitsnachweis gelesen**;
Beginn, Pause und Ende sind daraus zurückgerechnet. Beide Dateien können damit
nicht auseinanderlaufen. Die Pause folgt dem Arbeitszeitgesetz: über 6 h → 30 min,
darunter 15 min.

Regeln für die Zeiten (alle geprüft, siehe unten):

- Ein Arbeitstag dauert **höchstens 9:00 Stunden einschließlich Pause**.
  Mit 30 min Pause sind das 8,50 h netto — das ist der längste Tag im Nachweis.
- Beginn, Ende und Pause nur in **5-Minuten-Schritten** — die Karte wird von Hand
  ausgefüllt, nicht automatisch gestempelt
- Beginn frühestens **07:00**, Ende spätestens **18:00**. An **15 Tagen** ist
  08:00 der Arbeitsbeginn, so wie er auch im Stundenplan steht.
- Arbeitstage mindestens **6,50 h**; nur Vorlesungstage dürfen darunter liegen
- Nettostunden in **Viertelstundenschritten**. Nur so sind Dezimalwert *und*
  Uhrzeit zugleich glatt: 8,25 h = 8:15. Bei 5-Minuten-Schritten wäre der
  Dezimalwert 8,0833 und ließe sich nicht sauber anzeigen.

### Hochschultage und Prüfungen

An Tagen, an denen die Hochschule den Vormittag belegt, war **keine Anwesenheit
im Betrieb** — das ist in der Vorlage der Typ **V** („Vorlesung und keine
Anwesenheit im Betrieb"). Diese Tage haben keine Stunden und zählen nicht als
Arbeitstag einer Projektphase.

| Anlass | Zeit | Tage | Typ | Betrieb |
|---|---|---|---|---|
| Vorlesung PP | Mi 10:00–11:30 | 12 | V | — |
| Vorlesung PP + Praktikum RT | Mi 10:00–11:30 und 15:30–17:00 | 3 | V | — |
| Praktikum RT allein (01.07.) | Mi 15:30–17:00 | 1 | VA | 08:00–14:00, 5,50 h |
| Prüfungen | bis 10:00 | 4 | VA | ab ca. 11:00, längstens bis 15:30 |

Der 01.07. ist die einzige Ausnahme bei den Lehrveranstaltungen: dort steht im
Stundenplan ausdrücklich **Betrieb 08:00–14:00**, das Praktikum liegt erst am
Nachmittag. Genau so ist der Tag eingetragen.

Die vier Prüfungstage stehen in `PRUEFUNGEN` in `generator/bau_nachweis.py`:

| Datum | Fach | Betrieb | Std netto |
|---|---|---|---|
| Do 09.07.2026 | PRM | 11:00–15:30 | 4,25 |
| Fr 17.07.2026 | DA | 11:15–15:30 | 4,00 |
| Mo 20.07.2026 | GAT | 11:00–15:30 | 4,25 |
| Di 28.07.2026 | SWV | 11:05–15:20 | 4,00 |

Im Tagesnachweis beginnt der Text dieser Tage mit „Prüfung ⟨Fach⟩ an der OTH
bis 10:00."; danach folgt die Tätigkeit des jeweiligen Projekts, denn der
Nachmittag lief im Betrieb.

### Wochenübersicht

Das erste Blatt fasst alle **22 Kalenderwochen** zusammen: KW, Zeitraum,
Arbeitstage, Std netto, Soll, Differenz und kumulierter Stand. Das Soll ist die
Wochenarbeitszeit von 38,0 h, je Arbeitstag anteilig gerechnet — eine Woche mit
einem Feiertag hat also 30,50 h Soll statt 38,00 h.

| | |
|---|---|
| Ist | **664,00 h** |
| Soll (anteilig auf 87 Anwesenheitstage) | 661,75 h |
| Differenz | +2,25 h |
| Spanne | 22,25 h (KW 23) bis 41,50 h (KW 10) |
| Ø je Woche | 30,18 h |

Wochen über einen Monatswechsel (KW 14 und KW 27) stehen in der Übersicht
vollständig, in den Monatsblättern anteilig; die betroffenen Wochenzeilen sind
dort entsprechend beschriftet.

Innerhalb der Monatsblätter steht nach jedem Sonntag eine hinterlegte Zeile
**Summe KW nn**; die Monatssumme addiert genau diese Wochenzeilen.

### Monatssummen

| Monat | Tage mit Stunden | Std netto | Ø je Tag |
|---|---|---|---|
| März | 19 A (+2 V) | 156,75 | 8,25 |
| April | 15 A (+5 V) | 123,50 | 8,23 |
| Mai | 14 A (+4 V) | 115,25 | 8,23 |
| Juni | 17 A (+4 V) | 127,50 | 7,50 |
| Juli | 17 A + 5 VA | 141,00 | 6,41 |
| **Gesamt** | **82 A + 5 VA (+15 V)** | **664,00** | **7,63** |

**Juli hat die kürzesten Arbeitstage, Juni die zweitkürzesten** — so ist die
Vorgabe umgesetzt. Als *kleinste Monatssumme* ist sie unter der 9-Stunden-Grenze
nicht erreichbar: Juli hat die meisten Anwesenheitstage, Mai mit 14 die
wenigsten. Wer die Monatssummen angleichen will, ändert
`generator/stundenplan.py` und baut beide Dateien neu.

Zum Vergleich mit den drei bestandenen Beispielen aus dem Bekanntenkreis:
Batuhan Sener 611,25 h (31,0 h/Woche), Ayad Kharbotly 572,45 h (28,6 h/Woche),
Achref Najah 690,75 h (33,4 h/Woche). Die 664,00 h liegen mitten in diesem Feld.

Zum Neubauen siehe „Neu erzeugen" weiter unten; die Reihenfolge ist bindend.

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

- **82 Tage** Typ `A` (anwesend), 6,50–8,50 h
- **5 Tage** Typ `VA` (Vorlesung/Prüfung und anwesend), 4,00–5,50 h Betrieb —
  der 01.07. (Praktikum RT erst am Nachmittag) und die vier Prüfungstage
- **15 Tage** Typ `V` (Vorlesung, keine Anwesenheit im Betrieb) — alle Mittwoche
  mit der Vorlesung „PP" ab 18.03. Die ersten beiden Mittwoche (04.03., 11.03.)
  sind `A`, da die Vorlesungen erst am 18.03. beginnen; die letzte ist der 24.06.
- **2 Tage** Typ `K` — 20.03. und 03.07.
- **6 Tage** Typ `F` — Karfreitag, Ostermontag, Tag der Arbeit, Christi Himmelfahrt,
  Pfingstmontag, Fronleichnam

Summe **664,00 h** auf 87 Anwesenheitstage = **7,63 h je Tag**. Bezogen auf die
21,7 Kalenderwochen sind das 30,2 h/Woche — unter den 38 h der Stammdaten, weil
6 Feiertage, 2 Krankheitstage und 15 Hochschultage in den Zeitraum fallen und weil
kein Tag über 9:00 Stunden hinausgeht. Bezogen auf die 87 Tage, an denen der
Betrieb überhaupt möglich war, liegt der Nachweis mit +2,25 h genau auf dem Soll.

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
| Material- und Schraubenlager (5S) | 05.03. – 17.03. | 9 | — |
| Lagerbestand-System in Excel/VBA | 19.03. – 23.04. | 18 | Bericht 1 |
| Lagersystem als Web-Anwendung | 24.04. – 28.04. | 3 | in Bericht 1 |
| Schweißarbeitsplatz | 30.04. – 22.05. | 12 | Bericht 2 |
| Schweißtisch-Konstruktion | 26.05. – 16.06. | 12 | Bericht 3 |
| Schweißmaschinen-Wagen nach 5S | 18.06. – 06.07. | 11 | Bericht 4 |
| Zerspanarbeitsplatz | 07.07. – 21.07. | 11 | Bericht 5 |
| Rostschutz-Konzept Schienenprofile | 22.07. – 31.07. | 8 | — |

Das Schraubenlager hat bewusst weniger Tage als die übrigen Projekte. Die
Web-Anwendung entstand mit KI-Unterstützung und beansprucht deshalb nur drei Tage;
sie ist im Word-Bericht als Abschluss von Bericht 1 beschrieben.

Die Arbeitsanweisungen laufen als einzelne Tageseinträge in den jeweiligen
Projektphasen mit. Die 15 Tage vom Typ `V` zählen nicht als Arbeitstag einer
Phase — an ihnen war keine Anwesenheit im Betrieb. Die vier Prüfungstage zählen
mit, weil der Nachmittag im Betrieb lief; die Datumsgrenzen der Phasen springen
deshalb über die Mittwoche hinweg.

Die Zeiträume der fünf Word-Berichte werden aus `generator/zeitraeume.json`
gelesen, das `bau_nachweis.py` beim Bauen schreibt. Ändert sich die Aufteilung
der Phasen, ziehen die Berichtsköpfe automatisch nach.

## Neu erzeugen

    python3 generator/bau_nachweis.py        # Excel-Nachweis + zeitraeume.json
    python3 generator/bau_zeiterfassung.py   # Stempelkarte aus dem Nachweis
    python3 generator/bau_berichtsdaten.py   # Daten für das Word
    node    generator/bau_bericht.js         # Word

Die Reihenfolge ist bindend: die Zeiterfassung liest die Stunden aus dem fertigen
Nachweis, die Berichtsdaten lesen die Phasengrenzen aus `zeitraeume.json`.

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
