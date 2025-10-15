# Die folgende Funktion berechnet einen Mittelwert
def mittelwert(zahl1, zahl2, zahl3):
    mittelwert = (zahl1+zahl2+zahl3)/3
    return mittelwert

def ausgabe(wert):
    print(f"Der Mittelwert ist {wert:.3f}")


# Hauptprogramm
ausgabe(mittelwert(10,20,30))

ergebnis = mittelwert(3.4, 88.3, -77)
ausgabe(ergebnis)
