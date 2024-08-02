# 아스키코드 사용해야함 ord(문자) -> 숫자로 변환
# A는 65, a는 97
# 문제에서 a는 1, A는 27

words = input() # 문자 입력
total = 0 # 문자를 숫자화 한 총 값
flag = 1 # 소수 판별 flag

for i in words:
    if i.islower(): # 문자가 소문자인 경우
        total += ord(i) - 96
    else: # 대문자인 경우
        total += ord(i) - 38

# 에라토스테네스의 체
# 2부터 어떤 숫자의 제곱근까지에 대해서
for i in range(2, int(total**(0.5))+1):
    if total % i == 0:
        flag = 0
        break

if flag == 1:
    print("It is a prime word.")
else:
    print("It is not a prime word.")