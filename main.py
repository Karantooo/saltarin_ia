import time
import os

from juego.tablero import Tablero
from menu.utils import leer_tableros, guardar_log
from menu.menu_inicial import mostrar_menu

# Ejemplo de uso
if __name__ == "__main__":
    ruta_archivo, algoritmo_seleccionado, tiempo = mostrar_menu()
    tableros = leer_tableros(ruta_archivo)

    busqueda_metodo = {
        "DFS": Tablero.dfs_solucion,
        "BFS": Tablero.bfs_solucion,
        "UCS": Tablero.ucs_solucion,
        "A*": Tablero.a_star_solucion
    }
    mapa_actual = 1
    log_respuesta = ""
    for tablero in tableros:
        m, n, inicio, objetivo, matriz_valores = tablero
        tablero = Tablero(m, n, inicio, objetivo, matriz_valores)
        solucion = busqueda_metodo[algoritmo_seleccionado](tablero, tiempo)
        if solucion[0]:
            camino = solucion[1][::-1]

            tablero.dibujar_camino(camino)

            time.sleep(1)
            estadisticas = tablero.mostrar_con_solucion(len(camino) - 1)
        else:
            estadisticas = tablero.mostrar_sin_solucion()
        log_respuesta += str(mapa_actual) + "- " + estadisticas + "\n"
        mapa_actual += 1
        time.sleep(1)
    guardar_log(algoritmo_seleccionado + "_" + os.path.basename(ruta_archivo), log_respuesta)
