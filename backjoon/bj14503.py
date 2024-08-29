from collections import deque

N, M = map(int, input().split()) # 세로 N, 가로 M
robot_x, robot_y, robot_d = map(int, input().split()) # 로봇의 현재 위치와 방향
place = [list(map(int, input().split())) for _ in range(N)] # 청소해야할 장소

visited = [[0] * M for _ in range(N)]