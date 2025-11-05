import csv
with open('C:\\Users\\sadsd\\Programación-2025\\prog-2025-2-10am-unidad5-Santialdiaz\\Variables.csv', 'r') as csvfile:   #usamos el manejador de contexto
    lector = csv.reader(csvfile, delimiter=";") #se utiliza el método reader
    for fila in lector:          #con el for se itera sobre el objeto para leer
        print(fila)