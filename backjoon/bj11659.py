import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

## 1차 시도, 답은 나오는데 시간초과
## 완탐으로 풀면 시간초과가 발생한다.
## 누적합을 구한 후, 구간합을 구하면 좀 더 빠르게 구할 수 있다.
# 1. 누적 합 구하기: S[i] = S[i-1] + A[i]
# 2. 구간 합 구하기: S[j] - S[i-1]

# import sys

# N, M = map(int, sys.stdin.readline().split())

# lst = list(map(int, sys.stdin.readline().split()))

# for _ in range(M):
#     I, J = map(int, sys.stdin.readline().split())
#     print(sum(lst[I-1:J]))

sum_lst = [0]
temp_num = 0

for num in lst:
    temp_num += num
    sum_lst.append(temp_num)

for _ in range(M):
    I, J = map(int, input().split())
    print(sum_lst[J] - sum_lst[I-1])