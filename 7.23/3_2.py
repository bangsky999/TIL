number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1

def create_user():
    
    increase_user()
    user_info = {}
    user_info['name'] = '홍길동'
    user_info['age'] = 30
    user_info['address'] = '서울'
    print(f"{user_info['name']}님 환영합니다!")
    return user_info

    
    

print(number_of_people)
result = create_user()
print(result)
print(number_of_people)