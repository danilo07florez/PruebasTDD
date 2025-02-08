Feature: procesar pago

Scenario: 1. Pago con tarjeta de credito
Given el usuario ha agregado productos al carrito
And el usuario esta en la pagina de pago
When el usuario ingresa los datos de su tarjeta de credito
And el usuario hace clic en "Pagar"
Then  mostrar un mensaje de confirmacion

Scenario: 2. Resumen del pedido
Given el usuario ha agregado productos al carrito
And el usuario esta en la pagina de pago
When el usuario revisa el resumen del pedido
Then el sistema debe mostrar todos los productos, precios y el total a pagar


Scenario: 3. Error de pago
Given el usuario ha agregado productos al carrito
And el usuario esta en la pagina de pago
When el usuario ingresa datos de pago incorrectos
Then el sistema debe mostrar de error indicando que el pago no se pudo procesar