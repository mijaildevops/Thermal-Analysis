# DB
import pymysql

# //////////////////////////////////////
# Conexion- from Visual Studio
# //////////////////////////////////////
from Conexion import Conexion


def AddDataFrameScala (GuidTest, FrameProcess, Scala, TotalPixelsImg, PixelBlack, Pixelcolor, PorcentajeColorPixel, TimeScala):

    # Connect to the database
    connection = pymysql.connect(host=Conexion[0],
                            user=Conexion[1],
                            password=Conexion[2],
                            db=Conexion[3],
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
        # Create a new record
                         
            sql = "INSERT INTO `DataFrameScala` ( `Guid`, `Frame`, `ScalaId`, `TotalPixels`, `BlackPixels`,  `ColorPixels`,  `PerCentumColor`,  `ElapsedTime`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (GuidTest, FrameProcess, Scala, TotalPixelsImg, PixelBlack, Pixelcolor, PorcentajeColorPixel, TimeScala))
            
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

            #print ("///////////////////////////////////////////////////////////////////")
            #print ("   --  Se realizo Registro del Analisis del Frame-Scala", FrameProcess, "- Scala", Scala)
            #print ("///////////////////////////////////////////////////////////////////")

    finally:
        connection.close()

def AddFrameProcessing (GuidTest, FrameProcess, SumPorcentaje, ElapsedTime):

    # Connect to the database
    connection = pymysql.connect(host=Conexion[0],
                            user=Conexion[1],
                            password=Conexion[2],
                            db=Conexion[3],
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
        # Create a new record
                         
            sql = "INSERT INTO `FrameProcessing` ( `Guid`, `Frame`, `TotalPerCentum`, `ElapsedTime`) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (GuidTest, FrameProcess, SumPorcentaje, ElapsedTime))
            
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()

            print ("///////////////////////////////////////////////////////////////////")
            print ("   --  Se realizo Registro del Analisis del Frame Totales", FrameProcess)
            print ("///////////////////////////////////////////////////////////////////")

    finally:
        connection.close()