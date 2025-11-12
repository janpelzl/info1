eineListe = list(range(7,40,7))
print(eineListe)
print(f"Die Liste enthält {len(eineListe)} Zahlen.")

# Iteriere durch alle Elemente der Liste
# 1. Mit einer for-Schleife
for i in range(len(eineListe)):
    print(eineListe[i])

# 2. Mit dem in Operator
for i in eineListe:
    print(i)