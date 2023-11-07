# 대소문자 바꾸기
# 브론즈 V

# 단어 입력
word = input()

for i in word:
    # 대문자인지 판별하는 isupper()
    # 대문자면 소문자로 바꾸고 이어붙임
    if i.isupper():
        print(i.lower(), end='')
    # 대문자 아니면 (=소문자) 대문자로 변환후 이어붙임
    else:
        print(i.upper(), end='')