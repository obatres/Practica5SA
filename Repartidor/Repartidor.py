# Libreria que se utiliza para el envio de datos por medio de JSON
import json
# Libreria que permite realizar HTTP requests
import requests
# Libreria que obtiene el dia y la hora
from datetime import datetime

# Archivo de Logs
Log = open("LogRepartidor.txt", "w")

# -----------------------------Solicitar pedido al restaurante---------------
# URL para solicitar pedido
urlSolicitarPedido = "http://localhost:56949/api/buscliente/"
# Id del cliente que solicita pedido
idCliente = "1"
# Request que solicita el pedido al servidor del restaurante
response = requests.get(urlSolicitarPedido+idCliente)
# Fecha y hora actual
now = datetime.now()
# Log del pedido solicitado
Log.write(str(now)+" "+"Pedido solicitado "+str(response.json())+" "+"\n")


# -----------------------------Solicitar estado del pedido al restaurante
# Id del pedido
pedido = response.json().get("id")
# Id del cliente que posee el pedido
cliente = response.json().get("idCliente")
# Estado del pedido del cliente
estado = response.json().get("estado")
# Log del estado del pedido solicitado
Log.write(str(now)+" el pedido "+str(pedido)+" del cliente " +
          str(cliente)+" se encuentra en el estado "+str(estado)+" "+"\n")

# ----------------------------Marcar como entregado-------------------------
# URL para solicitar pedido
urlSolicitarPedido = "http://localhost:56949/api/buscliente/"
# Id del cliente que solicita pedido
idCliente = "1"
# Request que solicita el pedido al servidor del restaurante
response = requests.get(urlSolicitarPedido+idCliente)
# Variable pedido que aloja el pedido que se va a modificar
pedido = response.json()
# Cambio de estado del pedido
pedido["estado"] = 0

# URL para actualizar un pedido en el  restaurante
urlEnviarPedido = urlSolicitarPedido + "actualizar"
# variable headers que inidican en que formato se esta enviando la informacion
headers = {
    'content-type': 'application/json'
}
# Variable data que contiene la informacion necesaria para colocar un pedido en el servidor del restaurante
data = pedido

# Variable responser que realizar la accion POST al servidor restaurante para colocar el pedido
response = requests.request("POST", urlEnviarPedido,
                            data=json.dumps(data), headers=headers)

print(response.status_code)
if response.status_code == 201:
    # Pedido creado correctamente
    Log.write(str(now)+'  pedido actualizado'+"\n")
else:
    # Pedido no se pudo crear
    Log.write(str(now)+" No se ha podido actualizar el  pedido\n")
# Cierra Archivo de Logs
Log.close()
