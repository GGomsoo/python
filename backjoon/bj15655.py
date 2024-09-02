def solution(long, start, lst):
    if long == M: # 수열의 길이가 M과 동일하다면
        ans.append(lst) # 정답 list에 해당 수열을 추가
        return
    
    else:
        for i in range(start, N): # 시작값부터 N개까지
            if not visited[i]: # 사용한 적 없는 숫자라면
                visited[i] = 1 # 사용
                solution(long + 1, i + 1, lst + [arr[i]]) # 수열 길이 + 1, for문 시작값 + 1 (앞에 사용한 숫자는 더이상 X), 수열 추가
                visited[i] = 0 # return으로 돌아오면, 해당 숫자를 다시 쓸 수 있도록 사용표시를 0으로 초기화

N, M = map(int, input().split()) # N개의 자연수 중 M개를 고른 수열
arr = sorted(map(int, input().split())) # N개의 수를 오름차순으로 정렬
visited = [0] * N # 숫자를 썻는지에 대한 방문체크
ans = [] # 수열을 담을 list

solution(0, 0, []) # 수열의 길이, 중복 방지를 위한 for문 시작값, 초기 수열 (빈 값)

for i in ans:
    print(*i)