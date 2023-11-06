# 배수와 약수
# 브론즈 III


while True:
    # 숫자 2개 A, B
    A, B = map(int, input().split())

    # A랑 B 둘 다 0 == break
    if A == 0 and B == 0:
        break

    # A가 B의 약수 == factor
    elif A < B and B % A == 0:
        print('factor')

    # A가 B의 배수 == multiple
    elif A > B and A % B == 0:
        print('multiple')

    # 둘 다 아님 == neither
    else:
        print('neither')