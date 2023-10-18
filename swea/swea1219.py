import sys; sys.stdin=open('swea1219_input.txt')
def 함수(v):
    visited[v] = 1
    for w in adj[v]:
        if not visited[w]:
            함수(w)


T = 10
for test1 in range(1, T+1):
    tc, M = map(int, input().split())
    road = list(map(int, input().split()))
    visited = [0] * 100
    adj = [[] for _ in range(100)]

    # 순서쌍이 16쌍
    # 그래서 데이터 받을 때 i*2, i*2+1 로 처리
    for i in range(M):
        s, g = road[i*2], road[i*2+1]
        adj[s].append(g)

    S, G = 0, 99
    함수(S)
    if visited[S] == 1 and visited[G] == 1:
        print(f"#{test1} 1")
    else:
        print(f"#{test1} 0")
