from excepcion_personalizada import SinStockException
from producto import Producto
from sucursal import Sucursal
from bodega import Bodega

def probar_excepciones():
    try:
        producto = Producto("martillos", 9)
        producto.comprar(10)
    except SinStockException as e:
        print(e)

    try:
        sucursal = Sucursal("Sucursal A")
        sucursal.comprar_producto("clavos", 25)
    except SinStockException as e:
        print(e)

    try:
        bodega = Bodega("Bodega A")
        bodega.comprar_producto("Sucursal B", "frenillos", 55)
    except SinStockException as e:
        print(e)

def calcular_valor_promedio(compras):
    if len(compras) == 0:
        raise ValueError("El cliente no tiene compras registradas")
    total = sum(compras)
    return total / len(compras)

def probar_valor_promedio():
    compras_cliente1 = [50, 30, 20]

    try:
        promedio_cliente1 = calcular_valor_promedio(compras_cliente1)
        print(f"Promedio cliente 1: {promedio_cliente1}")
    except ValueError as e:
        print(e)

    compras_cliente2 = [20,30,45]
    try:
        promedio_cliente2 = calcular_valor_promedio(compras_cliente2)
        print(f"Promedio cliente 2: {promedio_cliente2}")
    except ValueError as e:
        print(e)

probar_excepciones()
probar_valor_promedio()
probar_valor_promedio()