from excepcion_personalizada import SinStockException

class Producto:
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.stock = stock

    def comprar(self, cantidad):
        if cantidad > self.stock:
            raise SinStockException(self.nombre)
        self.stock -= cantidad

