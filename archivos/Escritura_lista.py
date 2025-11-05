lista = ["My Way", "Back to Black", "Oro de Ley", "Gwendolyne", "Hey"]
ubicacion = "C:\\Users\\sadsd\\OneDrive\\Desktop\\Archivos"
modo = "x"

nombre_archivo = "canciones.txt" 
fp = open(ubicacion+"\\"+nombre_archivo, modo, encoding="utf-8")
#fp.writelines(lista)
for cancion in lista:
    fp.write(cancion+"\n")

fp.close()

