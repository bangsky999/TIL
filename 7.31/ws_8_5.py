class Animal:
    num_of_animal = 0 # 클래스 변수(속성)


class Dog(Animal):
    sound = '멍멍' # 클래스 

class Cat(Animal):
    sound = '야옹'

class Pet(Dog, Cat):
    def __str__(self):
        super().__str__()
        return f'애완동물은 {self.sound} 소리를 냅니다.'

print(Pet.sound)