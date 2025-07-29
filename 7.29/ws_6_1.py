# 아래 함수를 수정하시오.
def union_sets(set1, set2):
    res = set1.union(set2) 
    return res
def union_multiple_sets(*sets): # * 기호는 파라미터 앞에만 붙는다.
    # 함수 안에서 사용할 때는 * 없이 사용.
    # * 없이 사용해도 여러개의 값이 튜플로 들어가 있음.
    # print(list(sets))
    if len(sets) < 2:
        print('최소 두 개의 셋이 필요합니다.')
    else:
        set3 = set()
        for i in sets:
            set3 = set3.union(i) # union한 결과를 가지고 다시 set3를 업데이트
        return set3

result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)  # {1, 2, 3, 4, 5}

result = union_multiple_sets({1, 2}, {3, 4}, {5, 6})
print(result)  # {1, 2, 3, 4, 5, 6}

result = union_multiple_sets({1, 2})
if result: # result None => False
    print(result)
# 출력 : 최소 두 개의 셋이 필요합니다
