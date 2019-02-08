import requests
import json

with open('data_test_predict2.json') as json_file:
    json_data = json.load(json_file)
print(json_data)
url = "http://127.0.0.1:8000/predict"
# url = "http://127.0.0.1:8080/predict"
response = requests.post(url, json=json_data)


# print(json_data)
print(f'{response.status_code} {response.text}')
