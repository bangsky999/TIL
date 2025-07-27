'''
matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]
'''
matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]

# 아래에 코드를 작성하세요
# matrix_len = 0
# for i in matrix:
#     matrix_len += 1
# print(matrix_len)


# for number in matrix:
#     temporary_len = 0
#     for j in number:
#         temporary_len += 1
#     print(number, f'리스트는 {temporary_len}개 만큼 요소를 가지고 있습니다.')

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        print(f'matrix의 {matrix[x][y]} 번째 요소의 값은 {x}, {y}입니다.')
        