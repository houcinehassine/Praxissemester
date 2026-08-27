# Generator

Die gesamte Website und der Ergebnisbericht werden aus diesen Skripten erzeugt.
Reines Python 3, keine Abhängigkeiten. Alle Pfade sind relativ zum Repository –
die Skripte laufen von überall aus.

## Aufbau

| Ordner / Datei | Inhalt |
|---|---|
| `build_projekt1.py` … `build_projekt7.py` | Je Projekt: Seitenliste, Kopf, Subnavigation, Fußzeile, `write_page()` |
| `seiten/pN_pageXX.py` | Je eine Seite eines Projekts. Ruft das zugehörige `build_projektN` auf. |
| `tabellen/*.html` | Ausgelagerte Tabellen für Projekt 1 |
| `build_quellen.py` | Erzeugt `quellen/index.html` aus den Dateien in `quellen/dateien/` |
| `bericht/` | Erzeugt den Ergebnisbericht für den Betrieb |

## Website neu bauen

Eine einzelne Seite:

    python3 generator/seiten/p6_page04.py

**Wichtig:** Ändert sich die `PAGES`-Liste in einem `build_projektN.py`, müssen
**alle** Seiten dieses Projekts neu erzeugt werden – die Subnavigation ist in
jede Seite fest eingebaut:

    for f in generator/seiten/p6_page*.py; do python3 "$f"; done

Die Quellenseite:

    python3 generator/build_quellen.py

## Ergebnisbericht neu bauen

Die Skripte bauen aufeinander auf und müssen in dieser Reihenfolge laufen:

    python3 generator/bericht/kap_1_3.py
    python3 generator/bericht/kap_4.py
    python3 generator/bericht/kap_5_6.py
    python3 generator/bericht/kap_7.py
    python3 generator/bericht/montage.py
    python3 generator/bericht/final.py

Ergebnis: `Ergebnisbericht-Praxissemester.html` im Repository-Wurzelverzeichnis.

Der Bericht zieht seine Tabellen **direkt aus den fertigen Projektseiten**
(`helfer.tab()` sucht eine Überschrift und übernimmt die darauf folgende
Tabelle). Wird eine Projektseite geändert, genügt ein erneuter Berichtslauf –
die Zahlen bleiben automatisch konsistent. Bilder werden als Data-URI
eingebettet, damit die Datei eigenständig bleibt.

`verweise.py` schreibt Verweise auf Seitenzahlen der Website in Verweise auf
Abschnitte des Berichts um und meldet, wenn einer übrig bleibt.

Die Zwischendateien `bericht/_k*.py` und `bericht/_montage.py` werden bei jedem
Lauf neu geschrieben und sind nicht versioniert.

## PDF erzeugen

Das PDF entsteht aus derselben HTML-Datei über Chromium (Playwright), Format A4
mit den Druckregeln aus `bericht/bericht.css`.
