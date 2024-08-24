N = int(input())

dp = [0] * (N+1)

for i in range(1, N+1):
    if i == 1:
        dp[i] = 1
    if i == 2:
        dp[i] = 3
    if i >= 3:
        dp[i] = dp[i-1] + 2 * dp[i-2]
        
print(dp[-1] % 10007)