# Libreria que se utiliza para el envio de datos por medio de JSON
import json
# Libreria que permite realizar HTTP requests
import requests

# Prueba de estatus del request al bus del cliente http://localhost:56949/api/buscliente/
urlSolicitarPedido = "http://localhost:56949/api/buscliente/"

# URL para agregar un pedido
urlEnviarPedido = urlSolicitarPedido + "agregar"

headers = {
    'content-type': 'application/json'
}
# Variable data que contiene la informacion necesaria para colocar un pedido en el servidor del restaurante
data = {
    "id": 10,
    "descripcion": "Pedido 10",
    "idrestaurante": 10,
    "idrepartidor": 10,
    "idcliente": 11,
    "estado": 10
}

# Realiza un POST al esb para agregar un pedido en el servidor del restaurante
def responseAdd(header, data, url):
    return requests.post(url,data=json.dumps(data), headers=header)

# Verifica el status del request, que sea 201, en este caso es equivalente a la creacion de un nuevo elemento en el servidor
def test_Add():
    assert responseAdd(headers,data,urlEnviarPedido).status_code==201