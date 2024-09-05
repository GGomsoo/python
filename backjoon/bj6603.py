def solution(long, start):
    if long == 6:
        print(*ans)
        return
    else:
        for i in range(start, N):
            if not visited[i]:
                visited[i] = 1
                ans.append(numbers[i])
                solution(long + 1, i + 1)
                ans.pop()
                visited[i] = 0


while True:
    S = list(map(int, input().split()))
    N = S[0]
    numbers = S[1:]
    visited = [0] * (N + 1)
    ans = []
    
    # 종료 조건
    if N == 0:
        break
    else:
        solution(0, 0)
        print()