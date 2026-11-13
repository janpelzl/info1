# Berechne die Summe aller Zahlen von 1 bis n
n = int(input("Bitte n eingeben: "))
summe = 0
for zahl in range(1,n+1):
#    print(zahl, end=",")
    summe = summe + zahl
print(f"Die Summe von allen Zahlen von 1 bis {n} beträgt {summe}")
print(n*(n+1)/2)