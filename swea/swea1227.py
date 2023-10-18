# SWEA 1227 S/W 문제해결 기본 7일차 - 미로2
# 1 : 벽 / 0 : 길 / 2 : 출발 / 3 : 도착
# 시작점 -> 도착점 가능 1 불가능 0

import sys; sys.stdin=open('swea1227_input.txt')
from collections import deque

def find_start():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

def escape_maze(si, sj):
    global ans
    # 시작점 방문체크
    visited[si][sj] = 1
    Q = deque()
    # Q에 시작점 좌표 입력
    Q.append((si, sj))

    while Q:
        goi, goj = Q.popleft()

        # 만약 Q에서 빼온 좌표가 미로의 도착점이라면
        if maze[goi][goj] == 3:
            # 길이 있으니까 1을 출력
            ans = 1

        # 그게 아니라면
        else:
            # 네방향 탐색하면서 미로를 진행
            di = [-1, 0, 1, 0]
            dj = [0, 1, 0, -1]
            for k in range(4):
                ni = goi + di[k]
                nj = goj + dj[k]
                # 미로의 새로운 i, j 값이 미로 범위 내에 있고
                if 0 <= ni < N and 0 <= nj < N:
                    # 방문 안했고, 벽이 아니라면
                    if not visited[ni][nj] and maze[ni][nj] != 1:
                        # 방문체크 후 Q에 입력
                        visited[ni][nj] = 1
                        Q.append((ni, nj))


T = 10
for test1 in range(1, T+1):
    # input에 tc넣는거 있음! 주의
    tc = int(input())
    # 미로 크기 100 x 100
    N = 100
    # 미로 정보 입력
    maze = [list(map(int, input())) for _ in range(N)]
    # 방문확인
    visited = [[0]*N for _ in range(N)]

    # 시작점 -> 도착점 가능 여부
    ans = 0
    # 시작점 찾는 함수
    si, sj = find_start()
    # 미로 탈출
    escape_maze(si, sj)

    print(f"#{test1} {ans}")
