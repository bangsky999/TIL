# 정수와 연산자만을 사용
print(3 * 2)    # 3의 2배의 값
print(3 ** 2)   # 3의 제곱 값
print((3 ** 2) // (3 * 2), (3 ** 2) % (3 * 2))  # 3의 제곱 값을 3의 2배의 값으로 나눈 몫과 나머지
print((3 ** 2) + ((-3) ** 2))   # 3의 제곱 값에 -3의 제곱 값을 더한 값

# 변수 사용
value_a = 3 * 2
value_b = 3 ** 2
value_c = (-3) ** 2

print(value_a)    # 3의 2배의 값
print(value_b)   # 3의 제곱 값
print(value_b // value_a, value_b % value_a)  # 3의 제곱 값을 3의 2배의 값으로 나눈 몫과 나머지
print(value_b + value_c)   # 3의 제곱 값에 -3의 제곱 값을 더한 값