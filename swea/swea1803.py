# swea 1803 Shortest Path Faster - 그래프(dfs)
# 제약 사항 1 <= N <= 100,000 / N-1 <= M <= 300,000
# 각 간선의 가중치는 1,000,000 이하인 양의 정수
'''
2
2 1 1 2
1 2 1
3 2 3 1
3 2 2
1 2 1
'''
def 함수(v, weight):
    global ans
    ans = max(ans, weight)
    visited[v] = 1

    for w in range(1, N+1):
        if adj[v][w] and not visited[w]:
            visited[w] = 1
            함수(w, weight + adj[v][w])
            visited[w] = 0


T = int(input())
for test1 in range(1, T+1):
    N, M, start, end = map(int, input().split())

    adj = [[0]*(N+1) for _ in range(N+1)]
    visited = [0] * (N+1)

    for _ in range(M):
        s, g, weight = map(int, input().split())
        adj[s][g] = adj[g][s] = weight

    ans = 0

    for i in range(1, N+1):
        함수(i, 0)

    print(f"#{test1} {ans}")
