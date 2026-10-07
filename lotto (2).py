import random


def lottoziehung(anzahl=6):
    # Liste mit den Zahlen 1 bis 45 erstellen
    zahlen = list(range(1, 46))
    gezogene_zahlen = []

    # 6 Zahlen ziehen
    for k in range(anzahl):
        # Das aktuelle Ende der Liste (wird mit jedem Durchgang 1 kleiner)
        letzter_index = 44 - k

        # Einen zufälligen Index im gültigen Bereich wählen
        zufalls_index = random.randint(0, letzter_index)

        # Zahl am Index merken
        gezogene = zahlen[zufalls_index]
        gezogene_zahlen.append(gezogene)

        # PER SLICING: Die gezogene Zahl ans Ende verschieben!
        # Wir nehmen alle Zahlen vor und nach dem Index und hängen die gezogene Zahl ganz hinten an
        zahlen = zahlen[:zufalls_index] + zahlen[zufalls_index+1:] + [gezogene]

    return gezogene_zahlen


def statistik_aktualisieren(statistik, ziehung):
    # Wird nach JEDER Ziehung aufgerufen: Zähler jeder gezogenen Zahl um 1 erhöhen
    for zahl in ziehung:
        statistik[zahl] = statistik[zahl] + 1


def lotto_statistik(anzahl_ziehungen):
    # Dictionary für die Statistik erstellen (Zahl 1-45 hat am Anfang 0 Ziehungen)
    statistik = {}
    for z in range(1, 46):
        statistik[z] = 0

    # Mehrere Ziehungen durchführen
    for a in range(anzahl_ziehungen):
        ziehung = lottoziehung()
        statistik_aktualisieren(statistik, ziehung)

    return statistik


# --- Testen des Programms ---

# Eine einfache Ziehung
print("Gezogene Lottozahlen:", lottoziehung())

# Beweis: alle 45 Zahlen ziehen -> keine doppelt
alle = lottoziehung(45)
print("Alle 45 gezogen, keine doppelt:", len(set(alle)) == 45)

# Statistik mit 1000, 10000 und 100000 Ziehungen
for durchlaeufe in [1000, 10000, 100000]:
    ergebnis = lotto_statistik(durchlaeufe)

    print(f"\nStatistik nach {durchlaeufe} Ziehungen:")
    for zahl in ergebnis:
        print("Zahl", zahl, "wurde", ergebnis[zahl], "mal gezogen")
