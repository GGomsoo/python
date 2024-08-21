import sys; input = sys.stdin.readline

N = int(input())
lst1 = list(map(int, input().split()))
M = int(input())
lst2 = list(map(int, input().split()))

ans = {}

for m in lst2:
    ans[m] = 0

for n in lst1:
    if n in ans:
        ans[n] = 1

for a in ans:
    print(ans[a], end=" ")