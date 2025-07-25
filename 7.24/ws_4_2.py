import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'

dummy_data = []
for i in range(1,11):
    API = API_URL + str(i)
    response = requests.get(API_URL)
    parsed_data = response.json()
    name = parsed_data[i-1]['name']
    dummy_data.append(name)
print(dummy_data)

    