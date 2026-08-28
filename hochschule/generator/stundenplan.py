# -*- coding: utf-8 -*-
"""Nettostunden je Monat.

Alle Werte sind Vielfache von 0,25 h. Nur so ist beides zugleich glatt:
der Dezimalwert (8,25) und die Uhrzeit (8:15). Bei 5-Minuten-Schritten wie
8:05 waere der Dezimalwert 8,0833 und liesse sich nicht sauber anzeigen.

Vorgaben:
  - Arbeitstage mindestens 6,50 h, Vorlesungstage duerfen darunter liegen
  - Juli die kleinste, Juni die zweitkleinste Monatssumme
  - Beginn ab 07:00, Ende bis 18:00
"""

# Monat -> (Anzahl A-Tage, Zielsumme A, Untergrenze, Obergrenze)
ZIEL_A = {
    3: (19, 180.50, 8.75, 10.25),
    4: (15, 146.25, 9.00, 10.25),
    5: (14, 136.50, 9.00, 10.25),
    6: (17, 131.75, 7.00,  8.50),
    7: (21, 141.75, 6.50,  7.25),
}
ZIEL_VA = {3: (2, 11.00), 4: (5, 27.50), 5: (4, 22.00), 6: (4, 22.00), 7: (1, 5.50)}
VA_MIN, VA_MAX = 4.75, 6.00


def _reihe(n, summe, lo, hi):
    """n Werte in 0,25er-Schritten zwischen lo und hi mit exakt dieser Summe."""
    schritte_lo, schritte_hi = round(lo * 4), round(hi * 4)
    ziel = round(summe * 4)
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


def stunden(monat, typ, lfd):
    """Nettostunden fuer den lfd-ten Tag dieses Typs im Monat."""
    if typ == "A":
        n, s, lo, hi = ZIEL_A[monat]
        return _reihe(n, s, lo, hi)[lfd]
    n, s = ZIEL_VA[monat]
    return _reihe(n, s, VA_MIN, VA_MAX)[lfd]


if __name__ == "__main__":
    MON = {3: "März", 4: "April", 5: "Mai", 6: "Juni", 7: "Juli"}
    gesamt = 0
    print(f"{'Monat':7} {'A-Tage':>26} {'Summe A':>8} {'VA':>16} {'Monat':>8}")
    for m in MON:
        a = _reihe(*ZIEL_A[m])
        v = _reihe(ZIEL_VA[m][0], ZIEL_VA[m][1], VA_MIN, VA_MAX)
        gesamt += sum(a) + sum(v)
        print(f"{MON[m]:7} {min(a):.2f}–{max(a):.2f} ({len(a)} Tage) {sum(a):8.2f} "
              f"{min(v):.2f}–{max(v):.2f} ({len(v)}) {sum(a)+sum(v):8.2f}")
    print(f"{'Gesamt':7} {'':26} {'':8} {'':16} {gesamt:8.2f}  ->  {gesamt/21.71:.1f} h/Woche")
