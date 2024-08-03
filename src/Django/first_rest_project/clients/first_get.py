import requests


url = 'http://localhost:8000/api/'
response = requests.get(url)

print(f"{response.text=}")
print(f"{response.headers=}")