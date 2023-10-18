# SWEA 11760 응용구현 02 완전검색 - 최소합
# import sys; sys.stdin=open('swea11760_input.txt')
def 함수(si, sj, total):
    global min_total
    # 재귀 종료 조건
    if si == sj == N-1:
        min_total = min(min_total, total)

    # 가지치기
    if min_total < total:
        return

    # 반복문
    # 오른쪽이나 아래로만 이동 가능
    di = [0, 1]
    dj = [1, 0]
    for k in range(2):
        ni = si + di[k]
        nj = sj + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            함수(ni, nj, total + numbers[ni][nj])


T = int(input())
for test1 in range(1, T+1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    min_total = 1e12

    # 시작점 좌표와 값을 함수 input값으로
    함수(0, 0, numbers[0][0])
    print(f"#{test1} {min_total}")
