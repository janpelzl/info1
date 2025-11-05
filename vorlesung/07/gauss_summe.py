# Berechnung der Summe aller Zahlen von 1 bis n
n = int(input("Bitte n eingeben: "))
summe = 0
for zahl in range(1,n+1):
    summe = summe + zahl

print(f"Die Summe der Zahlen von 1 bis {n} ist {summe}")