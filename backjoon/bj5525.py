# 다시 풀어봐야 한다

N = int(input())
M = int(input())
S = input()

P = "IOI" + "OI" * (N-1)
ans = 0

for i in range(M-len(P)):
    if S[i:i+len(P)] == P:
        ans += 1

print(ans)