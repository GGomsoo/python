from collections import deque
import sys; input = sys.stdin.readline

def bfs():
    q = deque(virus)

    while q:
        bug, j, i, time = q.popleft() # 바이러스의 종류, 위치, 시간을 추출

        if time == S: # 퍼진 시간이 S와 같다면 멈춘다
            break

        dj = [-1, 1, 0, 0] # 상하좌우 순서
        di = [0, 0, -1, 1]

        for kk in range(4): # 바이러스는 상하좌우의 방향으로 증식
            nj = j + dj[kk]
            ni = i + di[kk]

            if 0 <= ni < N and 0 <= nj < N: # 시험관 범위 내에 있으면서
                if not examiner[nj][ni]: # 해당 위치에 아무런 바이러스도 없다면
                    examiner[nj][ni] = bug # 바이러스 증식
                    q.append((examiner[nj][ni], nj, ni, time+1)) # 해당 바이러스의 종류, 위치, 흐른 시간을 다시 q에 기록

N, K = map(int, input().split())
examiner = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
virus = []

for j in range(N):
    for i in range(N):
        if examiner[j][i]:
            virus.append((examiner[j][i], j, i, 0)) # 처음 배치된 바이러스의 종류, 위치, 시간을 기록

virus.sort() # 바이러스 1번부터 정렬하기
bfs()

print(examiner[X-1][Y-1])