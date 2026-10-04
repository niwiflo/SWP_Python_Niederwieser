import random

MAX_ZAHL = 45        # Zahlen von 1 bis 45
ANZAHL_GEZOGEN = 6   # 6 Zahlen pro Ziehung


# ---------------------------------------------------------------
# Teil 1: Lottoziehung als Methode
# ---------------------------------------------------------------
def lottoziehung(anzahl=ANZAHL_GEZOGEN, max_zahl=MAX_ZAHL):
    """Zieht 'anzahl' verschiedene Zahlen aus 1..max_zahl.
    Pro gezogener Zahl wird der Zufallsgenerator genau EINMAL benutzt."""
    topf = list(range(1, max_zahl + 1))   # alle Kugeln im Topf
    gezogen = []

    for _ in range(anzahl):
        # zufaelligen Index nur aus den NOCH VORHANDENEN Kugeln waehlen
        index = random.randint(0, len(topf) - 1)
        zahl = topf[index]
        gezogen.append(zahl)

        # gezogene Kugel entfernen: letzte Kugel an ihre Stelle setzen
        topf[index] = topf[-1]
        topf.pop()

    return gezogen


# ---------------------------------------------------------------
# Teil 2: Statistik
# ---------------------------------------------------------------
def statistik_erstellen(max_zahl=MAX_ZAHL):
    """Dictionary mit allen Zahlen als Schluessel und Zaehler 0."""
    return {zahl: 0 for zahl in range(1, max_zahl + 1)}


def statistik_aktualisieren(statistik, ziehung):
    """Wird nach JEDER Ziehung aufgerufen und erhoeht die Zaehler."""
    for zahl in ziehung:
        statistik[zahl] += 1


def lotto_statistik(anzahl_ziehungen):
    """Macht 'anzahl_ziehungen' Ziehungen und zaehlt mit."""
    statistik = statistik_erstellen()
    for _ in range(anzahl_ziehungen):
        ziehung = lottoziehung()
        statistik_aktualisieren(statistik, ziehung)
    return statistik


def statistik_ausgeben(statistik, anzahl_ziehungen):
    erwartet = anzahl_ziehungen * ANZAHL_GEZOGEN / MAX_ZAHL
    print(f"\n=== Statistik nach {anzahl_ziehungen} Ziehungen ===")
    print(f"Erwartet pro Zahl: ca. {erwartet:.1f} mal")
    for zahl, anzahl in statistik.items():
        abweichung = (anzahl - erwartet) / erwartet * 100
        print(f"Zahl {zahl:2d}: {anzahl:8d} mal  ({abweichung:+6.2f} %)")
    haeufigste = max(statistik, key=statistik.get)
    seltenste = min(statistik, key=statistik.get)
    print(f"Am haeufigsten: {haeufigste} ({statistik[haeufigste]} mal)")
    print(f"Am seltensten:  {seltenste} ({statistik[seltenste]} mal)")


# ---------------------------------------------------------------
# Hauptprogramm
# ---------------------------------------------------------------
if __name__ == "__main__":
    # 1) Eine Ziehung am Bildschirm ausgeben
    zahlen = lottoziehung()
    print("Die Lottozahlen lauten:", sorted(zahlen))

    # 2) Beweis: alle 45 Zahlen ziehen -> keine doppelt
    alle = lottoziehung(anzahl=45)
    print("Alle 45 gezogen, keine doppelt:", len(set(alle)) == 45)

    # 3) Statistik fuer 1000, 10000, 100000 Ziehungen
    for n in [1000, 10000, 100000]:
        stat = lotto_statistik(n)
        statistik_ausgeben(stat, n)
