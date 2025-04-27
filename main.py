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
    if tablero.bfs_solucion(0.3):
        tablero.mostrar_con_solucion()
    else:
        tablero.mostrar_sin_solucion()
    time.sleep(1)
