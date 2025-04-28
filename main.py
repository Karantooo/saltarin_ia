import time

from juego.tablero import Tablero


def leer_tableros(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    tableros = []
    i = 0
    while i < len(lineas):
        if not lineas[i].strip():
            i += 1
            continue  # Saltar líneas vacías si hay

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


# Ejemplo de uso
if __name__ == "__main__":

    tableros = leer_tableros(r"./mapas/ejemplo.txt")
    for tablero in tableros:
        m, n, inicio, objetivo, matriz_valores = tablero
        tablero = Tablero(m, n, inicio, objetivo, matriz_valores)
        solucion = tablero.ucs_solucion(0.1)
        if solucion[0]:
            camino = solucion[1][::-1]
            print(solucion)
            tablero.dibujar_camino(camino)

            time.sleep(1)
            tablero.mostrar_con_solucion()
        else:
            tablero.mostrar_sin_solucion()
        time.sleep(1)
