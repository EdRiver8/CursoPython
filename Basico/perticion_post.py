import requests

#simular que se envian datos a un restaurante =>
url ="https://webhook.site/3becc972-a41e-4218-b299-7c213c374c87"
payload = {"plato":"pasta", "cantidad":2}
query_params = {"nombre":"Ed"}
response = requests.post(url, data=payload, params=query_params)
print(response.status_code)
print(response.text)# respuesta vacia