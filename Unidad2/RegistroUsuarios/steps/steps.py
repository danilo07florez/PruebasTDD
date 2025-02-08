import re
from behave import given, when, then

usuarios_registrados = ["danilo.florez@autonoma.edu.co", "jeraldine.cordoba@autonoma.edu.co", "luis.trejos@autonoma.edu.co", "policarpo.galindo@autonoma.edu.co", "jhon.echeverri@autonoma.edu.co"]  # Base de datos simulada

@given('el usuario esta en la pagina de registro')
def step_impl(context):
    context.en_pagina_registro = True
    print("Usuario accedió a la página de registro.")



@when('el usuario ingresa un correo electronico valido y una contrasena')
def step_ingresa_datos_validos(context):
    context.correo = "nuevo_usuario@example.com"
    context.contrasena = "admin123"
    context.registro_exitoso = context.correo not in usuarios_registrados ##validacion

@then('mensaje de registro Exitoso')
def step_mensaje_registro_exitoso(context):
    if context.registro_exitoso:
        print("Se registro el nuevo usuario exitosamente.")
    else:
        print("El correo ya está registrado.")


###--escenario 2---
@when('el usuario ingresa un correo electronico ya registrado')
def step_impl(context):
    context.correo = "danilo.florez@autonoma.edu.co"
    context.registro_exitoso = context.correo not in usuarios_registrados


###--escenario 3---
@when('el usuario ingresa un correo electronico invalido')
def step_usuario_ingresa_correo_invalido(context):
    context.correo = "correo-invalido"
    # Validación de correo simple usando regex
    patron_correo = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    context.correo_valido = re.match(patron_correo, context.correo) is not None


@then('mensaje de correo invalido')
def step_mensaje_correo_invalido(context):
    if not context.correo_valido:
        print("El correo ingresado es inválido.")
    else:
        print("El correo ingresado es válido.")

