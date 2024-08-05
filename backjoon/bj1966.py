from collections import deque

tc = int(input())

for _ in range(tc):
    N, M = map(int, input().split()) # 문서의 개수, 문서가 현재 몇번째에 놓여있는지
    q_impt = deque(list(map(int, input().split()))) # 문서들의 중요도
    marking = deque(list(i for i in range(N))) # 내가 원하는 서류의 순서를 기억하기 위한 lst
    marking[M] = "ans" # 원하는 서류의 순서에 "ans"라고 표시
    my_turn = 0

    while True:
        if q_impt[0] == max(q_impt): # Q의 가장 앞에 있는 문서의 중요도가 제일 큰 경우
            my_turn += 1 # 순서 + 1

            if marking[0] == "ans": # 그 앞에 있는 서류가 정답인 경우
                print(my_turn) # 내 순서가 몇번째인지 출력 후 while문 닫기
                break
            else:
                q_impt.popleft() # 정답이 아니라면 계속 뺀다
                marking.popleft()
        
        else:
            # 가장 앞에 있는 문서의 중요도가 제일 큰 경우가 아니라면, Q의 맨 뒤로 보낸다
            q_impt.append(q_impt.popleft()) 
            marking.append(marking.popleft())