# 괄호
# 올바른 괄호 문자열 판별하기
# 괄호의 짝이 다 맞으면 yes, 아니면 no

T = int(input())

my_stack = []

for _ in range(T):
    brackets = input() # 괄호 입력

    for i in brackets: # 입력한 괄호문에 대해
        if i == "(": # 왼쪽 괄호면
            my_stack.append(i) # 스택에 추가
        
        if i == ")": # 오른쪽 괄호면
            if len(my_stack) != 0 and my_stack[-1] == "(": # 스택 비어있지 않으면서, 스택의 가장 끝에 있는게 왼쪽 괄호면
                my_stack.pop() # 빼버리기
            else: # 그게 아니면 스택에 추가
                my_stack.append(i)
    
    if len(my_stack) == 0: # 스택이 비어있다 == 올바른 괄호 문자열
        print("YES")
    else:
        print("NO")
    
    my_stack.clear() # 확인 후, 다음 tc를 위해서 스택을 비워주기