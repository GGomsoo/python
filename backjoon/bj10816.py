import sys

N = int(input())
card_1 = sorted(map(int, sys.stdin.readline().split()))

M = int(input())
card_2 = list(map(int, sys.stdin.readline().split()))

# 답은 나오는데 시간초과
# ans = [0] * M

# for i in range(N):
#     for j in range(M):
#         if card_2[j] == card_1[i]:
#             ans[j] += 1

# for key in ans:
#     print(key, end=" ")

## 이분탐색 이용했지만, 중복된 숫자에 대해 누적을 못함
# ans_list = [0] * M

# def e_boon(start, end, key):
#     global ans_list

#     while start <= end:
#         if start > end:
#             break

#         mid = (start + end) // 2
#         if card_1[mid] == key:
#             ans_list[card_2.index(key)] += 1
#             return
        
#         elif card_1[mid] > key:
#             end = mid - 1
#         elif card_1[mid] < key:
#             start = mid + 1

# for key_point in card_2:
#     e_boon(0, N-1, key_point)

# for ans in ans_list:
#     print(ans, end=" ")

ans = {}

for key in card_1:
    if key in ans:
        ans[key] += 1
    else:
        ans[key] = 1

for key in card_2:
    if key in ans:
        print(ans[key], end=" ")
    else:
        print(0, end=" ")