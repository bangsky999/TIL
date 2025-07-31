# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0 # 클래스 변수(속성)

    def __init__(self):
        Animal.num_of_animal += 1

class Dog(Animal):
    # 아래 클래스를 수정하시오.
    def bark(self):
        print('멍멍!')
        return Animal.num_of_animal

# 아래 클래스를 수정하시오.
class Cat:
    def meow(self):
        print('야옹!')


cat1 = Cat()
cat1.meow()
