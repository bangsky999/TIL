# 아래에 코드를 작성하시오.
class Myth:
    type_of_myth = 0

    def __init__(self, name):
        self.type_of_myth = 123132
        self.name = name
        Myth.type_of_myth += 1 # 같은 클래스 내에서 클래스 변수에 접근할때, self.안쓰고 Myth.하는 이유? - 1
                               # 클래스 변수 접근시는 클래스.밖에 안됨

    # def some_method(self):
    #     self.type_of_myth 클래스 변수와 메서드 안에서 self.변수는 다름

    @staticmethod
    def description():
        print(f'현재까지 생성된 신화의 수 : {Myth.type_of_myth}')
        print('신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.')

myth1 = Myth('dangun')
myth2 = Myth('greek & rome')

print(myth1.name)
print(myth2.name)

Myth.description()


# 클래스 != 인스턴스(self) ->
# self : 인스턴스가 자기 자신을 가리키는 참조변수