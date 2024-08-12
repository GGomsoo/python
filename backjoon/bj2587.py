ans = []

for _ in range(5):
    ans.append(int(input()))
ans.sort()

N = len(ans)

# 평균값
print(sum(ans) // N)
# 중간값
print(ans[N//2])