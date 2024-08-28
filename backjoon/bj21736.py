from collections import deque

N, M = map(int, input().split()) # 세로 N, 가로 M

campas = [list(input()) for _ in range(N)] # 캠퍼스
visited = [[0] * M for _ in range(N)]
ans = 0 # 만날 수 있는 사람의 수

def bfs(j, i):
    global ans
    visited[j][i] = 1
    q = deque([(j, i)]) # 도연이 좌표 q에 삽입

    while q:
        j, i = q.popleft()
        dj = [-1, 0, 1, 0]
        di = [0, 1, 0, -1]

        # 상하좌우 이동
        for k in range(4):
            nj = j + dj[k]
            ni = i + di[k]

            if 0 <= nj < N and 0 <= ni < M: 
                if not visited[nj][ni] and campas[nj][ni] != "X": # 들른 적 없고, 벽이 아니라면
                    if campas[nj][ni] == "P": # 그곳에 사람이 있다면
                        ans += 1 # 만난 사람 수 추가
                    visited[nj][ni] = 1 # 사람이 없고 그냥 길인 경우에는, 지나온 표시 해주기
                    q.append((nj, ni))


for j in range(N):
    for i in range(M):
        if not visited[j][i] and campas[j][i] == "I": # 도연이를 시작점으로
            bfs(j, i)

if ans: # 만난 사람이 있다면, 인원수 출력
    print(ans)
else: # 없다면 TT 출력
    print("TT")