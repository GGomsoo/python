# SWEA 11874 종이붙이기
'''
3
30
50
70
'''
def 함수(N):
    global ans
    n = N // 10
    memo = [0] * (n+1)
    memo[0] = memo[1] = 1
    # memo[2] = 3 = memo[1] + memo[0] * 2
    # memo[3] = 5 = memo[2] + memo[1] * 2
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2] * 2
    ans = memo[i]
    # return memo[i]으로 작성하고
    # print(f"#{test1} {함수(N)}") 으로 작성해도 정답 나온다.


T = int(input())
for test1 in range(1, T+1):
    N = int(input())
    ans = 0
    함수(N)
    print(f"#{test1} {ans}")
