from cliente import Cliente
from almacen import Almacen
from condicion_pago import CondicionPago
from venta import Venta

def test_registrar_venta():
    cliente = Cliente("C001", "Cliente1")
    cliente.grabar_cliente()

    almacen = Almacen("A001", "Almacen1")
    almacen.grabar_almacen()

    condicion_pago = CondicionPago("CP001", "Contado")
    condicion_pago.grabar_condicion_pago()

    venta = Venta.registrar_venta("V001", cliente, 5.0, almacen, condicion_pago)
    assert len(Venta.listar_ventas()) == 1
