import numpy
import matplotlib.pyplot as plt

x = numpy.arange(0.0, 7, 0.05)
y = 5*numpy.sin(x)
plt.plot(x,y, linewidth=2)
plt.xlabel("Zeit in Sekunden")
plt.ylabel("y(x)")
plt.title("Darstellung der Funktion y(x)=5*sin(x)")
plt.grid(True)
plt.show()