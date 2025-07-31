# 아래 클래스를 수정하시오.
class StringRepeater:
    def __init__(self):
        pass

    def repeat_string(self, repeat_num, string):
        for _ in range(repeat_num):
            print(string)

# 인스턴스 생성 시 초기화할 값이 없으므로 __init__에는 매개변수가 없음
repeater1 = StringRepeater()
# 메서드 호출시 필요한 값(repeat_num, string)을 전달
repeater1.repeat_string(3, "Hello")
