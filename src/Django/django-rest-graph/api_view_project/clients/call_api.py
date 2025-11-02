import requests

url = 'http://localhost:8000/api/item/'

response = requests.get(url)
print('--- GET Method ---')
print(response.text)

response = requests.post(url)
print('--- POST Method ---')
print(response.text)

response = requests.delete(url)
print('--- DELETE Method ---')
print(response.status_code)
print(response.text)
