# A = 65, a = 97
S = input() # 주어진 단어, 알파벳 소문자로만 이루어져 있다
ans = [0] * 26 # 알파벳 개수 26개

for i in S: # 주어진 단어
    for j in range(97, 123): # 알파벳 소문자의 아스키코드 범위
        if i == chr(j):
            ans[j % 97] += 1
print(*ans)