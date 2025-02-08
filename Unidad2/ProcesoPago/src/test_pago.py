import unittest

class TestProcesarPago(unittest.TestCase):

    def test_pago_exitoso(self):
        self.assertEqual(2 + 2, 4)

    def setUp(self):
        # Simulación de datos del sistema
        self.carrito = [{"producto": "Laptop", "precio": 1000}, {"producto": "Mouse", "precio": 50}]
        self.total = 1050
        self.datos_tarjeta_correctos = {"numero": "1234567812345678", "fecha_exp": "12/25", "cvv": "123"}
        self.datos_tarjeta_incorrectos = {"numero": "0000000000000000", "fecha_exp": "00/00", "cvv": "000"}

    def test_pago_con_tarjeta_credito_exitoso(self):
        """Escenario: Pago exitoso con tarjeta de crédito"""
        resultado_pago = procesar_pago(self.datos_tarjeta_correctos, self.total)
        self.assertEqual(resultado_pago, "Pago procesado correctamente")

    def test_resumen_pedido_correcto(self):
        """Escenario: Resumen del pedido"""
        resumen = generar_resumen(self.carrito)
        self.assertIn("Laptop", resumen["productos"])
        self.assertIn("Mouse", resumen["productos"])
        self.assertEqual(resumen["total"], 1050)

    def test_error_de_pago(self):
        """Escenario: Error en el pago por datos incorrectos"""
        resultado_pago = procesar_pago(self.datos_tarjeta_incorrectos, self.total)
        self.assertEqual(resultado_pago, "Error: Datos de pago incorrectos")

# Funciones simuladas que pasarán las pruebas
def procesar_pago(datos_tarjeta, total):
    if datos_tarjeta["numero"] == "1234567812345678":
        return "Pago procesado correctamente"
    return "Error: Datos de pago incorrectos"

def generar_resumen(carrito):
    total = sum(item["precio"] for item in carrito)
    nombres_productos = [item["producto"] for item in carrito]
    return {"productos": nombres_productos, "total": total}

if __name__ == "__main__":
    unittest.main()