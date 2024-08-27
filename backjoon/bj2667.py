from collections import deque

N = int(input()) # 지도의 크기
apart = [list(map(int, input())) for _ in range(N)] # 지도
visited = [[0] * N for _ in range(N)] # 방문체크
cnt = [] # 단지 담을 list

# BFS 활용
def solution(i, j):
    visited[i][j] = 1 # 받아온 좌표에 대해 방문체크
    width = 1 # 넓이 1 시작
    q = deque([(i, j)]) # 해당 좌표를 q에 삽입

    while q:
        i, j = q.popleft() # 다시 추출

        di = [0, 1, 0, -1]
        dj = [-1, 0, 1, 0]

        for k in range(4): # 네방향 탐색
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N: # 신규 좌표가 지도 범위 내에 있으면서
                if not visited[ni][nj] and apart[ni][nj]: # 방문한 적 없으면서, 집이 있는 경우라면
                    visited[ni][nj] = 1 # 방문체크
                    width += 1 # 넓이 +1
                    q.append((ni, nj)) # 다시 해당 좌표를 q에 삽입
    cnt.append(width) # while 문이 끝났다면, 단지 넓이에 대한 값을 리스트에 추가

for i in range(N):
    for j in range(N):
        if not visited[i][j] and apart[i][j] == 1: # 방문 한 적 없으면서, 집이 있다면
            solution(i, j) # 함수 진행

cnt.sort() # 오름차순 정렬
print(len(cnt)) # 단지 갯수 = list의 길이
for c in cnt: # 리스트내 요소들을 for 문을 통하여 추출
    print(c)