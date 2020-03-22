# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 22:17:53 2020
#GRÁFICA DEL FRACTAL DE MANDELBROT en la elipse [(x+0.5)**2/1.5**2+y**2=1]
*PILLOW,*RGBA,*time
@author: Andree
"""
from PIL import Image   #pkg pillow para graficar 
import time as t        #time para medir el tiempo de ejecucion
from numba import jit   #pkg numba para reducir el tiempo de ejecucion
#paleta colores
colores=[
(88, 200, 146 ),(63, 164, 115),(39, 121, 82 ),(20, 76, 49  ),(9, 44, 28  ),
(90, 150, 190 ),(63, 116, 150),(40, 83, 111 ),(22, 51, 70  ),(11, 29, 41 ),
(255, 192, 112),(235, 171, 90),(174, 122, 56),(110, 74, 29 ),(64, 42, 14 ),
(255, 149, 112),(235, 127, 90),(174, 86, 56 ),(110, 50, 29 ),(64, 26, 14 ),
(255, 132, 0  ),(243, 127, 3 ),(203, 109, 9 ),(158, 87, 12 ),(124, 69, 10)]

@jit                    #jit permite una pseudo compilacion de las funciones
def mandelbrot(c):      
    z=0
    for i in range(maxIt):
        z = z*z + c 
        if abs(z)>2:
            return i
    return 0
# limites de graficación y densidad de pixeles
xlim = (-2,1)
ylim = (-1.5,1.5)
sx = 2030
sy = 2080

maxIt = len(colores)  # iteraciones maximas permitidas


inicio=t.time()
image = Image.new("RGBA", (sx, sy)) 
for y in range(sy): 
    zy = y * (ylim[1] - ylim[0]) / (sy - 1)  + ylim[0] 
    for x in range(sx): 
        zx = x * (xlim[1] - xlim[0]) / (sx - 1)  + xlim[0]  
        if ((zx+0.5)/1.5)**2 + (zy/1.25)**2 <=1:
            i=mandelbrot(zx + zy * 1j) 
            image.putpixel((x, y), colores[i])
        else:
            image.putpixel((x, y), (0,0,0,0))
fin=t.time()  
image.show()
image.save("MANDELBROTSET.png")
print("tiempo de ejecución: ",fin-inicio)
