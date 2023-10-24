# 코딩은 체육과목 입니다
# 브론즈 V

N = int(input())

ans = 0
for i in range(1, N+1):
    if i % 4 == 0:
        ans += 1

print(f"{'long ' * ans}int")