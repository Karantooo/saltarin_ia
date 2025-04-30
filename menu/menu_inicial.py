import pygame
import pygame_menu
from tkinter import Tk, filedialog
from typing import List, Tuple

# Ocultar ventana de Tkinter al usar filedialog
Tk().withdraw()

archivo_seleccionado = [""]
algoritmo_seleccionado = ["DFS"]

tiempo_entre_pasos = 0.3

lista_algoritmos = ('DFS', 'BFS', 'A*', 'UCS')
loop_menu = True

def seleccionar_archivo():
    ruta = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if ruta:
        archivo_seleccionado[0] = ruta
        print("Archivo seleccionado:", ruta)


def seleccionar_algoritmo(value, _):
    algoritmo_seleccionado[0] = value[0][0]
    print("Algoritmo seleccionado:", value)

def comenzar():
    global loop_menu
    if not archivo_seleccionado[0]:
        print("Debes seleccionar un archivo primero.")
        return
    try:
        loop_menu = False

    except Exception as e:
        print("Error al leer el archivo:", e)

def set_valor(value: float):
    global tiempo_entre_pasos
    tiempo_entre_pasos = value

def mostrar_menu() -> Tuple[str, str]:
    pygame.init()
    surface = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Selector de archivo y algoritmo")


    menu = pygame_menu.Menu('Configuración del problema', 600, 400, theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button('Seleccionar archivo', seleccionar_archivo)
    menu.add.selector('Algoritmo :', [(a, a) for a in lista_algoritmos], onchange=seleccionar_algoritmo)
    menu.add.range_slider(
        'Velocidad en segundos:',
        default=0.3,
        range_values=(0.0, 1.0),
        increment=0.1,
        value_format=lambda x: f'{x:.1f}',  # Formato mostrado
        onchange=set_valor
    )
    menu.add.button('Comenzar', comenzar)
    menu.add.button('Salir', pygame_menu.events.EXIT)

    while loop_menu:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return "", "", []

        surface.fill((0, 0, 0))
        menu.update(events)
        menu.draw(surface)
        pygame.display.flip()

    pygame.quit()

    return archivo_seleccionado[0], algoritmo_seleccionado[0], tiempo_entre_pasos