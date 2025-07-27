number_of_book = 100

def rental_book(name, number):
    decrease_book(number)
    print(f'{name}님이 {number}권의 책을 대여하였습니다.')

# 함수에서 전역변수를 사용하려면  global선언 or 변수 하나 더 만들어서 계산만 할 것
# 할당 변수 = a 를 할거면 global 선언
# 계산의 도구 result = 변수 - a 할거면 glbal 선언안해도 됨.
def decrease_book(number):
    global number_of_book
    number_of_book -= number
    print(f'남은 책의 수 : {number_of_book}')

rental_book('홍길동', 3)