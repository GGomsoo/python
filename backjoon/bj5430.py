from collections import deque

T = int(input()) # test case 개수

for _ in range(T):
    P = input() # 수행할 함수 p
    N = int(input()) # 배열의 길이
    arr = input().strip() # 정수가 들어있는 배열 ( [1,2,3,4] 형태 )
    q = deque((arr[1:-1].split(","))) # 배열 내 숫자만 추가하기 위한 파싱

    if N == 0:
        q = deque([])

    flag = 1 # q가 비었는지 확인용
    r_cnt = 0 # R이 나온 횟수
    for order in P:
        if order == "R": # 함수 R이 들어오면
            r_cnt += 1 # 횟수 + 1
        
        if order == "D": # D가 들어오면
            if q: # q에 내용물이 있으면서
                if r_cnt % 2 == 0: # 뒤집은 횟수가 짝수 == 제자리
                    q.popleft() # 맨 처음 내용물을 뺀다
                else:
                    q.pop()
            else: # q에 내용물이 없으면
                print("error") # error 출력
                flag = 0 # q가 비었다는 표시
                break # 진행종료
    
    if flag:
        if r_cnt % 2 == 0: # 뒤집은 횟수가 짝수라면 그대로 출력. 왜냐면 짝수번 뒤집으면 결과는 똑같기 때문
            print("[" + ",".join(q) + "]")
        else: # 뒤집은 횟수가 홀수라면
            q.reverse() # 뒤집어서 출력한다
            print("[" + ",".join(q) + "]")