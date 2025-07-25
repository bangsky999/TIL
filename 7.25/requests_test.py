import requests
import pprint
url = "https://fakestoreapi.com/carts"
data = requests.get(url).json() # 조회 요청 # json()은 내부 데이터를 딕셔너리 형태로 ㅂ ㅕㄴ환
pprint.pprint(data) # 200: 정상 , 404: 그런 데이터는 우리 서버에 없다

