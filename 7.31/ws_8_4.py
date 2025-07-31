class Animal:
    num_of_animal = 0 # 클래스 변수(속성)


class Dog(Animal):
    def bark(self):
        print('멍멍 !')

class Cat(Animal):
    def meow(self):
        print('야옹 !')

# 아래 클래스를 수정하시오.
class Pet(Dog, Cat):
    def __init__(self, sound):
        self.sound = sound # 인스턴스 변수
        '''
        상속시 super안쓰는 이유
        1. 현재 animal의 생성자 메서드가 없고 초기화가 불필요
        2. 만약 animal에 생성자가 있고, 동물 세는 기능 필요하면 super사용
        '''
    def make_sound(self):
        print('그르르')

    def play(self):
        print('애완동물과 놀기')


pet1 = Pet("그르르") # 인스턴스 변수가 있다?? -> 생성자 변수가 있다.
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()
