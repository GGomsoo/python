from collections import deque

N, M = map(int, input().split()) # 가로 N, 세로 M

war = [list(input()) for _ in range(M)] # 전쟁터
visited = [[0] * N for _ in range(M)] # 병사 체크
white, black = 0, 0 # 아군(흰색), 적군(파란색)

# 병사는 한 명 이상 존재한다.
def white_power(j, i):
    global white
    visited[j][i] = 1
    q = deque([(j, i)])
    temp1 = 1 # 초기값 1

    while q:
        j, i = q.popleft()
        di = [0, 1, 0, -1]
        dj = [-1, 0, 1, 0]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < M:
                if not visited[nj][ni] and war[nj][ni] == "W": # 확인 안 한 병사이면서, 아군이라면
                    visited[nj][ni] = 1
                    temp1 += 1 # 병사수 추가
                    q.append((nj, ni))
    
    white += temp1 ** 2 # 아군의 파워에 병사 ** 2 수를 누적
    

def black_power(j, i):
    global black
    visited[j][i] = 1
    q = deque([(j, i)])
    temp2 = 1

    while q:
        j, i = q.popleft()
        di = [0, 1, 0, -1]
        dj = [-1, 0, 1, 0]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < M:
                if not visited[nj][ni] and war[nj][ni] == "B":
                    visited[nj][ni] = 1
                    temp2 += 1
                    q.append((nj, ni))
    
    black += temp2 ** 2

# 아군 확인
for j in range(M):
    for i in range(N):
        if not visited[j][i] and war[j][i] == "W":
            white_power(j, i)

# 적군 확인
for j in range(M):
    for i in range(N):
        if not visited[j][i] and war[j][i] == "B":
            black_power(j, i)

print(white, black)