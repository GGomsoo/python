# 개수 세기
# 브론즈 V

N = int(input())
arr = list(map(int, input().split()))
find = int(input())

ans = 0
for i in arr:
    if i == find:
        ans += 1

print(ans)