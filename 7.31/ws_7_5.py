# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # __str__ 매직 메서드를 정의하면 print()나 str()을 사용할 때 자동 호출됨
    # 인스턴스를 print()에 직접 전달하면 __str__이 실행되어 문자열을 반환
    def __str__(self):
        return f'Shape: width={self.width}, height={self.height}'


shape1 = Shape(5, 3)
print(shape1)