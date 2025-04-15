import pygame
from juego.constants import *
from juego.agente import Agente

class Casilla:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor  # valor saltarín


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
        self.ancho = max(columnas * self.tamano_celda, self.tamano_celda * 3)
        self.alto = (filas + 1) * self.tamano_celda
        self.ventana = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption("Laberinto Saltarín")

    def dibujar(self):
        self.tablero_dibujar()
        self.objetivo_dibujar()
        self.agente_dibujar()
        self.movimientos_cantidad_dibujar()

        pygame.display.flip()

    def movimientos_cantidad_dibujar(self):
        texto = pygame.font.SysFont(None, 24).render(
            "Movimientos dados: " + str(self.agente.movimientos_dados),
            True,
            BLACK
        )
        self.ventana.blit(texto, (0, self.filas * self.tamano_celda))

    def agente_dibujar(self):
        ag_x = self.agente.columna * self.tamano_celda + self.tamano_celda // 2
        ag_y = self.agente.fila * self.tamano_celda + self.tamano_celda // 2
        pygame.draw.circle(self.ventana, BLUE, (ag_x, ag_y), self.tamano_celda // 3)

    def objetivo_dibujar(self):
        og_x = self.objetivo[1] * self.tamano_celda
        og_y = self.objetivo[0] * self.tamano_celda
        pygame.draw.rect(self.ventana, GREEN, (og_x, og_y, self.tamano_celda, self.tamano_celda))

    def tablero_dibujar(self):
        self.ventana.fill(WHITE)
        for i in range(self.filas):
            for j in range(self.columnas):
                x = j * self.tamano_celda
                y = i * self.tamano_celda
                pygame.draw.rect(self.ventana, GRAY, (x, y, self.tamano_celda, self.tamano_celda), 1)
                valor = self.casillas[i][j].valor
                texto = pygame.font.SysFont(None, 24).render(str(valor), True, BLACK)
                self.ventana.blit(texto, (x + 20, y + 20))

    def loop(self):
        corriendo = True
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

