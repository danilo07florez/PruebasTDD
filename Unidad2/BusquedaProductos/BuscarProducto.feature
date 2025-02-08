Feature: Busqueda de Productos

Scenario: 1. busqueda por nombre
Given el usuario esta en la pagina principal
When el usuario ingresa el nombre de un producto
Then mostrar los productos que coinciden con el nombre ingresado


Scenario: 2. Busqueda por categoria
Given el usuario esta en la pagina principal
When el usuario selecciona una categoria en la barra de busqueda
And el usuario hace clic en "Buscar"
Then mostrar los productos que coinciden con el nombre ingresado

Scenario: 3. Sin resultados
Given el usuario esta en la pagina principal
When el usuario ingresa un termino de busqueda que no coincide con ningun producto
And el usuario hace clic en "Buscar"
Then mostrar los productos que coinciden con el nombre ingresado