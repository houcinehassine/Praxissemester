# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt4 import *

body = seiten_kopf(2, "Grundlagen verstehen",
    "Drei Begriffe, die im Projekt ständig vorkommen: die Schweißverfahren (MAG/MIG &amp; E-Hand), "
    "die 5S-Methode und das Item-Profil-System &ndash; von Grund auf erklärt.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>Kurz: Was passiert beim Schweißen?</h2>
      <ul class="ergebnis-liste">
        <li><span>Zwei Metallteile werden durch große Hitze verschmolzen &ndash; dauerhaft verbunden.</span></li>
        <li><span>Die Hitze kommt vom Lichtbogen &ndash; ein elektrischer „Dauerfunke“ zwischen Elektrode und Werkstück (mehrere tausend °C).</span></li>
        <li><span>Meist kommt Zusatzmaterial dazu (Draht oder Stab), das die Fuge auffüllt.</span></li>
      </ul>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Der eine Unterschied, den man sich merken muss:</strong>
        Luft (Sauerstoff) macht die Naht schlecht &ndash; das Schmelzbad muss geschützt werden.
        MAG/MIG schützt mit Gas aus einer Flasche. E-Hand schützt sich selbst &ndash; durch die
        Umhüllung der Stabelektrode, die zu Schutzgas + Schlacke verbrennt.
      </div>
    </section>

    <section>
      <h2>Verfahren 1: MAG/MIG (Schutzgas)</h2>
      <p>
        Die vorhandene Maschine am Platz. „MAG“ = Aktivgas (für Stahl), „MIG“ = Inertgas (für
        Alu/Edelstahl) &ndash; die Technik ist identisch.
      </p>
      <p style="margin-top:0.75rem"><strong>So funktioniert&rsquo;s:</strong> Endlos-Draht wird
      automatisch nachgeschoben &ndash; er ist Elektrode und Zusatzmaterial in einem. Aus der Düse
      strömt Schutzgas und legt sich schützend übers Schmelzbad. Ein Druck auf den
      Brennerknopf genügt; man „zieht“ statt ständig neu anzusetzen.</p>
      <div class="karten-grid-4" style="margin-top:0.75rem">
        <div class="mini-karte"><h4>+ Stärken</h4><p>Schnell, leicht zu lernen, kaum Nacharbeit (keine Schlacke); ideal für viel Naht, dünne bis mittlere Bleche.</p></div>
        <div class="mini-karte"><h4>&minus; Schwächen</h4><p>Braucht Gasflasche, ist zugempfindlich (drinnen kein Problem); Gerät größer/teurer.</p></div>
      </div>
    </section>

    <section>
      <h2>Verfahren 2: E-Hand (Stabelektrode)</h2>
      <p>
        Das zweite geforderte Verfahren &ndash; „Lichtbogenhandschweißen“: robust und ohne
        Gasflasche.
      </p>
      <p style="margin-top:0.75rem"><strong>So funktioniert&rsquo;s:</strong> Ein Metallstab mit
      Umhüllung steckt im Halter. Beim Schweißen verbrennt die Umhüllung &ndash; erzeugt selbst
      Schutzgas und eine Schlacke-Schicht, die die Naht abdeckt. Die Elektrode wird kürzer und
      muss gewechselt werden (kein Endlos-Draht).</p>
      <div class="karten-grid-4" style="margin-top:0.75rem">
        <div class="mini-karte"><h4>+ Stärken</h4><p>Kein Gas nötig, einfaches robustes Gerät, funktioniert im Wind/draußen; gut für dickeres Material, Reparaturen, enge Stellen.</p></div>
        <div class="mini-karte"><h4>&minus; Schwächen</h4><p>Schlacke abklopfen nötig &ndash; mehr Nacharbeit; mehr Übung für eine schöne Naht, Elektrodenwechsel.</p></div>
      </div>
    </section>

    <section>
      <h2>MAG/MIG vs. E-Hand &ndash; direkt verglichen</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Kriterium</th><th>MAG/MIG (Schutzgas)</th><th>E-Hand (Stabelektrode)</th></tr></thead>
          <tbody>
            <tr><td>Schutz der Naht</td><td>Gas aus Flasche</td><td>Umhüllung &rarr; Gas + Schlacke</td></tr>
            <tr><td>Zusatzmaterial</td><td>Endlos-Draht (automatisch)</td><td>Stabelektrode (wechseln)</td></tr>
            <tr><td>Tempo</td><td>Schnell</td><td>Mittel</td></tr>
            <tr><td>Nacharbeit</td><td>Wenig (keine Schlacke)</td><td>Schlacke abklopfen</td></tr>
            <tr><td>Lernaufwand</td><td>Einfacher</td><td>Mehr Übung</td></tr>
            <tr><td>Wind/Zug</td><td>Empfindlich &rarr; drinnen</td><td>Unempfindlich</td></tr>
            <tr><td>Gasflasche</td><td>Nötig</td><td>Nicht nötig</td></tr>
            <tr><td>Typisch für</td><td>Alltag, viel Naht, dünn&ndash;mittel</td><td>Reparatur, dick, wo kein Gas</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        Für den Platz heißt das: MAG/MIG ist das Haupt-Verfahren (schnell, sauber), E-Hand deckt
        Sonderfälle ab. Der Arbeitsplatz braucht Werkzeuge für beides.
      </div>
    </section>

    <section>
      <h2>Und die „Nachbearbeitung“?</h2>
      <p>Der Arbeitgeber will Werkzeuge für Schweißen UND Nachbearbeitung &ndash; das sind die Arbeiten NACH der Naht:</p>
      <ul class="ergebnis-liste">
        <li><span><strong>Schlacke abklopfen</strong>(bei E-Hand) &rarr; Schlackenhammer.</span></li>
        <li><span><strong>Schweißspritzer entfernen</strong>&rarr; Meißel/Bürste.</span></li>
        <li><span><strong>Schleifen</strong>&ndash; Naht glätten, Kanten entgraten &rarr; Winkelschleifer.</span></li>
        <li><span><strong>Bürsten</strong>&ndash; Naht reinigen &rarr; Drahtbürste.</span></li>
        <li><span><strong>Prüfen</strong>&ndash; Maß &amp; Naht kontrollieren &rarr; Messwerkzeug.</span></li>
        <li><span><strong>Reinigen</strong>&ndash; Arbeitsplatz sauber halten.</span></li>
      </ul>
    </section>

    <section>
      <h2>Die 5S-Methode &ndash; Ordnung mit System</h2>
      <p>5S ist eine Methode aus der Lean-Produktion für saubere, effiziente Arbeitsplätze &ndash; fünf Schritte, alle beginnen (im Japanischen) mit „S“. Genau das will der Arbeitgeber sehen.</p>
      <div class="stepper">
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">1</span>
            <span class="schritt-titel">Sortieren (Seiri)</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Nur behalten, was wirklich gebraucht wird. Rest weg.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">2</span>
            <span class="schritt-titel">Systematisieren (Seiton)</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Fester, beschrifteter Platz für jedes Werkzeug.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">3</span>
            <span class="schritt-titel">Säubern (Seiso)</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Sauber halten: Spritzer &amp; Schleifstaub weg.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">4</span>
            <span class="schritt-titel">Standardisieren (Seiketsu)</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Gleiche Ordnung für alle &ndash; Regeln, Schattenbretter.</p></div>
        </div>
        <div class="schritt">
          <button class="schritt-button" aria-expanded="false">
            <span class="schritt-nummer">5</span>
            <span class="schritt-titel">Selbstdisziplin (Shitsuke)</span>
            <span class="schritt-pfeil">&#9662;</span>
          </button>
          <div class="schritt-inhalt"><p>Dranbleiben, zur Gewohnheit machen.</p></div>
        </div>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>So sieht 5S am Schweißplatz aus:</strong>
        1 nur nötige Werkzeuge &middot; 2 Lochwand mit Umriss je Werkzeug (Schattenbrett) &middot;
        3 Ablage für Schleifstaub, Absaugung &middot; 4 gleicher Aufbau für alle 3 Mitarbeiter &middot;
        5 Werkzeug nach Gebrauch zurücklegen. Das „feste Station + Wagen“-Konzept (Seite 3) setzt
        1, 2 und 4 bereits praktisch um.
      </div>
    </section>

    <section>
      <h2>Item-Profil vs. „normale Werkbank“</h2>
      <p class="section-intro">Die zwei Bauweisen, die ursprünglich gegenübergestellt werden sollten. Beide bauen dasselbe &ndash; aber ganz anders.</p>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>🧩 Item-Profil</h4><p>Alu-Baukasten mit T-Nuten, zusammengeschraubt wie „Metall-Lego“. + Kein Schweißen, sehr flexibel &amp; umbaubar, sauber, leicht. + Zubehör einfach anklemmbar. &minus; Teurer pro Meter. &minus; Alu + Hitze/Spritzer heikel &ndash; als heiße Schweiß-Oberfläche ungeeignet.</p></div>
        <div class="mini-karte"><h4>🔩 Normale Werkbank</h4><p>Stahlrohr/-platte, geschweißt und lackiert. + Sehr robust &amp; schwer, steht stabil. + Günstiger im Material, hält Hitze &amp; Spritzer gut aus. + Ideal als heiße Schweiß-Tischplatte. &minus; Starr, muss geschweißt/lackiert werden.</p></div>
      </div>
      <div class="warn-box" style="margin-top:0.75rem">
        <strong>Kleiner Profi-Gedanke fürs Projekt:</strong> Oft ist eine Mischung am schlausten &ndash;
        die heiße Tischplatte aus Stahl, für Gestell/Wagen ebenfalls Stahl und für die Station
        Kaufteile. Genau diese Kombination wurde am Ende umgesetzt: Item wurde im Projekt nicht
        gebaut (siehe Seite 3, Nutzungskonzept).
      </div>
    </section>

{projekt_nav("index.html", "Überblick", "03-rahmenbedingungen.html", "Rahmenbedingungen")}
  </main>
"""

write_page("02-grundlagen.html", "Projekt 4: Grundlagen", body)
