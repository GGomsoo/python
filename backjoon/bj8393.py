# 합
# 브론즈 V
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램

N = int(input())

ans = 0
for i in range(1, N+1):
    ans += i
print(ans)