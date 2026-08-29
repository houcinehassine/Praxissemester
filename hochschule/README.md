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

### Hochschultage im Stundenplan

Der Stundenplan enthält zwei Lehrveranstaltungen. Beide sind jetzt abgebildet:

| Veranstaltung | Zeit | Tage | Folge im Nachweis |
|---|---|---|---|
| Vorlesung PP | Mi 10:00–11:30 | 15 | danach in den Betrieb |
| Praktikum Regelungstechnik | Mi 15:30–17:00 | 4 | siehe unten |

- **12 Tage** nur Vorlesung PP → Typ **VA**, Arbeitsbeginn ab 11:45
- **3 Tage** (29.04., 20.05., 27.05.) Vorlesung PP *und* Praktikum RT. Die
  Hochschule belegt den Tag von 10:00 bis 17:00; zwischen Regensburg und Essing
  bleibt keine sinnvolle Betriebszeit. Diese Tage sind Typ **V** —
  „Vorlesung und keine Anwesenheit im Betrieb", so wie die Vorlage ihn vorsieht.
  Sie zählen deshalb auch nicht als Arbeitstag einer Projektphase.
- **1 Tag** (01.07.) nur Praktikum RT. Der Stundenplan nennt hier ausdrücklich
  Betrieb 08:00–14:00; genau so steht der Tag in der Zeiterfassung (Typ VA, 5,50 h).

### Wochenübersicht

Das erste Blatt fasst alle **22 Kalenderwochen** zusammen: KW, Zeitraum,
Arbeitstage, Std netto, Soll, Differenz und kumulierter Stand. Das Soll ist die
Wochenarbeitszeit von 38,0 h, je Arbeitstag anteilig gerechnet — eine Woche mit
einem Feiertag hat also 30,50 h Soll statt 38,00 h.

| | |
|---|---|
| Ist | **739,25 h** |
| Soll (anteilig auf 99 Arbeitstage) | 753,00 h |
| Differenz | −13,75 h |
| Spanne | 23,75 h (KW 22) bis 41,50 h (KW 10) |
| Ø je Woche | 33,60 h |

Wochen über einen Monatswechsel (KW 14 und KW 27) stehen in der Übersicht
vollständig, in den Monatsblättern anteilig; die betroffenen Wochenzeilen sind
dort entsprechend beschriftet.

Innerhalb der Monatsblätter steht nach jedem Sonntag eine hinterlegte Zeile
**Summe KW nn**; die Monatssumme addiert genau diese Wochenzeilen.

### Monatssummen

| Monat | Arbeitstage | Std netto | Ø je Arbeitstag |
|---|---|---|---|
| März | 19 A + 2 VA | 167,75 | 7,99 |
| April | 15 A + 4 VA (+1 V) | 145,00 | 7,63 |
| Mai | 14 A + 2 VA (+2 V) | 126,00 | 7,88 |
| Juni | 17 A + 4 VA | 148,00 | 7,05 |
| Juli | 21 A + 1 VA | 152,50 | 6,93 |
| **Gesamt** | **86 A + 13 VA + 3 V** | **739,25** | **7,47** |

**Juli hat die kürzesten Arbeitstage, Juni die zweitkürzesten** — so ist die
Vorgabe umgesetzt. Als *kleinste Monatssumme* ist sie unter der 9-Stunden-Grenze
nicht erreichbar: Juli hat mit 21 die meisten Arbeitstage und käme selbst am
Minimum von 6,50 h auf 142,00 h, während Mai mit nur 14 Arbeitstagen auch am
Maximum von 8,50 h nur 130,50 h erreicht. Wer die Monatssummen angleichen will,
ändert `generator/stundenplan.py` und baut beide Dateien neu.

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

- **86 Tage** Typ `A` (anwesend), 6,50–8,50 h
- **13 Tage** Typ `VA` (Vorlesung und anwesend), 5,00–5,75 h Betrieb — 12 Mittwoche
  mit der Vorlesung „PP" 10:00–11:30 und der 01.07. mit dem Praktikum
  Regelungstechnik am Nachmittag. Die ersten beiden Mittwoche (04.03., 11.03.) sind
  `A`, da die Vorlesungen erst am 18.03. beginnen.
- **3 Tage** Typ `V` (Vorlesung, keine Anwesenheit im Betrieb) — 29.04., 20.05.,
  27.05.: an diesen Mittwochen liegen Vorlesung PP und Praktikum RT im selben Tag.
- **2 Tage** Typ `K` — 20.03. und 03.07.
- **6 Tage** Typ `F` — Karfreitag, Ostermontag, Tag der Arbeit, Christi Himmelfahrt,
  Pfingstmontag, Fronleichnam

Summe **739,25 h** auf 99 Arbeitstage = **7,47 h je Tag**. Bezogen auf die
21,7 Kalenderwochen sind das 34,1 h/Woche — unter den 38 h der Stammdaten, weil
6 Feiertage, 2 Krankheitstage und 3 Hochschultage in den Zeitraum fallen und weil
kein Tag über 9:00 Stunden hinausgeht.

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
| Schweißarbeitsplatz | 24.04. – 18.05. | 14 | Bericht 2 |
| Schweißtisch-Konstruktion | 19.05. – 11.06. | 14 | Bericht 3 |
| Schweißmaschinen-Wagen nach 5S | 12.06. – 30.06. | 13 | Bericht 4 |
| Zerspanarbeitsplatz | 01.07. – 20.07. | 13 | Bericht 5 |
| Rostschutz-Konzept Schienenprofile | 21.07. – 31.07. | 9 | — |

Das Schraubenlager hat bewusst weniger Tage als die übrigen Projekte. Die
Web-Anwendung entstand mit KI-Unterstützung und beansprucht deshalb nur drei Tage;
sie ist im Word-Bericht als Abschluss von Bericht 1 beschrieben.

Die Arbeitsanweisungen laufen als einzelne Tageseinträge in den jeweiligen
Projektphasen mit. Die drei Tage vom Typ `V` zählen nicht als Arbeitstag einer
Phase — an ihnen war keine Anwesenheit im Betrieb.

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
