# problem14.py
# ---
# 정수 `n`을 입력받아 각 자릿수를 모두 더한 값을 반환하는 `sum_of_digits` 함수를 완성하시오.
# 단, 이번에는 재귀를 한 번만 사용하여 각 자릿수를 더하시오.
# 예) 987 → 9+8+7 = 24
# ---

def sum_of_digits(n):
    # 재귀 종료 조건
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n//10)

###################################################################################
print(sum_of_digits(987))   # 24
print(sum_of_digits(1234))  # 10
print(sum_of_digits(9))     # 9
print(sum_of_digits(99))    # 18
print(sum_of_digits(0))     # 0
