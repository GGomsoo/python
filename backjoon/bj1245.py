from collections import deque
import sys; input = sys.stdin.readline

def BFS(j, i):
    global flag
    visited[j][i] = 1
    q = deque([(j, i)])

    while q:
        j, i = q.popleft()

        # X좌표와 Y좌표 차이 모두 1이하일 경우 ( => 8방향 )
        dj = [-1, -1, 0, 1, 1, 1, 0, -1]
        di = [0, 1, 1, 1, 0, -1, -1, -1]

        for k in range(8):
            nj = j + dj[k]
            ni = i + di[k]

            if 0 <= nj < N and 0 <= ni < M:
                if mt[nj][ni] > mt[j][i]: # 산봉우리와 인접한 격자는 모두 산봉우리 높이보다 작야아 한다
                    flag = 0 # 높은 경우를 제외

                if not visited[nj][ni] and mt[nj][ni] == mt[j][i]: # 산봉우리는 같은 높이를 가지는 하나의 격자 혹은 인접 격자들의 집합
                    visited[nj][ni] = 1
                    q.append((nj, ni))

N, M = map(int, input().split()) # 세로N, 가로M
mt = [list(map(int, input().split())) for _ in range(N)] # 농장
visited = [[0] * M for _ in range(N)] # 방문체크
ans = 0 # 봉우리 개수

for j in range(N):
    for i in range(M):
        if not visited[j][i] and mt[j][i] > 0: # 방문 하지않은 산
            flag = 1 # 산봉우리라는 표시
            BFS(j, i)

            if flag: # 해당 좌표가 산봉우리가 맞다면
                ans += 1 # 봉우리 개수 추가

print(ans)