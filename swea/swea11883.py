# SWEA 11883 stack2 배열 최소 합
import sys; sys.stdin=open('swea11883_input.txt')
def 함수(depth, total):
    global min_sum
    # 재귀 종료 조건
    if depth == N:
        min_sum = min(total, min_sum)

    # 가지 치기
    if min_sum < total:
        return

    # 반복문
    for i in range(N):
        if not visited[i]:
            # 재귀 들어가기 전 행동
            visited[i] = 1
            # 재귀 호출
            함수(depth + 1, total + arr[depth][i])
            # 돌아와서 방문 초기화
            visited[i] = 0


T = int(input())
for test1 in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    # 최소합
    min_sum = 1e12
    함수(0, 0)
    print(f"#{test1} {min_sum}")