# 사분면 고르기
# 브론즈 V

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
if x < 0 and y > 0:
    print(2)
if x < 0 and y < 0:
    print(3)
if x > 0 and y < 0:
    print(4)