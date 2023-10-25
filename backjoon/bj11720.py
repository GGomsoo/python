# 숫자의 합
# 브론즈 IV

# 숫자의 갯수
N = int(input())
# 숫자를 문자열로 입력받음
numbers = input()

ans = 0
# 숫자 갯수동안 for문 돌면서
for i in range(N):
    # 입력받은 숫자 문자열을 인덱스값 이용하면서 ans에 정수형태로 누적
    ans += int(numbers[i])

print(ans)