# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, Width, Height):
        self.Width = Width
        self.Height = Height

    # area구하는 메서드 만들기
    def Area(self):
        return self.Width * self.Height
    
    def Perimeter(self):
        return 2 * (self.Width + self.Height)

    # 같은 클래스 안에 있으므로 self.Area(), self.Perimeter()로 메서드 호출 가능
    def print_info(self):
        print(f'Width: {self.Width}')
        print(f'Height: {self.Height}')
        print(f'Area: {self.Area()}')
        print(f'Perimeter: {self.Perimeter()}')


shape1 = Shape(5, 3)
shape1.print_info()
