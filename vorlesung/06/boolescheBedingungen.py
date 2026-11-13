# gleichwertige if-Bedingung
zahl = int(input("Zahl eingeben: "))
if zahl >= 0:
    if zahl < 1000:
        print("Die Zahl ist zwischen 0 und 1000")

if zahl >= 0 and zahl < 1000:
    print("Die Zahl ist zwischen 0 und 1000")

if 0 <= zahl < 1000:
    print("Die Zahl ist zwischen 0 und 1000")
