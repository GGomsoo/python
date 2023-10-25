# 공 바꾸기
# 브론즈 II


N, M = map(int, input().split())

# 1번부터 N번까지 번호가 적힌 공이 들어있는 바구니
basket = list(range(1, N+1))

# 공 바꿀 횟수만큼
for _ in range(M):
    # 시작 바구니, 끝 바구니 번호 입력
    s, g = map(int, input().split())
    # 공에 적힌 번호 - 1 = 인덱스 번호
    # 서로서로 바꿔 ( bubble sort )
    basket[s-1], basket[g-1] = basket[g-1], basket[s-1]

# 공 다 바꾼, 최종적인 바구니 출력
for i in range(N):
    print(basket[i], end=' ')