import os
import csv

ruta_base = r"C:\Users\sadsd\Programación-2025\prog-2025-2-10am-unidad5-Santialdiaz\Reto"

def listar_archivos():
    """Muestra los archivos disponibles en la carpeta indicada"""
    print("\nArchivos en la carpeta actual:\n")

    try:
        archivos = os.listdir(ruta_base)
        if not archivos:
            print("No hay archivos en esta carpeta.")
        else:
            for archivo in archivos:
                print("-", archivo)
    except FileNotFoundError:
        print("La ruta especificada no existe. Verifica 'ruta_base'.")


# -----------------------------
# FUNCIONES PARA ARCHIVOS .TXT
# -----------------------------

def contar_palabras_caracteres(nombre):
    ruta = os.path.join(ruta_base, nombre)
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            texto = f.read()
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return

    palabras = texto.split()
    total_palabras = len(palabras)
    total_caracteres = len(texto)
    sin_espacios = len(texto.replace(" ", ""))

    print("\nResultados:")
    print("Número de palabras:", total_palabras)
    print("Caracteres (con espacios):", total_caracteres)
    print("Caracteres (sin espacios):", sin_espacios)


def reemplazar_palabra(nombre):
    ruta = os.path.join(ruta_base, nombre)
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            texto = f.read()
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return

    palabra_buscar = input("Palabra a buscar: ")
    palabra_nueva = input("Palabra por la que se reemplazará: ")

    nuevo_texto = texto.replace(palabra_buscar, palabra_nueva)

    with open(ruta, "w", encoding="utf-8") as f:
        f.write(nuevo_texto)

    print("Reemplazo completado.")


def histograma_vocales(nombre):
    ruta = os.path.join(ruta_base, nombre)
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            texto = f.read().lower()
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return

    vocales = ["a", "e", "i", "o", "u"]
    conteos = {}

    for v in vocales:
        conteos[v] = texto.count(v)

    print("\nHistograma de vocales:")
    for v in vocales:
        barras = "*" * conteos[v]
        print(f"{v}: {barras} ({conteos[v]})")


# -----------------------------
# FUNCIONES PARA ARCHIVOS .CSV
# -----------------------------

def mostrar_15_filas(nombre):
    ruta = os.path.join(ruta_base, nombre)
    try:
        with open(ruta, newline="", encoding="utf-8") as f:
            lector = csv.reader(f)
            for i, fila in enumerate(lector):
                print(fila)
                if i == 14:
                    break
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except:
        print("Error al leer el archivo.")


def calcular_estadisticas(nombre):
    ruta = os.path.join(ruta_base, nombre)
    columna = input("Ingrese el nombre de la columna a analizar: ")

    try:
        with open(ruta, newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            datos = []
            for fila in lector:
                valor = fila.get(columna, "")
                if valor != "":
                    try:
                        datos.append(float(valor))
                    except:
                        pass
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return

    if len(datos) == 0:
        print("No hay datos numéricos en esa columna.")
        return

    n = len(datos)
    promedio = sum(datos) / n
    datos_ordenados = sorted(datos)
    if n % 2 == 0:
        mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
    else:
        mediana = datos_ordenados[n//2]
    maximo = max(datos)
    minimo = min(datos)
    varianza = sum((x - promedio) ** 2 for x in datos) / n
    desviacion = varianza ** 0.5

    print("\nEstadísticas de la columna", columna)
    print("Cantidad de datos:", n)
    print("Promedio:", promedio)
    print("Mediana:", mediana)
    print("Desviación estándar:", desviacion)
    print("Valor máximo:", maximo)
    print("Valor mínimo:", minimo)


def graficar_columna(nombre):
    ruta = os.path.join(ruta_base, nombre)
    columna = input("Ingrese el nombre de la columna numérica: ")

    try:
        with open(ruta, newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            datos = []
            for fila in lector:
                valor = fila.get(columna, "")
                if valor != "":
                    try:
                        datos.append(float(valor))
                    except:
                        pass
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return

    if len(datos) == 0:
        print("No hay datos numéricos en esa columna.")
        return

    print(f"\nGráfico textual de la columna '{columna}':")
    max_valor = max(datos)
    for i, valor in enumerate(datos[:20]):  # solo los primeros 20 valores
        longitud = int((valor / max_valor) * 50)
        barras = "*" * longitud
        print(f"{i+1:02d}: {barras} ({valor})")


# -----------------------------
# MENÚS
# -----------------------------

def menu_txt():
    nombre = input("Ingrese el nombre del archivo .txt (con extensión): ")

    while True:
        print("\n--- Submenú Archivos .TXT ---")
        print("1. Contar palabras y caracteres")
        print("2. Reemplazar palabra")
        print("3. Histograma de vocales")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            contar_palabras_caracteres(nombre)
        elif opcion == "2":
            reemplazar_palabra(nombre)
        elif opcion == "3":
            histograma_vocales(nombre)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")


def menu_csv():
    nombre = input("Ingrese el nombre del archivo .csv (con extensión): ")

    while True:
        print("\n--- Submenú Archivos .CSV ---")
        print("1. Mostrar las primeras 15 filas")
        print("2. Calcular estadísticas")
        print("3. Graficar columna (texto)")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_15_filas(nombre)
        elif opcion == "2":
            calcular_estadisticas(nombre)
        elif opcion == "3":
            graficar_columna(nombre)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")


def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Listar archivos en la carpeta actual")
        print("2. Procesar archivo de texto (.txt)")
        print("3. Procesar archivo separado por comas (.csv)")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_archivos()
        elif opcion == "2":
            menu_txt()
        elif opcion == "3":
            menu_csv()
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
