# 팩토리얼
# 브론즈V

N = int(input())

ans = 1
if N > 0:
    for i in range(1, N+1):
        ans *= i

print(ans)