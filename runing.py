import requests

response = requests.post('http://127.0.0.1:5000/coordinates', json={'x': 4, 'y': 3})
print(response.json())

