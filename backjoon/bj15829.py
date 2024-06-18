# Hashing
# 입력값은 알파벳 소문자
# 아스키코드로 변환이 point
# 소문자 a의 아스키코드는 97, 고유번호는 1번
# ord 함수를 통해 변환 후, 96을 뺀다

문자열길이 = int(input())
문자 = input()
r = 31
M = 1234567891
정답 = 0

for i in range(문자열길이):
    고유번호 = ord(문자[i]) - 96
    정답 += 고유번호 * ( r ** i)

print(정답 % M)