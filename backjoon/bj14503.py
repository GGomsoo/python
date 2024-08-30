from collections import deque
import sys; input = sys.stdin.readline

N, M = map(int, input().split()) # 세로크기 N, 가로크기 M
r, c, d = map(int, input().split()) # y, x, d
place = [list(map(int, input().split())) for _ in range(N)] # 방의 상태
visited = [[0] * M for _ in range(N)] # 방의 방문체크
ans = 0

def cleanRoom(i, j, d):
    global ans
    visited[i][j] = 1 # 입력받은 방의 좌표에 대해 방문체크
    q = deque([(i, j)]) # 좌표를 q에 삽입

    while q:
        i, j = q.popleft() # q에서 추출

        # 1번: 현재 칸이 아직 청소되지 않은 경우
        if place[i][j] == 0: # 해당 좌표의 값이 0이면
            place[i][j] = 2 # 해당 칸을 청소한다 ( 2로 변경 )
            ans += 1 # 청소한 방의 개수 추가
        
        # 3번: 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
        di = [-1, 0, 1, 0] # 네방향 탐색 ( 북 동 남 서 )
        dj = [0, 1, 0, -1]
        for _ in range(4):
            d = (d + 3) % 4 # 반시계 방향으로 90도 돌게 해주는 로직
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < N and 0 <= nj < M: # 새로운 위치가 방의 범위를 벗어나지 않고
                if not visited[ni][nj] and not place[ni][nj]: # 들른적도 없고, 청소도 안 되어있다면
                    visited[ni][nj] = 1 # 방문표시
                    q.append((ni, nj)) # 해당 방의 좌표를 q에 삽입
                    break # 1번으로 돌아간다.
        
        # 2번: 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        else:
            # 후진 준비한다
            bi = i - di[d]
            bj = j - dj[d]
            # 후진하려는 위치가 방의 범위를 벗어나지 않고
            if 0 <= bi < N and 0 <= bj < M:
                # 그 위치가 벽이 아니라면 후진
                if place[bi][bj] != 1:
                    q.append((bi, bj))
                # 벽이면 작동을 멈춘다
                else:
                    break

cleanRoom(r, c, d)
print(ans)