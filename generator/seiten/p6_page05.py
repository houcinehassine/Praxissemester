# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt6 import *

body = seiten_kopf(5, "Grundkonzept &ndash; Idee 1 &amp; Idee 2",
    "Zwei erste CAD-Entwürfe in Autodesk Inventor: ein schlanker Kompaktrahmen gegen einen "
    "breiten Werkstattwagen mit Lochblechwänden &ndash; mit klarer Entscheidung am Ende.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>📦 Idee 1 &ndash; Kompaktrahmen mit Lamellenwand</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Merkmal</th><th>Beschreibung</th></tr></thead>
          <tbody>
            <tr><td>Grundstruktur</td><td>Geschweißter Rahmen aus Vierkant-/Rechteckrohr, hochrechteckige Bauform</td></tr>
            <tr><td>Seitenwand</td><td>Waagerechte Lamellen (Schlitzwand) &ndash; Aufnahme für Einhängehaken und Halterungen</td></tr>
            <tr><td>Oberer Korb</td><td>Offener Rahmenkasten &ndash; Platz für Schweißgerät</td></tr>
            <tr><td>Bodenplatte</td><td>Auskragend nach vorne &ndash; Standfläche für Gasflasche</td></tr>
            <tr><td>Charakter</td><td>Sehr schlank, geringe Stellfläche, hoher Schwerpunkt</td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Kritische Punkte:</strong> Kippgefahr durch hohen Schwerpunkt + schmale Basis
        &middot; nur eine Gasflasche vorgesehen (Anforderung: 2) &middot; keine Rollen im Entwurf,
        Mobilität nicht gelöst.
      </div>
    </section>

    <section>
      <h2>🛠️ Idee 2 &ndash; Werkstattwagen mit Lochblechwänden</h2>
      <p>Weiterentwickelter Entwurf: breitere Basis, mehrere Ablageebenen, umlaufende Lochblechwände und Kreuzverstrebungen zur Aussteifung.</p>
      <div class="bild-vergleich" style="margin-top:0.75rem">
        <div class="bild-box">
          <span class="label">CAD-Isometrie mit eingeblendeter Bemaßung</span>
          <img src="img/idee2-bemassung-cad.jpg" alt="CAD-Isometrie des Werkstattwagens mit Lochblechwänden, Diagonalstreben, Einhängehaken oben und grün eingeblendeten Maßen 700 mm, 1100 mm, 1500 mm und 1450 mm" />
          <p class="bildtext">Idee 2 mit den im Modell vermaßten Hauptabmessungen: Breite 700, Aufbauhöhe 1100, Gesamthöhe 1500, Länge 1450 mm.</p>
        </div>
      </div>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Maß</th><th>Wert</th><th>Bedeutung</th></tr></thead>
          <tbody>
            <tr><td>Breite</td><td>700 mm</td><td>Breite der oberen Ablage / Wagenbreite</td></tr>
            <tr><td>Höhe (Aufbau)</td><td>1100 mm</td><td>Höhe bis Oberkante Lochblechwand</td></tr>
            <tr><td>Gesamthöhe</td><td>1500 mm</td><td>Gesamthöhe inkl. Ständer/Griffbereich</td></tr>
            <tr><td>Länge / Tiefe</td><td>1450 mm</td><td>Längsausdehnung des Untergestells</td></tr>
          </tbody>
        </table>
      </div>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Baugruppe</th><th>Ausführung / Funktion</th></tr></thead>
          <tbody>
            <tr><td>Untergestell</td><td>4 Standfüße aus Rohrprofil, umlaufender Bodenrahmen mit Blecheinlage</td></tr>
            <tr><td>Untere Ablage</td><td>Bodenplatte &ndash; Stellfläche für Gasflaschen / schwere Geräte (tiefer Schwerpunkt)</td></tr>
            <tr><td>Mittlere Ablage</td><td>Zwischenboden für Schweißgerät bzw. Verbrauchsmaterial</td></tr>
            <tr><td>Obere Ablage</td><td>Arbeits-/Abstellfläche in Griffhöhe</td></tr>
            <tr><td>Lochblechwände</td><td>Umlaufend an drei Seiten &ndash; Aufnahme für Werkzeughaken (5S-Schattenbrett möglich)</td></tr>
            <tr><td>Diagonalstreben</td><td>Kreuzverstrebung gegen Verwindung &ndash; deutlich höhere Steifigkeit als Idee 1</td></tr>
            <tr><td>Einhängehaken</td><td>Umgekehrte U-Profile oben &ndash; Aufnahme für Schlauchpakete, Massekabel, Brenner</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>⚖️ Direktvergleich Idee 1 ↔ Idee 2</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Kriterium</th><th>Idee 1 (Kompaktrahmen)</th><th>Idee 2 (Werkstattwagen)</th></tr></thead>
          <tbody>
            <tr><td>Standfläche</td><td>Klein / schmal</td><td>Groß (700 × 1450 mm)</td></tr>
            <tr><td>Standsicherheit</td><td>⭐⭐ Kippgefahr</td><td>⭐⭐⭐⭐⭐ Breite Basis, tiefer Schwerpunkt</td></tr>
            <tr><td>Steifigkeit</td><td>⭐⭐⭐ Ohne Diagonalen</td><td>⭐⭐⭐⭐⭐ Kreuzverstrebt</td></tr>
            <tr><td>Ablageflächen</td><td>1 Ebene + Bodenplatte</td><td>3 Ebenen</td></tr>
            <tr><td>Werkzeugaufnahme</td><td>Lamellenwand (1 Seite)</td><td>Lochblech (3 Seiten) + Haken</td></tr>
            <tr><td>Gasflaschen</td><td>1 Stück</td><td>2 Stück möglich</td></tr>
            <tr><td>5S-Eignung</td><td>⭐⭐⭐ Begrenzt</td><td>⭐⭐⭐⭐⭐ Schattenbrett-fähig</td></tr>
            <tr><td>Materialaufwand</td><td>💰 Gering</td><td>💰💰💰 Höher</td></tr>
            <tr><td>Fertigungsaufwand</td><td>⭐⭐ Einfach</td><td>⭐⭐⭐⭐ Mehr Schweißnähte</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Zwischenfazit:</strong> Idee 2 erfüllt die Anforderungen (3 Geräte + 2 Gasflaschen,
        5S, Standsicherheit) deutlich besser und wird als Vorzugsvariante weiterverfolgt.
        Idee 1 dient als Referenz für eine schlanke Minimallösung.
      </div>
    </section>

    <section>
      <h2>❓ Offene Punkte zur Weiterbearbeitung</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>Mobilität</strong>Rollen (2 Lenk- + 2 Bockrollen) noch nicht konstruiert &ndash; Tragfähigkeit &gt; 300 kg prüfen.</span></li>
        <li><span><strong>Höhenverstellung</strong>Anforderung „höhenverstellbar“ im aktuellen Modell noch nicht umgesetzt.</span></li>
        <li><span><strong>Gasflaschensicherung</strong>Kette / Bügel nach DGUV erforderlich.</span></li>
        <li><span><strong>Länge 1450 mm</strong>für einen mobilen Wagen sehr lang &ndash; Reduktion prüfen.</span></li>
        <li><span><strong>Profilquerschnitte</strong>Wandstärken und Rohrmaße festlegen.</span></li>
        <li><span><strong>Lochbild</strong>Raster und Lochdurchmesser auf Standard-Werkzeughaken abstimmen.</span></li>
      </ul>
    </section>

{projekt_nav("04-ideensammlung.html", "Ideensammlung", "06-masse-ergonomie.html", "Maße & Ergonomie")}
  </main>
"""

write_page("05-grundkonzept.html", "Projekt 6: Grundkonzept Idee 1 & 2", body)
