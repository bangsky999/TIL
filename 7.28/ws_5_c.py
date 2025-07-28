original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []

def restructure_word(word, arr):
    for i in word:
        if i.isdecimal() == True:
            for _ in range(int(i)):
                arr.pop()
        else:
            arr.remove(i)
    return arr



### 왜 이게 하나씩 나눠져서 들어가지..?

## 리스트.append(한원소) : 하나의 원소로서 집어넣음
## 리스트.extend(리스트) : 리스트의 원소들을 하나씩 집어넣음.

arr.extend(original_word)
print(arr)

result = restructure_word(word, arr)
print(result)
print(''.join(result))
