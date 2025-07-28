'''
# 아래 함수를 수정하시오.
def even_elements():
    pass


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
'''

## 목표: 홀수는 제거, 짝수만 가져오겠다.
'''
for문과 pop은 같이 안쓰는게 좋다. pop을 하는 순간 리스트가 변경됨 => 기존 반복이 꼬임

while (리스트):
    pop 
이런식이면 리스트가 비워질떄까지 반복
'''
def even_elements_2(nums):



    res = []
    # nums pop이 다할때까지 true를 반환
    while nums:
        el = nums.pop(0)

        if el % 2 == 0:
            # extend를 하나 요소만 넣으려면 iterable을 넣어야하는데 list나 tuple
            res.extend([el])
    
    return res
