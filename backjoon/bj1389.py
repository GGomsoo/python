# 케빈 베이컨의 6단계 법칙
# 너비 우선 탐색
# 최단 경로
from collections import deque

def solution(v):
    visited = [0] * (N+1)
    visited[v] = 1
    q = deque([v])

    while q:
        v = q.popleft()
        for w in range(1, N+1):
            if not visited[w] and friendship[v][w]:
                visited[w] = visited[v] + 1
                q.append(w)
    
    return sum(visited)

N, M = map(int, input().split()) # 유저의 수 N, 친구 관계의 수 M
friendship = [[0] * (N+1) for _ in range(N+1)] # 친구관계표
ans = [] # 친구들의 케빈 베이컨 수 합산

for _ in range(M):
    A, B = map(int, input().split())
    friendship[A][B] = friendship[B][A] = 1 # 친구관계

for i in range(1, N+1): # 1번부터 N번까지 사람들에 대해서
    ans.append(solution(i))

print(ans.index(min(ans)) + 1) # 케빈 베이컨의 수가 가장 작은 사람(인덱스값 + 1)을 출력한다.