from Fun import Plot
import numpy as np
from numpy import pi


x = np.linspace(-3*pi,3*pi,100)
y = np.sin(x)

# Llamamos la funcion
Plot(x, y, 'Función Seno. $R=[-\pi,\pi]$')

# Segunda llamada
Plot(x, 2*y)
