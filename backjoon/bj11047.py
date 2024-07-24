N, K = map(int, input().split())
coins = []
coins_cnt = 0

for _ in range(N):
    coins.append(int(input()))

for i in range(len(coins)-1, -1, -1):
    if K >= coins[i]:
        coins_cnt += K // coins[i]
        K %= coins[i]

print(coins_cnt)

# 그리디