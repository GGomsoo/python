# SWEA 1238 S/W 문제해결 기본 10일차 - Contact
# import sys; sys.stdin=open('swea1238_input.txt')
from collections import deque
def emergency_call(start):
    # 들어오자마자 방문확인
    visited[start] = 1
    Q = deque()
    # Q에 시작당번 넣기
    Q.append(start)

    while Q:
        v = Q.popleft()

        # 1부터 100까지
        for w in range(1, V+1):
            # 방문 안했고 서로 연락망 연결되어 있다면
            if not visited[w] and emergency[v][w]:
                # Q에 집어넣기
                Q.append(w)
                # 방문 확인하기. 앞 사람에게 연락 받았기 때문에 순번이 +1
                visited[w] = visited[v] + 1


# test_case 10개라고 주어짐
T = 10
# 사람들의 번호 1부터 100
V = 100
for test1 in range(1, T+1):
    data_length, start = map(int, input().split())
    data = list(map(int, input().split()))

    # 인접 행렬
    emergency = [[0] * (V+1) for _ in range(V+1)]
    # 방문확인
    visited = [0] * (V+1)

    # from, to 대입
    for i in range(0, data_length, 2):
        from_, to_ = data[i], data[i+1]
        # 양방향이 아니다
        emergency[from_][to_] = 1

    # 시작 당번부터 비상연락망 시작
    emergency_call(start)

    # 마지막에 연락 받은사람
    last_receiver = 0
    # 1부터 100까지
    for i in range(1, V+1):
        # visited에 누적된 숫자들 비교하면서 마지막에 연락을 받은사람 찾기
        if visited[last_receiver] <= visited[i]:
            last_receiver = i

    print(f"#{test1} {last_receiver}")
