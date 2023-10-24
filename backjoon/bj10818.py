# 최소, 최대
# 브론즈 III

N = int(input())
numbers = list(map(int, input().split()))
print(min(numbers), max(numbers))

# 아래 코드 답이 아니라는데 왜지? 음?
# min_v = 1e12
# max_v = 0

# for i in range(N):
#     if numbers[i] < min_v:
#         min_v = numbers[i]

#     elif numbers[i] > max_v:
#         max_v = numbers[i]

# print(min_v, max_v)