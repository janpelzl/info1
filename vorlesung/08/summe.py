# Berechne Summe aller Zahlen von 1 bis n mit einer for-Schleife und einer while-Schleife

# for-Schleife
n = 10
summe = 0
for i in range(1,n+1):
    summe = summe + i
print(f"Ergebnis der for-Schleife: {summe}")

# und jetzt die while-Schleife
summe = 0
zahl = 0
while zahl <= n:
    summe = summe + zahl
    zahl = zahl + 1
print(f"Ergebnis der while-Schleife: {summe}")
