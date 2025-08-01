'''
<문제>
- 주어진 문자열을 뒤집는 재귀 함수를 완성하시오. 
- 함수 reverse_string은 문자열을 인자로 받아, 그 문자열을 뒤집은 결과를 반환한다.
'''


'''
    ("hello")

    o ("hell")

    o (l ("hel"))

    o (l (l ("he")))

    o (l (l (e ("h"))))

    'olleh'
'''

def reverse_string(s):
    if len(s) == 1:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])
    





############## 테스트 코드 삭제 금지 #################
print(reverse_string("hello"))  # 'olleh'
print(reverse_string("world"))  # 'dlrow'
print(reverse_string("python"))  # 'nohtyp'
#####################################################
