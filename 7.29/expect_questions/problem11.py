# problem11.py
# ---
# 정수 `n`을 입력받아 소수 여부를 판별하는 `is_primes` 함수를 완성하시오.
# 소수란 1과 자기 자신으로만 나누어지는 2 이상의 정수를 의미한다.
# n이 2 미만이거나 정수가 아닐 경우 False를 반환하시오.
# ---

# 입력받기 위한 input 함수는 절대 사용하지 않습니다.
def is_primes(n):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    if type(n) != int or n < 2:
        return False
    else:
        lst = []
        for i in range(1, n+1):
            if n % i == 0:
                lst.append(i)
        if len(lst) == 2:
            return True
        else:
            return False
    
###################################################################################
# 테스트 코드
print(is_primes(2))   # True
print(is_primes(11))  # True
print(is_primes(15))  # False
print(is_primes(1))   # False
print(is_primes("7")) # False

