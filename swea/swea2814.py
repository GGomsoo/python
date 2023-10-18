# swea 2814 최장경로 - 그래프
# N 개의 정점 M개의 간선
# DFS
'''
2
1 0
3 2
1 2
3 2
'''
def 함수(v, lst):
    global ans
    ans = max(ans, len(lst))

    # 인접 리스트에 대해
    for w in range(1, N+1):
        # 입력받은 lst에 인접 정점이 들어있지 않으면
        if adj[v][w] and w not in lst:
            # 재귀 돌면서 lst에 인접 정점을 추가
            함수(w, lst+[w])


T = int(input())
for test1 in range(1, T+1):
    # 정점의 갯수 M, 간선의 갯수 N
    N, M = map(int, input().split())

    # 인접 리스트
    adj = [[0]*(N+1) for _ in range(N+1)]

    # 인접 이어주기
    for _ in range(M):
        s, g = map(int, input().split())
        # 인접 리스트에 append
        adj[s][g] = adj[g][s] = 1

    ans = 0
    # 1번부터 N번까지의 정점에 대해
    for i in range(1, N+1):
        # 출발 정점, [정점]
        함수(i, [i])

    print(f"#{test1} {ans}")
