import requests

url = 'http://127.0.0.1:8000/api/item/'

response = requests.get(url)
print(response.text)

response = requests.post(url)
print(response.text)

response = requests.delete(url)
print(response.status_code)
print(response.text)