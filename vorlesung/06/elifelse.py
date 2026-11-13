zahl = int(input("Bitte eine ganze Zahl eingeben: "))
if zahl < 0:
    print(f"{zahl} ist kleiner Null.")
elif 0 <= zahl <= 1000:
    print(f"{zahl} ist zwischen Null und Tausend.")
else:
    print(f"{zahl} ist größer als Tausend.")