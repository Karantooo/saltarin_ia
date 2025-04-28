import time

from juego.tablero import Tablero

# Ejemplo de uso
if __name__ == "__main__":
    m, n = 5, 5
    inicio = (0, 0)
    objetivo = (1, 3)
    matriz_valores = [
        [3, 4, 1, 3, 1],
        [3, 3, 3, 3, 2],
        [3, 1, 2, 2, 3],
        [4, 2, 3, 3, 3],
        [4, 1, 4, 3, 2]
    ]
    tablero = Tablero(m, n, inicio, objetivo, matriz_valores)
    solucion = tablero.bfs_solucion(0.1)
    if solucion[0]:
        camino = solucion[1][::-1]
        print (camino)
        camino
        tablero.dibujar_camino(camino)

        time.sleep(1)
        tablero.mostrar_con_solucion()
    else:
        tablero.mostrar_sin_solucion()
    time.sleep(1)
