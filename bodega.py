from excepcion_personalizada import SinStockException

class Bodega:
    def __init__(self, nombre):
        self.nombre = nombre
        self.sucursales = {}

    def agregar_sucursal(self, sucursal):
        self.sucursales[sucursal.nombre] = sucursal

    def comprar_producto(self, sucursal, producto, cantidad):
        if sucursal not in self.sucursales:
            raise SinStockException(producto)
        self.sucursales[sucursal].comprar_producto(producto, cantidad)
