def back(long, start, lst):
    if long == M: # 목표 수열의 길이에 도달하면
        ans.append(lst) # 완성된 수열을 list에 담는다
        return # 이전 연산으로 돌아간다
    else:
        # 비내림차순 = 11 17 18 19 77 78 79 88 89 99
        # 같은 수를 사용해도 된다 = 방문체크 X
        for i in range(start, N): # 초기 start의 값은 0
            # for문 진행할 땐, 77과 같이 같은 숫자를 사용하여 수열을 완성
            # 수열 길이 +1, 같은 수 사용해도 되기 때문에 0, 수열에 자연수 중 하나 추가
            back(long + 1, start, lst + [arr[i]])
            
            # 수열 완성됐을 때, return 되면서 for문의 시작 범위를 1 증가
            start += 1 
            

N, M = map(int, input().split()) # 자연수 개수 N, 수열 길이 M
arr = sorted(map(int, input().split())) # 자연수들을 오름차순으로 정렬하여 받는다
ans = [] # 완성된 수열을 담을 list
back(0, 0, []) # 초기 수열의 길이, for문 시작 범위, 초기 수열

# ans에 담긴 수열들을 언패킹하면서 출력
for i in ans:
    print(*i)