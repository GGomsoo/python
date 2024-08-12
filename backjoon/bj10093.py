import sys
input = sys.stdin.readline

A, B = map(int, input().split())

if A < B:
    print(B-A-1)
    for i in range(A+1, B):
        print(i, end=" ")
if B < A:
    print(A-B-1)
    for i in range(B+1, A):
        print(i, end=" ")
if A == B:
    print(0)

# a랑 b의 크기만 비교하고, 같은 경우를 고려하지 않아서 틀렸었다.