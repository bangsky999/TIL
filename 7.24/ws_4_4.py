import requests
from pprint import pprint as print

dummy_data = []
for i in range(1, 11):
    user_info = {}
    API_URL = f'https://jsonplaceholder.typicode.com/users/{i}'
    response = requests.get(API_URL).json()
    if (
        -80 < float(response['address']['geo']['lat']) < 80
        and -80 < float(response['address']['geo']['lng']) < 80
    ):
        user_info = {
            'name': response['name'],
            'lat': response['address']['geo']['lat'],
            'lng': response['address']['geo']['lng'],
            'company': response['company']['name'],
        }
        dummy_data.append(user_info)

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

# 사용자 리스트를 받아서 회사별로 정리할 함수 정의
def create_user(dummy_data): 
    # 결과를 저장할 딕셔너리 생성(회사이름: [사용자 이름 리스트])
    censored_user_list = {}
    # dummy_data 안에 있는 각 사용자 정보 하나씩 반복
    for data in dummy_data:
        # censorship함수로 블랙리스트 회사 검사 -> True면 넘어감
        if censorship(data):
            # 만약 해당 회사 이름이 있으면 
            if censored_user_list.get(data['company']):
                # 리스트에 데이터 추가 
                censored_user_list.get(data['company']).append(data['name'])
            else:
                # 그 회사 이름으로 리스트 만들어서 넣기
                censored_user_list[data['company']] = data['name']
    return censored_user_list

# 사용자 한명의 데이터를 받아 블랙리스트 회사인지 확인하는 함수
def censorship(data):
    # 블랙리스트에 있다면
    if data['company'] in black_list:
        # 등록불가 & false 반환
        print(f'{data["company"]} 소속의 {data['name']} 은/는 등록할 수 없습니다.')
        return False
    else:
        # 등록 가능 메시지 & true 반환
        print('이상 없습니다.')
        return True
