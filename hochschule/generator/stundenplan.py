# -*- coding: utf-8 -*-
"""Nettostunden je Monat.

Alle Werte sind Vielfache von 0,25 h. Nur so ist beides zugleich glatt:
der Dezimalwert (8,25) und die Uhrzeit (8:15). Bei 5-Minuten-Schritten wie
8:05 waere der Dezimalwert 8,0833 und liesse sich nicht sauber anzeigen.

Vorgaben:
  - Ein Tag dauert hoechstens 9:00 Stunden einschliesslich Pause.
    Bei 30 min Pause sind das hoechstens 8,50 h netto.
  - Arbeitstage mindestens 6,50 h, Vorlesungstage duerfen darunter liegen
  - Juli die kuerzesten, Juni die zweitkuerzesten Arbeitstage
  - Beginn ab 07:00, Ende bis 18:00

Zur Monatssumme statt Tageslaenge: Juli hat mit 21 die meisten Arbeitstage,
Mai mit 14 die wenigsten. Unter der 9-Stunden-Grenze kann Juli deshalb nicht
zugleich die kleinste Monatssumme haben - selbst am Minimum von 6,50 h laege
Juli bei 142,00 h, waehrend Mai auch am Maximum nur 130,50 h erreicht.
Die Vorgabe ist hier deshalb als kuerzeste Tage umgesetzt, nicht als
kleinste Monatssumme.
"""
import datetime as dt

# Monat -> (Anzahl A-Tage, Zielsumme, Untergrenze, Obergrenze)
ZIEL_A = {
    3: (19, 156.75, 7.75, 8.50),
    4: (15, 123.50, 7.75, 8.50),
    5: (14, 115.25, 7.75, 8.50),
    6: (17, 127.50, 7.00, 8.00),
    7: (21, 147.00, 6.50, 7.50),
}
# Vorlesungstage: erst die Vorlesung PP 10:00-11:30, danach in den Betrieb.
# Frueheste Ankunft 11:45, spaetestes Ende 18:00, davon 30 min Pause.
ZIEL_VA = {
    3: (2, 11.00, 5.25, 5.75),
    4: (4, 21.50, 5.25, 5.75),
    5: (2, 10.75, 5.25, 5.75),
    6: (4, 20.50, 5.00, 5.50),
    7: (1,  5.50, 5.50, 5.50),
}

# Der 01.07. steht so im Stundenplan: Betrieb 08:00-14:00, danach das
# Praktikum Regelungstechnik 15:30-17:00. 6:00 abzueglich 30 min Pause.
FESTE_TAGE = {dt.date(2026, 7, 1): 5.50}


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
    ziel = ZIEL_A if typ == "A" else ZIEL_VA
    return _reihe(*ziel[datum.month])[lfd]


if __name__ == "__main__":
    MON = {3: "März", 4: "April", 5: "Mai", 6: "Juni", 7: "Juli"}
    gesamt = 0
    print(f"{'Monat':7} {'A-Tage':>28} {'Summe A':>8} {'VA-Tage':>20} {'Monat':>9}")
    for m in MON:
        a = _reihe(*ZIEL_A[m])
        v = _reihe(*ZIEL_VA[m])
        gesamt += sum(a) + sum(v)
        print(f"{MON[m]:7} {min(a):.2f}–{max(a):.2f} (Ø {sum(a)/len(a):.2f}, {len(a):2} Tage) {sum(a):8.2f} "
              f"{min(v):.2f}–{max(v):.2f} ({len(v)}) {sum(a)+sum(v):9.2f}")
    print(f"{'Gesamt':7} {'':28} {'':8} {'':20} {gesamt:9.2f}")
    print(f"  hoechster Tag: {max(max(_reihe(*ZIEL_A[m])) for m in MON):.2f} h netto "
          f"= 9:00 brutto mit 30 min Pause")
