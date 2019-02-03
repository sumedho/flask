import json
import requests


data = {'name':'john', 'age':20}

# POST request to server
response = requests.post('http://localhost:1000/data', json=data)

print(response.content)