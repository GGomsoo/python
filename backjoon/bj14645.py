# 그냥 입력받고 "비와이"만 잘 출력하면 된다
import sys

N, K = map(int, sys.stdin.readline().split())

for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())

print("비와이")