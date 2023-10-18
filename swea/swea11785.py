# SWEA 11785 LIST1 min max

T = int(input())
for test1 in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    min_number = 1e12
    max_number = 0

    # 이제 min, max 쓸 수 있다 ㅠㅠ
    for i in range(N):
        min_number = min(min_number, numbers[i])
        max_number = max(max_number, numbers[i])

    ans = max_number - min_number
    print(f"#{test1} {ans}")
