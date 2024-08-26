from collections import deque

N = int(input()) # 컴퓨터의 수
M = int(input()) # 연결된 컴퓨터 쌍의 수

# DFS
def solution(v):
    global ans
    visited[v] = 1 # 중복 확인을 방지하기 위한 컴퓨터 확인체크
    ans += 1 # 너 감염됐다

    for w in range(1, N+1): # 1번부터 N까지
        if not visited[w] and linked[v][w]: # 해당 컴퓨터 확인한 적 없고, 연결되어 있다면
            solution(w) # 해당 번호의 컴퓨터와 연결된게 있는지 또 확인하러 가기

# BFS
def solution2(v):
    global ans
    visited[v] = 1 # 해당 컴퓨터 확인 표시
    q = deque([v]) # 컴퓨터 번호를 q에 삽입

    while q:
        v = q.popleft() # 번호를 추출
        for w in range(1, N+1):
            if not visited[w] and linked[v][w]: # 미확인 컴퓨터이면서 연결되어있다면
                visited[w] = 1 # 확인체크
                ans += 1 # 감염개수 증가
                q.append(w) # 해당 컴퓨터 번호를 q에 삽입

linked = [[0] * (N+1) for _ in range(N+1)] # 연결된 컴퓨터들 표시 ( 양방향 그래프 )
visited = [0] * (N+1) # 컴퓨터 확인리스트
ans = 0 # 감염된 컴퓨터 개수

for _ in range(M):
    s, e = map(int, input().split()) # 직접 연결된 컴퓨터 번호 쌍
    linked[s][e] = linked[e][s] = 1 # 양방향으로 연결됬다는 1표시

# # DFS
# solution(1) # 1번 컴퓨터를 통해 바이러스에 걸린 컴퓨터 찾으러가기
# print(ans - 1) # 전체 개수에서 1번 컴퓨터를 뺀 개수

# BFS
solution2(1)
print(ans)