from cv2 import cv2
import numpy as np
 
#Cargamos la imagen:
img = cv2.imread('camara-termica.jpg')
 
#Convertimos la imagen a hsv:
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#Nota 1: la constante COLOR_BGR2HSV indica que queremos pasar de BGR a HSV.
#Nota 2: la función cvtColor() también sirve para transformar a otros espacios de color.
 
#Establecemos el rango mínimo y máximo de H-S-V:

# Rojo low
rango_bajos = np.array([0, 100, 20])
rango_altos = np.array([7, 255, 255])

# Amrillo
#rango_bajos = np.array([19,50,50])
#rango_altos = np.array([33, 255, 255])

# Verde-Azul
#rango_bajos = np.array([45, 100, 20])
#rango_altos = np.array([125, 255, 255])

# Violeta
#rango_bajos = np.array([140,50,50])
#rango_altos = np.array([160, 255, 255])

#Recordatorio: El rango HSV funciona de la siguiente forma:
#-La 1a componente es la tonalidad (Hue), en nuestro caso amarillo.
#-La 2a componente es la saturación (Saturation) , que hace el color + o - grisáceo.
#-La 3a componente es el valor (Value), que hace el color + o - oscuro.
 
 
#Detectamos los píxeles que estén dentro del rango que hemos establecido:
mask = cv2.inRange(hsv, rango_bajos, rango_altos)
print ("Mask", mask)
x = np.mean(mask, axis=(0, 1))
print (x)


#Mostramos la imagen original y la máscara:
cv2.imshow("Original", img)
#cv2.imshow("Amarillo", mask)

#Mostramos la imagen original y la máscara:
cv2.imshow("Temperatura", mask)
 
#Salimos pulsando cualquier tecla:
print("\nPulsa cualquier tecla para cerrar las ventanas\n")
cv2.waitKey(0)
cv2.destroyAllWindows()