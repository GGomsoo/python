from collections import deque
import sys; input = sys.stdin.readline

def solution(x, y):
    visited[x][y] = 1 # 해당 좌표의 섬에 방문했다는 표시
    q = deque([(x, y)]) # 섬에 대한 좌표를 q에 삽입

    while q:
        i, j = q.popleft() # 좌표를 가져오고
        di = [0, 1, 1, 1, 0, -1, -1, -1] # 8방향 탐색한다
        dj = [-1, -1, 0, 1, 1, 1, 0, -1]

        for k in range(8):
            ni = i + di[k] # 새로운 좌표를 만들고
            nj = j + dj[k]
            if 0 <= ni < h and 0 <= nj < w: # 해당 좌표가 지도의 범위 내에 있으면서
                if not visited[ni][nj] and land[ni][nj] == 1: # 방문한 적이 없는 섬이라면
                    visited[ni][nj] = 1 # 방문했다는 표시를 한다 ( 중복 방지 )
                    q.append((ni, nj)) # 그 좌표를 다시 q에 넣고

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0: # 너비와 높이의 입력에 0이 들어오면 종료
        break

    else:
        land = [list(map(int, input().split())) for _ in range(h)] # 지도
        visited = [[0] * w for _ in range(h)] # 섬 방문 여부
        ans = 0

        for i in range(h):
            for j in range(w): # 지도에 대해서
                if not visited[i][j] and land[i][j] == 1: # 해당 좌표가 섬이면서 방문한적이 없다면?
                    solution(i, j) # 이어진 다른 섬이 있는지 확인하러가기
                    ans += 1 # 확인이 완료되면 개수를 추가
        print(ans)