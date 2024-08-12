# N * M 크기의 배열, 1이상 K이하의 정수를 채워넣기
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split()) 
ans = []

for i in range(N):
    temp = []
    for j in range(M):
        temp.append(i+j+1)
    ans.append(temp)

if ans[N-1][M-1] <= K:
    print("YES")
    for i in ans:
        print(*i)
else:
    print("NO")