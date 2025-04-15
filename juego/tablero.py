import pygame
from juego.constants import *

class Casilla:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor  # valor saltarín

class Agente:
    def __init__(self, fila, columna, x_frontera, y_frontera):
        self.fila = fila
        self.columna = columna
        self.x_frontera = x_frontera
        self.y_frontera = y_frontera
        self.movimientos_dados = 0

    def mover_horizontal(self, distancia):
        if 0 <= self.columna + distancia <= self.x_frontera:
            self.columna += distancia
            self.movimientos_dados += 1

    def mover_vertical(self, distancia):
        if 0 <= self.fila + distancia <= self.x_frontera:
            self.fila += distancia
            self.movimientos_dados += 1


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
        self.agente = Agente(*inicio, filas - 1, columnas - 1)
        self.tamano_celda = TAM_CASILLA
        self.ancho = columnas * self.tamano_celda
        self.alto = filas * self.tamano_celda
        self.ventana = pygame.display.set_mode((self.ancho, self.alto + 70))
        pygame.display.set_caption("Laberinto Saltarín")

    def dibujar(self):
        self.ventana.fill(WHITE)
        for i in range(self.filas):
            for j in range(self.columnas):
                x = j * self.tamano_celda
                y = i * self.tamano_celda
                pygame.draw.rect(self.ventana, GRAY, (x, y, self.tamano_celda, self.tamano_celda), 1)
                valor = self.casillas[i][j].valor
                texto = pygame.font.SysFont(None, 24).render(str(valor), True, BLACK)
                self.ventana.blit(texto, (x + 20, y + 20))

        # Dibujar objetivo
        og_x = self.objetivo[1] * self.tamano_celda
        og_y = self.objetivo[0] * self.tamano_celda
        pygame.draw.rect(self.ventana, GREEN, (og_x, og_y, self.tamano_celda, self.tamano_celda))

        # Dibujar agente
        ag_x = self.agente.columna * self.tamano_celda + self.tamano_celda // 2
        ag_y = self.agente.fila * self.tamano_celda + self.tamano_celda // 2
        pygame.draw.circle(self.ventana, BLUE, (ag_x, ag_y), self.tamano_celda // 3)

        pygame.display.flip()

    def loop(self):
        corriendo = True
        while corriendo:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_DOWN:
                        desplazamiento = self.casillas[self.agente.fila][self.agente.columna].valor
                        self.agente.mover_vertical(desplazamiento)
                    if evento.key == pygame.K_UP:
                        desplazamiento = self.casillas[self.agente.fila][self.agente.columna].valor
                        self.agente.mover_vertical(-desplazamiento)
                    if evento.key == pygame.K_RIGHT:
                        desplazamiento = self.casillas[self.agente.fila][self.agente.columna].valor
                        self.agente.mover_horizontal(desplazamiento)
                    if evento.key == pygame.K_LEFT:
                        desplazamiento = self.casillas[self.agente.fila][self.agente.columna].valor
                        self.agente.mover_horizontal(-desplazamiento)

            self.dibujar()
        pygame.quit()

