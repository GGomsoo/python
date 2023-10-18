# SWEA 2817 문제풀이4 - 부분 수열의 합 ( 9/1 )
'''
1
4 3
1 2 1 2
'''
# def 함수(depth, total):
#     global ans
#     # 재귀 종료 조건
#     if depth == N:
#         if total == K:
#             ans += 1
#             return
#
#     # 가지 치기
#     if total > K:
#         return
#
#     # 반복문
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = 1
#             함수(depth + 1, total + numbers[i])
#             visited[i] = 0
#
#
T = int(input())
for test1 in range(1, T+1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    ans = 0
    for i in range(1 << N):
        k = 0
        for j in range(N):
            if i & (1 << j):
                k += numbers[j]

        if k == K:
            ans += 1
    print(f"#{test1} {ans}")
