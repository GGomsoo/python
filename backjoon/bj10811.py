# 바구니 뒤집기
# 브론즈 II

N, M = map(int, input().split())

# 1번부터 N번까지의 바구니
basket = list(range(1, N+1))

# 여기 구현 못해먹겠다
for _ in range(M):
    s, g = map(int, input().split())
    
    for i in range(s, g+1):
        pass