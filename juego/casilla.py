import juego.constants

class EstadosExploracion:
    NO_EXPLORADO = juego.constants.GRAY
    EXPLORANDO = juego.constants.PINK
    EXPLORADO = juego.constants.BLUE

class Casilla:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor  # valor saltarín
        self.explorado = EstadosExploracion.NO_EXPLORADO

