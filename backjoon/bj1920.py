N = int(input())
A_list = set(map(int, input().split()))
M = int(input())
B_list = list(map(int, input().split()))

for i in B_list:
    print(1) if i in A_list else print(0)

# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 
# 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 
# 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

# 1차 시도, 그냥 for 문 돌려서 시간초과
# 2차 시도, A_list를 입력 받을 때, sorted로 선언 후 진행했는데 시간초과
# 3차 시도, set 함수를 사용하여 성공