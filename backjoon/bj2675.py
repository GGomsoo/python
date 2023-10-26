# 문자열 반복
# 브론즈 II
# 입력 문자열 들어오면 주어진 횟수만큼 문자 반복
# EX)3 ABC면 AAABBBCCC 나오게


T = int(input())

for _ in range(T):
    # 반복횟수R, 입력받을 문자열 abc
    # map 사용 안하고 input().split() 해도된다.
    R, abc = map(str, input().split())

    # 입력받은 문자열의 길이만큼
    for i in range(len(abc)):
        # 입력값 전부 문자열로 받았으니까
        # 반복횟수R 정수화 시킨 다음
        # 문자열 인덱스값으로 받아와서 하나하나 곱해주고
        # 이어붙임
        print(int(R) * abc[i], end='')
    # 줄바꿈
    # 이거 안해서 틀렸음
    print()
