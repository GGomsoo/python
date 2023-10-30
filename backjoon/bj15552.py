# 빠른 A+B
# 브론즈 IV

import sys

N = int(input())

for _ in range(N):
    # 파이썬이라면
    # input() 대신 sys.stdin.readline() 사용하라고 권고
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)