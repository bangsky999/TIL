# problem12.py
# ---
# 문자열 `s`를 입력받아, 문자열 안에 포함된 모든 숫자를 찾아 합산한 값을 반환하는 `calc_sum_number` 함수를 완성하시오.
# 숫자가 하나도 없는 경우 0을 반환하시오.
# 예) "ab12c3" → 1 + 2 + 3 = 6
# ---

# 입력받기 위한 input 함수는 절대 사용하지 않습니다.
def calc_sum_number(s):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    sum = 0
    for i in s:
        if i.isdecimal():
            sum += int(i)
    return sum

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

###################################################################################
# 아래 코드를 삭제하는 경우 모든 책임은 삭제한 본인에게 있습니다.
# 테스트 코드 삭제 금지
print(calc_sum_number("ab12c3"))   # 6
print(calc_sum_number("hello"))    # 0
print(calc_sum_number("a1b2c3"))   # 6
print(calc_sum_number("12345"))    # 15
print(calc_sum_number(""))         # 0
