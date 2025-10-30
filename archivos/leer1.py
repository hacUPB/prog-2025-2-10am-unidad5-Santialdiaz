#1. Abrir el archivo y definir el modo
archivo = open("texto.txt","r")  

#2. Leer el archivo
#datos = archivo.read(100)

#for datos in range(5):
#    datos = archivo.readline #una linea es hasta donde se encuentre un enter 

#con readlines se lee todo el archivo pero cada linea es un elemento de la lista, cada dato es una cadena de caracters
datos = archivo.readlines()
print(datos)

#Un archivo de python si es iterbale pq se puede recorrer por medio de for
#for datos in archivo:
 #   print(datos)
             

#Cadenas de caracteres tambien son iterables
#Yo me puedo referir a cada una de las letras de caracteres como una lista, en este caso imprimir la primera letra
#for datos in archivo:
#    print(datos[0])



#ES IMPORTANTE CERRAR EL ARCHIVO #EOF significa end of file y no lee mas, se detiene.
archivo.close()   