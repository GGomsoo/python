from collections import deque

N = int(input()) # N x N 크기
land = [list(map(int, input().split())) for _ in range(N)] # 지역 정보

max_rain = 0 # 해당 지역 내 최고 높이
ans = 0 # 물에 안 잠긴 지역

def solution(i, j, rain):
    visited[i][j] = 1
    q = deque([(i, j)])

    while q:
        i, j = q.popleft()

        di = [0, 1, 0, -1]
        dj = [-1, 0, 1, 0]

        for k in range(4): # 네방향 탐색
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if not visited[ni][nj] and land[ni][nj] > rain: # 방문 안했고, 해당 지역이 강수량보다 높은 지역이라면
                    visited[ni][nj] = 1 # 방문 처리
                    q.append((ni, nj)) # q에 해당 지역의 좌표 삽입

for l in land:
    max_rain = max(max_rain, *l) # 지역 순회하면서 최대값 구하기
# print(max_rain)

for k in range(max_rain):
    temp = 0 # 강수량에 따른 안전지역 카운트
    visited = [[0] * N for _ in range(N)] # 강수량에 따른 방문체크 초기화

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and land[i][j] > k: # 방문 안했고, 강수량보다 높은 지역이라면
                solution(i, j, k) # BFS
                temp += 1 # 지역 + 1
    
    if ans < temp:
        ans = temp

print(ans)