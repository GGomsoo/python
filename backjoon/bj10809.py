# 알파벳 찾기
# 브론즈 II
# 소문자로만 이루어진 단어 S 주어짐
# 단어가 처음 등장하는 위치(인덱스값) 출력

S = input()
# 알파벳 a부터 z까지 깔아두고
# 알파벳 순서 틀려서 1회 틀림
alphabet = 'abcdefghijklmnopqrstuvwxyz'

idx = 0
# 알파벳에 대해서
for i in alphabet:
    # i가 S에 들어있으면
    if i in S:
        # 위치를 출력
        print(S.index(i), end=' ')
    # S에 없는 알파벳이면
    else:
        # -1 출력
        print(-1, end=' ')