import time

from juego.tablero import Tablero
from menu.utils import leer_tableros
from menu.menu_inicial import mostrar_menu

# Ejemplo de uso
if __name__ == "__main__":
    ruta_archivo, algoritmo_seleccionado, tiempo = mostrar_menu()
    tableros = leer_tableros(ruta_archivo)

    busqueda_metodo = {
        "DFS": Tablero.dfs_solucion,
        "BFS": Tablero.bfs_solucion,
        "UCS": Tablero.ucs_solucion,
    }
    print(algoritmo_seleccionado)
    for tablero in tableros:
        m, n, inicio, objetivo, matriz_valores = tablero
        tablero = Tablero(m, n, inicio, objetivo, matriz_valores)
        solucion = busqueda_metodo[algoritmo_seleccionado](tablero, tiempo)
        if solucion[0]:
            camino = solucion[1][::-1]
            print(solucion)
            tablero.dibujar_camino(camino)

            time.sleep(1)
            tablero.mostrar_con_solucion()
        else:
            tablero.mostrar_sin_solucion()
        time.sleep(1)
