# 수열 / 백준 2559

def K일합계산(온도):
    합목록 = []
    합 = 0
    for j in range(K):
        합 += 온도[j]
    합목록.append(합)

    for i in range(N-K):
        온도의합 = 합목록[-1] + 온도[i+K] - 온도[i]
        합목록.append(온도의합)

    최대값 = -987654321
    for 온도 in 합목록:
        if 최대값 < 온도:
            최대값 = 온도
    return 최대값

N, K = map(int, input().split())
온도 = list(map(int, input().split()))
print(K일합계산(온도))
