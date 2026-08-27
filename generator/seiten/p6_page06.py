# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt6 import *

body = seiten_kopf(6, "Maße &amp; Ergonomie",
    "Grundfläche, Höhen und Positionen mit typischen Startwerten &ndash; und der dabei aufgedeckte "
    "Widerspruch zwischen Annahme und realem Aufmaß.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>1️⃣ Maße (typische Startwerte)</h2>
      <p class="section-intro">Annahmen &ndash; laut Originaldokument später durch echte Maße zu ersetzen.</p>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Maß</th><th>Wert</th><th>Bemerkung</th></tr></thead>
          <tbody>
            <tr><td>Grundfläche (Stellfläche)</td><td>~750 × 1000 mm</td><td>fasst Maschine auf Auszug + Flasche</td></tr>
            <tr><td>Arbeitshöhe / obere Ablage</td><td>~900 mm</td><td>bequem stehend</td></tr>
            <tr><td>Gerätefach (nutzbar)</td><td>~560 × 900 × 850 mm</td><td>für die Maschine, auf Auszug</td></tr>
            <tr><td>MIG-Maschine (Annahme)</td><td>~500 × 850 × 800 mm</td><td>Typenschild-Maß nachtragen</td></tr>
            <tr><td>Gasflasche (50 L)</td><td>Ø230 × 1500 mm</td><td>hinten, stehend, angekettet</td></tr>
            <tr><td>Rollen</td><td>Ø160 mm</td><td>4×, 2 mit Feststellbremse</td></tr>
            <tr><td>Gesamthöhe (mit Flasche)</td><td>~1650 mm</td><td>Flasche überragt Ablage</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>⚠️ Abgleich: Annahme vs. reales Aufmaß</h2>
      <p>Die Startwerte weichen deutlich vom Aufmaß vor Ort (Seite 2) ab. Vor der Detailkonstruktion muss geklärt werden, welche Werte gelten.</p>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Bauteil / Maß</th><th>Annahme</th><th>Aufmaß vor Ort</th><th>Abweichung</th></tr></thead>
          <tbody>
            <tr><td>MIG-Maschine Breite</td><td>~500 mm</td><td>430 mm</td><td>&minus;70 mm</td></tr>
            <tr><td>MIG-Maschine Tiefe</td><td>~850 mm</td><td>610 mm</td><td>&minus;240 mm</td></tr>
            <tr><td>MIG-Maschine Höhe</td><td>~800 mm</td><td>520 mm</td><td>&minus;280 mm</td></tr>
            <tr><td>Gasflasche Ø</td><td>Ø230 mm</td><td>Ø220 mm</td><td>&minus;10 mm</td></tr>
            <tr><td>Gasflasche Höhe</td><td>1500 mm</td><td>1640 mm</td><td>+140 mm</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Interpretation:</strong> Die Annahme-Maße sind deutlich größer als die gemessene
        Maschine. Zwei mögliche Erklärungen: Es ist eine andere/größere Maschine gemeint, oder die
        Annahme enthält bereits Sicherheitszuschläge für Anschlüsse und Bedienraum.
        Empfehlung: Annahme als Bauraum-Reserve beibehalten, aber im Bericht als solche kennzeichnen.
      </div>
    </section>

    <section>
      <h2>2️⃣ Kernkonzept: Maschine auf Schwerlast-Vollauszug</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Anforderung</th><th>Beschreibung</th><th>Konstruktive Folge</th></tr></thead>
          <tbody>
            <tr><td>Tragfähigkeit</td><td>Auszug für Maschinengewicht auslegen: ~80&ndash;100 kg</td><td>Schwerlastauszug ≥ 100 kg wählen (Sicherheit einrechnen)</td></tr>
            <tr><td>Verriegelung</td><td>Auszug darf beim Fahren nicht selbsttätig aufgehen</td><td>Push-to-open-Sperre oder separater Riegel</td></tr>
            <tr><td>Kabellänge</td><td>Schlauchpaket und Kabel müssen beim Ausziehen mitgehen</td><td>Überlänge + definierte Kabelführung (Haspel/Schleife)</td></tr>
            <tr><td>Kippmoment</td><td>Bei ausgezogener Maschine verlagert sich der Schwerpunkt nach vorne</td><td>Standsicherheit im ausgezogenen Zustand nachweisen</td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Kritischer Punkt &ndash; Standsicherheit im Auszugszustand:</strong> Bei ~80&ndash;100 kg
        Maschine auf Vollauszug wandert der Schwerpunkt weit über die Vorderachse hinaus.
        Gegenmaßnahmen: Feststellbremsen zwingend anziehen, Gasflasche als Gegengewicht hinten,
        ggf. Ausklappstütze. Der Nachweis ist erforderlich &ndash; nicht nur im eingefahrenen
        Zustand rechnen.
      </div>
    </section>

    <section>
      <h2>🧍 Ergonomische Bewertung</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Kriterium</th><th>Wert</th><th>Bewertung</th></tr></thead>
          <tbody>
            <tr><td>Arbeitshöhe</td><td>900 mm</td><td><span class="st-ok">✅ Gut</span> &ndash; typische Greifhöhe stehend liegt bei 850&ndash;1100 mm</td></tr>
            <tr><td>Bedienhöhe Maschine</td><td>ca. 300&ndash;850 mm</td><td><span class="st-warn">⚠️</span> Untere Bedienelemente erfordern Bücken &ndash; Auszug mildert das ab</td></tr>
            <tr><td>Flaschenwechsel</td><td>Flasche ~1500&ndash;1640 mm</td><td><span class="st-warn">⚠️</span> Schwer (ca. 60&ndash;75 kg voll) &ndash; Hebehilfe / niedrige Aufstellebene nötig</td></tr>
            <tr><td>Rollendurchmesser</td><td>Ø160 mm</td><td><span class="st-ok">✅ Gut</span> &ndash; große Rollen überwinden Schwellen und Kabel leichter</td></tr>
            <tr><td>Schiebekraft</td><td>&mdash;</td><td><span class="st-no">❌</span> Noch nicht bewertet &ndash; Gesamtmasse abschätzen</td></tr>
            <tr><td>Griffhöhe</td><td>&mdash;</td><td><span class="st-no">❌</span> Noch nicht festgelegt &ndash; Empfehlung 950&ndash;1150 mm</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>⚖️ Grobe Gewichtsabschätzung (für Rollenauswahl)</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Position</th><th>Masse (ca.)</th><th>Grundlage</th></tr></thead>
          <tbody>
            <tr><td>MIG-Maschine</td><td>80&ndash;100 kg</td><td>Angabe aus der Auszugsauslegung</td></tr>
            <tr><td>Gasflasche 50 L (voll)</td><td>60&ndash;75 kg</td><td>Erfahrungswert Stahlflasche</td></tr>
            <tr><td>Schubladenblock + Inhalt</td><td>25&ndash;40 kg</td><td>Zukaufteil + Verbrauchsmaterial</td></tr>
            <tr><td>Werkzeug, PSA, Feuerlöscher</td><td>10&ndash;15 kg</td><td>Schätzung</td></tr>
            <tr><td>Rahmen (Kantrohr, Bleche)</td><td>40&ndash;60 kg</td><td>Abhängig von Profilwahl</td></tr>
            <tr class="total-row"><td>Gesamt</td><td>≈ 215&ndash;290 kg</td><td>&rarr; Rollen ≥ 100 kg Tragkraft je Rolle wählen</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">
        Bei 4 Rollen und 290 kg ergibt sich rechnerisch ~73 kg je Rolle. Da sich die Last beim
        Fahren ungleich verteilt (besonders bei ausgezogener Maschine), sollten Rollen mit
        mindestens 100&ndash;150 kg Tragkraft gewählt werden.
      </p>
    </section>

    <section>
      <h2>❓ Offene Punkte O-01 bis O-07</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Nr.</th><th>Offener Punkt</th><th>Benötigt für</th></tr></thead>
          <tbody>
            <tr><td>O-01</td><td>Typenschild-Maße und Gewicht der MIG-Maschine</td><td>Gerätefach, Auszugsauswahl</td></tr>
            <tr><td>O-02</td><td>Widerspruch Maschinenmaße: 500×850×800 vs. 430×610×520</td><td>Rahmenmaße</td></tr>
            <tr><td>O-03</td><td>Maßgebende Flaschengröße (1500 / 1640 / &gt;1800 mm?)</td><td>Halterung, Gesamthöhe</td></tr>
            <tr><td>O-04</td><td>Einbaumaß des zugekauften Schubladenblocks</td><td>Rahmenaufteilung</td></tr>
            <tr><td>O-05</td><td>Seitenansicht als CAD-Zeichnung</td><td>Dokumentation</td></tr>
            <tr><td>O-06</td><td>Standsicherheitsnachweis bei ausgezogener Maschine</td><td>Sicherheit</td></tr>
            <tr><td>O-07</td><td>Griffposition und -höhe</td><td>Ergonomie</td></tr>
          </tbody>
        </table>
      </div>
    </section>

{projekt_nav("05-grundkonzept.html", "Grundkonzept: Idee 1 & 2", "07-variante-a-neubau.html", "Variante A: Neubau SW-001")}
  </main>
"""

write_page("06-masse-ergonomie.html", "Projekt 6: Maße & Ergonomie", body)
