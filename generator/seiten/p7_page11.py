# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt7 import *

body = seiten_kopf(11, "Arbeitssicherheit",
    "Gefährdungsbeurteilung für den Zerspanplatz &ndash; gesetzlich vorgeschrieben nach "
    "§ 5 ArbSchG. Gefährdungen erkennen, bewerten, Maßnahmen festlegen.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>⚖️ Rechtsgrundlage</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Vorschrift</th><th>Was sie fordert</th></tr></thead>
          <tbody>
            <tr><td><strong>ArbSchG § 5</strong></td><td>Pflicht zur Gefährdungsbeurteilung für jeden Arbeitsplatz</td></tr>
            <tr><td><strong>BetrSichV</strong></td><td>Sicherer Betrieb der Arbeitsmittel &ndash; hier: Dreh- und Fräsmaschine</td></tr>
            <tr><td><strong>DGUV Vorschriften / Informationen</strong></td><td>Ergänzende Regeln, z. B. Prüfung elektrischer Betriebsmittel nach DGUV V3</td></tr>
            <tr><td colspan="2">Dokumentation und regelmäßige Aktualisierung sind ebenfalls Pflicht &ndash; eine einmal erstellte Beurteilung reicht nicht.</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Warum die Beurteilung in dieses Projekt gehört:</strong> Sie ist nicht als Beiwerk
        angehängt, sondern hängt direkt an der Planung. Ob der Spänehaken in Zone A liegt, ob das
        Licht 500 lx erreicht, ob die Wege frei bleiben &ndash; das sind Planungsentscheidungen mit
        unmittelbarer Sicherheitswirkung. Wer den Platz plant, legt damit auch die Gefährdungen
        fest.
      </div>
    </section>

    <section>
      <h2>🛑 STOP-Prinzip &ndash; die Rangfolge der Maßnahmen</h2>
      <div class="stepper">
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">S</span>
            <span class="schritt-titel">Substitution</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Die Gefahr vermeiden oder ersetzen &ndash; zum Beispiel durch einen weniger gefährdenden Kühlschmierstoff. Wirksamste Stufe, weil die Gefährdung ganz entfällt.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">T</span>
            <span class="schritt-titel">Technisch</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Schutzeinrichtungen, Absaugung, Not-Aus, Spanschutzscheibe. Wirkt ohne Zutun des Menschen &ndash; deshalb Vorrang vor allen organisatorischen Regeln.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">O</span>
            <span class="schritt-titel">Organisatorisch</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Unterweisung, Reinigungsplan (hier: 5S / Seiso), freie Wege. Wirkt nur, wenn sie eingehalten wird &ndash; deshalb erst an dritter Stelle.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">P</span>
            <span class="schritt-titel">Persönlich (PSA)</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Schutzbrille, Gehörschutz, Handschuhe &ndash; ausdrücklich als <em>letzte</em> Stufe. PSA schützt nur die eine Person, die sie trägt, und nur solange sie getragen wird.</p></div>
        </div>
      </div>
    </section>

    <section>
      <h2>⚠️ Gefährdungsbeurteilung Zerspanplatz</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Gefährdung</th><th>Mögliche Folge</th><th>Schutzmaßnahme</th><th>Restrisiko</th></tr></thead>
          <tbody>
            <tr><td>Rotierende Teile / Einzug</td><td>schwere Verletzung</td><td>Schutzeinrichtung, enge Kleidung, Haarnetz, <strong>keine Handschuhe an der rotierenden Maschine</strong></td><td><span class="st-warn">mittel</span></td></tr>
            <tr><td>Späne (heiß, scharf)</td><td>Schnitt, Verbrennung, Augenverletzung</td><td>Spänehaken statt Hand, Schutzbrille, Spanschutzscheibe</td><td><span class="st-ok">gering</span></td></tr>
            <tr><td>Wegfliegende Werkstücke</td><td>Augen- / Kopfverletzung</td><td>Aufspannung prüfen, Schutzbrille, Schutzscheibe</td><td><span class="st-ok">gering</span></td></tr>
            <tr><td>Lärm der Maschinen</td><td>Gehörschäden</td><td>Gehörschutz, ggf. Lärmmessung</td><td><span class="st-ok">gering</span></td></tr>
            <tr><td>Kühlschmierstoff (Haut / Dämpfe)</td><td>Hautreizung, Ekzem</td><td>Hautschutzplan, Absaugung, Handschuhe nur bei Nacharbeit</td><td><span class="st-ok">gering</span></td></tr>
            <tr><td>Scharfe Kanten / Grat</td><td>Schnittverletzung</td><td>Entgratwerkzeug, Schnittschutzhandschuhe (nur außerhalb der Maschine)</td><td><span class="st-ok">gering</span></td></tr>
            <tr><td>Heben schwerer Werkstücke</td><td>Rückenbelastung</td><td>Hebehilfe, ergonomische Arbeitshöhe, richtige Hebetechnik</td><td><span class="st-warn">mittel</span></td></tr>
            <tr><td>Stolpern / Rutschen (Späne, Öl)</td><td>Sturz</td><td>Sauberkeit (5S / Seiso), Antirutschmatte, freie Wege</td><td><span class="st-ok">gering</span></td></tr>
            <tr><td>Elektrische Gefährdung</td><td>Stromschlag</td><td>geprüfte Betriebsmittel (DGUV V3), Not-Aus erreichbar</td><td><span class="st-ok">gering</span></td></tr>
            <tr><td>Unzureichende Beleuchtung</td><td>Fehler, Unfälle</td><td>≥ 500 lx nach DIN EN 12464-1</td><td><span class="st-ok">gering</span></td></tr>
          </tbody>
        </table>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Der wichtigste Einzelpunkt: keine Handschuhe an der rotierenden Maschine.</strong>
        Das wirkt widersprüchlich, weil Handschuhe sonst überall Schutz bedeuten. An Dreh- und
        Fräsmaschine kehrt sich das um: Ein Handschuh kann sich im rotierenden Teil verfangen und
        die Hand mitziehen &ndash; die bloße Hand nicht in gleicher Weise. Handschuhe gehören
        deshalb nur zur Nacharbeit außerhalb der Maschine. Genau diese Unterscheidung muss in der
        Unterweisung ausdrücklich angesprochen werden.
      </div>
    </section>

    <section>
      <h2>🟡 Die beiden mittleren Restrisiken</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Gefährdung</th><th>Warum das Restrisiko nicht auf „gering" sinkt</th><th>Was zusätzlich zu prüfen ist</th></tr></thead>
          <tbody>
            <tr><td>Rotierende Teile / Einzug</td><td>Die Maßnahmen sind überwiegend organisatorisch und persönlich (Kleidung, Verhalten) &ndash; die Gefahr selbst bleibt bestehen, solange die Maschine läuft.</td><td>Prüfen, ob die Schutzeinrichtungen an den vorhandenen Maschinen dem aktuellen Stand entsprechen und ob sie sich im Alltag nicht umgehen lassen.</td></tr>
            <tr><td>Heben schwerer Werkstücke</td><td>Auch bei richtiger Technik bleibt eine Belastung; sie hängt vom Werkstückgewicht ab, nicht von der Ausrüstung.</td><td>Prüfen, ob eine Hebehilfe (Kran, Hebetisch) am Platz verfügbar ist und ob die Werkbank die dabei entstehenden Lasten trägt (≥ 500 kg, Seite 6).</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>👤 Unterweisung &amp; Wiederholung</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>Erst-Unterweisung vor Arbeitsaufnahme</strong>Danach mindestens jährlich wiederholen &ndash; das ist keine Empfehlung, sondern Pflicht.</span></li>
        <li><span><strong>Themen</strong>Maschinenbedienung, Späne und PSA, Not-Aus, Verhalten im Notfall, 5S-Sauberkeit.</span></li>
        <li><span><strong>Dokumentieren</strong>Datum, Inhalt und Unterschrift festhalten &ndash; ohne Nachweis gilt die Unterweisung als nicht erfolgt.</span></li>
        <li><span><strong>Betriebsanweisungen aushängen</strong>Sichtbar an den Maschinen und an der Werkbank, nicht im Ordner.</span></li>
      </ul>
    </section>

{projekt_nav("10-wirtschaftlichkeit.html", "Wirtschaftlichkeit & Amortisation", "12-umsetzung-audit.html", "Umsetzung, Zeitplan & Audit")}
  </main>
"""

write_page("11-arbeitssicherheit.html", "Projekt 7: Arbeitssicherheit", body)
