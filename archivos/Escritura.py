ubicacion = "C:\\Users\\sadsd\\OneDrive\\Desktop\\Archivos"
#\ se usa para comandos de texto 
nombre_archivo = "frutas.txt"
modo = "a" #solo escriuta, solo sobreescribre
fp = open(ubicacion+"\\"+nombre_archivo, modo, encoding="utf-8")
frase = input("Por favor ingresa una frase: ")
fp.write(frase)
#TAREA: Solcitar al usuario que ingrese una variable entrera y una float al usuario y la escriben en el archivo
#SOLUCION 
numero_entero = int(input("Por favor ingresa tu edad: "))
numero_flotante = float(input("Por favor ingresa tu estatura: "))

fp.write("Frase: " + frase + "\n")
fp.write("Número entero: " + str(numero_entero) + "\n")
fp.write("Número flotante: " + str(numero_flotante) + "\n")

fp.close()