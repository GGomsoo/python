# swea 1247 - 백트래킹 - 최적 경로
# 회사 출발 -> 냉장고 배달 - > 집으로 퇴근
# 배달 다 하고 집으로 돌아오는 경로 중 가장 짧은 경로 찾기
# 회사, 집, 배달장소 좌표가 순서대로 제공
from collections import deque

def 함수(delivery, x, y, total):
    global min_distance
    # 가지 치기
    if total > min_distance:
        return
    # 재귀 종료 조건
    # 배달 다 했으면
    if delivery == customers:
        total += abs(x-house[0]) + abs(y-house[1])
        min_distance = min(min_distance, total)
        return
    # 반복문
    for i in range(customers):
        if not visited[i]:
            visited[i] = True
            # distance = total + abs(x - Q[i][0]) + abs(y - Q[i][1])
            distance = total + abs(x-lets_go[i][0]) + abs(y-lets_go[i][1])
            # 함수(delivery + 1, Q[i][0], Q[i][1], distance)
            함수(delivery + 1, lets_go[i][0], lets_go[i][1], distance)
            visited[i] = False


T = int(input())
for test1 in range(1, T+1):
    # 고객의 수
    customers = int(input())
    # 회사, 집, 고객주소 좌표
    address_list = list(map(int, input().split()))
    # 방문 체크리스트
    # 0, 1 보다 True, False 빠르다고 한 것 같아서 해봄
    visited = [False for _ in range(customers)]
    # 최단 거리
    min_distance = 1e9
    # 주소 넣을 리스트를 deque() 로 해버림
    # 이거 사실 deque 안써도 될 것 같음
    # 그냥 연습겸 써봄
    # Q = deque()

    # deque 사용 안하고 그냥 list로
    lets_go = []
    company_list = []
    house_list = []

    for i in range(0, len(address_list), 2):
        # Q에 튜플 형식으로 (x, y) 좌표 넣음
        # Q.append((address_list[i], address_list[i + 1]))
        lets_go.append((address_list[i], address_list[i+1]))
    # 맨 처음 좌표는 회사 좌표
    # company = Q.popleft()
    company = lets_go.pop(0)
    # 그 다음 좌표는 집 좌표
    # house = Q.popleft()
    house = lets_go.pop(0)

    # 함수 호출(방문 고객 수, 회사 x좌표, 회사 y좌표, 거리)
    # 회사에서 출발
    함수(0, company[0], company[1], 0)
    # 정답 출력
    print(f"#{test1} {min_distance}")
