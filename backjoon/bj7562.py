from collections import deque

T = int(input())

def bfs(i, j, a, b):
    visited[i][j] = 1 # 방문체크
    q = deque([(i, j)]) # q에 현재 위치 삽입

    while q:
        i, j = q.popleft() # 위치 추출

        if i == a and j == b: # 추출한 위치가 목표 위치라면
            return visited[i][j] - 1 # 누적횟수 -1 ( 초기값 1로 설정했기 때문에 -1 해준다 )
        
        di = [1, 2, 2, 1, -1, -2, -2, -1] # 8방향 탐색
        dj = [-2, -1, 1, 2, 2, 1, -1, -2]

        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < l and 0 <= nj < l: # 새로운 위치가 체스판 범위 내에 있다면
                if not visited[ni][nj]: # 방문 안했다면
                    visited[ni][nj] = visited[i][j] + 1 # 횟수 1씩 누적
                    q.append((ni, nj))
    
for _ in range(T):
    l = int(input()) # 체스판 한 변의 길이
    visited = [[0] * l for _ in range(l)] # 체스판 크기
    i, j = map(int, input().split()) # 현재 위치
    ans1, ans2 = map(int, input().split()) # 목표 위치
    print(bfs(i, j, ans1, ans2))
        