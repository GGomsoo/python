K = int(input()) # 관리하는 숫자의 갯수
lst = [] # 입력받는 숫자를 넣을 스택
lst2 = []

for _ in range(K):
    num = int(input()) # 숫자를 입력받고
    if num != 0: # 0이 아니면
        lst.append(num) # lst에 추가
    else: # 숫자가 0이면
        lst.pop() # 가장 최근에 쓴 수를 지운다

print(sum(lst))