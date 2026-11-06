import math
def gesamtwiderstandParallelschaltung(r1, r2, r3=math.inf, r4=math.inf, r5=math.inf):
    rges = 1/(1/r1+1/r2+1/r3+1/r4+1/r5)
    return rges

rges = gesamtwiderstandParallelschaltung(10,10)
print(f"Die Parallelschaltung hat einen Gesamtwiderstand von Rges={rges:1.2f}")