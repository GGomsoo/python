N = int(input()) # 통화한 갯수
call = list(map(int, input().split())) # 통화한 시간

youngsik, minsik = 0, 0

# 영식
for i in call:
    if i < 30:
        youngsik += 10
    else:
        youngsik += (10 + 10 * (i // 30))

# 민식
for i in call:
    if i < 60:
        minsik += 15
    else:
        minsik += (15 + 15 * (i // 60))

# 영식이 요금제가 저렴한 경우
if youngsik < minsik:
    print(f"Y {youngsik}")

# 민식이 요금제가 저렴한 경우
elif youngsik > minsik:
    print(f"M {minsik}")

# 두 요금제 요금이 같은 경우
else:
    print(f"Y M {youngsik}")