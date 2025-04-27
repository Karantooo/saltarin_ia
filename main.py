import time

from juego.tablero import Tablero

# Ejemplo de uso
if __name__ == "__main__":
    m, n = 5, 2
    inicio = (0, 0)
    objetivo = (1, 1)
    matriz_valores = [
        [0, 4],
        [3, 3],
        [3, 1],
        [4, 2],
        [4, 1]
    ]
    tablero = Tablero(m, n, inicio, objetivo, matriz_valores)
    if tablero.dfs_solucion(0.1):
        time.sleep(1)
    else:
        tablero.mostrar_sin_solucion()
        time.sleep(1)
