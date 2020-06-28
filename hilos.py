import threading
import time
import datetime
import logging

def consultar (id):
    time.sleep(2)
    pass

def guardar (id, data):
    time.sleep(5)
    pass

tiempo_ini = datetime.datetime.now()

t1 = threading.Thread(name="hilo_1", target=consultar, args=(1, ))
t2 = threading.Thread(name="hilo_2", target=guardar, args=(1, "Pilas desde t2"))

t1.start()
t2.start()

t1.join()
t2.join()


tiempo_fin = datetime.datetime.now()

print ("Tiempo trasnscurridfo " + str(tiempo_fin.second - tiempo_ini.second))