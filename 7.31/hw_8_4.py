# 아래 클래스를 수정하시오.
class UserInfo:
    user_dict = {}
    def __init__(self): 
        self.value = False
    # "self.변수 = 변수"가 필수적이다 => 생성자 메서드에서 생성

    # "self.변수 = 변수"가 추가적으로 필요하더라 => 메서드에서 사용할 수도 있음
    def get_user_info(self):
        try: # 에러가 나는 코드를 발생시킨다.
            self.name = input('이름을 입력하세요 : ')
            self.age = int(input('나이을 입력하세요 : '))
        
        except ValueError: # 입력값 에러 발생시
            print('나이는 숫자로 입력해야 합니다.')
            self.value = False
        else:
            UserInfo.user_dict[self.name] = self.age
            self.value = True

            if self.name == "":
                self.value = False

    def display_user_info(self):
        if self.value == True: 
            print(f'이름 : {self.name}')
            print(f'나이 : {self.age}')

        else:
            print('사용자 정보가 입력되지 않았습니다.')

user = UserInfo()

user.get_user_info()
user.display_user_info()
print(user.name)