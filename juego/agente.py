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
            return True
        return False

    def es_coordenada_valida_horizontal(self, distancia):
        return 0 <= self.columna + distancia <= self.x_frontera

    def es_coordenada_valida_vertical(self, distancia):
        return 0 <= self.fila + distancia <= self.y_frontera

    def mover_vertical(self, distancia):
        if 0 <= self.fila + distancia <= self.y_frontera:
            self.fila += distancia
            self.movimientos_dados += 1
            return True
        return False
