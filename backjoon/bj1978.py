# 소수 찾기

# 숫자의 갯수
N = int(input())

# 숫자들
numbers = map(int, input().split())

# 정답(소수의 갯수)
ans = 0

# 숫자들 중에서
for num in numbers:
    # 소수 판별 변수
    not_sosu = 0

    # 소수찾기 시작
    if num > 1:

        # 2부터 num-1까지에 대해
        for i in range(2, num):
            # num을 i로 나눈 나머지가 0이면
            if num % i == 0:
                # 넌 소수가 아니다.
                not_sosu += 1
        
        if not_sosu == 0:
            ans += 1

print(ans)