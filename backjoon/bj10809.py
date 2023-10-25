# 알파벳 찾기
# 브론즈 II
# 소문자로만 이루어진 단어 S 주어짐
# 단어가 처음 등장하는 위치(인덱스값) 출력

S = input()
alphabet = 'abcdefghijklnmopqrstuvwxyz'

idx = 0
for i in alphabet:
    if i in S:
        print(S.index(i), end=' ')
    else:
        print(-1, end=' ')