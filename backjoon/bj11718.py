# 그대로 출력하기
# 브론즈 V
# 안 떠올라서 구글 검색했는데 try ~ except 사용... 개에바

while True:
    try:
        word = input()
        print(word)
    except EOFError:
        break