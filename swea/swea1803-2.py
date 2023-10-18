import sys; sys.stdin=open('swea1803_input.txt')
import heapq
def 함수(start):
    # 우선순위 큐
    heap = []
    # 힙에 가중치와 시작점을 넣어준다
    heapq.heappush(heap, (0, start))
    # 시작점에 대한 가중치를 0으로 초기화
    D[start] = 0

    while heap:
        distance, now = heapq.heappop(heap)

        if D[now] > distance:
            break

        for next in adj[now]:
            next_v = next[0]
            cost = next[1]

            new_weight = distance + cost

            if D[next_v] >= new_weight:
                D[next_v] = new_weight
                heapq.heappush(heap, (new_weight, next_v))


T = int(input())
for test1 in range(1, T + 1):
    # 정점의 갯수, 간선의 갯수, 출발 정점, 도착 정점
    N, M, start, goal = map(int, input().split())

    adj = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    # 가중치! 다익스트라로 풀 때 필요하다
    D = [1e12] * (N + 1)

    for _ in range(M):
        s, g, weight = map(int, input().split())
        adj[s].append([g, weight])
        adj[g].append([s, weight])

    함수(start)
    print(f"#{test1} {D[goal]}")