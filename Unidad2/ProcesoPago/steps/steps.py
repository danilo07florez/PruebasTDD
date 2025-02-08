from behave import given, when, then

carrito = [
    {"producto": "Laptop", "precio": 1000},
    {"producto": "Mouse", "precio": 50}
]


@given('el usuario ha agregado productos al carrito')
def step_agrega_productos(context):
    context.carrito = [{"producto": "Laptop", "precio": 1000}]
    print(f"Productos en el carrito: {len(context.carrito)} artículos.")
  

@given('el usuario esta en la pagina de pago')
def step_usuario_pagina_pago(context):
    context.en_pagina_pago = True
    print("El usuario está en la pagina de pago.")

@when('el usuario ingresa los datos de su tarjeta de credito')
def step_usuario_ingresa_tarjeta(context):
    context.datos_tarjeta = {"numero": "4111111111111111", "cvv": "123", "expira": "12/25"}
    context.pago_exitoso = context.datos_tarjeta["numero"].startswith("4")

@when('el usuario hace clic en "Pagar"')
def step_usuario_clic_pagar(context):
    if not context.pago_exitoso:
        context.error_pago = True

@then('mostrar un mensaje de confirmacion')
def step_mensaje_confirmacion(context):
    if context.pago_exitoso:
        print("Pago procesado con éxito. ¡Gracias por tu compra!")
    else:
        print("Hubo un error en el procesamiento del pago.")


###--escenario 2---
@when('el usuario revisa el resumen del pedido')
def step_usuario_revisa_resumen(context):
    context.resumen_pedido = context.carrito
    context.total_pagar = sum(item["precio"] for item in context.resumen_pedido)

@then('el sistema debe mostrar todos los productos, precios y el total a pagar')
def step_mostrar_resumen(context):
    print("Resumen del pedido:")
    for item in context.resumen_pedido:
        print(f"- {item['producto']}: ${item['precio']}")
    print(f"Total a pagar: ${context.total_pagar}")


###--escenario 3---
@when('el usuario ingresa datos de pago incorrectos')
def step_usuario_datos_incorrectos(context):
    context.datos_tarjeta = {"numero": "0000000000000000", "cvv": "999", "expira": "01/20"}
    context.pago_exitoso = False
    context.error_pago = True

@then('el sistema debe mostrar de error indicando que el pago no se pudo procesar')
def step_mostrar_error_pago(context):
    if context.error_pago:
        print("Error: No se pudo procesar el pago. Por favor, verifica los datos de la tarjeta.")