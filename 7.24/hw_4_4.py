
list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_list = [
    '장생전',
    '위대한 개츠비',
    '원생몽유록',
    '이생규장전',
    '데미안',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]

missing_book = []

for each_book in rental_list:
    if each_book not in list_of_book:
        missing_book.append(each_book)
if missing_book:
    for i in missing_book:
        print(f'{i} 을/를 보충하여야 합니다.')

        
else: # for문을 수행하는 동안 break문을 만나지 않았다면
    print('모든 도서가 대여 가능한 상태입니다.')

### 리스트 컴프리헨션 잘 모르겠음 ###
# if missing_book: => missing book에 값이 하나라도 있으면 True라는 뜻