# 백준 2563 색종이


종이의수 = int(input())
가로세로 = 100
도화지 = [[0]*가로세로 for _ in range(가로세로)]
넓이 = 0
for _ in range(종이의수):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):  # 100 x 100 도화지
            if 도화지[i][j] == 0:
                도화지[i][j] = 1
                넓이 += 1

# for 음 in 도화지:
#     print(*음)

print(넓이)