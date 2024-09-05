def solution(long):
    if long == M:
        print(*ans)
        return
    
    else:
        use = 0
        for i in range(N):
            if use != arr[i]:
                use = arr[i]
                ans.append(arr[i])
                solution(long + 1)
                ans.pop()

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
ans = []
solution(0)