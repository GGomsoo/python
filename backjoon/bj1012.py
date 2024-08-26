from collections import deque

T = int(input())

# BFS
def solution(y, x):
    visited[y][x] = 1
    q = deque([(y, x)])

    while q:
        y, x = q.popleft()
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]

            if 0 <= nx < M and 0 <= ny < N:
                if not visited[ny][nx] and baechu[ny][nx]:
                    visited[ny][nx] = 1
                    q.append((ny, nx))

for _ in range(T):
    M, N, K = map(int, input().split()) # 가로, 세로, 배추 심은 갯수
    baechu = [[0] * M for _ in range(N)] # 배추밭
    visited = [[0] * M for _ in range(N)] # 방문리스트
    ans = 0 # 필요한 지렁이 마리수

    for _ in range(K): # 배추 심은 갯수만큼
        X, Y = map(int, input().split()) # 좌표 얻어오고
        baechu[Y][X] = 1 # 배추밭의 해당 좌표에 배추 표시
    
    for j in range(N):
        for i in range(M):
            if not visited[j][i] and baechu[j][i]:
                solution(j, i)
                ans += 1
    
    print(ans)