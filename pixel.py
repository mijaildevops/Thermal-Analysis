from PIL import Image
 
foto = Image.open('balls_colors.jpg')
 
datos = list(foto.getdata())
 
'''la linea anterior tambien podria escribirse como:
 
datos = list(Image.Image.getdata(foto))'''
 
#al finalizar cerramos el objeto instanciado
print (len(datos))
for dato in datos:
    print(dato)
    print(dato[0])
    if (int(dato[0]) < 8 ):
        print ("Rojo")
    elif (int(dato[0]) > 19 and int(dato[0]) < 33 ):
        print ("amarillo")
    else:
        print ("otro Color")
    input()

foto.close()
