N = int(input())

for i in range(1, N+1):
    print(" " * (N-i) + "*" * (i*2-1) + " ")

# 오른쪽 별은 공백이 1개만 있다. 예제를 잘 살펴보자