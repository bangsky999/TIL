data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.
result = []
for i in data_1:
    # 대문자거나 공백인지 확인
    if i.isupper() is True or i == ' ':
        result.append(i)
print(''.join(result))


data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []

# 아래에 코드를 작성하시오.
a = data_2.find('내')
b = data_2.find('힘')
c = data_2.find('들')
d = data_2.find('다')
arr.append(a)
arr.append(b)
arr.append(c)
arr.append(d)
print(arr)
brr = arr.sort()
print(arr)

prr = data_2[arr[0]], data_2[arr[1]], data_2[arr[2]], data_2[arr[3]]
print(''.join(prr))
