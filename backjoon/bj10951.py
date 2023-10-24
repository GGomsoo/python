# A+B -4
# 브론즈 V

# 실패
# A, B = map(int, input().split())
# print(A+B)

# try / except 사용하라하네?
while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break