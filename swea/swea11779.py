# SWEA 11779 응용 구현 06 그래프의 기본과 탐색 - 연산
# import sys; sys.stdin=open('swea11779_input.txt')
from collections import deque
def 함수(v):
    # 들어와서 방문체크
    visited[v] = 1
    Q = deque()
    # 들어온 숫자를 Q에 추가
    Q.append(v)
    
    while Q:
        # Q에서 뽑은 s
        s = Q.popleft()
        
        # 연산을 하면서 얻은 s가 M과 같다면
        if s == M:
            # 연산이기 때문에 방문체크 -1 값
            return visited[s] - 1
        
        # 연산 +1, -1, *2, -10 중에서
        for w in [s+1, s-1, s*2, s-10]:
            # 연산값이 방문체크 한 적 없고, 조건 범위 안에 있다면
            if not visited[w] and 1 <= w <= 1_000_000:
                # Q에 넣고
                Q.append(w)
                # 연산했다는 의미의 방문체크 +1
                visited[w] = visited[s] + 1

T = int(input())
for test1 in range(1, T+1):
    # 자연수 N, 연산을 통해 얻은 다른 자연수 M
    N, M = map(int, input().split())
    # 1 <= N, M <= 1_000_000
    # N != M
    visited = [0] * (1_000_000 + 1)
    print(f"#{test1} {함수(N)}")
