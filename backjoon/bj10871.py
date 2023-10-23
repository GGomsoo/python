# X보다 작은 수
# 브론즈 V

N, X = map(int, input().split())
arr = list(map(int, input().split()))

for i in arr:
    if i < X:
        print(i, end=' ')