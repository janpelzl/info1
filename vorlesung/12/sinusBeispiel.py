# umständlich
from math import *
zahlen = [1,2,3,4,5,6]
ergebnis = []
for zahl in zahlen:
    y = sin(zahl)
    ergebnis.append(y)
print(ergebnis)

# elegant mit numpy
from numpy import *
zahlen = array([1,2,3,4,5,6])
ergebnis = sin(zahlen)
print(ergebnis)
