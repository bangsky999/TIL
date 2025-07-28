# 아래 함수를 수정하시오.
def find_min_max(lst):
    min_vel = lst[0]
    max_vel = lst[0]
    for i in lst:
        if i > max_vel:
            max_vel = i
        elif i < min_vel:
            min_vel = i

    return min_vel, max_vel


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
