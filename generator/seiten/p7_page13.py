# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt7 import *

body = seiten_kopf(13, "Fazit, Quellen &amp; Normen",
    "Was das Konzept leistet, was ehrlicherweise offen bleibt &ndash; und die vollständige "
    "Übersicht der Normen und Regelwerke, an denen sich die Planung orientiert.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>📊 Stand am Projektende</h2>
      <div class="kennzahlen-grid">
        <div class="kennzahl"><strong>5/5</strong><span>Teilaufgaben bearbeitet</span></div>
        <div class="kennzahl"><strong>35</strong><span>Werkzeugpositionen bepreist</span></div>
        <div class="kennzahl"><strong>8</strong><span>Varianten &amp; Konzepte bewertet</span></div>
        <div class="kennzahl"><strong>10</strong><span>Gefährdungen beurteilt</span></div>
      </div>
      <p style="margin-top:0.75rem">
        Aus einer Aufgabenstellung in einem Satz ist ein durchgerechnetes Arbeitsplatzkonzept
        geworden: vollständige Werkzeugliste mit Preisen, 5S-Ordnung mit Zonenzuordnung, vier
        Bauvarianten und vier Layout-Konzepte in 3D, eine gewichtete Nutzwertanalyse, eine
        Amortisationsrechnung mit Sensitivitätsbetrachtung und eine Gefährdungsbeurteilung nach
        § 5 ArbSchG.
      </p>
    </section>

    <section>
      <h2>✅ Was das Konzept leistet</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>Vollständigkeit statt Auswahl</strong>Der Werkzeugbedarf ist nach Arbeitsschritt aufgenommen, nicht nach Katalog &ndash; dadurch fallen Lücken beim Durchgehen auf. 35 Positionen in sechs Gruppen, inklusive Nacharbeit und Hilfsmitteln, die sonst gern vergessen werden.</span></li>
        <li><span><strong>Jede Entscheidung mit Zahlen hinterlegt</strong>Die Werkzeugliste ergibt 4.825 € netto, die Nutzwertanalyse einen Rangwert je Variante, die Amortisationsrechnung 26,5 Monate. Nichts davon beruht auf „das passt schon".</span></li>
        <li><span><strong>5S nicht als Schlagwort</strong>Die fünf S sind konkret am Platz umgesetzt und in Zonen A/B/C übersetzt &ndash; mit einer Begründung, warum welches Werkzeug in welcher Zone liegt.</span></li>
        <li><span><strong>Das Layout bildet die Ordnung ab</strong>Konzept 2 wurde nicht gewählt, weil es hübsch aussieht, sondern weil Lochwand, Schubladen und Hochschränke genau den drei Zonen entsprechen.</span></li>
        <li><span><strong>Sicherheit mitgeplant, nicht angehängt</strong>Spänehaken in Zone A, 500 lx Beleuchtung, freie Wege &ndash; die Gefährdungsbeurteilung greift auf Planungsentscheidungen zurück, statt sie nachträglich zu bewerten.</span></li>
      </ul>
    </section>

    <section>
      <h2>🧠 Was das Projekt methodisch gezeigt hat</h2>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>📉 Ein knappes Ergebnis ist auch ein Ergebnis</h4><p>0,20 Punkte Abstand zwischen Platz 1 und 2 tragen keine Entscheidung. Das ehrlich zu sagen ist wertvoller, als einen Sieger auszurufen.</p></div>
        <div class="mini-karte"><h4>🎚️ Annahmen durchrechnen</h4><p>Erst die Sensitivitätsbetrachtung zeigt, dass die Wirtschaftlichkeit selbst bei halbierter Zeitersparnis trägt &ndash; das macht die Aussage belastbar.</p></div>
        <div class="mini-karte"><h4>🔗 Alles hängt zusammen</h4><p>Die Banktiefe von 600 mm entscheidet über ein Layout-Konzept, die Zonenlogik über die Schrankaufteilung, der Spänehaken über eine Gefährdung.</p></div>
        <div class="mini-karte"><h4>👥 Drei Personen ändern alles</h4><p>Mengen, Bankbreite, Höhenverstellung, Standardisierung &ndash; fast jede Festlegung folgt aus dieser einen Rahmenbedingung.</p></div>
      </div>
    </section>

    <section>
      <h2>❗ Was ehrlicherweise offen bleibt</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Prio</th><th>Offener Punkt</th><th>Nächster Schritt</th></tr></thead>
          <tbody>
            <tr><td><span class="prio prio--hoch">hoch</span></td><td>Bauvariante nicht entschieden</td><td>Angebote für item-Profil und Systemmodule einholen &ndash; die Nutzwertanalyse kann es allein nicht klären</td></tr>
            <tr><td><span class="prio prio--hoch">hoch</span></td><td>Alle Preise sind Richtwerte, keine Angebote</td><td>Marktrecherche durch echte Angebote ersetzen; Kostenliste und Amortisation rechnen dann neu</td></tr>
            <tr><td><span class="prio prio--hoch">hoch</span></td><td>Raum- und Maschinenmaße sind Beispielannahmen</td><td>Werkstatt real aufmessen und Grundriss aktualisieren</td></tr>
            <tr><td><span class="prio prio--mittel">mittel</span></td><td>Wandverankerung der Hochschränke ungeprüft</td><td>Wandaufbau und Tragfähigkeit vor Ort feststellen</td></tr>
            <tr><td><span class="prio prio--mittel">mittel</span></td><td>Traglast 500 kg nicht gegen ein Produkt geprüft</td><td>Datenblatt des gewählten Fabrikats gegen die Anforderung halten</td></tr>
            <tr><td><span class="prio prio--mittel">mittel</span></td><td>Beleuchtungsstärke nicht gemessen</td><td>500 lx am Platz nachmessen; ggf. Zusatzleuchte einplanen</td></tr>
            <tr><td><span class="prio prio--niedrig">niedrig</span></td><td>Belegungsplan der Lochwand fehlt</td><td>Shadow-Board zeichnen: welches Werkzeug an welche Position</td></tr>
            <tr><td><span class="prio prio--niedrig">niedrig</span></td><td>Zeitraum-Unschärfe beim ersten Audit</td><td>Klären, ob Phase 7 noch in den Projektzeitraum fällt (Seite 12)</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Der gemeinsame Nenner dieser Punkte:</strong> Sie alle betreffen den Schritt von
        der Planung in die Realität &ndash; echte Angebote statt Richtpreise, echte Raummaße statt
        Annahmen, echte Messwerte statt Normvorgaben. Die Planung selbst ist vollständig; was
        fehlt, ist ihre Bestätigung vor Ort.
      </div>
    </section>

    <section>
      <h2>📚 Quellen &amp; Normbezug</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Thema</th><th>Norm / Regelwerk</th><th>Kernaussage</th></tr></thead>
          <tbody>
            <tr><td>Ergonomie / Arbeitshöhe</td><td>DIN EN ISO 14738</td><td>Arbeitsplatzmaße aus Körpermaßen (Ellenbogenhöhe); stehend ca. 850&ndash;1050 mm, Höhenverstellung empfohlen</td></tr>
            <tr><td>Körpermaße</td><td>DIN 33402-2</td><td>Perzentil-Körpermaße als Auslegungsgrundlage</td></tr>
            <tr><td>Grundsätze Ergonomie</td><td>DIN EN ISO 6385</td><td>Ergonomische Gestaltung von Arbeitssystemen</td></tr>
            <tr><td>Beleuchtung</td><td>DIN EN 12464-1 &middot; ASR A3.4</td><td>Wartungswerte: Grobbearbeitung 300 lx, mittlere Maschinen-/Montagearbeit 500 lx, Feinarbeit 750 lx</td></tr>
            <tr><td>Arbeitsstätte / Sicherheit</td><td>ArbStättV + ASR &middot; BetrSichV</td><td>Anforderungen an Arbeitsstätten, Verkehrswege, Betrieb von Arbeitsmitteln</td></tr>
            <tr><td>Maschinensicherheit</td><td>DIN EN ISO 12100</td><td>Risikobeurteilung und Risikominderung an Maschinen</td></tr>
            <tr><td>PSA</td><td>EN 166 &middot; EN 352 &middot; EN 388</td><td>Augenschutz &middot; Gehörschutz &middot; Schutzhandschuhe</td></tr>
            <tr><td>5S-Methode</td><td>Lean / Toyota-Produktionssystem</td><td>Ordnungsmethode (keine DIN-Norm); ergänzt das Qualitätsmanagement nach DIN EN ISO 9001</td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Datenhinweis zur gesamten Dokumentation:</strong> Preise sind Netto-Richtwerte aus
        Marktrecherche &ndash; Beispielwerte, keine Angebote. Raum- und Maschinenmaße im Grundriss
        sind Beispielannahmen. Vor der Umsetzung sind beide durch reale Angebote und die jeweils
        gültige Normfassung zu ersetzen.
      </div>
    </section>

    <section>
      <h2>🔗 Zusammenhang mit den anderen Projekten</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Projekt</th><th>Verbindung zum Zerspanarbeitsplatz</th></tr></thead>
          <tbody>
            <tr><td><a href="../projekt-4/index.html">Projekt 4 &ndash; Schweißarbeitsplatz</a></td><td>Dieselbe Methodik auf den Schweißbereich angewandt: Werkzeugliste, Nutzwertanalyse, feste Station nach 5S. Der Zerspanplatz geht darüber hinaus mit Amortisationsrechnung und Gefährdungsbeurteilung.</td></tr>
            <tr><td><a href="../projekt-5/index.html">Projekt 5 &ndash; Schweißtisch</a></td><td>Zeigt, wie eine Eigenbau-Variante konkret aussieht, wenn sie durchkonstruiert wird &ndash; genau der Aufwand, der hier bei Variante 4 nur bewertet, aber nicht betrieben wurde.</td></tr>
            <tr><td><a href="../projekt-6/index.html">Projekt 6 &ndash; Schweißwagen</a></td><td>Der mobile Werkzeugwagen aus Layout-Konzept 3 entspricht dem Gedanken des Schweißwagens: Werkzeug fährt zum Werkstück statt umgekehrt.</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>💬 Persönliches Fazit</h2>
      <div class="zitat-box">
        Am lehrreichsten war die Nutzwertanalyse &ndash; aber nicht, weil sie eine Antwort geliefert
        hat, sondern weil sie keine eindeutige geliefert hat. 4,15 gegen 3,95 sieht nach einem
        Sieger aus, ist aber innerhalb der Schätzunsicherheit ein Gleichstand. Diese Grenze der
        eigenen Methode zu erkennen und nicht zu überspielen, halte ich für das Wichtigste, was ich
        aus diesem Projekt mitnehme.
      </div>
    </section>

{projekt_nav("12-umsetzung-audit.html", "Umsetzung, Zeitplan & Audit", "../../index.html#projekte", "Zurück zur Projektübersicht")}
  </main>
"""

write_page("13-fazit-quellen.html", "Projekt 7: Fazit, Quellen & Normen", body)
