'''
4 4 1 100
7 10 3 40
6 3 2 70
2 2 3 2 2 2 2 3 3 4 4 3 2 2 3 3 3 2 2 3
4 4 1 4 4 1 4 4 1 1 1 4 1 4 3 3 3 3 3 3
'''
# 제자리 상 우 하 좌
di = [0, -1, 0, 1, 0]
dj = [0, 0, 1, 0, -1]

# 빈 리스트 10 * 10
지도 = [[[] for _ in range(10)] for _ in range(10)]

for _ in range(3):
    si, sj, coverage, power = map(int, input().split())

    for i in range(10):
        for j in range(10):
            if abs(si-i-1) + abs(sj-j-1) <= coverage:
                지도[j][i].append(power)

# 사용자 이동경로
A_move = [0] + list(map(int, input().split()))
B_move = [0] + list(map(int, input().split()))
print(A_move)
print(B_move)

Ai, Aj = (0, 0)
Bi, Bj = (9, 9)
max_charge = 0

for row in 지도:
    print(*row)
