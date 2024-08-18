# 흑돌 == 1, 백돌 == 2
# import sys; sys.stdin=open("swea4615_input.txt")

def game(x, y, color):
    global N # 게임판의 길이를 global 변수로 받아온다
    osello[x][y] = color # 입력한 돌의 위치에 색깔을 바꾼다

    # 가로, 세로, 대각선 이동
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    # 반대색 구분용
    reverse = [0, 2, 1]

    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]

        tmp = []
        # 게임판 내부 이면서, 반대색인 경우
        while 0 <= nx < N and 0 <= ny < N and osello[nx][ny] == reverse[color]:
            tmp.append((nx, ny)) # 해당 좌표를 저장해둔다.
            nx += dx[k] # 그리고 그 방향으로 진행
            ny += dy[k]

        # 방향으로 진행했는데, 처음 돌이랑 같은 색깔이라면?
        if 0 <= nx < N and 0 <= ny < N and osello[nx][ny] == color:
            for nnx, nny in tmp: # 다른 돌 좌표를 불러와서
                osello[nnx][nny] = color # 내 돌로 바꾼다

T = int(input()) # test case
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 한 변의 길이 N, 돌 놓는 횟수 M

    # 게임판 초기 설정
    osello = [[0] * N for _ in range(N)]
    osello[N//2-1][N//2-1] = osello[N//2][N//2] = 2
    osello[N//2-1][N//2] = osello[N//2][N//2-1] = 1

    # 돌 입력하기
    for _ in range(M):
        x, y, c = list(map(int, input().split()))
        game(x-1, y-1, c)

    # 게임판 확인하면서 돌 갯수 계산
    white, black = 0, 0
    for i in range(N):
        for j in range(N):
            if osello[i][j] == 2:
                white += 1
            elif osello[i][j] == 1:
                black += 1
    
    print(f"#{tc} {black} {white}")