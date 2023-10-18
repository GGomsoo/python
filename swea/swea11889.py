# SWEA 11889 Queue - 노드의 거리 ( 8/18 )
# import sys; sys.stdin=open('swea11889_input.txt')
def 함수(v):
    # 들어오자마자 방문체크
    visited[v] = 1
    # 빈 Q 생성 + Q에 v 추가
    Q = [v]

    while Q:
        # Q에서 뽑아온 정점
        s = Q.pop(0)
        # 뽑아온 정점이 도착점이라면
        if s == G:
            # 결과 도출
            # 정점 방문갯수 - 1
            return visited[s] - 1
        else:
            # 인접리스트에 대하여
            for w in adj[s]:
                # 미방문 했다면
                if not visited[w]:
                    # Q에 추가하고
                    Q.append(w)
                    # 다음 레벨이기 때문에 +1
                    visited[w] = visited[s] + 1
    # 연결되지 않았다면 0을 출력
    return 0


T = int(input())
for test1 in range(1, T+1):
    # 정점의 갯수, 간선의 갯수
    V, E = map(int, input().split())

    # 방문 체크
    visited = [0] * (V+1)
    # 인접 리스트 생성
    adj = [[] for _ in range(V+1)]

    for _ in range(E):
        s, g = map(int, input().split())
        adj[s].append(g)
        adj[g].append(s)

    # 시작점, 도착점
    S, G = map(int, input().split())
    print(f"#{test1} {함수(S)}")
