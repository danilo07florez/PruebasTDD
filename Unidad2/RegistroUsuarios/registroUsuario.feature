Feature: registrar usuario

Scenario: 1. Creacion usuario nuevo
Given el usuario esta en la pagina de registro
When el usuario ingresa un correo electronico valido y una contrasena
Then  mensaje de registro Exitoso


Scenario: 2. Correo ya registrado
Given el usuario esta en la pagina de registro
When el usuario ingresa un correo electronico ya registrado
Then  mensaje de registro Exitoso

Scenario: 3. Correo invalido
Given el usuario esta en la pagina de registro
When el usuario ingresa un correo electronico invalido
Then  mensaje de correo invalido

 