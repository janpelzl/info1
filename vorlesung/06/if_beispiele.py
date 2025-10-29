zahl = input("Bitte Zahl eingeben: ")

if zahl.isnumeric():
    print("Danke!")
    zahl = int(zahl)
    if zahl >= 0:
        print("Die Zahl ist größer als 0")
    else:
        print("Die Zahl ist negativ")

else:
    print("Problem: Bitte eine Zahl eingeben!")



