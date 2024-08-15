# 최단거리 == BFS == Queue 사용하기

from collections import deque

N, M = map(int, input().split()) # N x M 크기의 배열로 표현된 미로

mz = [list(map(int, input())) for _ in range(N)] # 미로
visited = [[0] * M for _ in range(N)] # 미로 방문체크용

def mirror(si, sj): # 미로의 최단거리 구하는 함수
    visited[si][sj] == 1 # 방문한 지점은 1로 표시
    Q = deque([(si, sj)]) # 방문한 좌표를 Q에 담음

    while Q:
        si, sj = Q.popleft() # 좌표를 꺼내고
        if (si, sj) == (N-1, M-1): # 종점인지 확인
            return visited[si][sj] + 1
        
        # 종점이 아닌 경우 네방향 탐색, 길을 찾는다
        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]

        for k in range(4):
            ni = si + di[k]
            nj = sj + dj[k]

            # 새로운 좌표가 미로를 벗어나는지 확인
            if 0 <= ni < N and 0 <= nj < M:
                # 방문하지 않았고, 길인 경우 해당 좌표를 다시 Q에 넣음
                if not visited[ni][nj] and mz[ni][nj] == 1:
                    Q.append((ni, nj))
                    # 거리 + 1
                    visited[ni][nj] = visited[si][sj] + 1

print(mirror(0, 0))