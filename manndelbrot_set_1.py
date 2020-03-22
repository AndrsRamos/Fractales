##andrsRamos##
"plot del fractal de mandelbrot"

import matplotlib.pyplot as plt
from numba import jit
import time as t
@jit
def mandelbrot(c):
    z=c
    for i in range(20):
        z = z*z + c 
        if abs(z)>2:
            return 0
    return 1
inicio=t.time()
"---limites de la graficación----"
xlim=[-2,.7]
ylim=[-1,1]
"---Tamaño de la imagen (pixeles)"
xdensity=100
ydensity=100


deltax=(xlim[1]-xlim[0])/xdensity
deltay=(ylim[1]-ylim[0])/ydensity

for i in range (ydensity):
    y0=ylim[0]+deltay*(i)
    for j in range(xdensity):
        x0=xlim[0]+deltax*(j)
        if mandelbrot(x0+y0*1j)==1:
            plt.plot(x0,y0,'.')
plt.show()
fin=t.time()
print("tiempo de ejecucion: ",fin-inicio)
