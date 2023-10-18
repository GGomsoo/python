# SWEA 11763 응용 구현 02 완전검색 - 전자카트 ( 8/30 )
# 다음에 다시 풀어보는걸로
# 1-2-3-1 경로 뭐가 있던데 안 풀었던거라 조금 어려움 겪는 중
import sys; sys.stdin=open('swea11763_input.txt')
def 함수(depth, total):
    global min_battery
    # 재귀 종료 조건
    if depth == N:
        min_battery = min(min_battery, total)

    # 가지치기
    if total > min_battery:
        return

    # 반복문
    for i in range(N):
        # 방문 안 했다면
        if not visited[i]:
            # 함수 전 행동
            visited[i] = 1
            # 함수 호출
            함수(depth + 1, total + battery[depth][i])
            # 돌아와서 초기화
            visited[i] = 0


T = int(input())
for test1 in range(1, T+1):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    visited[0] = 1
    min_battery = 1e12
    함수(0, 0)
    print(f"#{test1} {min_battery}")
