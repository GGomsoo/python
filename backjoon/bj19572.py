# A와 B에 동시에 뿌리는 비의 양 d1
# A와 C에 동시에 뿌리는 비의 양 d2
# B와 C에 동시에 뿌리는 비의 양 d3

d1, d2, d3 = map(int, input().split())

A = (d1 + d2 - d3) / 2
B = d1 - A
C = d2 - A

# 조건에 맞게 비를 내릴 수 있다 == 각 구역에 대한 비의 양이 0보다 크다
if A > 0 and B > 0 and C > 0:
    print(1)
    print(round(A, 1), round(B, 1), round(C, 1)) # 소수 첫째 자리까지 반올림
else:
    print(-1)