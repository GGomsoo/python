# 주사위 세개
# 브론즈 IV
# 1부터 6까지 눈 가진 3개의 주사위
# 같은 눈 3개 나오면 10000 + 같은 눈 * 1000 상금
# 같은 눈 2개 나오면 1000 + 같은 눈 * 100 상금
# 모두 다른 눈 나오면 그중 가장 큰 눈 * 100 상금


dice = list(map(int, input().split()))

WWCD = 0

if dice[0] == dice[1] == dice[2]:
    WWCD = 10000 + dice[0] * 1000

elif dice[0] == dice[1]:
    WWCD = 1000 + dice[0] * 100

elif dice[0] == dice[2]:
    WWCD = 1000 + dice[0] * 100

elif dice[1] == dice[2]:
    WWCD = 1000 + dice[1] * 100

else:
    WWCD = max(dice) * 100

print(WWCD)