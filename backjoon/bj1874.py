N = int(input()) # N까지의 수에 대한 입력

stack, ans, cnt, possible = [], [], 1, True # 수열, 정답, 카운팅, 수열 가능여부
# ans_stack = []

for i in range(N):
    num = int(input()) # 수열에 대한 숫자 입력

    while cnt <= num: # 카운팅한 숫자가 입력한 숫자보다 작거나 같을 경우동안 스택에 숫자 추가
        stack.append(cnt) # 수열 스택에 추가
        ans.append("+") # 정답 스택에 + 추가
        cnt += 1 # 카운팅 + 1

    # while 문 종료되면서 if 문 실행
    if stack[-1] == num: # 스택의 마지막 숫자가 입력한 숫자(완성해야하는 수열의 숫자)랑 같다면
        stack.pop() # 스택에서 숫자를 pop
        ans.append("-") # 정답 스택에 "-" 를 추가
        # ans_stack.append(num)

    else: # 그게 아니라면, 이 수열은 완성할 수 없다
        possible = False
        break

if not possible:
    print("NO")
else:
    for i in ans:
        print(i)