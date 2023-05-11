class SinStockException(Exception):
    def __init__(self, producto):
        self.producto = producto

    def __str__(self):
        return f"No hay stock disponible para el producto {self.producto}"
