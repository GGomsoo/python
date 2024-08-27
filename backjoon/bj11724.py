from collections import deque

N, M = map(int, input().split()) # 정점의 개수 N, 노드의 개수 M

visited = [0] * (N+1) # 정점 방문체크
link = [[] * (N+1) for _ in range(N+1)] # 서로 연결됨을 표시하기 위한 lst
ans = 0 # 개수

# PyPy로 제출해야 정답된다.
def DFS(v):
    global ans
    visited[v] = 1 # 해당 정점 방문체크

    for w in range(1, N+1): # 1부터 N번의 정점까지에 대해서
        if not visited[w] and link[v][w]: # 방문한 적 없고, 서로 연결되어 있다면
            DFS(w) # DFS 실행

def BFS(v):
    global ans
    visited[v] = 1
    q = deque([v])

    while q:
        v = q.popleft()

        for w in range(1, N+1):
            if not visited[w] and link[v][w]:
                visited[w] = 1
                q.append(w)

for _ in range(M): # 노드의 개수만큼 for문 진행
    s, e = map(int, input().split()) # 시작점, 끝점 입력
    link[s][e] = link[e][s] = 1 # 서로 연결

for i in range(1, N+1): # 1번부터 N번까지 정점에 대해
    if not visited[i]: # 방문한 적 없다면
        # DFS(i) # DFS 실행
        BFS(i)
        ans += 1 # 나오면서 연결요소의 개수 + 1

print(ans)