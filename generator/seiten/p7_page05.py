# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt7 import *

body = seiten_kopf(5, "5S-Ordnung &amp; Zonen A/B/C",
    "Teilaufgabe C: Die fünf S nicht als Theorie, sondern konkret an diesem Platz &ndash; und die "
    "Zuordnung jedes einzelnen Werkzeugs aus der Liste zu Zone A, B oder C.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>🈵 Die fünf Schritte am Arbeitsplatz</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>S</th><th>Bedeutung</th><th>Umsetzung an diesem Platz</th></tr></thead>
          <tbody>
            <tr><td><strong>Seiri</strong></td><td>Sortieren</td><td>Nur benötigte Werkzeuge am Platz; Defektes und Doppeltes aussortieren</td></tr>
            <tr><td><strong>Seiton</strong></td><td>Systematisieren</td><td>Fester Platz mit Beschriftung, Shadow-Board an der Lochwand, Schaumeinlagen in den Schubladen</td></tr>
            <tr><td><strong>Seiso</strong></td><td>Säubern</td><td>Späne täglich entfernen, Messmittel sauber und geölt halten</td></tr>
            <tr><td><strong>Seiketsu</strong></td><td>Standardisieren</td><td>Foto-Standard des Sollzustands, Farbcodes, gleiche Regeln für alle drei Personen</td></tr>
            <tr><td><strong>Shitsuke</strong></td><td>Selbstdisziplin</td><td>Schichtende-Check, regelmäßiges Audit (Checkliste auf Seite 12)</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Der eigentliche Knackpunkt ist das fünfte S:</strong> Sortieren, Aufräumen und
        Putzen schafft jeder einmal. Ob die Ordnung nach drei Monaten noch steht, entscheidet
        allein Shitsuke &ndash; und das braucht etwas Messbares. Deshalb gehört die
        Audit-Checkliste mit ihren 20 Punkten zwingend zum Konzept und nicht als optionale Beigabe
        ans Ende.
      </div>
    </section>

    <section>
      <h2>🎨 Das Zonenprinzip</h2>
      <p>
        Die Grundregel lautet: <strong>oft gebraucht = greifbar, selten gebraucht = im Schrank</strong>.
        Daraus ergeben sich drei Zonen, die zugleich der räumlichen Aufteilung von Konzept 2
        entsprechen (Seite 8):
      </p>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>🅰️ Zone A &middot; täglich</h4><p>Lochwand mittig über der Bank &ndash; ohne einen Schritt zu gehen erreichbar.</p></div>
        <div class="mini-karte"><h4>🅱️ Zone B &middot; wöchentlich</h4><p>Schubladen unter der Arbeitsplatte &ndash; ein Griff nach unten.</p></div>
        <div class="mini-karte"><h4>🅲 Zone C &middot; selten</h4><p>Hochschrank seitlich &ndash; ein bis zwei Schritte, dafür geschlossen und staubfrei.</p></div>
      </div>
    </section>

    <section>
      <h2>📌 Zonen-Zuordnung &ndash; was steht wo?</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Zone A &ndash; täglich (Lochwand)</th><th>Zone B &ndash; wöchentlich (Schubladen)</th><th>Zone C &ndash; selten (Schrank)</th></tr></thead>
          <tbody>
            <tr><td>Häufigste Drehmeißel &amp; Schaftfräser</td><td>Bohrer-, Gewinde- &amp; Fräsersätze</td><td>Teilapparat / Rundtisch</td></tr>
            <tr><td>Messschieber (digital)</td><td>Wendeschneidplatten + Halter</td><td>Vierbackenfutter, Reserve-Wendeplatten</td></tr>
            <tr><td>Messuhr</td><td>Bügelmessschraube (Mikrometer)</td><td>Gewinde-Nachschneider</td></tr>
            <tr><td>Entgratwerkzeug</td><td>Anschlagwinkel, Radien-/Fühler-/Gewindelehren</td><td>Schleifleinen-Vorrat, Verbrauchsmaterial</td></tr>
            <tr><td>Feilen (griffbereit)</td><td>Handwerkzeug-Grundsatz, Drehmomentschlüssel</td><td>PSA-Ersatz</td></tr>
            <tr><td>Hand-/Drahtbürste</td><td>Schraubstock-Zubehör, Pratzen, Parallelunterlagen</td><td>Werkstattwagen / Ablage (separat)</td></tr>
            <tr><td>Kühlschmierstoff + Pinsel</td><td>Kantentaster, Zentrierbohrer</td><td>&nbsp;</td></tr>
            <tr><td>Spänehaken + Handfeger</td><td>&nbsp;</td><td>&nbsp;</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Prinzip Shadow-Board:</strong> Jedes Werkzeug hat einen festen, markierten Platz
        &ndash; als Umriss auf der Lochwand oder als Ausschnitt in der Schaumeinlage. Ein Fehlteil
        fällt dadurch sofort auf, ohne dass jemand nachzählen muss.
      </div>
    </section>

    <section>
      <h2>🧭 Warum diese Zuordnung so und nicht anders</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Entscheidung</th><th>Begründung</th></tr></thead>
          <tbody>
            <tr><td>Messschieber in A, Mikrometer in B</td><td>Der Messschieber ist das Standardmessmittel im Minutentakt. Die Bügelmessschraube kommt nur bei engen Toleranzen zum Einsatz &ndash; und ist im geschlossenen Fach besser vor Spänen geschützt.</td></tr>
            <tr><td>Kühlschmierstoff in A</td><td>Wird beim Zerspanen laufend nachgetragen. Steht er im Schrank, wird er weggelassen &ndash; mit Folgen für Standzeit und Oberfläche.</td></tr>
            <tr><td>Spänehaken in A</td><td>Sicherheitsrelevant: Ist er nicht direkt greifbar, greifen Leute mit der Hand in die Späne. Der Zusammenhang zur Gefährdungsbeurteilung auf Seite 11 ist unmittelbar.</td></tr>
            <tr><td>Wendeschneidplatten in B, nicht A</td><td>Der Wechsel ist ein Rüstvorgang, kein Dauergriff. In der Schublade liegen sie außerdem sortiert nach Geometrie statt lose an einem Haken.</td></tr>
            <tr><td>Teilapparat in C</td><td>Schwer, teuer, selten gebraucht &ndash; und im Schrank staubgeschützt. In Zone A würde er nur Platz für tägliches Werkzeug wegnehmen.</td></tr>
            <tr><td>PSA-Ersatz in C, PSA selbst am Mann</td><td>Die getragene Ausrüstung ist personengebunden; nur der Nachschub gehört in den Schrank.</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>⚠️ Wo die 5S-Ordnung erfahrungsgemäß bricht</h2>
      <div class="warn-box">
        <strong>Drei bekannte Schwachstellen, die im Konzept berücksichtigt sind:</strong>
        Erstens die Ablage „für gleich": Werkstücke und Werkzeug, die kurz abgelegt und nie
        weggeräumt werden &ndash; dagegen hilft der Schichtende-Check. Zweitens der geteilte
        Schraubstockschlüssel und ähnliche Einzelstücke, die wandern &ndash; dagegen hilft ein
        markierter Platz direkt an der Maschine. Drittens die Späne: Sie sind der einzige Punkt,
        der täglich Arbeit macht, und werden als Erstes geopfert, wenn es eilig wird &ndash;
        deshalb ist Sauberkeit ein eigener Audit-Prüfpunkt und nicht nur eine Regel.
      </div>
    </section>

{projekt_nav("04-kostenliste.html", "Bepreiste Werkzeugliste", "06-werkbank-masse.html", "Werkbank: Maße & Ergonomie")}
  </main>
"""

write_page("05-5s-ordnung.html", "Projekt 7: 5S-Ordnung & Zonen", body)
