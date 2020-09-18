# Libreria que se utiliza para el envio de datos por medio de JSON
import json
# Libreria que permite realizar HTTP requests
import requests

# Prueba de estatus del request al bus del cliente http://localhost:56949/api/buscliente/
urlSolicitarPedido = "http://localhost:56949/api/buscliente/"

# Realiza un request a la URL
def Response(url):
    return requests.get(url)

#Verifica que el estado del request sea 200, que es equivalente a un request valido
def test_statusResponse():
    assert Response(urlSolicitarPedido).status_code == 200

