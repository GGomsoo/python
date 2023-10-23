import sys; sys.stdin=open('swea11783_input.txt')
import heapq

def 함수(v):
    heap = []
    heapq.heappush(heap, (0, v))
    D[v] = 0
    
    while heap:
        dist, now = heapq.heappop(heap)
        
T = int(input())
for test1 in range(1, T+1):
    N, E = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    
    for _ in range(E):
        s, g, w = map(int, input().split())
        adj[s].append((g, w))
        
    D = [1e12] * (N+1)
    함수(0)