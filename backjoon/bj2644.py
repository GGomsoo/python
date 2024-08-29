from collections import deque

N = int(input()) # 인원수
x, y = map(int, input().split()) # 촌수를 계산해야 하는 서로 다른 두 사람
M = int(input()) # 가족관계의 수
ans = 0

def bfs(v):
    visited[v] = 1
    q = deque([v])

    while q:
        v = q.popleft()

        if v == x: # 촌수 계산 해야하는 가족에 도달했다면
            return visited[v] - 1 # 총 계산 -1 ( 기본값을 1로 시작 )
        
        for w in range(1, N+1):
            if not visited[w] and family[v][w]:
                visited[w] = visited[v] + 1
                q.append(w)

family = [[0] * (N+1) for _ in range(N+1)] # 가족관계 리스트
visited = [0] * (N+1) # 방문체크

for _ in range(M):
    parents, child = map(int, input().split()) # 부모, 자식
    family[parents][child] = family[child][parents] = 1 # 서로 연결

ans = bfs(y) # 함수에 부모(자식) 번호를 넣어줌

if ans:
    print(ans)
else:
    print(-1)