N, M = map(int, input().split())

for num in range(1, N*M+1):
    if num % M == 0:
        print(num, end="\n")
    else:
        print(num, end=" ")