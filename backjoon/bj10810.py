# 공 넣기
# 브론즈 III


# 공 번호, 공 넣을 횟수
N, M = map(int, input().split())

# 빈 바구니
basket = [0] * (N+1)

for _ in range(M):
    # s번부터 g번까지의 바구니에 ball로 채울거다
    # 이전에 무슨 공이 들어있던 결국 마지막에 든 공을 출력한다
    s, g, ball = map(int, input().split())
    for i in range(s, g+1):
        basket[i-1] = ball
        
# 바구니에 든 공들 출력
for i in range(N):
    print(basket[i], end=' ')