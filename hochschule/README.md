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
Pause**, über 6 h → 30 min, über 9 h → 45 min. Kurze Schichten laufen durch.

Regeln für die Zeiten (alle geprüft, siehe unten):

- Ein Arbeitstag hat höchstens **10,00 h netto** — mehr lässt das
  Arbeitszeitgesetz auch im Ausnahmefall nicht zu (§ 3 ArbZG).
- Beginn, Ende und Pause nur in **5-Minuten-Schritten** — die Karte wird von Hand
  ausgefüllt, nicht automatisch gestempelt
- Beginn frühestens **07:00**, Ende spätestens **18:00** — in der Prüfungsphase
  ab 15.06. spätestens **15:00**
- Nettostunden in **Viertelstundenschritten**. Nur so sind Dezimalwert *und*
  Uhrzeit zugleich glatt: 8,25 h = 8:15. Bei 5-Minuten-Schritten wäre der
  Dezimalwert 8,0833 und ließe sich nicht sauber anzeigen.

### Die drei Abschnitte

Die reinen Betriebstage folgen drei Abschnitten (`generator/stundenplan.py`):

| Abschnitt | Zeitraum | A-Tage | Spanne | Ø | Summe |
|---|---|---|---|---|---|
| **Startphase** | 02.03. – 13.03. | 10 | 9,00–10,00 | 9,53 | 95,25 |
| **Sammelphase** | 16.03. – 12.06. | 45 | 7,25–9,75 | 7,93 | 357,00 |
| **Prüfungsphase** | ab 15.06. | 27 | 6,75–7,50 | 7,22 | 195,00 |

- **Startphase** — die ersten zwei Wochen sind Einarbeitung, jeden Tag 9 bis 10
  Stunden.
- **Sammelphase** — Grundlast 7,25 bis 7,75 h. Dazu bekommt **jeder Monat vier
  längere Tage**, um Stunden vorzuarbeiten: zweimal 8,00 h und zweimal zwischen
  9 und 10 h, über den Monat verteilt (`SAMMEL_EXTRA` und `SAMMEL_LAGE`).
- **Prüfungsphase** — ab der zweiten Junihälfte ist täglich um **15:00** Schluss,
  damit Zeit für die Prüfungsvorbereitung bleibt. Das begrenzt den Tag auf
  7,50 h netto (07:00 + 8:00 brutto − 30 min Pause).

### Hochschultage und Prüfungen

An Tagen mit Hochschultermin wird **vor und nach dem Termin** gearbeitet. Diese
Tage haben ein festes Zeitfenster (`FENSTER` in `generator/hochschultage.py`)
und stehen im Nachweis als Typ **VA**:

| Anlass | Tage | Betrieb | Pause | Std netto |
|---|---|---|---|---|
| Vorlesung PP (bis 12.06.) | 10 | 07:00–09:30 **und** 12:00–17:00 | 2:30 | 7,50 |
| Vorlesung PP (ab 15.06.) | 2 | 07:00–09:30 **und** 12:00–15:00 | 2:30 | 5,50 |
| Vorlesung PP + Praktikum RT | 3 | 07:00–09:30 | — | 2,50 |
| nur Praktikum RT (01.07.) | 1 | 08:00–14:00 | — | 6,00 |
| Prüfungen | 4 | 11:00–15:00 | — | 4,00 |

In der Stempelkarte steht die Lücke von 09:30 bis 12:00 als **Pause 2:30** —
sie deckt Fahrt, Vorlesung und die gesetzliche Ruhepause ab.

- Die **drei Tage mit Vorlesung PP *und* Praktikum RT** (29.04., 20.05., 27.05.)
  sind von 10:00 bis 17:00 durch die OTH belegt; dort bleibt nur der Vormittag
  im Betrieb.
- Der **01.07.** steht so im Stundenplan: Betrieb 08:00–14:00, danach das
  Praktikum. Ohne Pause sind das glatte 6,00 h.
- Die **vier Prüfungstage** (09.07. PRM, 17.07. DA, 20.07. GAT, 28.07. SWV):
  Prüfung bis 10:00, danach 11:00–15:00 im Betrieb.

Im Tagesnachweis beginnt der Text dieser Tage mit einem Vorspann („Vorlesung PP
10:00-11:30 an der OTH, davor und danach im Betrieb.", „Prüfung PRM an der OTH
bis 10:00." …); danach folgt die Tätigkeit des jeweiligen Projekts.

### Wochenübersicht

Das erste Blatt fasst alle **22 Kalenderwochen** zusammen: KW, Zeitraum,
Arbeitstage, Std netto, Soll, Differenz und kumulierter Stand. Das Soll ist die
Wochenarbeitszeit von 38,0 h, je Arbeitstag anteilig gerechnet — eine Woche mit
einem Feiertag hat also 30,50 h Soll statt 38,00 h.

| | |
|---|---|
| Ist | **762,75 h** |
| **Soll laut Vertrag § 6** | **775,25 h** |
| **Differenz** | **−12,50 h** |
| Spanne | 26,50 h (KW 22) bis 48,00 h (KW 10) |
| Ø je Kalenderwoche (22 KW) | 34,67 h |

Der Vertrag nennt in **§ 6** nur die Wochenarbeitszeit von 38,0 h, **keine
Gesamtstundenzahl**. Sie ergibt sich aus dem Zeitraum: 110 Werktage (Mo–Fr)
abzüglich 6 Feiertagen und 2 Krankheitstagen = **102 Arbeitstage × 7,60 h =
775,25 h**. Der Nachweis liegt mit 762,75 h um 12,50 h darunter — das sind die
20 Tage, an denen die OTH einen Teil des Tages belegt hat und von denen der
Vertrag nichts weiß.

Die Spalte *Soll* in der Tabelle ist etwas anderes — sie vergleicht Woche für
Woche und rechnet 38,0 h anteilig je Anwesenheitstag, wobei ein Vorlesungs-,
Praktikums- oder Prüfungstag als **halber Tag** zählt.

Wochen über einen Monatswechsel (KW 14 und KW 27) stehen in der Übersicht
vollständig, in den Monatsblättern anteilig; die betroffenen Wochenzeilen sind
dort entsprechend beschriftet.

Innerhalb der Monatsblätter steht nach jedem Sonntag eine hinterlegte Zeile
**Summe KW nn**; die Monatssumme addiert genau diese Wochenzeilen.

### Monatssummen

| Monat | Tage mit Stunden | Std netto | Ø je Tag |
|---|---|---|---|
| März | 19 A + 2 VA | 182,50 | 8,69 |
| April | 15 A + 5 VA | 150,00 | 7,50 |
| Mai | 14 A + 4 VA | 129,75 | 7,21 |
| Juni | 17 A + 4 VA | 156,00 | 7,43 |
| Juli | 17 A + 5 VA | 144,50 | 6,57 |
| **Gesamt** | **82 A + 20 VA** | **762,75** | **7,48** |

März liegt vorn, weil dort die Startphase mit 9 bis 10 Stunden am Tag liegt;
Juli hinten, weil dort die Prüfungsphase und vier Prüfungstage liegen.

Zum Vergleich mit den drei bestandenen Beispielen aus dem Bekanntenkreis:
Batuhan Sener 611,25 h (31,0 h/Woche), Ayad Kharbotly 572,45 h (28,6 h/Woche),
Achref Najah 690,75 h (33,4 h/Woche). Die 762,75 h liegen darüber.

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

- **82 Tage** Typ `A` (anwesend), 6,75–10,00 h je nach Abschnitt
- **20 Tage** Typ `VA` (Vorlesung/Praktikum/Prüfung und anwesend), 2,50–7,50 h —
  12 Vorlesungstage, 3 Tage mit Vorlesung und Praktikum RT, der 01.07. und die
  vier Prüfungstage
- **keine Tage** vom Typ `V` — an jedem Hochschultag war auch Betriebszeit
- **2 Tage** Typ `K` — 20.03. und 03.07.
- **6 Tage** Typ `F` — Karfreitag, Ostermontag, Tag der Arbeit, Christi Himmelfahrt,
  Pfingstmontag, Fronleichnam

Summe **762,75 h** auf 102 Anwesenheitstage = **7,48 h je Tag**. Bezogen auf die
21,7 Kalenderwochen sind das 35,1 h/Woche — unter den 38 h der Stammdaten, weil
6 Feiertage und 2 Krankheitstage in den Zeitraum fallen und weil an den
20 Hochschul- und Prüfungstagen nur ein Teil des Tages im Betrieb war.

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
| Schweißarbeitsplatz | 24.04. – 15.05. | 14 | Bericht 2 |
| Schweißtisch-Konstruktion | 18.05. – 08.06. | 14 | Bericht 3 |
| Schweißmaschinen-Wagen nach 5S | 09.06. – 25.06. | 13 | Bericht 4 |
| Zerspanarbeitsplatz | 26.06. – 17.07. | 15 | Bericht 5 |
| Rostschutz-Konzept Schienenprofile | 20.07. – 31.07. | 10 | — |

Das Schraubenlager hat bewusst weniger Tage als die übrigen Projekte. Die
Web-Anwendung entstand mit KI-Unterstützung und beansprucht deshalb nur drei Tage;
sie ist im Word-Bericht als Abschluss von Bericht 1 beschrieben.

Die Arbeitsanweisungen laufen als einzelne Tageseinträge in den jeweiligen
Projektphasen mit. **Alle 102 Anwesenheitstage** zählen als Arbeitstag einer
Phase, auch die Hochschul- und Prüfungstage — an jedem von ihnen wurde im
Betrieb gearbeitet.

Die Zeiträume der fünf Word-Berichte werden aus `generator/zeitraeume.json`
gelesen, das `bau_nachweis.py` beim Bauen schreibt. Ändert sich die Aufteilung
der Phasen, ziehen die Berichtsköpfe automatisch nach.

## Neu erzeugen

    npm install docx image-size --prefix generator   # einmalig
    python3 generator/hochschultage.py       # nur zur Kontrolle: Tagestypen
    python3 generator/bau_nachweis.py        # Excel-Nachweis + zeitraeume.json
    python3 generator/bau_zeiterfassung.py   # Stempelkarte aus dem Nachweis
    python3 generator/bau_berichtsdaten.py   # Daten für das Word
    node    generator/bau_bericht.js         # Word

Die Reihenfolge ist bindend: die Zeiterfassung liest die Stunden aus dem fertigen
Nachweis, die Berichtsdaten lesen die Phasengrenzen aus `zeitraeume.json`.

### Abbildungen im Word-Bericht

`generator/bau_berichtsdaten.py` verweist je Bild auf eine echte Datei aus den
Projektordnern (`ABBILDUNGEN`, repo-relativer Pfad); `bau_bericht.js` bettet sie
mit `docx.ImageRun` direkt ein, verkleinert auf höchstens 480×380 px und setzt
die Bildunterschrift „Abbildung n.m: …" darunter. Projekt 3 (Web-Anwendung) und
Projekt 4 (Schweißarbeitsplatz) haben keine Bilder in der Website hinterlegt;
Bericht 2 bleibt deshalb bewusst ohne Abbildung, mit einem kurzen Hinweissatz
statt eines erfundenen Bildes. Für Bericht 5 liegt unter
`generator/berichtsbilder/zerspan-vier-varianten.png` eine 2×2-Montage der vier
Werkbank-Varianten aus Projekt 7 — die einzige Bilddatei, die nicht 1:1 aus der
Website stammt, sondern für den Bericht zusammengesetzt wurde.

Laut Informationsveranstaltung von Prof. Galka (Folie „Anforderungen") müssen
mindestens 3 der 5 Berichte Abbildungen enthalten; aktuell sind es 4 (Berichte
1, 3, 4, 5) mit zusammen 13 Bildern.

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
