# 아래 함수를 수정하시오.
def remove_duplicates(nums):
    new_lst = []
    # set으로 중복 제거
    aaa = list(set(nums))
    new_lst.append(aaa)
    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result[0])
