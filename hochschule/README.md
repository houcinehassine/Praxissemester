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
nicht auseinanderlaufen. Die Pause folgt dem Arbeitszeitgesetz: **bis 6 h keine
Pause**, über 6 h → 30 min. Kurze Schichten laufen also durch.

Regeln für die Zeiten (alle geprüft, siehe unten):

- Ein Arbeitstag dauert **höchstens 9:00 Stunden einschließlich Pause**.
  Mit 30 min Pause sind das 8,50 h netto — das ist der längste Tag im Nachweis.
- Beginn, Ende und Pause nur in **5-Minuten-Schritten** — die Karte wird von Hand
  ausgefüllt, nicht automatisch gestempelt
- Beginn frühestens **07:00**, Ende spätestens **18:00**. An **15 Tagen** ist
  08:00 der Arbeitsbeginn, so wie er auch im Stundenplan steht.
- Arbeitstage mindestens **6,50 h**; nur Prüfungstage dürfen darunter liegen
- **Die Schichten werden über das Semester kürzer**: März hat die längsten Tage
  (Ø 8,39 h), danach absteigend bis Juli (Ø 7,00 h an den vollen Tagen)
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
| Vorlesung PP | Mi 10:00–11:30 | 12 | VA | ab ca. 12:15, je 4,00 h |
| Vorlesung PP + Praktikum RT | Mi 10:00–11:30 und 15:30–17:00 | 3 | V | — |
| Praktikum RT allein (01.07.) | Mi 15:30–17:00 | 1 | VA | 08:00–14:00, 6,00 h |
| Prüfungen | bis 10:00 | 4 | VA | ab ca. 11:00, je 4,00 h |

Der 01.07. ist die einzige Ausnahme bei den Lehrveranstaltungen: dort steht im
Stundenplan ausdrücklich **Betrieb 08:00–14:00**, das Praktikum liegt erst am
Nachmittag. Genau so ist der Tag eingetragen.

#### Die Schicht nach der Vorlesung

An jedem Mittwoch mit Vorlesung PP — außer den drei Tagen mit zusätzlichem
Praktikum RT — geht es nach der Vorlesung noch für **vier Stunden** in den
Betrieb, ab etwa 12:15 und damit ohne Pause. Das sind 12 Tage:

18.03. · 25.03. · 01.04. · 08.04. · 15.04. · 22.04. · 06.05. · 13.05. ·
03.06. · 10.06. · 17.06. · 24.06.

Die Startzeiten streuen zwischen 12:10 und 12:25 (`KURZSCHICHT_STARTS` in
`generator/hochschultage.py`), das Ende liegt entsprechend zwischen 16:10
und 16:25.

Ohne Schicht bleiben nur die **drei Tage mit Vorlesung PP *und* Praktikum RT**
(29.04., 20.05., 27.05.). Die Hochschule belegt dort 10:00 bis 17:00; für die
Fahrt nach Essing und zurück bleibt keine Zeit. Sie stehen als Typ V.

Die vier Prüfungstage stehen in `PRUEFUNGEN` in `generator/bau_nachweis.py`:

| Datum | Fach | Betrieb | Pause | Std netto |
|---|---|---|---|---|
| Do 09.07.2026 | PRM | 11:00–15:00 | — | 4,00 |
| Fr 17.07.2026 | DA | 11:05–15:05 | — | 4,00 |
| Mo 20.07.2026 | GAT | 11:00–15:00 | — | 4,00 |
| Di 28.07.2026 | SWV | 11:10–15:10 | — | 4,00 |

Diese vier Schichten und der 01.07. (08:00–14:00, 6,00 h) laufen **ohne Pause**
durch — bis 6 Stunden Arbeitszeit verlangt das Arbeitszeitgesetz keine.

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
| Ist | **709,50 h** |
| Soll (anteilig auf 99 Anwesenheitstage) | 687,75 h |
| Differenz | **+21,75 h** |
| Spanne | 23,00 h (KW 22) bis 42,00 h (KW 11) |
| Ø je Woche | 32,25 h |

Beim Soll zählt ein Vorlesungs-, Praktikums- oder Prüfungstag als **halber Tag**:
der Vormittag gehört der OTH, der Nachmittag dem Betrieb. Ein voller Tag zählt
mit 7,60 h. Eine Fußnote auf dem Blatt sagt das ebenfalls. Die Differenz je
Woche bleibt so überall zwischen −2,50 h und +4,00 h.

Wochen über einen Monatswechsel (KW 14 und KW 27) stehen in der Übersicht
vollständig, in den Monatsblättern anteilig; die betroffenen Wochenzeilen sind
dort entsprechend beschriftet.

Innerhalb der Monatsblätter steht nach jedem Sonntag eine hinterlegte Zeile
**Summe KW nn**; die Monatssumme addiert genau diese Wochenzeilen.

### Monatssummen

Die vollen Betriebstage werden von Monat zu Monat kürzer — am Anfang, während
der Einarbeitung und der großen Excel-Arbeit, sind die Tage am längsten:

| Monat | Tage mit Stunden | Std netto | Ø voller Tag | Spanne |
|---|---|---|---|---|
| März | 19 A + 2 VA | 167,50 | **8,39** | 8,25–8,50 |
| April | 15 A + 4 VA (+1 V) | 138,25 | 8,15 | 7,75–8,50 |
| Mai | 14 A + 2 VA (+2 V) | 119,25 | 7,95 | 7,50–8,50 |
| Juni | 17 A + 4 VA | 143,50 | 7,50 | 7,00–8,00 |
| Juli | 17 A + 5 VA | 141,00 | 7,00 | 6,50–7,50 |
| **Gesamt** | **82 A + 17 VA (+3 V)** | **709,50** | | |

„Ø voller Tag" ist der Schnitt der reinen Betriebstage; die kurzen Schichten an
Hochschul- und Prüfungstagen sind darin nicht enthalten. Über alle 99
Anwesenheitstage liegt der Schnitt bei 7,17 h. Die Werte stehen in
`generator/stundenplan.py`; wer die Kurve ändern will, ändert dort `ZIEL_A`
und baut beide Dateien neu.

Zum Vergleich mit den drei bestandenen Beispielen aus dem Bekanntenkreis:
Batuhan Sener 611,25 h (31,0 h/Woche), Ayad Kharbotly 572,45 h (28,6 h/Woche),
Achref Najah 690,75 h (33,4 h/Woche). Die 709,50 h liegen leicht darüber.

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
- **17 Tage** Typ `VA` (Vorlesung/Prüfung und anwesend), 4,00–6,00 h Betrieb —
  zwölf Schichten nach der Vorlesung PP, die vier Prüfungstage und der 01.07.
  (Praktikum RT erst am Nachmittag)
- **3 Tage** Typ `V` (Vorlesung, keine Anwesenheit im Betrieb) — 29.04., 20.05.
  und 27.05., die drei Mittwoche mit Vorlesung PP *und* Praktikum RT
- **2 Tage** Typ `K` — 20.03. und 03.07.
- **6 Tage** Typ `F` — Karfreitag, Ostermontag, Tag der Arbeit, Christi Himmelfahrt,
  Pfingstmontag, Fronleichnam

Summe **709,50 h** auf 99 Anwesenheitstage = **7,17 h je Tag**. Bezogen auf die
21,7 Kalenderwochen sind das 32,7 h/Woche — unter den 38 h der Stammdaten, weil
6 Feiertage, 2 Krankheitstage und 3 volle Hochschultage in den Zeitraum fallen,
weil an den 17 Vorlesungs- und Prüfungstagen nur der Nachmittag im Betrieb war
und weil kein Tag über 9:00 Stunden hinausgeht.

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
| Schweißmaschinen-Wagen nach 5S | 12.06. – 29.06. | 12 | Bericht 4 |
| Zerspanarbeitsplatz | 30.06. – 20.07. | 14 | Bericht 5 |
| Rostschutz-Konzept Schienenprofile | 21.07. – 31.07. | 9 | — |

Das Schraubenlager hat bewusst weniger Tage als die übrigen Projekte. Die
Web-Anwendung entstand mit KI-Unterstützung und beansprucht deshalb nur drei Tage;
sie ist im Word-Bericht als Abschluss von Bericht 1 beschrieben.

Die Arbeitsanweisungen laufen als einzelne Tageseinträge in den jeweiligen
Projektphasen mit. Nur die 3 Tage vom Typ `V` zählen nicht als Arbeitstag einer
Phase — an ihnen war keine Anwesenheit im Betrieb. Alle übrigen Vorlesungs- und
Prüfungstage zählen mit, weil an ihnen im Betrieb gearbeitet wurde.

Die Zeiträume der fünf Word-Berichte werden aus `generator/zeitraeume.json`
gelesen, das `bau_nachweis.py` beim Bauen schreibt. Ändert sich die Aufteilung
der Phasen, ziehen die Berichtsköpfe automatisch nach.

## Neu erzeugen

    python3 generator/hochschultage.py       # nur zur Kontrolle: Tagestypen
    python3 generator/bau_nachweis.py        # Excel-Nachweis + zeitraeume.json
    python3 generator/bau_zeiterfassung.py   # Stempelkarte aus dem Nachweis
    python3 generator/bau_berichtsdaten.py   # Daten für das Word
    node    generator/bau_bericht.js         # Word

Die Reihenfolge ist bindend: die Zeiterfassung liest die Stunden aus dem fertigen
Nachweis, die Berichtsdaten lesen die Phasengrenzen aus `zeitraeume.json`.

`generator/hochschultage.py` stuft jeden Kalendertag ein — Vorlesung, Praktikum,
Prüfung, Feiertag — und ist die gemeinsame Quelle für Nachweis und
Zeiterfassung. `generator/tagestexte.py` enthält die Tagesbeschreibungen nach Phasen,
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
