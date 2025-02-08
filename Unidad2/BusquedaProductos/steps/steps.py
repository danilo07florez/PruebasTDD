from behave import given, when, then

productos = [
    {"nombre": "Laptop", "categoria": "Electrónica"},
    {"nombre": "Silla", "categoria": "Muebles"},
    {"nombre": "Smartphone", "categoria": "Electrónica"},
    {"nombre": "Mesa", "categoria": "Muebles"},
]

resultados_busqueda = []

@given('el usuario esta en la pagina principal')
def step_usuario_en_pagina_principal(context):
    context.en_pagina_principal = True
    print("El usuario está en la página principal.")

@when('el usuario ingresa el nombre de un producto')
def step_busqueda_por_nombre(context):
    termino_busqueda = "Laptop"  # Simulación de entrada del usuario
    context.resultados = [p for p in productos if termino_busqueda.lower() in p["nombre"].lower()]


@when('el usuario hace clic en "Buscar"')
def step_usuario_clic_buscar(context):
    if hasattr(context, "categoria_seleccionada"):
        context.resultados = [p for p in productos if p["categoria"] == context.categoria_seleccionada]

@then('mostrar los productos que coinciden con el nombre ingresado')
def step_mostrar_resultados(context):
    if not context.resultados:
        print("No se encontraron resultados para la búsqueda.")
    else:
        print("Productos encontrados:")
        for producto in context.resultados:
            print(f"- {producto['nombre']} ({producto['categoria']})")

###-- escenario 2--
@when('el usuario selecciona una categoria en la barra de busqueda')
def step_busqueda_por_categoria(context):
    context.categoria_seleccionada = "Muebles"

###-- escenario 3--
@when('el usuario ingresa un termino de busqueda que no coincide con ningun producto')
def step_busqueda_sin_resultados(context):
    termino_busqueda = "Televisor"
    context.resultados = [p for p in productos if termino_busqueda.lower() in p["nombre"].lower()]