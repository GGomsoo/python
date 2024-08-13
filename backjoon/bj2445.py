N = int(input())

# 가운데 공백이 2*(N-i) 만큼 있음
for i in range(1, N+1):
    print("*" * i + " " * 2 * (N-i) + "*" * i)

for i in range(N-1, 0, -1):
    print("*" * i + " " * 2 * (N-i) + "*" * i)