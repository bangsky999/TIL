# 아래 함수를 수정하시오.
def reverse_string(words):
    # reversed함수에 list를 해주는 이유 !
    # 반복자를 돌려주기 때문에 list 필요 !
    return list(reversed(words))


result = ''.join(reverse_string("Hello, World!"))
print(result)  # !dlroW ,olleH
