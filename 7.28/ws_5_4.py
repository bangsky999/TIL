# 아래 함수를 수정하시오.
# title로 대문자 만들기

def capitalize_words(word):
    # 공백 기준 분리
    spl1 = word.split(' ')
    resu = []
    for i in spl1:
        res=i[0]
        res1 = res.upper()
        res2 = res1+i[1:] 
        resu.append(res2)
    return resu


result = capitalize_words("hello, world!")
print(' '.join(result))
