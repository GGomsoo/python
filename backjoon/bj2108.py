# 수학, 구현, 정렬
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()

lst = [0] * (max(arr)+1)
# 산술 평균
print(sum(arr) // N)

# 중앙값
print(arr[N // 2])

# 최빈값
for i in arr:
    lst[i] += 1
print(lst.index(max(lst))) # 리스트에서 인덱스를 찾는 함수 'index'

# 최댓값과 최솟값의 차이
print(max(arr) - min(arr))