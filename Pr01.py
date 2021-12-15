from Fun import Plot
import numpy as np
from numpy import pi


x = np.linspace(-2*pi,2*pi,100)
y = np.sin(x)

# Llamamos la funcion
Plot(x, y, 'Función Seno. $R=[-\pi,\pi]$')

