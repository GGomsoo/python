# SWEA 11886 Queue - 미로의 거리 ( 8/18 )

import sys; sys.stdin=open('swea11886_input.txt')
def start_point(maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


# 미로 탐방 시작
def gogogo(si, sj):
    # 들어오자마자 방문체크
    visited[si][sj] = 1
    # Q에 좌표 넣어주기
    Q = [(si, sj)]

    while Q:
        # Q에서 좌표 빼오기
        wi, wj = Q.pop(0)

        # 빼온 좌표가 미로의 도착지점이라면
        if maze[wi][wj] == 3:
            # 도착지점의 방문체크값 - 2
            # 출발지점, 도착지점은 빼줘야한다
            return visited[wi][wj] - 2

        # 도착점 아니라면 네방향 탐색하면서 미로 탐색
        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]
        for k in range(4):
            ni = wi + di[k]
            nj = wj + dj[k]
            # 새로운 좌표로 사용할 값이 인덱스로 유효하다면
            if 0 <= ni < N and 0 <= nj < N:
                # 방문한 적 없고, 미로에서도 벽이 아니라면
                if not visited[ni][nj] and maze[ni][nj] != 1:
                    # Q에 새로운 좌표값을 추가
                    Q.append((ni, nj))
                    # 한 칸 진행했다는 의미로
                    # 새로운 지점 = 이전 지점 방문체크 +1
                    visited[ni][nj] = visited[wi][wj] + 1
    # 길이 없다면 0을 출력
    return 0


T = int(input())
for test1 in range(1, T+1):
    # 미로의 크기
    N = int(input())
    # 미로에 대한 정보
    maze = [list(map(int, input())) for _ in range(N)]
    # 미로의 크기와 동일한 크기의 방문체크
    visited = [[0] * N for _ in range(N)]
    # 미로 출발지점 찾기
    si, sj = start_point(maze)
    print(f"#{test1} {gogogo(si, sj)}")
