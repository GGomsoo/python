# 창용이 2트
def 함수(v):
    visited[v] = 1
    Q = [v]

    while Q:
        v = Q.pop(0)

        for w in range(1, N+1):
            if adj[v][w] and not visited[w]:
                visited[w] = 1
                Q.append(w)


T = int(input())
for test1 in range(1, T+1):
    # N명의 사람, M개의 인맥
    N, M = map(int, input().split())

    # 방문체크
    # 1번부터 N번까지니까 N+1 만큼 해주기
    visited = [0] * (N+1)

    # 우리는 아는 사람인가요? ( 인접 확인하기, 인접 행렬 )
    adj = [[0] * (N+1) for _ in range(N+1)]

    for _ in range(M):
        # 두 사람~
        s, g = map(int, input().split())
        # 서로 아는사이니까 ( 무방향 그래프 )
        adj[s][g] = adj[g][s] = 1

    # 총 몇 개의 무리인가요?
    ans = 0

    for i in range(1, N+1):
        if not visited[i]:
            ans += 1
            함수(i)

    print(f"#{test1} {ans}")
