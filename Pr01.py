from Fun import Plot
import numpy as np
from numpy import pi


x = np.linspace(-2*pi,2*pi,100)
y = np.sin(x)

# Llamamos la funcion
Plot(x, y, 'Función Seno. $R=[-\pi,\pi]$', sentinel=1)

# Segundo llamado
x1 = np.arange(0,10,0.1)
y1 = np.sqrt(x1)
Plot(x1, y1)

