from excepcion_personalizada import SinStockException

class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = {}

    def agregar_producto(self, producto, stock):
        self.productos[producto] = stock

    def comprar_producto(self, producto, cantidad):
        if producto not in self.productos:
            raise SinStockException(producto)
        self.productos[producto] -= cantidad
