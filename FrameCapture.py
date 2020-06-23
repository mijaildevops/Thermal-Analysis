from cv2 import cv2
import sys, time
#camera = cv2.VideoCapture(0) 


for i in range(20): 
    camera = 0
    # Take Frame to USB Camera
    #camera = cv2.VideoCapture(camera)
    # Take Frame to IP Camera
    camera = cv2.VideoCapture('http://100.97.218.207/vsblty/Recursos/Multiple/1920-Presidentes.jpg')
    print (camera)
    time.sleep(5)
    return_value, image = camera.read() 
    cv2.imwrite('opencv'+str(i)+'.png', image) 
    #input ()
    del(camera) 
