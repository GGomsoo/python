# 브론즈 V
# A+B -8
'''
5
1 1
2 3
3 4
9 8
5 2
'''
T = int(input())
for test1 in range(1, T+1):
    A, B = map(int, input().split())
    print(f"Case #{test1}: {A} + {B} = {A+B}")