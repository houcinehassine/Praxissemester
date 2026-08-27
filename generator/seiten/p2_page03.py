# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt2 import *

body = seiten_kopf(3, "Design der Excel-Oberfläche",
    "Vier Grundblätter bilden das Skelett des Systems: Dashboard, Artikeln Liste, "
    "Verlauf und Einstellungen. Screenshots direkt aus der Arbeitsmappe.") + f"""
  <main class="projekt-detail">

    <section>
      <div class="info-box">
        <strong>Quelle</strong>
        0102Design.pdf &middot; Beginn 24. April 2026
      </div>
    </section>

    <section>
      <h2>Blatt: Dashboard</h2>
      <p class="section-intro">Scannfunktionen &middot; Suchergebnis &middot; Exportieren</p>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Screenshot &middot; Dashboard</span>
          <img src="img/design-dashboard.jpg" alt="Dashboard-Blatt mit Scannfunktionen, Suchergebnis-Feldern und Exportbereich" />
          <p class="bildtext">Drei Bereiche: Scannfunktionen (Einbuchen/Ausbuchen/Artikel hinzufügen/löschen), Suchergebnis-Anzeige und Exportbereich mit Dateityp, Papierformat, Zielordner und E-Mail-Versand.</p>
        </div>
      </div>
    </section>

    <section>
      <h2>Blatt: Artikeln Liste</h2>
      <p class="section-intro">Scannfeld D4 &middot; Filtern nach &middot; Tabelle Artikel/Bestand</p>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Screenshot &middot; Artikeln Liste</span>
          <img src="img/design-artikelliste.png" alt="Artikeln-Liste-Blatt mit Scanfeld, Filterfeldern und leerer Bestandstabelle" />
          <p class="bildtext">Scanfeld in D4, ein Filterblock mit vier Kriterien (EAN/Barcode, Artikelform, Artikelmaterial, Material-Gruppe) und die Bestandstabelle mit Artikel- und Mengenspalten.</p>
        </div>
      </div>
    </section>

    <section>
      <h2>Blatt: Verlauf</h2>
      <p class="section-intro">Scannfeld F12 &middot; Filtern nach &middot; Tabelle Artikel/Bestand</p>
      <p>
        Gleicher Aufbau wie „Artikeln Liste“, zusätzlich mit Zeitstempel-Spalte
        „Datum+Uhr“ – hier wird jede Bewegung einzeln protokolliert statt nur
        der aktuelle Bestand.
      </p>
    </section>

    <section>
      <h2>Blatt: Einstellungen</h2>
      <p class="section-intro">Materialien-Gruppen als zentrale Nachschlagetabelle.</p>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Screenshot &middot; Einstellungen</span>
          <img src="img/design-einstellungen.png" alt="Einstellungen-Blatt mit Tabelle Materialien Gruppen: Baustahl BS, Vergütungsstahl VS, Automatenstahl AS, Edelstahl ES, Aluminium AL, Kunststoff KU" />
          <p class="bildtext">Die Tabelle „Materialien Gruppen“ legt fest, welche Buchstaben-Abkürzung (Spalte „Bezeichnung“) für jede Materialgruppe im Barcode verwendet wird – Grundlage für die automatische Barcode-Erzeugung.</p>
        </div>
      </div>
      <p style="margin-top:0.75rem">
        In späteren Versionen kommen hier weitere Nachschlagetabellen dazu:
        Profil-Abkürzungen, Lagerorte, Einheiten und Artikeltypen (Voll/Rest) –
        siehe Seite 7.
      </p>
    </section>

{projekt_nav("02-ausgangslage.html", "Ausgangslage &amp; Zielbild", "04-kernfunktionen.html", "Kernfunktionen")}
  </main>
"""

write_page("03-design.html", "Projekt 2: Design der Excel-Oberfläche", body)
