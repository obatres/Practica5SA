# Libreria que se utiliza para el envio de datos por medio de JSON
import json
# Libreria que permite realizar HTTP requests
import requests
# Libreria que obtiene el dia y la hora 
from datetime import datetime

# URL para solicitar pedido
urlSolicitarPedido = "http://localhost:56949/api/buscliente/"
# Id del cliente que solicita pedido
idCliente = "11"
# Request que solicita el pedido al servidor del restaurante
response = requests.get(urlSolicitarPedido)

print(response.status_code)