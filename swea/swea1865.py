# SWEA 1865 동철이의 일 분배
import sys; sys.stdin=open('swea1865_input.txt')
def letsgowork(depth, percent):
    global max_percent
    # 재귀 종료 조건
    if depth == N:
        max_percent = max(max_percent, percent)
        return

    # 가지 치기
    # 이전 확률보다 낮거나 같으면 거른다
    if max_percent >= percent:
        return

    # 반복문
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            letsgowork(depth + 1, (percent * daily_work[depth][i] * 0.01))
            visited[i] = 0


T = int(input())
for test1 in range(1, T+1):
    N = int(input())
    daily_work = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    max_percent = 0

    letsgowork(0, 1)
    # :.6f = 소숫점 6자리까지 나타내는 형식변환자
    # 이건 기억 안나서 이전에 풀었던거 봤음...ㅎ;
    print(f"#{test1} {max_percent * 100:.6f}")