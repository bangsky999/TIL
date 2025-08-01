'''
<문제>
- 크기가 N인 2차원 정사각 행렬이 주어졌을 때, 가장 큰 값을 가지는 행, 열 좌표를
반환하는 find_max_position 함수를 완성하시오.

- 행렬의 크기 N은 2이상 10이하이다.
- 가장 큰 값이 여러 개 있을 경우 행의 인덱스가 가장 작은 좌표를 리스트로 반환한다.
- 가장 큰 값이 여러개가 같은 행에 위치한 경우에는 열의 인덱스가 가장 작은 좌표를 리스트로 반환한다.
'''


def find_max_position(matrix):
    # 초기 max_num, max_c, max_r 값 설정
    max_num = 0
    max_c = 0
    max_r = 0
    # matrix의 길이 3만큼 range설정
    for r in range(len(matrix)):
        # matrix[0]의 길이 3만큼 range설정
        for c in range(len(matrix[0])):
            # matrix의 좌표값이 max_num보다 크면 재설정
            if matrix[c][r] > max_num:
                # 값 저장하기
                max_num = matrix[c][r]
                max_c = c
                max_r = r

    return max_r, max_c


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

# 예시 행렬 데이터
matrix1 = [[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]]

matrix2 = [[9, 2, 3], 
           [4, 5, 6], 
           [7, 8, 1]]

matrix3 = [[9, 2, 5], 
           [4, 9, 6], 
           [7, 8, 1]]
#####################################################
# 아래 코드를 삭제하는 경우
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(find_max_position(matrix1))  # [2, 2]
print(find_max_position(matrix2))  # [0, 0]
print(find_max_position(matrix3))  # [0, 0]
#####################################################

# matrix4 = [[1, 10, 5, 10],
#            [10, 5, 7, 9],
#            [1, 5, 8, 4], 
#            [10, 2, 5, 2]]
# print(find_max_position(matrix4))
