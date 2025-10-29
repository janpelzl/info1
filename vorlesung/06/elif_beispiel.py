# Programm unterscheidet die Eingabe nach Größe: <0, zwischen 0 und 100, >100
zahl = int(input("Bitte Zahl eingeben: "))

if zahl < 0:
    print("Zahl ist kleiner als 0")
elif zahl <=100:
    print("Zahl ist zwischen 0 und 100")
else:
    print("Zahl ist größer als 100")