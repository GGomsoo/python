from collections import deque

# 정상
def normal(i, j):
    visited1[i][j] = 1
    q = deque([(i, j)])

    while q:
        i, j = q.popleft()

        di = [0, 1, 0, -1]
        dj = [-1, 0, 1, 0]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            
            if 0 <= ni < N and 0 <= nj < N:
                # 방문한 적 없고, q에서 추출한 좌표와 새로운 좌표에 대한 grid 값이 동일한지 계산
                if not visited1[ni][nj] and grid[i][j] == grid[ni][nj]: 
                    visited1[ni][nj] = 1
                    q.append((ni, nj))

# 적록색맹
def haveRG(i, j):
    visited2[i][j] = 1
    qq = deque([(i, j)])

    while qq:
        i, j = qq.popleft()

        di = [0, 1, 0, -1]
        dj = [-1, 0, 1, 0]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < N:
                if not visited2[ni][nj] and grid[i][j] == grid[ni][nj]:
                    visited2[ni][nj] = 1
                    qq.append((ni, nj))

N = int(input())
grid = [list(input()) for _ in range(N)]
visited1 = [[0] * N for _ in range(N)] # 1 = 정상
visited2 = [[0] * N for _ in range(N)] # 2 = 적록색맹

ans1, ans2 = 0, 0 # 1 = 정상, 2 = 적록색맹

# 정상
for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            normal(i, j)
            ans1 += 1

# 먼저 정상인의 구역 수를 계산 후, grid를 적록색맹에 맞게 수정한다.
# 적록색맹
for i in range(N):
    for j in range(N):
        if grid[i][j] == "G":
            grid[i][j] = "R"

for i in range(N):
    for j in range(N):
        if not visited2[i][j]:
            haveRG(i, j)
            ans2 += 1

print(ans1, ans2)