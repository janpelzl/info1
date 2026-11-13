# Berechne die Fakultät von n, d.h. n!
n = int(input("Bitte n eingeben: "))
produkt = 1
for zahl in range(1,n+1):
    produkt = produkt * zahl
print(f"{n}!={produkt}")
