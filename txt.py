matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]

for x in matrix:
    for y in x:
        print(y)

for x in range(len(matrix)):
    for y in x:
        print(y)




# print(f'matrix의 {x}, {y} 번쨰 요소의 값은 {matrix[x][y]} 입니다.')