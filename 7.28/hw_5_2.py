# 아래 함수를 수정하시오.
def count_character(sent, word):
    cnt = 0
    for i in sent:
        if i == word:
            cnt += 1
    return cnt

result = count_character("Hello, World!", "o")
print(result)  # 2
