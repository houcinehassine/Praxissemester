# -*- coding: utf-8 -*-
"""Nettostunden je Monat.

Alle Werte sind Vielfache von 0,25 h. Nur so ist beides zugleich glatt:
der Dezimalwert (8,25) und die Uhrzeit (8:15). Bei 5-Minuten-Schritten wie
8:05 waere der Dezimalwert 8,0833 und liesse sich nicht sauber anzeigen.

Vorgaben:
  - Ein Tag dauert hoechstens 9:00 Stunden einschliesslich Pause.
    Bei 30 min Pause sind das hoechstens 8,50 h netto.
  - Arbeitstage mindestens 6,50 h, Pruefungstage duerfen darunter liegen
  - Die Schichten werden zum Ende hin kuerzer: Maerz die laengsten Tage,
    danach absteigend bis Juli
  - Beginn ab 07:00, Ende bis 18:00

Zur Monatssumme statt Tageslaenge: die absteigende Kurve gilt fuer die
Tageslaenge, nicht fuer die Monatssummen. Die haengen zusaetzlich an der Zahl
der Anwesenheitstage je Monat (Mai hat 14, Maerz 19), und die laesst sich nicht
frei waehlen.
"""
import datetime as dt

# Monat -> (Anzahl A-Tage, Zielsumme, Untergrenze, Obergrenze)
# Die Schichten werden von Monat zu Monat kuerzer: am Anfang, waehrend der
# Einarbeitung und der grossen Softwarearbeit, sind die Tage am laengsten.
ZIEL_A = {
    3: (19, 159.50, 8.25, 8.50),   # Ø 8,39
    4: (15, 122.25, 7.75, 8.50),   # Ø 8,15
    5: (14, 111.25, 7.50, 8.50),   # Ø 7,95
    6: (17, 127.50, 7.00, 8.00),   # Ø 7,50
    7: (17, 119.00, 6.50, 7.50),   # Ø 7,00
}
# An den Vorlesungstagen (Mittwoch, PP 10:00-11:30) war keine Anwesenheit
# im Betrieb - sie stehen als Typ V ohne Stunden im Nachweis. Es bleiben nur
# der 01.07. (Praktikum RT erst am Nachmittag) und die vier Pruefungstage;
# beide sind unten fest hinterlegt.
ZIEL_VA = {}

# Kurze Schichten laufen ohne Pause durch - das Arbeitszeitgesetz verlangt
# eine Pause erst ueber 6 Stunden.
# Der 01.07. steht so im Stundenplan: Betrieb 08:00-14:00, danach das
# Praktikum Regelungstechnik 15:30-17:00. Das sind glatte 6:00 ohne Pause.
# Die vier Pruefungstage enden um 10:00, danach vier Stunden im Betrieb.
FESTE_TAGE = {
    dt.date(2026, 7,  1): 6.00,
    dt.date(2026, 7,  9): 4.00,
    dt.date(2026, 7, 17): 4.00,
    dt.date(2026, 7, 20): 4.00,
    dt.date(2026, 7, 28): 4.00,
}


def _reihe(n, summe, lo, hi):
    """n Werte in 0,25er-Schritten zwischen lo und hi mit exakt dieser Summe."""
    schritte_lo, schritte_hi = round(lo * 4), round(hi * 4)
    ziel = round(summe * 4)
    if not n:
        return []
    if not (schritte_lo * n <= ziel <= schritte_hi * n):
        raise ValueError(f"Summe {summe} mit {n} Tagen zwischen {lo} und {hi} nicht erreichbar")
    grund = ziel // n
    rest = ziel - grund * n
    werte = [grund] * n
    # Rest gleichmaessig verteilt aufschlagen, damit die Werte streuen
    for k in range(rest):
        werte[(k * 7) % n] += 1
    # zusaetzlich auf und ab variieren, ohne die Summe zu aendern
    muster = [2, -1, 1, -2, 0, 1, -1, 2, -2, 1, 0, -1]
    for k in range(0, n - 1, 2):
        d = muster[(k // 2) % len(muster)]
        if schritte_lo <= werte[k] + d <= schritte_hi and schritte_lo <= werte[k + 1] - d <= schritte_hi:
            werte[k] += d
            werte[k + 1] -= d
    werte = [min(max(w, schritte_lo), schritte_hi) for w in werte]
    # Rundungsreste ausgleichen
    diff = ziel - sum(werte)
    i = 0
    while diff != 0:
        s = 1 if diff > 0 else -1
        if schritte_lo <= werte[i % n] + s <= schritte_hi:
            werte[i % n] += s
            diff -= s
        i += 1
        if i > 40 * n:
            raise ValueError("Summe nicht erreichbar")
    return [w / 4 for w in werte]


def stunden(datum, typ, lfd):
    """Nettostunden fuer den lfd-ten Tag dieses Typs im Monat des Datums."""
    if datum in FESTE_TAGE:
        return FESTE_TAGE[datum]
    if typ != "A":
        raise ValueError(f"{datum}: Typ {typ} braucht einen Eintrag in FESTE_TAGE")
    return _reihe(*ZIEL_A[datum.month])[lfd]


if __name__ == "__main__":
    MON = {3: "März", 4: "April", 5: "Mai", 6: "Juni", 7: "Juli"}
    gesamt = 0
    print(f"{'Monat':7} {'A-Tage':>28} {'Summe A':>8} {'feste Tage':>20} {'Monat':>9}")
    for m in MON:
        a = _reihe(*ZIEL_A[m])
        v = [h for d, h in FESTE_TAGE.items() if d.month == m]
        gesamt += sum(a) + sum(v)
        fest = f"{min(v):.2f}–{max(v):.2f} ({len(v)})" if v else "–"
        print(f"{MON[m]:7} {min(a):.2f}–{max(a):.2f} (Ø {sum(a)/len(a):.2f}, {len(a):2} Tage) {sum(a):8.2f} "
              f"{fest:>20} {sum(a)+sum(v):9.2f}")
    print(f"{'Gesamt':7} {'':28} {'':8} {'':20} {gesamt:9.2f}")
    print(f"  hoechster Tag: {max(max(_reihe(*ZIEL_A[m])) for m in MON):.2f} h netto "
          f"= 9:00 brutto mit 30 min Pause")
