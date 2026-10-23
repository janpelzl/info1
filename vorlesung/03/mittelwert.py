# Programm zur Berechnung eines Mittelwertes aus 3 Zahlen
def berechneMittelwert(wert1, wert2, wert3):
    mittelwert = (wert1+wert2+wert3)/3
    return mittelwert

print("Programm zur Berechnung eines Mittelwertes")
print()
zahl1 = float(input("Bitte Zahl 1 eingeben: "))
zahl2 = float(input("Bitte Zahl 2 eingeben: "))
zahl3 = float(input("Bitte Zahl 3 eingeben: "))
mittelwert = berechneMittelwert(zahl1,zahl2,zahl3)
print(f"Der Mittelwert beträgt {mittelwert}")
