N = int(input())
arr = []

for _ in range(N):
    X, Y = map(int, input().split())
    arr.append([X, Y])

arr.sort(key=lambda x: (x[0], x[1]))
for i in arr:
    print(i[0], i[1])


# sort 함수에서 key값 lambda 활용