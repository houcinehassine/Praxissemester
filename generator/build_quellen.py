# -*- coding: utf-8 -*-
import os, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DDIR = os.path.join(ROOT, "quellen", "dateien")

DOKS = [
 (1, "Schraubenlager-Projekt", "01_schraubenlager-projekt.html", "23.08.2026",
  "Die laufende Projektdokumentation zur Neuordnung des Schraubenlagers: Ausgangszustand, Ordnungskonzept, Umsetzungsschritte und Fotos aus der Werkstatt.",
  [("projekt-1", "Projekt 1: Schraubenlager")], "lager"),
 (2, "Schraubenlager &ndash; Projektbericht", "02_schraubenlager-projektbericht.html", "23.08.2026",
  "Der ausformulierte Projektbericht zur Neuorganisation des Schraubenlagers &ndash; Berichtsfassung mit Ergebnissen und Bewertung.",
  [("projekt-1", "Projekt 1: Schraubenlager")], "lager"),
 (3, "Lagerbestand &ndash; Dokumentation", "03_lagerbestand-dokumentation.html", "24.08.2026",
  "Vollständige Dokumentation des Excel/VBA-Lagerbestandssystems: Aufbau, Masken, Barcode-Logik und Funktionsumfang bis zur Tablet-Version.",
  [("projekt-2", "Projekt 2: Excel-Lagersystem")], "lager"),
 (4, "Lagerbestand &ndash; Arbeitsschritte", "04_lagerbestand-arbeitsschritte.html", "24.08.2026",
  "Die Entwicklung des Excel-Lagersystems Schritt für Schritt &ndash; chronologisch, mit Screenshots zu jedem Entwicklungsstand.",
  [("projekt-2", "Projekt 2: Excel-Lagersystem")], "lager"),
 (5, "Lagersystem &ndash; Projektbericht", "05_lagersystem-projektbericht.pdf", "24.08.2026",
  "Projektbericht zur Python/Streamlit-Neuentwicklung des Lagersystems &ndash; 11 Seiten, Kurzfassung.",
  [("projekt-3", "Projekt 3: Lagersystem in der Cloud")], "lager"),
 (6, "Lagersystem &ndash; Detaillierter Projektbericht", "06_lagersystem-projektbericht-detailliert.pdf", "24.08.2026",
  "Die ausführliche Fassung desselben Berichts &ndash; 14 Seiten mit Architektur, Datenmodell und Migrationsschritten.",
  [("projekt-3", "Projekt 3: Lagersystem in der Cloud")], "lager"),
 (7, "Lagersystem &ndash; Code-Dokumentation", "07_lagersystem-code-dokumentation.pdf", "24.08.2026",
  "Die technische Code-Dokumentation der Streamlit-Anwendung &ndash; 39 Seiten, Modul für Modul.",
  [("projekt-3", "Projekt 3: Lagersystem in der Cloud")], "lager"),
 (8, "Schweißarbeitsplatz &ndash; Projekt v13", "08_schweissarbeitsplatz-projekt-v13.html", "24.08.2026",
  "Die frühere Konzeptphase des Schweißarbeitsplatzes mit abstrakter Nutzwertanalyse. Bewusst als eigener Stand dokumentiert, weil die reale Umsetzung später anders ausfiel.",
  [("projekt-4", "Projekt 4: Schweißarbeitsplatz")], "schweiss"),
 (9, "Schweißarbeitsplatz &ndash; Projekt", "09_schweissarbeitsplatz-projekt.html", "24.08.2026",
  "Die reale Planung des Schweißarbeitsplatzes: Werkzeugliste, feste Station, Lochwände, Schubladen, Reinigung, PSA und Sicherheitskonzept nach 5S.",
  [("projekt-4", "Projekt 4: Schweißarbeitsplatz")], "schweiss"),
 (10, "Schweißtisch-Projekt", "10_schweisstisch-projekt.html", "24.08.2026",
  "Die Konstruktionsdokumentation des ausziehbaren Schweißtischs mit D16-Lochplatten-Spannsystem &ndash; von der ersten Idee bis zum Zeichnungssatz, mit allen CAD-Ansichten.",
  [("projekt-5", "Projekt 5: Schweißtisch")], "schweiss"),
 (11, "Schweißtisch-Projekt &ndash; Struktur", "11_schweisstisch-projekt-struktur.html", "24.08.2026",
  "Dieselbe Dokumentation in strukturierter Gliederung &ndash; die Grundlage für die Seitenaufteilung von Projekt 5.",
  [("projekt-5", "Projekt 5: Schweißtisch")], "schweiss"),
 (12, "Schweißwagen &ndash; Konstruktionsablauf", "12_schweisswagen-konstruktionsablauf.html", "26.08.2026",
  "Der gesamte Konstruktionsablauf des Schweißmaschinenwagens: IST-Aufnahme mit Werkstattfotos, Lastenheft, sechs Entwicklungsstufen und der Zeichnungssatz mit 21 Blättern.",
  [("projekt-6", "Projekt 6: Schweißwagen")], "schweiss"),
 (13, "Zerspanarbeitsplatz &ndash; Zeitstrahl v3", "13_zerspanarbeitsplatz-zeitstrahl-v3.html", "26.08.2026",
  "Die Konzeptplanung des Zerspanarbeitsplatzes in acht Kapiteln, mit den interaktiven Rechnern (Werkzeugpreise, Nutzwertanalyse, Amortisation, Audit) &ndash; ohne eingebettete Grafiken.",
  [("projekt-7", "Projekt 7: Zerspanarbeitsplatz")], "zerspan"),
 (14, "Zerspanarbeitsplatz &ndash; Finalfassung", "14_zerspanarbeitsplatz-final.html", "26.08.2026",
  "Dieselbe Fassung, zusätzlich mit den zehn eingebetteten 3D-Grafiken der Bauvarianten, Layout-Konzepte und des Werkstatt-Grundrisses.",
  [("projekt-7", "Projekt 7: Zerspanarbeitsplatz")], "zerspan"),
]

TAGS = {"lager": ("tag--lager", "Lager &amp; Organisation"),
        "schweiss": ("tag--schweiss", "Schweißarbeitsplatz"),
        "zerspan": ("tag--zerspan", "Zerspanung")}

def groesse(pfad):
    b = os.path.getsize(pfad)
    if b >= 1024 * 1024:
        return f"{b/1024/1024:.1f} MB".replace(".", ",")
    return f"{b/1024:.0f} KB"

gesamt = sum(os.path.getsize(os.path.join(DDIR, d[2])) for d in DOKS)
html_anz = sum(1 for d in DOKS if d[2].endswith(".html"))
pdf_anz = len(DOKS) - html_anz

karten = ""
for nr, titel, datei, datum, text, projekte, kat in DOKS:
    pfad = os.path.join(DDIR, datei)
    typ = "PDF" if datei.endswith(".pdf") else "HTML"
    cls, label = TAGS[kat]
    proj_links = " ".join(
        f'<a class="quelle-projekt" href="../projekte/{p}/index.html">&rarr; {n}</a>' for p, n in projekte)
    karten += f"""      <article class="quelle-karte" data-kategorie="{kat}">
        <div class="quelle-kopf">
          <span class="quelle-nr">{nr:02d}</span>
          <div>
            <h3>{titel}</h3>
            <span class="tag {cls}">{label}</span>
          </div>
        </div>
        <p class="quelle-text">{text}</p>
        <dl class="quelle-meta">
          <div><dt>Dateiname</dt><dd><code>{datei}</code></dd></div>
          <div><dt>Format</dt><dd>{typ}</dd></div>
          <div><dt>Größe</dt><dd>{groesse(pfad)}</dd></div>
          <div><dt>Übergeben am</dt><dd>{datum}</dd></div>
        </dl>
        <div class="quelle-aktionen">
          <a class="quelle-oeffnen" href="dateien/{datei}" target="_blank" rel="noopener">Original öffnen &nearr;</a>
          {proj_links}
        </div>
      </article>
"""

# Zuordnungstabelle
zuord = {}
for nr, titel, datei, datum, text, projekte, kat in DOKS:
    for p, n in projekte:
        zuord.setdefault((p, n), []).append(nr)
zeilen = ""
for (p, n), nrs in sorted(zuord.items()):
    liste = ", ".join(f"{x:02d}" for x in nrs)
    zeilen += f'<tr><td><a href="../projekte/{p}/index.html">{n}</a></td><td>{liste}</td><td>{len(nrs)}</td></tr>\n            '
zeilen += f'<tr class="total-row"><td>Gesamt</td><td>01&ndash;14</td><td>{len(DOKS)}</td></tr>'

seite = f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Quellen &amp; Originaldokumente | Mein Praxissemester</title>
  <link rel="icon" type="image/svg+xml" href="../favicon.svg" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../css/style.css" />
</head>
<body>

  <header class="site-header">
    <div class="inner">
      <a href="../index.html" class="logo">Mein <span>Praxissemester</span></a>
      <nav>
        <a href="../index.html">Start</a>
        <a href="../index.html#projekte">Projekte</a>
        <a href="index.html">Quellen</a>
      </nav>
    </div>
  </header>

  <header class="seiten-kopf">
    <div class="inner">
      <div class="breadcrumb"><a href="../index.html">Start</a> &rsaquo; Quellen</div>
      <h1>Quellen &amp; Originaldokumente</h1>
      <p class="intro">
        Alle {len(DOKS)} Originaldokumente, aus denen diese Website entstanden ist &ndash; unverändert
        im Ursprungszustand. Jede Karte nennt Inhalt, Format, Größe und Übergabedatum und verweist
        auf das Projekt, das daraus aufgebaut wurde.
      </p>
    </div>
  </header>

  <main class="projekt-detail">

    <section>
      <div class="kennzahlen-grid">
        <div class="kennzahl"><strong>{len(DOKS)}</strong><span>Dokumente</span></div>
        <div class="kennzahl"><strong>{html_anz}</strong><span>HTML-Dokumentationen</span></div>
        <div class="kennzahl"><strong>{pdf_anz}</strong><span>PDF-Berichte</span></div>
        <div class="kennzahl"><strong>{gesamt/1024/1024:.0f} MB</strong><span>Gesamtumfang</span></div>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Warum diese Seite existiert:</strong> Die Projektseiten fassen zusammen, ordnen und
        rechnen nach. Diese Seite zeigt, worauf sie beruhen. Die Dateien sind exakt so abgelegt, wie
        sie übergeben wurden &ndash; ohne Kürzung, ohne Korrektur. So lässt sich jede Angabe auf der
        Website bis zur Quelle zurückverfolgen.
      </div>
    </section>

    <section>
      <h2>🗂️ Zuordnung zu den Projekten</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Projekt</th><th>Quelldokumente</th><th>Anzahl</th></tr></thead>
          <tbody>
            {zeilen}
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>📄 Alle Dokumente</h2>
      <p class="section-intro">
        „Original öffnen" öffnet die Datei in einem neuen Tab, genau so wie sie übergeben wurde.
        Die großen HTML-Dateien enthalten eingebettete Bilder und brauchen einen Moment zum Laden.
      </p>
      <div class="quellen-liste">
{karten}      </div>
    </section>

    <section>
      <h2>ℹ️ Hinweise zum Bestand</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>Zwei Dokumentenpaare sind eng verwandt</strong>Nr. 10 und 11 beschreiben dasselbe Schweißtisch-Projekt (einmal fortlaufend, einmal strukturiert). Nr. 13 und 14 sind dieselbe Zerspan-Dokumentation &ndash; einmal ohne, einmal mit eingebetteten Grafiken. Beide Fassungen sind bewusst erhalten.</span></li>
        <li><span><strong>Unverändert übernommen</strong>An keiner Datei wurde etwas geändert &ndash; nur die Dateinamen wurden vereinheitlicht und durchnummeriert, damit die Reihenfolge der Projekte erkennbar bleibt.</span></li>
        <li><span><strong>Interaktive Inhalte funktionieren weiter</strong>Die Rechner in Nr. 13 und 14 (Werkzeugpreise, Nutzwertanalyse, Amortisation, 5S-Audit) sind lauffähig, weil die Dateien vollständig sind.</span></li>
        <li><span><strong>Was diese Sammlung nicht enthält</strong>Die CAD-Modelle selbst, die Excel-Arbeitsmappe des Lagersystems und den Streamlit-Quellcode &ndash; von diesen liegen hier nur die Dokumentationen und Berichte vor.</span></li>
      </ul>
    </section>

    <nav class="projekt-nav">
      <a href="../index.html">
        <span class="richtung">&larr; Zurück</span>
        Startseite
      </a>
      <a class="naechste" href="../index.html#projekte">
        <span class="richtung">Weiter &rarr;</span>
        Projektübersicht
      </a>
    </nav>
  </main>

  <footer class="site-footer">
    Praxissemester-Dokumentation
  </footer>

  <script src="../js/main.js"></script>
</body>
</html>
"""

with open(os.path.join(ROOT, "quellen", "index.html"), "w", encoding="utf-8") as f:
    f.write(seite)
print("quellen/index.html geschrieben,", len(seite), "Zeichen |", len(DOKS), "Dokumente |", f"{gesamt/1024/1024:.1f} MB")
