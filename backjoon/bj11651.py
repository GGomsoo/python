N = int(input())
arr = []

for _ in range(N):
    X, Y = map(int, input().split())
    arr.append([X, Y])

arr.sort(key=lambda x: (x[1], x[0]))

for i in arr:
    print(i[0], i[1])