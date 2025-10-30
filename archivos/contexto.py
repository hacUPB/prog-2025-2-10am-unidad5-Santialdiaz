nombre_archivo = "texto.txt" 
ubicacion = "C:\\Users\\sadsd\\OneDrive\\Desktop\\Archivos"
with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    # Leer todas las lineas dentro de una lista
    lista = archivo.readlines()

for c in lista:
    print(c)