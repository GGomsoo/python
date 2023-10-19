# 윤년
# 브론즈 V
# 윤년은 연도가 4의 배수이면서 100배수가 아닐때 or 400의 배수


years = int(input())

if (years % 4 == 0 and years % 100 != 0) or years % 400 == 0:
    print(1)
else:
    print(0)