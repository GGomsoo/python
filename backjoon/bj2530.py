# 시 분 초
H, M, S = map(int, input().split())
cooking = int(input())

S = S + cooking
if S >= 60:
    M += S // 60
    S %= 60

    if M >= 60:
        H += M // 60
        M %= 60

        if H >= 24:
            H %= 24

print(H, M, S)