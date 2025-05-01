import os

def leer_tableros(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    tableros = []
    i = 0
    while i < len(lineas):
        if not lineas[i].strip():
            i += 1
            continue  # Saltar líneas vacías si hay
        if lineas[i].strip() == "0":
            break

        # Leer m, n, inicio y objetivo
        valores = list(map(int, lineas[i].split()))

        m, n = valores[0], valores[1]
        inicio = (valores[2], valores[3])
        objetivo = (valores[4], valores[5])
        i += 1

        # Leer la matriz
        matriz_valores = []
        for _ in range(m):
            fila = list(map(int, lineas[i].split()))
            matriz_valores.append(fila)
            i += 1

        # Guardar el tablero leído
        tableros.append((m, n, inicio, objetivo, matriz_valores))

    return tableros


def guardar_log(nombre_archivo, contenido):
    carpeta_logs = "logs"

    if not os.path.exists(carpeta_logs):
        os.makedirs(carpeta_logs)

    nombre_archivo = nombre_archivo.replace("*", "star")

    ruta_completa = os.path.join(carpeta_logs, nombre_archivo)

    with open(ruta_completa, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)