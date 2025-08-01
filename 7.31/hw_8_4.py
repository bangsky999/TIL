# 아래 클래스를 수정하시오.
class UserInfo:
    user_dict = {}
    def __init__(self): # 인스턴스 변수가 없는데 생성자에 변수 설정 how????????????
        # self.name = name
        # self.age = age
        self.value = False

    def get_user_info(self): # 여기는 생성자 변수 입력안해도되나??????????
        
        try: # 에러가 나는 코드를 발생시킨다.
            self.name = input('이름을 입력하세요 : ') # name, age 변수를 클래스 내에서 공유하려면 self.형식?????
            self.age = int(input('나이을 입력하세요 : ')) # self의 역할이 뭐지 그럼??????
        
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
# print(user.name)
user.get_user_info()
user.display_user_info()
print(user.name)