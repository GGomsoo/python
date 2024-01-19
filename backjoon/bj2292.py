N = int(input())

# 시작 벌집 ( 초기값 1 )
start_bee_home = 1

# 벌집까지 가는 거리 ( 초기값 1 )
dist = 1

# 입력한 N이 시작 벌집보다 큰 경우
while N > start_bee_home:
    # 벌집 확장
    start_bee_home += 6 * dist
    
    # 확장 했으니 거리 증가
    dist += 1

# 결과값인 거리 출력
print(dist)