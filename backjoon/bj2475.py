# 검증수
# 브론즈 V

고유번호 = list(map(int, input().split()))

ans = 0
for i in 고유번호:
    ans += i**2

print(ans % 10)