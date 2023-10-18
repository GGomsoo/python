# swea 7465 - dfs - 창용 마을 무리의 개수
'''
2
6 5
1 2
2 5
5 1
3 4
4 6
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
'''
from collections import deque
def make_group(v):
    visited[v] = 1
    Q = deque()
    Q.append(v)

    while Q:
        v = Q.popleft()

        for w in adj[v]:
            if not visited[w]:
                visited[w] = 1
                Q.append(w)


T = int(input())
for test1 in range(1, T+1):
    N, M = map(int, input().split())

    # 방문 체크
    visited = [0] * (N+1)

    # 우리 서로 아는사이 인가요?
    adj = [[] for _ in range(N+1)]

    for _ in range(M):
        s, g = map(int, input().split())
        adj[s].append(g)
        adj[g].append(s)

    # 총 몇 개의 무리가 있을까요?
    group = 0

    for i in range(1, N+1):
        if not visited[i]:
            group += 1
            make_group(i)

    print(f"#{test1} {group}")
