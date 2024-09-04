def solution(long, start, lst):
    if long == M:
        ans.append(lst)
        return
    
    else:
        use = 0 # 중복사용 방지
        for i in range(start, N):
            if not visited[i] and use != arr[i]:
                visited[i] = 1
                use = arr[i]
                solution(long + 1, i + 1, lst + [arr[i]])
                visited[i] = 0

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
visited = [0] * N
ans = []

solution(0, 0, []) # 초기 수열의 길이, 비내림차순을 위한 for문 시작 범위, 초기 수열

for i in ans:
    print(*i)