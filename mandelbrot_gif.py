# -*- coding: utf-8 -*-
"""
Created on Mar 18 2020
#GRÁFICA DEL FRACTAL DE MANDELBROT
*PILLOW,*RGBA
@author: AndrsRamos
"""
from PIL import Image

def mandelbrot(c,j):
    z=0
    for i in range(j):
        z = z*z + c 
        if abs(z)>2:
            return i
    return 0
#paleta de colores
colores=[
(88, 200, 146 ),(63, 164, 115),(39, 121, 82 ),(20, 76, 49  ),(9, 44, 28  ),
(90, 150, 190 ),(63, 116, 150),(40, 83, 111 ),(22, 51, 70  ),(11, 29, 41 ),
(255, 192, 112),(235, 171, 90),(174, 122, 56),(110, 74, 29 ),(64, 42, 14 ),
(255, 149, 112),(235, 127, 90),(174, 86, 56 ),(110, 50, 29 ),(64, 26, 14 ),
(255, 132, 0  ),(243, 127, 3 ),(203, 109, 9 ),(158, 87, 12 ),(124, 69, 10)]
# limites de graficación  
xlim = (-2,2)
ylim = (-2,2)
# densidad de pixeles
sx = 380
sy = 380  

imagenes=[]
for k in range(len(colores)):
    img = Image.new("RGBA", (sx, sy)) #inicializa la imagen
    for y in range(sy): 
        zy = y * (ylim[1] - ylim[0]) / sy  + ylim[0] 
        for x in range(sx): 
            zx = x * (xlim[1] - xlim[0]) / sx  + xlim[0] 
            z = zx + zy * 1j
            i=mandelbrot(z,k+1)
            img.putpixel((x, y), colores[i])
            if zx**2 + zy**2 >4:
                img.putpixel((x,y), (255,255,255,255))
    imagenes.append(img)
imagenes[0].save('mandelbrotgif.gif',save_all=True,
                 append_images=imagenes[1:], duration=180, loop=0)
#image.save("mangif"+str(k)+".png") 
