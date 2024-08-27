from collections import deque

def solution(j, i):
    visited[j][i] = 1 # 방문체크
    width = 1 # 방문 했으니 넓이 1
    q = deque([(j, i)]) # Q에 해당 좌표를 삽입

    while q:
        j, i = q.popleft() # 추출

        dj = [-1, 0, 1, 0]
        di = [0, 1, 0, -1]

        for k in range(4): # 네방향 탐색
            nj = j + dj[k]
            ni = i + di[k]

            if 0 <= nj < M and 0 <= ni < N: # 새로운 좌표가 모눈종이 영역 내에 있는가?
                if not visited[nj][ni] and not paper[nj][ni]: # 미방문 + 색칠X 라면
                    visited[nj][ni] = 1 # 방문표시
                    width += 1 # 넓이 + 1
                    q.append((nj, ni)) # 해당 좌표를 다시 Q에 삽입
                    
    ans.append(width) # 탐색 끝나면, 함수 내 최종 넓이를 ans 리스트에 추가

M, N, K = map(int, input().split()) # 세로, 가로, K개의 직사각형의 좌표

paper = [[0] * (N) for _ in range(M)] # 모눈종이
visited = [[0] * (N) for _ in range(M)] # 방문체크
ans = [] # 나머지 영역을 담을 리스트

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split()) # 직사각형 좌표

    for j in range(y1, y2):
        for i in range(x1, x2):
            paper[j][i] += 1 # 그림 그리기

# for p in paper: # 디버깅용
#     print(p)

for j in range(M):
    for i in range(N):
        if not visited[j][i] and not paper[j][i]: # 방문 안했고, 색칠도 되어있지 않다면
            solution(j, i) # BFS

ans.sort() # 오름차순 정렬
print(len(ans)) # 분리되어 나누어지는 영역의 개수
print(*ans) # 영역의 넓이