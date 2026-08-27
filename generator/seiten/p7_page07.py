# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt7 import *

body = seiten_kopf(7, "Vier Bauvarianten",
    "Teilaufgabe D: Vier grundsätzlich verschiedene Wege zur selben Werkbank &ndash; jeder in 3D "
    "dargestellt, mit Vor- und Nachteilen und einer Einordnung, für welchen Betrieb er passt.") + f"""
  <main class="projekt-detail">

    <section>
      <div class="info-box">
        <strong>Warum vier und nicht zwei:</strong> Die Aufgabenstellung nennt item-Profil und
        Standard-Werkbank. Ergänzt wurden Systemmodule als naheliegender Mittelweg und der Eigenbau
        &ndash; weil der Betrieb eine Metallwerkstatt ist und geschweißte Stahlkonstruktionen dort
        Kernkompetenz sind. Erst mit allen vieren deckt der Vergleich die reale Entscheidungslage
        ab.
      </div>
    </section>

    <section>
      <h2>1️⃣ Variante 1 &middot; item-Profil (Alu-Baukasten)</h2>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Variante 1 in 3D</span>
          <img src="img/variante1-item-profil.png" alt="Isometrische Darstellung einer Werkbank aus blauem Aluminium-Nutprofil mit Holzarbeitsplatte, Lochwand-Rückwand aus Profilen und offenem Zwischenboden aus Querstreben" />
          <p class="bildtext">Offener Rahmen aus Aluprofil mit T-Nut &ndash; Anbauteile lassen sich an jeder Stelle einhängen und wieder versetzen.</p>
        </div>
      </div>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Vorteile</th><th>Nachteile</th></tr></thead>
          <tbody>
            <tr><td>Sehr flexibel &ndash; jede Halterung ist versetzbar</td><td rowspan="3">Teuerste Option von allen vier Varianten</td></tr>
            <tr><td>Ergonomisch, Höhenverstellung gut umsetzbar</td></tr>
            <tr><td>Jederzeit erweiterbar, ohne zu schweißen oder zu bohren</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">
        Der T-Nut-Aufbau ist genau das, was ein 5S-Konzept braucht: Wenn sich beim ersten Audit
        zeigt, dass ein Haken 20 cm weiter links sitzen sollte, ist das eine Sache von einer Minute
        &ndash; kein neues Loch, kein Nachlackieren.
      </p>
    </section>

    <section>
      <h2>2️⃣ Variante 2 &middot; Stahl-Standard</h2>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Variante 2 in 3D</span>
          <img src="img/variante2-stahl-standard.png" alt="Isometrische Darstellung einer klassischen Stahlwerkbank mit geschlossenem Unterschrank, Schubladenblock und Lochwand über der Arbeitsplatte" />
          <p class="bildtext">Klassische Stahlwerkbank mit Schubladenblock &ndash; als Katalogware sofort verfügbar.</p>
        </div>
      </div>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Vorteile</th><th>Nachteile</th></tr></thead>
          <tbody>
            <tr><td>Robust &ndash; für den Werkstattbetrieb gebaut</td><td rowspan="3">Wenig flexibel: Was ab Werk nicht vorgesehen ist, lässt sich kaum nachrüsten</td></tr>
            <tr><td>Günstig in der Anschaffung</td></tr>
            <tr><td>Sofort einsatzbereit, kein Aufbau- oder Bauaufwand</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>3️⃣ Variante 3 &middot; Systemmodule</h2>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Variante 3 in 3D</span>
          <img src="img/variante3-systemmodule.png" alt="Isometrische Darstellung einer modular aufgebauten Werkbank: drei getrennte, nebeneinandergestellte Schrankmodule – zwei Schubladenblöcke und ein Türschrank – unter einer durchgehenden Holzarbeitsplatte" />
          <p class="bildtext">Drei getrennte Module unter einer durchgehenden Platte &ndash; der Mittelweg zwischen Katalogware und Baukasten. Eine Lochwand ist hier noch nicht dargestellt, wäre aber ergänzbar.</p>
        </div>
      </div>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Vorteile</th><th>Nachteile</th></tr></thead>
          <tbody>
            <tr><td>Viel Stauraum durch kombinierbare Module</td><td rowspan="3">Kosten und Flexibilität jeweils im Mittelfeld &ndash; in keiner Disziplin die beste Wahl</td></tr>
            <tr><td>Später erweiterbar durch zusätzliche Module</td></tr>
            <tr><td>Gute Ordnung ab Werk (Schubladeneinteilung)</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>4️⃣ Variante 4 &middot; Eigenbau (Schweißkonstruktion)</h2>
      <div class="bild-vergleich">
        <div class="bild-box">
          <span class="label">Variante 4 in 3D</span>
          <img src="img/variante4-eigenbau.png" alt="Isometrische Darstellung einer selbstgebauten Werkbank aus geschweißten dunklen Stahl-Vierkantrohren mit zwei Holzplatten als Arbeits- und Ablagefläche" />
          <p class="bildtext">Geschweißte Stahlrohre mit aufgelegter Platte &ndash; im Material die mit Abstand günstigste Lösung.</p>
        </div>
      </div>
      <div class="tabelle-wrapper" style="margin-top:0.75rem">
        <table class="tabelle">
          <thead><tr><th>Vorteile</th><th>Nachteile</th></tr></thead>
          <tbody>
            <tr><td>Sehr günstig im Material (~800&ndash;1.500 €)</td><td rowspan="3">Hoher Bauaufwand &ndash; die Arbeitszeit fehlt an anderer Stelle; Optik variabel je nach Ausführung</td></tr>
            <tr><td>Robust &ndash; Dimensionierung frei wählbar</td></tr>
            <tr><td>Passgenau auf den Platz und die Maschinen zugeschnitten</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Querbezug zu Projekt 5 und 6:</strong> Genau diese Bauweise wurde beim Schweißtisch
        und beim Schweißwagen tatsächlich gewählt &ndash; dort mit fertigungsreifen
        Zeichnungssätzen. Der Betrieb kann das also. Beim Zerspanplatz spricht trotzdem etwas
        dagegen: Die Werkbank soll <em>schnell</em> stehen und Ordnung bringen, nicht selbst ein
        Konstruktionsprojekt werden.
      </div>
    </section>

    <section>
      <h2>⚖️ Alle vier im direkten Vergleich</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Variante</th><th>Vorteile</th><th>Nachteile</th><th>Anschaffung</th></tr></thead>
          <tbody>
            <tr><td><strong>V1 &middot; item-Profil</strong></td><td>Sehr flexibel, ergonomisch, erweiterbar</td><td>Teuerste Option</td><td>4.000&ndash;7.000 €</td></tr>
            <tr><td><strong>V2 &middot; Stahl-Standard</strong></td><td>Robust, günstig, sofort einsatzbereit</td><td>Wenig flexibel</td><td>1.500&ndash;3.000 €</td></tr>
            <tr><td><strong>V3 &middot; Systemmodule</strong></td><td>Viel Stauraum, erweiterbar, gute Ordnung</td><td>Mittlere Kosten &amp; Flexibilität</td><td>2.500&ndash;4.500 €</td></tr>
            <tr><td><strong>V4 &middot; Eigenbau</strong></td><td>Sehr günstig im Material, robust, passgenau</td><td>Hoher Bauaufwand, Optik variabel</td><td>~800&ndash;1.500 € Material</td></tr>
          </tbody>
        </table>
      </div>
      <p style="margin-top:0.75rem">
        Die Spanne zwischen der günstigsten und der teuersten Variante beträgt rund das Fünffache.
        Ob dieser Aufpreis gerechtfertigt ist, lässt sich nicht am Preis allein entscheiden &ndash;
        dafür ist die gewichtete Nutzwertanalyse auf Seite 9 da.
      </p>
    </section>

{projekt_nav("06-werkbank-masse.html", "Werkbank: Maße & Ergonomie", "08-layout-konzepte.html", "4 Layout-Konzepte")}
  </main>
"""

write_page("07-varianten.html", "Projekt 7: 4 Bauvarianten", body)
