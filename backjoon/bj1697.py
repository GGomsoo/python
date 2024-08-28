from collections import deque

N, K = map(int, input().split()) # 수빈이 위치, 동생 위치
visited = [0] * 100001 # 좌표의 최대점은 100,000이기 때문에 +1 한 100,001 까지 방문체크

def bfs(v):
    visited[v] = 1
    q = deque([v])

    while q:
        v = q.popleft()

        if v == K: # 동생 위치에 도달하면
            return visited[v] - 1 # 현재 위치까지 온 횟수 -1 ( 시작점을 1로 했기 때문에 -1 )

        for w in (v-1, v+1, v*2): # 위치가 v 일 때, 걷는다면 v-1, v+1, 순간이동 한다면 v*2
            if 0 <= w <= 100000 and not visited[w]: # 현재 위치가 범위 내에 있으면서, 방문한 적 없다면
                visited[w] = visited[v] + 1
                q.append(w)

print(bfs(N))