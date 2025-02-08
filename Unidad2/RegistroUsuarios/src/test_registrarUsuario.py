import unittest

class TestRegistroUsuario(unittest.TestCase):

    def setUp(self):
        # Simulación de base de datos simple
        self.usuarios_registrados = ["usuario1@gmail.com", "test@example.com"]

    def registrar_usuario(self, email, password):
        # Simulación de la lógica de registro
        if not self.es_correo_valido(email):
            return "Correo inválido"
        if email in self.usuarios_registrados:
            return "Correo ya registrado"
        self.usuarios_registrados.append(email)
        return "Registro exitoso"

    def es_correo_valido(self, email):
        # Validación básica para el formato del correo
        return "@" in email and "." in email

    def test_creacion_usuario_nuevo(self):
        """Scenario: Creación de usuario nuevo"""
        resultado = self.registrar_usuario("nuevo_usuario@gmail.com", "password123")
        self.assertEqual(resultado, "Registro exitoso")

    def test_correo_ya_registrado(self):
        """Scenario: Correo ya registrado"""
        resultado = self.registrar_usuario("usuario123@gmail.com", "password123")
        self.assertEqual(resultado, "Correo ya registrado")

    def test_correo_invalido(self):
        """Scenario: Correo inválido"""
        resultado = self.registrar_usuario("correo_invalido", "password123")
        self.assertEqual(resultado, "Correo inválido")

if __name__ == "__main__":
    unittest.main()