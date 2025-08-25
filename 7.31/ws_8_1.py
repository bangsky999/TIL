# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0


class Dog(Animal):
    def __init__(self):
        Animal.num_of_animal += 1


class Cat(Animal):
    def __init__(self):
        Animal.num_of_animal += 1


class Pet(Dog, Cat):
    @classmethod
    def access_num_of_animal(cls):
        # Animal.num_of_animal를 직접 써도 되지만,
        # cls를 사용하면 유연하게 동작 가능
        # 클래스 메서드에서 cls는 '클래스 자체'를 의미함.(클래스에만 접근)

        return f'동물의 수는 {cls.num_of_animal}마리 입니다.'


dog = Dog()
print(Pet.access_num_of_animal())
cat = Cat()
print(Pet.access_num_of_animal())
