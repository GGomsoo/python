import sys

N = int(input())    # 수의 개수 N
num_list = []   # 숫자 담을 빈 리스트

for _ in range(N):  # 수의 개수만큼 반복하여 숫자 입력
    num = int(sys.stdin.readline())
    num_list.append(num)    # 비어있던 리스트에 숫자들을 추가

num_list.sort() # 정렬 후 리스트 내 숫자들을 출력
for i in num_list:
    print(i)


# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 수가 주어진다. 
# 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 
# 수는 중복되지 않는다.
# 숫자 범위가 크고, 시간 제한이 2초
# 일반 input 으로 받는게 아닌, 빠른 입력을 이용해야한다.