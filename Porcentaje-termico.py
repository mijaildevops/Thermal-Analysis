from cv2 import cv2
import numpy as np
import time
 
#Cargamos la imagen:
img = cv2.imread('frame-test1.png')
 
#Convertimos la imagen a hsv:
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#Nota 1: la constante COLOR_BGR2HSV indica que queremos pasar de BGR a HSV.
#Nota 2: la función cvtColor() también sirve para transformar a otros espacios de color.
 
#Establecemos el rango mínimo y máximo de H-S-V:

# Rojo 
rango_bajosR = np.array([0, 100, 20])
rango_altosR = np.array([7, 255, 255])

# Amrillo
rango_bajosA = np.array([19,50,50])
rango_altosA = np.array([33, 255, 255])


# Verde-Azul
rango_bajosV = np.array([45, 100, 20])
rango_altosV = np.array([125, 255, 255])

# Violeta
rango_bajosF = np.array([140,50,50])
rango_altosF = np.array([160, 255, 255])

PorcentajePixel = []

def AnalisFrame (color, rango_bajos, rango_altos):
    #Detectamos los píxeles que estén dentro del rango que hemos establecido:
    ColorProcentaje = 0
    mask = cv2.inRange(hsv, rango_bajos, rango_altos)
    print(len(mask))
    ColorProcentaje = np.mean(mask, axis=(0, 1))
    PorcentajePixel.append(ColorProcentaje)
    print (ColorProcentaje)

    #Mostramos la imagen original y la máscara:
    cv2.imshow("Original", img)

    #Mostramos la imagen original y la máscara:
    cv2.imshow(color, mask)

    time.sleep(5)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
AnalisFrame ("Rojo", rango_bajosR, rango_altosR)
AnalisFrame ("Amarillo", rango_bajosA, rango_altosA)
AnalisFrame ("Verde", rango_bajosV, rango_altosV)
AnalisFrame ("Violeta", rango_bajosF, rango_altosF)
print (sum(PorcentajePixel))