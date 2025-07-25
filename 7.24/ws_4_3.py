
import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'

dummy_data = []
for i in range(1,11):
    API = API_URL + 'i'
    response = requests.get(API_URL)
    parsed_data = response.json()
    dict_id = {}
    name = parsed_data[i-1]['name']
    lat = parsed_data[i-1]['address']['geo']['lat']
    lng = parsed_data[i-1]['address']['geo']['lng']
    compamy_name = parsed_data[i-1]['company']['name']
    dict_id['company'] = compamy_name
    dict_id['lat'] = lat
    dict_id['lng'] = lng
    dict_id['name'] = name
    if float(lat) < 80 and float(lng) > -80:
        dummy_data.append(dict_id)
print(dummy_data)

    