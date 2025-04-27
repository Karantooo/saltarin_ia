import pygame
from juego.constants import *
from juego.agente import Agente
import time
from juego.casilla import Casilla, EstadosExploracion


class Tablero:
    def __init__(self, filas, columnas, inicio, objetivo, matriz_valores):
        pygame.init()
        self.filas = filas
        self.columnas = columnas
        self.inicio = inicio
        self.objetivo = objetivo
        self.casillas = [
            [Casilla(i, j, matriz_valores[i][j]) for j in range(columnas)]
            for i in range(filas)
        ]
        self.agente = Agente(*inicio,columnas - 1, filas - 1)
        self.tamano_celda = TAM_CASILLA
        self.ancho = max(columnas * self.tamano_celda, self.tamano_celda * 4)
        self.alto = (filas + 1) * self.tamano_celda
        self.ventana = pygame.display.set_mode((self.ancho, self.alto))

        self.coordenadas_vistas = set()
        pygame.display.set_caption("Laberinto Saltarín")

    def dibujar(self):
        self.__tablero_dibujar()
        self.__objetivo_dibujar()
        self.__agente_dibujar()
        self.__movimientos_cantidad_dibujar()

        pygame.display.flip()

    def loop(self):
        corriendo = True
        #self.dfs_solucion(0.0)
        while corriendo:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False
                elif evento.type == pygame.KEYDOWN:
                    desplazamiento = self.casillas[self.agente.fila][self.agente.columna].valor
                    if evento.key == pygame.K_DOWN:
                        self.agente.mover_vertical(desplazamiento)
                    if evento.key == pygame.K_UP:
                        self.agente.mover_vertical(-desplazamiento)
                    if evento.key == pygame.K_RIGHT:
                        self.agente.mover_horizontal(desplazamiento)
                    if evento.key == pygame.K_LEFT:
                        self.agente.mover_horizontal(-desplazamiento)

                    # Verificar victoria
                    if (self.agente.fila, self.agente.columna) == (self.objetivo[0], self.objetivo[1]):
                        print("GG")
                        corriendo = False

            self.dibujar()
        pygame.quit()

    def dfs_solucion(self, tiempo):

        coordenadas = (self.agente.fila, self.agente.columna)
        if coordenadas == self.objetivo:
            self.dibujar()
            return True

        # Evitar visitar la misma casilla
        if coordenadas in self.coordenadas_vistas:
            return False

        self.casillas[self.agente.fila][self.agente.columna].explorado = EstadosExploracion.EXPLORANDO

        self.coordenadas_vistas.add(coordenadas)
        self.dibujar()
        time.sleep(tiempo)

        desplazamiento = self.casillas[self.agente.fila][self.agente.columna].valor

        # Intentar mover en las 4 direcciones
        for mover in [self.agente.mover_horizontal, self.agente.mover_vertical]:
            for signo in [1, -1]:
                # Guardar coordenadas originales
                fila_orig, col_orig = self.agente.fila, self.agente.columna

                # Intentar mover
                desplazamiento = signo * desplazamiento
                mover(desplazamiento)
                if self.dfs_solucion(tiempo):
                    return True  # Terminar si se encontró la solución

                # Volver atrás (backtrack)
                self.agente.fila, self.agente.columna = fila_orig, col_orig
                self.dibujar()
                time.sleep(tiempo)
        self.casillas[self.agente.fila][self.agente.columna].explorado = EstadosExploracion.EXPLORADO

        return False

    def mostrar_sin_solucion(self):
        self.__mensaje_final("No hay solucion", RED)

    def __mensaje_final(self, mensaje, color):
        dimensiones_ventana = (max(self.ancho, 600), max(self.alto, 600))
        self.ventana = pygame.display.set_mode(dimensiones_ventana)
        # Vaciar la pantalla (rellenarla de blanco)
        self.ventana.fill(WHITE)

        # Crear el texto
        fuente = pygame.font.SysFont(None, 48)
        texto = fuente.render(mensaje, True, color)

        # Obtener el rectángulo del texto y centrarlo
        rect = texto.get_rect(center=(dimensiones_ventana[0] // 2, dimensiones_ventana[1] // 2))

        # Dibujar el texto
        self.ventana.blit(texto, rect)

        # Actualizar la pantalla
        pygame.display.flip()

    def __movimientos_cantidad_dibujar(self):
        texto = pygame.font.SysFont(None, 24).render(
            "Movimientos dados: " + str(self.agente.movimientos_dados),
            True,
            BLACK
        )
        self.ventana.blit(texto, (0, self.filas * self.tamano_celda))

    def __agente_dibujar(self):
        ag_x = self.agente.columna * self.tamano_celda + self.tamano_celda // 2
        ag_y = self.agente.fila * self.tamano_celda + self.tamano_celda // 2
        pygame.draw.circle(self.ventana, BLUE, (ag_x, ag_y), self.tamano_celda // 3)

    def __objetivo_dibujar(self):
        og_x = self.objetivo[1] * self.tamano_celda
        og_y = self.objetivo[0] * self.tamano_celda
        pygame.draw.rect(self.ventana, GREEN, (og_x, og_y, self.tamano_celda, self.tamano_celda))

    def __tablero_dibujar(self):
        self.ventana.fill(WHITE)
        for i in range(self.filas):
            for j in range(self.columnas):
                x = j * self.tamano_celda
                y = i * self.tamano_celda

                color_casilla = self.casillas[i][j].explorado

                pygame.draw.rect(self.ventana, color_casilla, (x, y, self.tamano_celda, self.tamano_celda), 0)
                valor = self.casillas[i][j].valor
                texto = pygame.font.SysFont(None, 24).render(str(valor), True, BLACK)
                self.ventana.blit(texto, (x + 20, y + 20))

