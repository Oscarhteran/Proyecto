import numpy as np
import matplotlib.pyplot as plt

def Plot(x, y, Titulo='Grafico de prueba', sentinel=0):
    plt.plot(x, y)
    plt.title(Titulo)
    plt.grid(alpha=0.25)
    if sentinel == 0:
        plt.show()
    else:
        return 0
