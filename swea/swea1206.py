# SWEA 1206 View
import sys; sys.stdin=open('swea1206_input.txt')

T = int(input())
for test1 in range(1, T+1):
    N = int(input())
    building = list(map(int, input().split()))

    for i in range(2, N-2):
        left2 = building[i] - building[i - 2]
        left1 = building[i] - building[i - 1]
        right1 = building[i] - building[i + 1]
        right2 = building[i] - building[i + 2]

        views = 0
        for view in [left2, left1, right1, right2]:
            pass