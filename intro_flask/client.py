import requests

url = 'http://localhost:5000/'

response = requests.get(url)

if response.status_code == 200:
    print("Respuesta del servidor:")
    print(response.text)
else:
    print("Error al conectar con el servidor:", response.status_code)

params = {'nombre': 'Jonathan'}
response = requests.get(url+'saludar', params=params)

if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)

sumar = {'numero1': 4, 'numero2': 6}
response = requests.post(url + 'sumar', json=sumar)
if response.code == 200:
    datas = response.json()
    resultado = datas['resultado']
    print("Resultado de la suma:", resultado)
else:
    print("Error al conectar con el servidor (Sumar):", response.code)


