box = 4  # 직사각형 갯수
N = 100  # 좌표 1이상 100이하
arr = [[0] * N for _ in range(N)]
cnt = 0
for _ in range(box):
    x1, y1, x2, y2 = map(int, input().split())  # x, y 좌표

    for i in range(x1, x2):  # 직사각형 그리는중
        for j in range(y1, y2):
            arr[i][j] += 1  # 범위 색칠

for i in range(N):
    for j in range(N):
        if arr[i][j] > 1:  # 겹치는 부분들이 생겼음
            arr[i][j] = 1  # 1장으로 겹쳐버림

        if arr[i][j] == 1:
            cnt += 1
print(cnt)