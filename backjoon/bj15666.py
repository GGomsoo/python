def solution(long, start):
    if long == M: # 수열 완성조건 맞췄다면
        print(*ans) # 언패킹하여 출력
        return
    else:
        use = 0 # 사용한 숫자인지 판별
        for i in range(start, N):
            if use != arr[i]: # 해당 숫자를 쓴 적 없다면
                use = arr[i] # 사용 표시
                ans.append(arr[i])
                solution(long + 1, i) # 현재 인덱스에서 다시 시작할 수 있도록 i값을 전달
                ans.pop()

N, M = map(int, input().split()) # 자연수 개수 N, 수열의 길이 M
arr = sorted(map(int, input().split())) # 주어진 자연수들을 오름차순으로 정렬
ans = [] # 함수를 돌면서, 완성된 수열을 담는다

solution(0, 0) # 초기 수열의 길이 0, 비내림차순에 필요한 for문 시작값 0