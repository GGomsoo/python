# 바구니 뒤집기
# 브론즈 II
# 어려웠다

N, M = map(int, input().split())

# 1번부터 N번까지의 바구니
basket = list(range(1, N+1))

# 공 섞자
for _ in range(M):
    # 섞을 바구니 범위 설정
    s, g = map(int, input().split())
    # 바구니 섞은걸 다시 넣을 통
    basket_shake = []
    
    # 시작바구니 ~ 끝바구니
    for i in range(s-1, g):
        # 기존 바구니 끝 부분부터 앞으로 오면서 넣기
        basket_shake.append(basket[g-(i-(s-1))-1])
    for j in range(s-1, g):
        # 다시 정렬
        basket[j] = basket_shake[j-(s-1)]

for k in range(N):
    print(basket[k], end=' ')