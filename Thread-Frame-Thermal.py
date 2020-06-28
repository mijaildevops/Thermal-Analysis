from cv2 import cv2
import numpy as np

from datetime import datetime
StartProcess = datetime.now()
from time import time

from PIL import Image

# DB
import pymysql
# GUID
import uuid 

# Multi hilo_1 Test
import threading
import logging

#///////////////////////////////////////////
# Generamos Un GUID 
#///////////////////////////////////////////
IdUnico = uuid.uuid4()
GuidTest = str(IdUnico)

#////////////////////////
CountFrame = 1

#/////////////////////////////
# Scalas
Scalas = [1,2,3,4,5,6,7,8]

#///////////////////////
# Time start 

FrameProcess = 'scene1.png'

def FrameProcessing (Scala, FrameProcess):
    #print ("****************************************************")
    #print ("---------------New Frame Processing " , Scala,  "----------------")
    #/////////////////////////
    # Setting
    # Time start 

    #starttimeScala = time()
    PercentageTotal = []
    PixelBlack = 0
    Pixelcolor = 0

    # Clasificacion de scalas
    if (Scala == 1):
        # High Red
        Color = "High Red"
        Scala_bajos = np.array([170, 100, 20])
        Scala_altos = np.array([179, 255, 255])
    elif (Scala == 2):
        # Low Red
        Color = "Low Red"
        Scala_bajos = np.array([0, 100, 20])
        Scala_altos = np.array([8, 255, 255])
    elif (Scala == 3):
        # orange
        Color = "Orange"
        Scala_bajos = np.array([9, 100, 20])
        Scala_altos = np.array([19, 255, 255])
    elif (Scala == 4):
        # yellow
        Color = "Yellow"
        Scala_bajos = np.array([20, 100, 20])
        Scala_altos = np.array([40, 255, 255])
    elif (Scala == 5):
        # Green
        Color = "Green"
        Scala_bajos = np.array([41, 100, 20])
        Scala_altos = np.array([69, 255, 255])
    elif (Scala == 6):
        # light blue
        Color = "Light blue"
        Scala_bajos = np.array([70, 100, 20])
        Scala_altos = np.array([105, 255, 255])
    elif (Scala == 7):
        # blue
        Color = "Blue"
        Scala_bajos = np.array([106, 100, 20])
        Scala_altos = np.array([129, 255, 255])
    else:
        #fuchsia
        Color = "Fuchsia"
        Scala_bajos = np.array([130,100, 20])
        Scala_altos = np.array([169, 255, 255])
    starttimeScala = time()
    #print (Scala, Color, Scala_bajos, Scala_bajos)

    #Cargamos la imagen
    #FrameProcess = "scene" + str(CountFrame) + ".png"
    img = cv2.imread(FrameProcess)
    
    #Convertimos la imagen a hsv:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #Detectamos los píxeles que estén dentro del rango que hemos establecido:
    mask = cv2.inRange(hsv, Scala_bajos, Scala_altos)

    # Escribir Frame Mask (Blanco y Negro)
    FramePresado ='FramePresado-' + str(Scala) +'.png'
    cv2.imwrite(FramePresado, mask)

    # Frame Analisis (Blanco y Negro)
    FrameColor = Image.open(FramePresado)
    # total de Pixeles y color de cada uno
    datos = list(FrameColor.getdata())
    # Segmentar Pixeles 
    for dato in datos:
        if (int(dato)> 0):
            # Total de Pixeles Blanco-Color True
            Pixelcolor += 1
        else:
            # Total de Pixeles Negro-Color False
            PixelBlack += 1
    FrameColor.close()

    # Calculo Total de pixels y del % de Pixeles-color segun la scala
    TotalPixelsImg = len(datos)
    PorcentajeColorPixel = Pixelcolor*100/(Pixelcolor + PixelBlack)
    PorcentajeColorPixel = float("{0:.2f}".format(PorcentajeColorPixel))

    #AnalisisColor = [color, Pixelcolor]

    """print("")
    print (" - Frame: ", FrameProcess)
    print (" - ScalaID: ", Scala)
    print (" - Scala-Color: ", Color)
    print (" - Pixel-Total: ", TotalPixelsImg)
    print (" - Pixel-Back: ", PixelBlack)
    print (" - Pixel-Color: ", Pixelcolor)
    print (" - % Pixel-Color: ", PorcentajeColorPixel,"%")
    """
    print (" - ScalaID: ", Scala)
    print (" - Scala-Color: ", Color)
    print (" - % Pixel-Color: ", PorcentajeColorPixel,"%")

    PercentageTotal.append(PorcentajeColorPixel)

    # Time Frame Process
    elapsedtimeScala = time() - starttimeScala
    TimeScala = float("{0:.4f}".format(elapsedtimeScala))

    # 
    from AddFrameData import AddDataFrameScala
    AddDataFrameScala (GuidTest, FrameProcess, Scala, TotalPixelsImg, PixelBlack, Pixelcolor, PorcentajeColorPixel, TimeScala)

    #
    print("Elapsed time Scala: ", Scala, " %0.4f seconds." % elapsedtimeScala)
    #print ("")


i= 1
while i < 5:
    start_time = time()
    FrameProcess = 'scene' + str(i) + '.png'
    print ("-------------------", FrameProcess, "-------------------")
    t1 = threading.Thread(name="hilo_1", target=FrameProcessing, args=(1, FrameProcess))
    t2 = threading.Thread(name="hilo_2", target=FrameProcessing, args=(2, FrameProcess))
    t3 = threading.Thread(name="hilo_3", target=FrameProcessing, args=(3, FrameProcess))
    t4 = threading.Thread(name="hilo_4", target=FrameProcessing, args=(4, FrameProcess))
    t5 = threading.Thread(name="hilo_5", target=FrameProcessing, args=(5, FrameProcess))
    t6 = threading.Thread(name="hilo_6", target=FrameProcessing, args=(6, FrameProcess))
    t7 = threading.Thread(name="hilo_7", target=FrameProcessing, args=(7, FrameProcess))
    t8 = threading.Thread(name="hilo_8", target=FrameProcessing, args=(8, FrameProcess))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()

    elapsed_time = time() - start_time
    #TimeProcess = float("{0:.4f}".format(elapsed_time))
    #
    print("Elapsed time Total: %0.4f seconds." % elapsed_time)
    i += 1
