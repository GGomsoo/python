import sys; input = sys.stdin.readline
from collections import deque

def bfs(v):
    visited[v] = 1 # 수빈이 현재 위치 방문체크
    q = deque([v]) # q에 기록

    while q:
        v = q.popleft()

        if v == K: # 수빈이가 동생 위치에 도달했다면
            return visited[v] - 1 # 가는데 걸린 시간 -1

        for w in (v*2, v-1, v+1): # 순간이동 하는 경우 0초 후에 2*v, 걷는다면 1초 후 v-1, v+1
            # 그래서 순간이동 먼저 연산하도록 순서를 위와 같이 설정
            if 0 <= w <= limit and not visited[w]: # 범위 내에 있고, 들른 적 없다면
                if w == v*2: # 순간이동의 경우
                    visited[w] = visited[v] # 0초 이기 때문에 걸린 시간 변함 X
                    q.appendleft(w) # 우선적으로 처리하기 위해 q의 가장 앞에 기록
                else:
                    visited[w] = visited[v] + 1 # 걸으면 1초니까 +1
                    q.append(w)
            

N, K = map(int, input().split()) # 수빈이의 위치 N, 동생의 위치 K
limit = 100_000 # 움직일 수 있는 최대 범위
visited = [0] * (limit + 1)
print(bfs(N))
