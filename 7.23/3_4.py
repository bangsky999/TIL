# 기본 제공값
'''
def increase_user():
    pass

def create_user(name, age, address):
    pass

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']
'''
# 모든 유저를 등록하고, 반환 된 정보를 하나의 리스트에 담아 출력하도록 map함수 사용
# 아마 result = list(map(함수, 반복 가능한 것1, ...))
def increase_user():
    pass

def create_user(name, age, address):
    user_info = zip(name, age, address)
    total_list = list(map(lambda x: {'name': x[0], 'age': x[1], 'address': x[2]}, user_info))
    print(total_list)
    

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

for i in name:
    print(f'{i}님 환영합니다 !')
create_user(name, age, address)
