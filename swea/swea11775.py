# SWEA 11775 응용 구현 05 백트래킹 - 최소 생산 비용 ( 9/19 )
import sys; sys.stdin=open('swea11775_input.txt')
def 함수(depth, total):
    global min_cost
    # 재귀 종료 조건
    if depth == N:
        min_cost = min(min_cost, total)
        return

    # 가지 치기
    if total > min_cost:
        return

    # 반복문
    for i in range(N):
        if not visited[i]:
            # 재귀 들어가기 전
            visited[i] = 1
            # 재귀 호출
            함수(depth + 1, total + factory[depth][i])
            # 돌아와서 초기화
            visited[i] = 0


T = int(input())
for test1 in range(1, T+1):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_cost = 1e12
    함수(0, 0)
    print(f"#{test1} {min_cost}")