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


# def increase_user():
#     pass

# def create_user(n, a, ad):
#     user_info = {'name': n, 'age': a, 'address': ad}
#     print(f'{n}님 환영합니다!')
#     return user_info

# name = ['김시습', '허균', '남영로', '임제', '박지원']
# age = [20, 16, 52, 36, 60]
# address = ['서울', '강릉', '조선', '나주', '한성부']

# many_user = list(map(create_user, name, age, address))
# print(many_user)


# # 문제 주어진 것
# name = ['김시습', '허균', '남영로', '임제', '박지원']
# age = [20, 16, 52, 36, 60]
# address = ['서울', '강릉', '조선', '나주', '한성부']

# def create_user(n, a, ad):
#     user_info = {'name': n, 'age': a, 'address': ad}
#     print(f'{n}님 환영합니다!')
#     return user_info
		
# many_user = []
# for n, a, ad in zip(name, age, address):
# 		result= create_user(n,a,ad)
# 		many_user.append(result)
                
# print(many_user)

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

many_user = list(map(lambda n, a, ad: 
                     {'name': n, 'age': a, 'address': ad}, name, age, address))
print(many_user)