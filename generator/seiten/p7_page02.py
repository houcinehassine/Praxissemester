# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from build_projekt7 import *

body = seiten_kopf(2, "Aufgabe &amp; Rahmen",
    "Was genau geplant werden soll, in welche fünf bewerteten Teilaufgaben die Arbeit zerfällt "
    "und welche Rahmenbedingungen die Werkstatt vorgibt.") + f"""
  <main class="projekt-detail">

    <section>
      <h2>🎯 Die Aufgabe in einem Satz</h2>
      <div class="zitat-box">
        Plane einen Arbeitsplatz zum Zerspanen &ndash; Drehen und Fräsen, konventionell &ndash; mit
        allen Werkzeugen für Zerspan- und Nacharbeit, sauber nach der 5S-Methode organisiert, in
        mehreren Varianten mit technisch-wirtschaftlichem Vergleich.
        <span class="quelle">Aufgabenstellung Praxissemester</span>
      </div>
      <p style="margin-top:0.75rem">
        Drei Dinge stecken in diesem Satz, die den ganzen Projektverlauf bestimmen: Der Platz muss
        <strong>vollständig</strong> ausgerüstet sein (nicht nur die Hauptwerkzeuge), er muss
        <strong>nach einer Methode</strong> geordnet sein (5S, nicht nach Gefühl), und es reicht
        nicht, eine Lösung zu bauen &ndash; es müssen <strong>mehrere verglichen</strong> werden.
      </p>
    </section>

    <section>
      <h2>📋 Die fünf bewerteten Teilaufgaben</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>#</th><th>Teilaufgabe</th><th>Inhalt</th><th>Bearbeitet auf</th></tr></thead>
          <tbody>
            <tr><td><strong>A</strong></td><td>Werkzeuge aufnehmen</td><td>Alle Werkzeuge für Drehen, Fräsen und Nacharbeit erfassen</td><td>Seiten 3&ndash;4</td></tr>
            <tr><td><strong>B</strong></td><td>Werkbank planen</td><td>Aufbau, Maße, Schubladen, Lochwand, Halterungen</td><td>Seiten 6, 8</td></tr>
            <tr><td><strong>C</strong></td><td>5S anwenden</td><td>Feste Plätze, Shadow-Board, Standards</td><td>Seiten 5, 12</td></tr>
            <tr><td><strong>D</strong></td><td>Varianten</td><td>item-Profil, Stahl, System, Eigenbau</td><td>Seite 7</td></tr>
            <tr><td><strong>E</strong></td><td>Gegenüberstellung</td><td>Technisch-wirtschaftlicher Vergleich + Empfehlung</td><td>Seiten 9&ndash;10</td></tr>
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:0.75rem">
        <strong>Warum diese Reihenfolge zwingend ist:</strong> Ohne A (welche Werkzeuge?) lässt
        sich B (wie groß muss die Bank sein?) nicht beantworten. Ohne A und C (wie oft wird was
        gebraucht?) gibt es keine sinnvolle Zonenaufteilung. Und ohne die Werkzeugkosten aus A
        fehlt der Investitionsbetrag, den E gegen den Nutzen rechnen muss. Jede Teilaufgabe baut
        auf der vorherigen auf.
      </div>
    </section>

    <section>
      <h2>📐 Rahmenbedingungen der Werkstatt</h2>
      <div class="karten-grid-4">
        <div class="mini-karte"><h4>⚙️ Verfahren</h4><p>Drehen und Fräsen, beides konventionell &ndash; keine CNC.</p></div>
        <div class="mini-karte"><h4>👥 Personen</h4><p>3 Personen pro Schicht arbeiten an diesem Platz.</p></div>
        <div class="mini-karte"><h4>🕐 Schichten</h4><p>1 Schicht pro Tag &ndash; kein Mehrschichtbetrieb.</p></div>
        <div class="mini-karte"><h4>💰 Budget</h4><p>Kein festes Budget vorgegeben &ndash; dafür Begründungspflicht.</p></div>
      </div>
    </section>

    <section>
      <h2>🔗 Was aus den Rahmenbedingungen folgt</h2>
      <div class="tabelle-wrapper">
        <table class="tabelle">
          <thead><tr><th>Rahmenbedingung</th><th>Konsequenz für die Planung</th></tr></thead>
          <tbody>
            <tr><td>3 Personen pro Schicht</td><td>Handwerkzeug und Messmittel teils <strong>dreifach</strong> &ndash; jeder braucht seinen eigenen Messschieber, sonst entsteht genau die Suchzeit, die 5S beseitigen soll. Sichtbar in der Kostenliste: 3× Messschieber, 3× Entgratwerkzeug, 3× Handwerkzeug-Grundsatz, 3× PSA.</td></tr>
            <tr><td>Werkbank für alle 3</td><td>Ein <strong>zentraler</strong> Platz statt drei kleiner: Breite 1500&ndash;2000 mm statt einer Einzelbank. Teure Einzelstücke (Schraubstock, Teilapparat, Drehmomentschlüssel) werden nur einmal beschafft.</td></tr>
            <tr><td>Nur 1 Schicht</td><td>Ein täglicher Schichtende-Check reicht als 5S-Routine &ndash; keine Schichtübergabe-Standards nötig.</td></tr>
            <tr><td>Konventionelle Maschinen</td><td>Der Werkzeugbedarf ist handbetont: Drehmeißel statt Werkzeugmagazin, Kantentaster statt Messtaster, Handentgraten statt automatischer Nachbearbeitung.</td></tr>
            <tr><td>Kein festes Budget</td><td>Kein Sparzwang &ndash; aber auch kein Freibrief. Deshalb die Nutzwertanalyse (Seite 9) und die Amortisationsrechnung (Seite 10): Die Empfehlung muss sich begründen lassen, nicht auf ein Limit berufen.</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section>
      <h2>⚖️ Abgrenzung &ndash; was nicht Teil der Aufgabe ist</h2>
      <ul class="ergebnis-liste">
        <li><span><strong>Die Maschinen selbst</strong>Dreh- und Fräsmaschine sind vorhanden. Geplant wird der Arbeitsplatz drumherum &ndash; Werkbank, Werkzeug, Ordnung, Wege.</span></li>
        <li><span><strong>Der Raum</strong>Die Werkstatt wird nicht umgebaut. Der Grundriss auf Seite 8 zeigt nur die Anordnung; die Raummaße dort sind Beispielannahmen.</span></li>
        <li><span><strong>Die Beschaffung</strong>Preise sind recherchierte Netto-Richtwerte, keine Angebote. Der Schritt zur echten Bestellung folgt nach der Freigabe.</span></li>
        <li><span><strong>Der Bau</strong>Bei Variante 4 (Eigenbau) wäre die Fertigung ein eigenes Projekt &ndash; hier wird nur der Aufwand bewertet.</span></li>
      </ul>
    </section>

{projekt_nav("index.html", "Überblick", "03-werkzeugbedarf.html", "Werkzeugbedarf")}
  </main>
"""

write_page("02-aufgabe-rahmen.html", "Projekt 7: Aufgabe & Rahmen", body)
