from collections import deque
import sys; input = sys.stdin.readline

def solution(j, i):
    visited[j][i] = 1 # 방문체크
    temp_width = 1 # 임시 넓이. 방문했으니 1로 시작
    q = deque([(j, i)])

    while q:
        j, i = q.popleft()

        dj = [-1, 0, 1, 0]
        di = [0, 1, 0, -1]

        for k in range(4): # 네방향 탐색
            nj = j + dj[k]
            ni = i + di[k]

            if 0 <= nj < N and 0 <= ni < M:
                if not visited[nj][ni] and paper[nj][ni]: # 미방문 + 그림이 그려진 칸이라면
                    visited[nj][ni] = 1 # 방문표시
                    temp_width += 1 # 넓이 + 1
                    q.append((nj, ni))
                    
    return temp_width # 그림의 크기를 함수의 return 값으로 반환

N, M = map(int, input().split()) # 세로, 가로 크기
paper = [list(map(int, input().split())) for _ in range(N)] # 도화지
visited = [[0] * M for _ in range(N)] # 그림 방문체크
cnt = 0 # 그림의 개수
max_width = 0 # 가장 넓은 그림


for j in range(N):
    for i in range(M):
        if not visited[j][i] and paper[j][i]: # 확인 안했고, 그림이 그려져있다면
            cnt += 1 # 그림 개수 추가
            max_width = max(max_width, solution(j, i)) # 그림을 찾아가면서 넓이 비교

print(cnt)
print(max_width)