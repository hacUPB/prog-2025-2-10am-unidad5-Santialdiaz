#Ayudas de la iA: try, para evitar bloqueos al presentarse un error, me pareció más funcional y directo
import os
import csv
import matplotlib.pyplot as plt
import re


ruta_base = "C:\\Users\\sadsd\\Programación-2025\\prog-2025-2-10am-unidad5-Santialdiaz\\Reto"



def listar_archivos(ruta):
    """Lista archivos .csv y .txt en la carpeta indicada."""
    if not os.path.exists(ruta):
        print("La ruta no existe. Revisa la variable 'ruta_base'.")
        return []
    archivos = []
    for nombre in os.listdir(ruta):
        if nombre.lower().endswith(".csv") or nombre.lower().endswith(".txt"):
            archivos.append(nombre)
    if len(archivos) == 0:
        print("No se encontraron archivos .csv ni .txt en la carpeta.")
    else:
        print("\nArchivos encontrados:")
        for a in archivos:
            print("-", a)
    return archivos

# FUNCIONES PARA ARCHIVOS .TXT


def contar_palabras_y_caracteres(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print("Archivo no encontrado.")
        return
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        texto = f.read()
    palabras = texto.split()
    num_palabras = len(palabras)
    num_caracteres_con = len(texto)
    num_caracteres_sin = len(texto.replace(" ", ""))
    print("\nResultados:")
    print("Número de palabras:", num_palabras)
    print("Caracteres (con espacios):", num_caracteres_con)
    print("Caracteres (sin espacios):", num_caracteres_sin)

def reemplazar_palabra_txt(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print("Archivo no encontrado.")
        return
    palabra_buscar = input("Palabra a buscar: ")
    palabra_nueva = input("Palabra por la que se reemplazará: ")
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        texto = f.read()
    if palabra_buscar not in texto:
        print("La palabra buscada no está presente en el archivo.")
        return
    texto_nuevo = texto.replace(palabra_buscar, palabra_nueva)
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        f.write(texto_nuevo)
    print("Reemplazo completado y guardado en el archivo.")

def histograma_vocales_txt(ruta_archivo):
    if not os.path.exists(ruta_archivo):
        print("Archivo no encontrado.")
        return
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        texto = f.read().lower()
    vocales = ["a", "e", "i", "o", "u"]
    conteo = [texto.count(v) for v in vocales]
    print("\nOcurrencias de vocales:")
    for v, c in zip(vocales, conteo):
        print(f"{v}: {c}")
    plt.bar(vocales, conteo, color="skyblue", edgecolor="black")
    plt.title("Histograma de vocales")
    plt.xlabel("Vocal")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()

def submenu_txt():
    archivos = [f for f in os.listdir(ruta_base) if f.lower().endswith(".txt")]
    if len(archivos) == 0:
        print("No se encontraron archivos .txt en la carpeta.")
        return
    print("\nArchivos .txt disponibles:")
    for i, a in enumerate(archivos, start=1):
        print(f"{i}. {a}")
    sel = input("Selecciona el número del archivo .txt (o escribe el nombre): ")
    if sel.isdigit():
        idx = int(sel) - 1
        if 0 <= idx < len(archivos):
            nombre = archivos[idx]
        else:
            print("Selección inválida.")
            return
    else:
        nombre = sel
        if nombre not in archivos:
            print("Archivo no encontrado.")
            return
    ruta_archivo = os.path.join(ruta_base, nombre)
    while True:
        print("\n--- SUBMENÚ .TXT ---")
        print("1. Contar palabras y caracteres")
        print("2. Reemplazar una palabra")
        print("3. Histograma de vocales (gráfico)")
        print("4. Volver al menú principal")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            contar_palabras_y_caracteres(ruta_archivo)
        elif opcion == "2":
            reemplazar_palabra_txt(ruta_archivo)
        elif opcion == "3":
            histograma_vocales_txt(ruta_archivo)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

# FUNCIONES PARA ARCHIVOS .CSV

def leer_csv_sin_pandas(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        lineas = [l.strip() for l in f if l.strip() != ""]
    encabezado = lineas[0].split(",")
    datos = [linea.split(",") for linea in lineas[1:]]
    return encabezado, datos

def convertir_a_float(valor):
    """Intenta convertir cualquier formato numérico común (con , o .) a float."""
    if valor is None:
        return None
    valor = valor.strip()
    if valor == "" or valor.upper() in ("NA", "N/A", "-", "--"):
        return None

   
    valor = re.sub(r"[^\d,.\-]", "", valor)

    
    if "," in valor and "." in valor:
        if valor.find(",") > valor.find("."):
            valor = valor.replace(".", "").replace(",", ".")
        else:
            valor = valor.replace(",", "")
    elif "," in valor:

        valor = valor.replace(",", ".")
    try:
        return float(valor)
    except:
        return None

def detectar_columnas_numericas(encabezado, datos):
    """Detecta columnas con valores numéricos válidos."""
    columnas_validas = []
    for i, col in enumerate(encabezado):
        valores_convertidos = [convertir_a_float(fila[i]) for fila in datos if i < len(fila)]
        if any(v is not None for v in valores_convertidos):
            columnas_validas.append(col)
    return columnas_validas

def extraer_valores_columna(encabezado, datos, nombre_columna):
    """Extrae valores numéricos válidos de una columna dada."""
    if nombre_columna not in encabezado:
        return []
    idx = encabezado.index(nombre_columna)
    valores = []
    for fila in datos:
        if idx < len(fila):
            v = convertir_a_float(fila[idx])
            if v is not None:
                valores.append(v)
    return valores

def mostrar_15_filas_csv(ruta_archivo):
    encabezado, datos = leer_csv_sin_pandas(ruta_archivo)
    print("\nEncabezado:")
    print(encabezado)
    print("\nPrimeras 15 filas:")
    for i, fila in enumerate(datos[:15], start=1):
        print(f"{i}: {fila}")

def calcular_estadisticas_columna(valores):
    if len(valores) == 0:
        return None
    n = len(valores)
    minimo = min(valores)
    maximo = max(valores)
    promedio = sum(valores) / n
    orden = sorted(valores)
    if n % 2 == 1:
        mediana = orden[n // 2]
    else:
        mediana = (orden[n // 2 - 1] + orden[n // 2]) / 2
    var = sum((x - promedio) ** 2 for x in valores) / n
    desviacion = var ** 0.5
    return {
        "cantidad": n,
        "promedio": promedio,
        "mediana": mediana,
        "desviacion": desviacion,
        "minimo": minimo,
        "maximo": maximo
    }

def graficar_valores(valores, titulo, tipo):
    if tipo == "linea":
        plt.plot(valores, marker="o", linestyle="-")
    elif tipo == "barras":
        plt.bar(range(len(valores)), valores)
    elif tipo == "dispersion":
        plt.scatter(range(len(valores)), valores)
    elif tipo == "hist":
        plt.hist(valores, bins=20, edgecolor="black")
    else:
        print("Tipo de gráfica no reconocido.")
        return
    plt.title(titulo)
    plt.xlabel("Índice")
    plt.ylabel("Valor")
    plt.tight_layout()
    plt.show()

def submenu_csv():
    archivos_csv = [f for f in os.listdir(ruta_base) if f.lower().endswith(".csv")]
    if len(archivos_csv) == 0:
        print("No se encontraron archivos CSV en la carpeta.")
        return
    print("\nArchivos CSV disponibles:")
    for i, a in enumerate(archivos_csv, start=1):
        print(f"{i}. {a}")
    sel = input("Selecciona el número del archivo (o escribe el nombre): ")
    if sel.isdigit():
        idx = int(sel) - 1
        if 0 <= idx < len(archivos_csv):
            nombre = archivos_csv[idx]
        else:
            print("Selección inválida.")
            return
    else:
        nombre = sel
        if nombre not in archivos_csv:
            print("Archivo no encontrado.")
            return
    ruta_archivo = os.path.join(ruta_base, nombre)

    while True:
        print("\n--- SUBMENÚ CSV ---")
        print("1. Mostrar las 15 primeras filas")
        print("2. Calcular estadísticas de una columna")
        print("3. Graficar una columna")
        print("4. Volver al menú principal")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_15_filas_csv(ruta_archivo)

        elif opcion == "2":
            encabezado, datos = leer_csv_sin_pandas(ruta_archivo)
            columnas_validas = detectar_columnas_numericas(encabezado, datos)
            print("\nColumnas con valores numéricos detectadas:")
            for col in columnas_validas:
                print("-", col)
            columna = input("\nEscribe exactamente el nombre de la columna a analizar: ")
            if columna not in encabezado:
                print("Columna no encontrada.")
                continue
            valores = extraer_valores_columna(encabezado, datos, columna)
            if len(valores) == 0:
                print("No se encontraron valores numéricos en esa columna.")
                continue
            stats = calcular_estadisticas_columna(valores)
            print(f"\nEstadísticas para '{columna}':")
            print("Cantidad:", stats["cantidad"])
            print("Promedio:", round(stats["promedio"], 3))
            print("Mediana:", round(stats["mediana"], 3))
            print("Desviación estándar:", round(stats["desviacion"], 3))
            print("Mínimo:", stats["minimo"])
            print("Máximo:", stats["maximo"])

        elif opcion == "3":
            encabezado, datos = leer_csv_sin_pandas(ruta_archivo)
            columnas_validas = detectar_columnas_numericas(encabezado, datos)
            print("\nColumnas con valores numéricos detectadas:")
            for col in columnas_validas:
                print("-", col)
            columna = input("\nEscribe exactamente el nombre de la columna a graficar: ")
            if columna not in encabezado:
                print("Columna no encontrada.")
                continue
            valores = extraer_valores_columna(encabezado, datos, columna)
            if len(valores) == 0:
                print("No se encontraron valores numéricos en esa columna.")
                continue
            print("\nTipos de gráfica:")
            print("1. Línea\n2. Barras\n3. Dispersión\n4. Histograma")
            t = input("Selecciona (1-4): ")
            tipo = {"1": "linea", "2": "barras", "3": "dispersion", "4": "hist"}.get(t)
            if not tipo:
                print("Opción inválida.")
                continue
            graficar_valores(valores, columna, tipo)

        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

# MENÚ PRINCIPAL

def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Listar archivos (CSV y TXT)")
        print("2. Procesar archivo .txt")
        print("3. Procesar archivo .csv")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            listar_archivos(ruta_base)
        elif opcion == "2":
            submenu_txt()
        elif opcion == "3":
            submenu_csv()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    menu_principal()

