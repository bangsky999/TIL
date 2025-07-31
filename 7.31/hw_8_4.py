# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}

    def get_user_info(self):
        name = str(input('이름을 입력하세요 : '))
        age_input = input('나이를 입력하세요 : ')
        if not name or not age_input:
            print('사용자 정보가 입력되지 않았습니다.')
        
        try:
            age = int(age_input)
            self.user_data = {'name': name, 'age': age}

        except ValueError:
            print('나이는 숫자로 입력해야 합니다.')


    def display_user_info(self):
        if self.user_data:
            print('사용자 정보')
            print(f'이름: {self.user_data["name"]}')
            print(f'나이: {self.user_data["age"]}')
        else:
            print('사용자 정보가 입력되지 않았습니다.')

user = UserInfo()
user.get_user_info()
user.display_user_info()
