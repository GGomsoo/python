from collections import deque

M, N = map(int, input().split()) # 상자의 가로M, 세로N

tmt = [list(map(int, input().split())) for _ in range(N)] # 토마토 창고
q = deque([]) # 익은 토마토의 좌표를 넣을 q
time = 0 # 다 익는데까지 걸리는 시간

# 토마토 창고에서 익은 토마토를 찾은 후, 해당 좌표를 q에 삽입
for j in range(N):
    for i in range(M):
        if tmt[j][i] == 1:
            q.append((j, i))

# q에서 익은 토마토에 대한 좌표를 추출
def solution():
    while q:
        j, i = q.popleft()

        dj = [-1, 0, 1, 0]
        di = [0, 1, 0, -1]

        # 네방향 탐색
        for k in range(4):
            nj = j + dj[k]
            ni = i + di[k]

            # 신규 좌표가 창고 범위 내에 있으면서
            if 0 <= nj < N and 0 <= ni < M:
                # 아직 익지 않은 토마토라면, 익힌 후 1씩 더해준다
                if tmt[nj][ni] == 0:
                    tmt[nj][ni] = tmt[j][i] + 1
                    q.append((nj, ni))

solution()

# 토마토 창고 내에서
for mato in tmt:
    if 0 in mato: # 덜 익은 토마토가 섞여 있다면
        print(-1) # -1 을 출력 후, 해당 코드를 종료
        exit(0)
    time = max(time, *mato) # 모두 익을 때 까지 걸린 시간
print(time - 1) # 익은 토마토 (1) 부터 시작했기 때문에 -1 을 해준다.