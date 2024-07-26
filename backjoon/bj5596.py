minkook = list(map(int, input().split()))
manse = list(map(int, input().split()))
# 좀 더 간결하게 입력을 받는 방법이 있을텐데...

sum_mk = sum(minkook)
sum_ms = sum(manse)

print(max(sum_mk, sum_ms))