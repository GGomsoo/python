import sys; input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split()) # N 개의 노드, M 개의 노드 쌍

link = [[0] * (N+1) for _ in range(N+1)]
ans = 0

# BFS
def solution(start, end):
    visited[start] = 1
    q = deque([(start, 0)]) # q에 시작점과 초기거리 0을 삽입

    while q:
        v, dist = q.popleft() # 시작점과 거리를 q에서 추출

        if v == end: # 해당 노드가 종료점이라면
            return dist # 거리를 return
        
        for w in range(1, N+1): # 노드 탐색
            if not visited[w] and link[v][w]: # 미방문 + 연결된 노드라면
                visited[w] = 1 # 방문체크
                q.append((w, dist + link[v][w])) # q에 해당 노드, 누적된 거리를 삽입

# DFS
def solution2(start, end, dist): # 시작, 끝, 거리를 변수로 받음
    global ans
    visited[start] = 1 # 방문체크

    for w in range(1, N+1):
        if not visited[w] and link[start][w]: # 방문 안했고, 연결되어 있다면?
            if w == end: # 탐색점이 종료점과 같다면
                ans = dist + link[start][w] # ans에 해당 값을 대입
            else: # 그게 아니라면 계속 찾아본다
                solution2(w, end, dist + link[start][w])



for _ in range(N-1):
    s, e, d = map(int, input().split()) # 연결된 두 점과 거리
    link[s][e] = link[e][s] = d # 양방향 그래프

for _ in range(M): # 거리를 알고 싶은 M개의 노드 쌍
    ss, ee = map(int, input().split()) # 시작점, 끝점
    visited = [0] * (N+1) # 방문 체크용
    # DFS 용
    solution2(ss, ee, 0) 
    print(ans)

    # BFS 용
    # print(solution(ss, ee))