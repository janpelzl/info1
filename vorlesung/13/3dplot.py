import numpy
from matplotlib import pyplot

# assigning coordinates
a = numpy.linspace(-5, 5, 50)
b = numpy.linspace(-5, 5, 50)
x, y = numpy.meshgrid(a, b)
z = numpy.sin(numpy.sqrt(x**2 + y**2))

# creating the visualization
fig = pyplot.figure()
wf = pyplot.axes(projection ='3d')
wf.plot_wireframe(x, y, z, color ='green')

# displaying the visualization
wf.set_title('3D Plot Beispiel')
pyplot.show()