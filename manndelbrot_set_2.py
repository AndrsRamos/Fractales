# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 22:17:53 2020
#GRÁFICA DEL FRACTAL DE MANDELBROT CON LA LIBRERÍA MATPLOTLIB
@author: Andree
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import time as t
from numba import jit

@jit
def mandelbrot(c):
    z=c
    for i in range(50):
        z = z*z + c 
        if abs(z)>2:
            return 0
    return 1

inicio=t.time()
"-----limites de graficación y  densidad de pixeles-----"
x=np.linspace(-2.05,1.05,2000)
y=np.linspace(-1.35,1.35,2000)

"----graficacion----"
sx=np.size(x)
sy=np.size(y)
a=np.empty((sy,sx))
for i in range(sy):
    for j in range(sx):
        a[i,j]=mandelbrot(x[j]+y[i]*1j)
norm = colors.PowerNorm(0.3)
p=plt.imshow(a,cmap='Greys',norm=norm,extent=[-2.05,1.05,-1.35,1.35])
plt.show()
plt.savefig("mandelbrotfractal.png")
final=t.time()
print("tiempo : ",final-inicio)

        
        
