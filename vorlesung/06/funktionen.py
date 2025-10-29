from math import *
def parallelschaltung(r1, r2, r3=inf, r4=inf, r5=inf):
    rges = 1/(1/r1+1/r2+1/r3+1/r4+1/r5)
    return rges

r1 = 10
r2 = 10
r3 = 20
r4 = 30
r5 = 50
rges = parallelschaltung(r1,r2,r3,r4)
print(f"Der Gesamtwiderstand ist {rges:1.2f}")