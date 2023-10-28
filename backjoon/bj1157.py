# 단어 공부
# 브론즈 I
# 입력받은 단어 중 가장 많이 사용된 알파벳 찾아내기

# 생각 실패

word = input().upper()

abc_cnt = [0] * 26
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

idx = 0
for i in word:
    if i in alphabet:
        idx = alphabet.index(i)
        abc_cnt[idx] += 1

print(max(abc_cnt))