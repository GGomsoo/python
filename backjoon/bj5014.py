import sys; input = sys.stdin.readline
from collections import deque

F, S, G, U, D = map(int, input().split()) # F층짜리 건물, 현재위치S, 목표위치G, 엘베U층 오르고 D층 내려간다
visited = [0] * (F + 1) # 층수 방문 확인

def bfs(v):
    visited[v] = 1 # 층수 방문 확인
    q = deque([v]) # q에 삽입

    while q:
        v = q.popleft() # 해당 층 추출

        if v == G: # 해당 층이 목표층이라면
            return visited[v] - 1 # 이동한 횟수 -1 ( 시작을 1로 했기 때문 )
        
        for w in (v + U, v - D): # 해당 층에서 2층 오른 위치, 1층 내린 위치 중
            if 0 < w <= F and not visited[w]: # 건물 범위 내에 있고, 들른적 없다면
                visited[w] = visited[v] + 1 # 이동 횟수 + 1 증가
                q.append(w)
    
    if visited[G] == 0: # 엘리베이터로 도달 못했다면
        return "use the stairs" # 계단 이용해라
    
print(bfs(S)) # 현재 위치 시작