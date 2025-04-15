class Agente:
    def __init__(self, fila, columna, x_frontera, y_frontera):
        self.fila = fila
        self.columna = columna
        self.x_frontera = x_frontera
        self.y_frontera = y_frontera
        self.movimientos_dados = 0

    def mover_horizontal(self, distancia):
        print(str(self.x_frontera) + " " + str(self.columna + distancia))
        if 0 <= self.fila + distancia <= self.x_frontera:
            self.columna += distancia
            self.movimientos_dados += 1

    def mover_vertical(self, distancia):
        print(str(self.y_frontera) + " " + str(self.fila + distancia))
        if 0 <= self.fila + distancia <= self.y_frontera:
            self.fila += distancia
            self.movimientos_dados += 1
