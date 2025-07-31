class Animal:
    def move(self):
        print('동물')

class Bird(Animal):
    def move(self):
        super().move()
        print('새가')

b = Bird()
b.move()
    