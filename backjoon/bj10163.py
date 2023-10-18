# 백준 10163 색종이
import sys
input = sys.stdin.readline

색종이 = int(input())  # 색종이 장수
크기 = 1001
field = [[0] * 크기 for _ in range(크기)]

for 순서 in range(1,색종이+1):
    x1, y1, 너비, 높이 = map(int, input().split())  # 시작좌표 (x,y)
    for i in range(x1, x1 + 너비):
        for j in range(y1, y1 + 높이):
            field[i][j] = 순서

# for zz in field:  # 필드에 색종이 잘 붙어있나 확인
#     print(*zz)

for n in range(1, 색종이+1):  # 색종이 장 수 만큼 for 문 반복
    넓이 = 0  # 넓이 구해보자
    for 숫자 in field:  # 필드에 색종이 순서에 따른 숫자들이 기입되어 있음.
        for 찾는거 in 숫자:  # 순서대로 넓이를 구해보자
            if 찾는거 == n:  # 필드에 n번째 깔린 영역을 만나면?
                넓이 += 1  # 넓이 += 1
    print(넓이)
