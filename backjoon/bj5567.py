from collections import deque

def bfs(v):
    visited[v] = 1 # 일단 나에게도 청첩장을 준다
    q = deque([v])

    while q:
        v = q.popleft()
        for w in range(2, N+1): # 나를 제외한 나머지 친구들에게
            if not visited[w] and arr[v][w]: # 준 적 없고, 서로 친구관계라면
                visited[w] = visited[v] + 1 # 몇다리 건너인지 표시
                q.append(w)

N = int(input()) # 상근이의 동기들
arr = [[0] * (N+1) for _ in range(N+1)] # 동기들과의 친구관계
visited = [0] * (N+1) # 초대한 친구인지 확인하기

M = int(input()) # 친구관계의 수
for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1 # 우린 서로 친구

bfs(1) # 상근이의 학번은 1이다. 1부터 시작
ans = 0
for v in visited: # 친구들 중에서
    if 0 < v <= 3: # 나, 나의 친구, 친구의 친구인 경우라면
        ans += 1 # 정답에 누적

print(ans-1) # 최종값에서 1명 (본인) 을 제외한 값을 출력한다