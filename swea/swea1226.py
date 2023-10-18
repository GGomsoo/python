# SWEA 1226 S/W 문제해결 기본 7일차 - 미로1
# 16 x 16 미로
# 시작점 (1, 1) 도착점 (13, 13)
# 시작점부터 도착점까지 갈 수 있는지에 대한 여부 0, 1
# 1 벽 / 0 길 / 2 출발점 / 3 도착점
# import sys; sys.stdin=open('swea1226_input.txt')
def start():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


def escape_maze(si, sj):
    visited[si][sj] = 1
    Q = []
    Q.append((si, sj))

    while Q:
        wi, wj = Q.pop(0)

        if maze[wi][wj] == 3:
            return 1

        else:
            di = [-1, 0, 1, 0]
            dj = [0, 1, 0, -1]
            for k in range(4):
                ni = wi + di[k]
                nj = wj + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    if not visited[ni][nj] and maze[ni][nj] != 1:
                        visited[ni][nj] = 1
                        Q.append((ni, nj))
    return 0


T = 10
for test1 in range(1, T+1):
    tc = int(input())
    N = 16
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    si, sj = start()
    print(f"#{test1} {escape_maze(si, sj)}")
