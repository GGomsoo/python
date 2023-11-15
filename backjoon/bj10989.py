# 수 정렬하기 3
# 브론즈 I
# N개의 수가 주어졌을 때, 오름차순으로 정렬

# 이런식으로 입력받는거 아직 미숙
# 이거 왜 안됌?
# import sys
# input = sys.stdin.readline()
#
# # 수의 개수 N개
# N = int(sys.stdin.readline())
# # 숫자 입력받을건데, 최댓값이 10000임.
# num_list = [0] * 10001
#
# for _ in range(N):
#     # 숫자 입력받고
#     num = int(sys.stdin.readline())
#     # 리스트에 그 숫자에 해당하는 인덱스에 +1
#     num_list[num] += 1
#
# # 0부터 10000까지
# for i in range(len(num_list)):
#     # 숫자가 담긴 리스트의 값이 0이 아니라면
#     if not num_list[i]:
#         # 리스트의 수 만큼 i 값을 반복 출력
#         for _ in range(num_list[i]):
#             print(i)

import sys
input = sys.stdin.readline()

# 왜 이렇게 해?
N = int(input)
num_list = [0] * 10001

for _ in range(N):
    # 왜 이렇게 해?
    num = int(sys.stdin.readline())
    num_list[num] += 1

for i in range(len(num_list)):
    for _ in range(num_list[i]):
        print(i)
