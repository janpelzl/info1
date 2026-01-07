import numpy
import matplotlib.pyplot as plt

# Ausgangswerte (Verstärkerspannung, Innenwiderstand)
u0 = 200
ri = 4

# Widerstand des Lautsprechers von 0.5Ohm bis 20Ohm simulieren
rl = numpy.arange(0.5,20, 0.1)

# Gesamtwiderstand (Reihenschaltung)
rges = ri + rl

# Gesamtstrom I=U/R
i = u0/rges

# Spannung am Lautsprecher bzw. am Verstärker (Spannungsteiler-Regel)
ul = u0*rl/rges
ui = u0*ri/rges

# Verlustleistung am Lautsprecher bzw. Verstärker P = U*I
pl = ul * i
pi = ui * i

# Grafische Darstellung
plt.plot(rl, pl, "r", rl, pi, "b")
plt.title("Leistungsanpassung eines Verstärkers")
plt.xlabel("Widerstand des Lautsprechers in Ohm")
plt.ylabel("Leistung in [W] (rot: Lautsprecher, blau: Verstärker)")
plt.grid(True)
plt.show()