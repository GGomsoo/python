# SWEA 11879 미로
# 출발점 찾기
def find_start():
    for i in range(N):
        for j in range(N):
            if map_info[i][j] == 2:
                return i, j


# 미로 길 찾기
def letsgoexit(si, sj):
    global ans
    visited[si][sj] = 1

    if map_info[si][sj] == 3:
        ans = 1
        return

    else:
        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]
        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if not visited[ni][nj] and map_info[ni][nj] != 1:
                    letsgoexit(ni, nj)


T = int(input())
for test1 in range(1, T+1):
    N = int(input())
    map_info = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    # 길 있는지에 대한 여부 확인
    ans = 0

    si, sj = find_start()
    letsgoexit(si, sj)
    print(f"#{test1} {ans}")
