# 수학, 구현, 정렬
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
import sys
from collections import Counter

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()

# 산술 평균
print(round(sum(arr) / N))

# 중앙값
print(arr[N // 2])

# 최빈값
# for i in arr:
#     lst[i] += 1
# print(lst.index(max(lst))) # 리스트에서 인덱스를 찾는 함수 'index'
arr2 = Counter(arr).most_common() # 최빈값 구하는 Counter
if len(arr2) > 1 and arr2[0][1] == arr2[1][1]: # 최빈값이 만약 2개인 경우에는
    print(arr2[1][0]) # 두번째로 작은 수를 출력
else:
    print(arr2[0][0])

# arr2를 print 하면 [(숫자, 빈도수), (숫자, 빈도수)] 형태로 나타난다
# 그래서, 빈도수가 2개 이상인 경우에는 두번째 작은 수를 출력해야 하니
# arr2[1][0]

# 최댓값과 최솟값의 차이
print(max(arr) - min(arr))