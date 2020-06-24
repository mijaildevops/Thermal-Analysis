from cv2 import cv2

captura = cv2.VideoCapture('Video-Termico-Corte.mp4')
while (captura.isOpened()):
  ret, imagen = captura.read()
  cv2.imwrite('FramePresado.png', imagen)
  if ret == True:
    cv2.imshow('video', imagen)
    #cv2.imwrite('FramePresado.png', imagen)
    if cv2.waitKey(30) == ord('s'):
      break
  else: break
captura.release()
cv2.destroyAllWindows()