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
start_time = time()

while (CountFrame < 73):
   
    print ("******************************************")
    print ("--------------- New Frame ----------------")
    # Time start 
    starttimeFrame = time()
    PercentageTotal = []

    # interacciones por cada Scala definida
    for Scala in Scalas:

        starttimeScala = time()

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

        
        
        PixelBlack = 0
        Pixelcolor = 0

        #Cargamos la imagen
        FrameProcess = "scene" + str(CountFrame) + ".png"
        img = cv2.imread(FrameProcess)
        
        #Convertimos la imagen a hsv:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        #Detectamos los píxeles que estén dentro del rango que hemos establecido:
        mask = cv2.inRange(hsv, Scala_bajos, Scala_altos)

        # Escribir Frame Mask (Blanco y Negro)
        cv2.imwrite('FramePresado.png',mask)

        # Frame Analis (Blanco y Negro)
        FrameColor = Image.open('FramePresado.png')
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

        print("")
        print (" - Frame: ", FrameProcess)
        print (" - ScalaID: ", Scala)
        print (" - Scala-Color: ", Color)
        print (" - Pixel-Total: ", TotalPixelsImg)
        print (" - Pixel-Back: ", PixelBlack)
        print (" - Pixel-Color: ", Pixelcolor)
        print (" - % Pixel-Color: ", PorcentajeColorPixel,"%")

        PercentageTotal.append(PorcentajeColorPixel)

        # Time Frame Process
        elapsedtimeScala = time() - starttimeScala
        TimeScala = float("{0:.4f}".format(elapsedtimeScala))

        # 
        from AddFrameData import AddDataFrameScala
        AddDataFrameScala (GuidTest, FrameProcess, Scala, TotalPixelsImg, PixelBlack, Pixelcolor, PorcentajeColorPixel, TimeScala)

        #
        print("Elapsed time Scala: %0.4f seconds." % elapsedtimeScala)

    print("")
    CountFrame += 1

    # Time Frame Process
    elapsedtimeFrame = time() - starttimeFrame
    TimeFrame = float("{0:.4f}".format(elapsedtimeFrame))
    #
    print("Elapsed time Frame: %0.4f seconds." % elapsedtimeFrame)

    #
    SumPorcentaje = sum(PercentageTotal)
    from AddFrameData import AddFrameProcessing
    AddFrameProcessing (GuidTest, FrameProcess, SumPorcentaje, TimeFrame)


elapsed_time = time() - start_time
TimeProcess = float("{0:.4f}".format(elapsed_time))
#
print("Elapsed time Total: %0.4f seconds." % elapsed_time)

from datetime import datetime
EndProcess = datetime.now()
print (StartProcess)
print (EndProcess)