number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1

def create_user(name, age, address):
    print(f"{name}님 환영합니다!")
    return {'name': name, 'age': age, 'address': address}

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

user_info = []

create_user('김시습', 20, '서울')

create_user('허균', 16, '강릉')

create_user('남영로', 52, '조선')

create_user('임제', 36, '나주')

create_user('박지원', 60, '한성부')
for i in range(len(name)):
    # user = 
    user_info.append(create_user(name[i], age[i], address[i]))
print(user_info)


######map을 사용하는 방법을 모르겠음!!!!!!$$$$$$$$$$$$$$$$$$$$$#