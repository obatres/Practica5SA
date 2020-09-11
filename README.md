# Practica5SA.
# Practicas de Software Avanzado


> REServ es un crowdsourcing el cual tiene como objetivo prestar el servicio de delivery a varios restaurantes, dicha aplicacion consta de 3 partes:

## Servidor REST API
### Restaurante
> El cual esta desarrollado en C# y almacena los datos momentaneamente en una estructura de datos

## Cliente REST 
### Cliente
> El api que presta los servicios al cliente esta desarrollado en Pyhton y consume de los servicios que provee el servidor restaurante.

### Repartidor
> El api que presta los servicios a los repartidores esta desarrollado en Python y consumer de los servicios que provee el servidor del restaurante. 


>En conjunto, las tres partes son capaces de manejar pedidos con estado, dandole al cliente un tracker para que sepa el estado de su pedido en cualquier momento despues de realizar su orden. 

## Video de demostracion del funcionamiento
> https://youtu.be/4b3pe2dHBow

## CI
> La integracion continua esta a cargo de Travis CI https://travis-ci.com el cual es un gestor de integracion continua en la nube. La configuracion de esta integracion se puede ver en el archivo llamado .travis.yml para mayor informacion. 

## Historial de versiones
* 0.1
  * CAMBIO: Se integra la funcion abstracta de un cliente. 
* 0.2
  * CAMBIO: Se integra la funcion abstracta de un repartidor 
* 0.2.1
  * CAMBIO: Correcciones en el archivo de confuguracion de Travis CI
* 0.2.2
  * CAMBIO: Correcciones en el archivo de configuracion de Travis CI
  *         Agregados los requerimientos del API
* 0.2.3
  * CAMBIO: Correcciones en el archivo de configuracion de Travis CI
  *         Agregadas las pruebas unitarias del API
* 1.2.3
  * CAMBIO: Libreria Pytest agregada
