import requests


url ='http://localhost:8000/api/'
response = requests.get(url)

print(f"status_code={response.status_code}")
print(f"response_headers={response.headers}")
print(f"body={response.text}")
