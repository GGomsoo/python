import sys; input = sys.stdin.readline
from collections import deque

def solution(v):
    q = deque([v])
    visited = [0] * (N+1)
    visited[v] = 1
    cnt = 1

    while q:
        v = q.popleft()

        for w in linked[v]:
            if not visited[w]:
                visited[w] = 1
                cnt += 1
                q.append(w)
    
    return cnt

N, M = map(int, input().split()) # 컴퓨터 개수 N, 신뢰관계 개수 M
linked = [[] for _ in range(N+1)] # 컴퓨터의 신뢰 관계 리스트

for _ in range(M):
    A, B = map(int, input().split()) # A가 B를 신뢰한다 => B를 해킹하면 A도 해킹할 수 있다.
    linked[B].append(A)

ans = [] # 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호
max_cnt = 0 # 한 번에 가장 많이 해킹한 컴퓨터의 수
for i in range(1, N+1): # 1 번부터 N 번까지 컴퓨터에 대해
    temp_cnt = solution(i) # i 번 컴퓨터가 해킹한 컴퓨터 수
    if temp_cnt > max_cnt: # 해당 번호 컴퓨터가 해킹을 가장 많이 했다면
        max_cnt = temp_cnt # 최대값으로 해당값을 변경
        ans.clear() # 기존 컴퓨터 번호가 담긴 list를 초기화
        ans.append(i) # 새롭게 컴퓨터 번호를 담아준다
    elif temp_cnt == max_cnt: # 해킹한 컴퓨터 대수가 서로 같다면
        ans.append(i) # 리스트 초기화하지 않고 담아준다.

print(*ans) # 언패킹하여 출력