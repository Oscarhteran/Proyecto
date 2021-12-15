import numpy as np
import matplotlib.pyplot as plt

def Plot(x, y, Titulo='Grafico de prueba'):
    plt.plot(x, y)
    plt.title(Titulo)
    plt.grid(alpha=0.25)
    plt.show()
