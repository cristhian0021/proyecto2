from venta_detalle import VentaDetalle

class Venta:
    def __init__(self, codigo_venta, cliente, descuento, almacen, condicion_pago):
        self.codigo_venta = codigo_venta
        self.cliente = cliente
        self.descuento = descuento
        self.almacen = almacen
        self.condicion_pago = condicion_pago
        self.detalles_venta = []

    def agregar_venta_detalle(self, producto, cantidad, descuento):
        detalle = VentaDetalle(producto, producto.nombre_producto, producto.precio_unitario, cantidad, descuento)
        self.detalles_venta.append(detalle)
        print(f"Producto {producto.nombre_producto} agregado a la venta.")

    def calcular_total(self):
        total = sum(detalle.calcular_subtotal() for detalle in self.detalles_venta)
        total -= total * (self.descuento / 100)
        return total

    def grabar_venta(self):
        ventas_temporales.append(self)
        print(f"Venta {self.codigo_venta} grabada correctamente.")

    @staticmethod
    def listar_ventas():
        return ventas_temporales

    @staticmethod
    def registrar_venta(codigo_venta, cliente, descuento, almacen, condicion_pago):
        nueva_venta = Venta(codigo_venta, cliente, descuento, almacen, condicion_pago)
        ventas_temporales.append(nueva_venta)
        return nueva_venta

# Lista temporal para simular el almacenamiento
ventas_temporales = []
