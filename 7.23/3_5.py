number_of_people = 0


def increase_user():
    pass


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user():
    pass


many_user = []
for i in range(len(name)):
    user = create_user(name[i], age[i], address[i])
    user_info.append(user)


def rental_book(info):
    
    return info[name], info[age]


def decrease_book(number):
    result = number_of_book - number
    print(f"남은 책의 수 : {result}")