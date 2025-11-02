import requests

url ='http://localhost:8000/api/country_datetime/'

# response = requests.get(url, params={"timezone": 'US/Eastern'})
# response = requests.post(url, data={"timezone": 'US/Eastern'})
response = requests.post(url, data={"timezone": 'US/Easter'}) # timezone値が不正

print(f"status_code={response.status_code}")
print(f"response_text={response.text}")
print(f"response_headers={response.headers}")

# クライアント側の処理
if response.status_code == 400:
    print('実行失敗')