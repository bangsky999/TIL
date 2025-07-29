# 아래 함수를 수정하시오.

def intersection_sets(s1, s2):
    res = s1 & s2
    res1 = len(res)
    
    if res: # if res가 있다면, True라면
        return res1, res
    else: # false라면
        print('공통 요소가 없습니다.')
        return res1, res
result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result)  # (1, {3})

result = intersection_sets({1, 2}, {3, 4})
print(result)  # (0, set())
# 출력: 공통 요소가 없습니다
