def solution(long, lst):
    if long == M: # 길이가 M과 같다면
        ans.append(lst)
        return # 이전 연산으로 돌아간다
    
    else:
        use = 0 # 넌 썻던 숫자니?
        for i in range(N): # 자연수 개수만큼 for문 진행
            if not visited[i] and use != arr[i]: # 사용한 적 없는 숫자라면
                visited[i] = 1 # 사용
                use = arr[i] # 'arr[i]' 숫자는 사용했다. 라고 표시
                # ans.append(arr[i])
                solution(long + 1, lst + [arr[i]]) # 수열 길이 1 증가, 수열에 해당 자연수를 추가
                # ans.pop()
                visited[i] = 0 # return 되어 돌아올 때, 썻던 숫자를 다른 환경에서 쓸 수 있도록 초기화

N, M = map(int, input().split()) # 자연수 개수 N, 수열의 길이 M자
arr = sorted(map(int, input().split())) # N개의 자연수들
visited = [0] * N # 중복사용 방지
ans = [] # 완성된 수열이 들어올 list
solution(0, []) # 초기 수열의 길이 0, 빈 수열 []

for i in ans:
    print(*i)