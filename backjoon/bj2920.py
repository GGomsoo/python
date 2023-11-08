# 음계
# 브론즈 II

# 다장조 c d e f g a b C
# c는 1로, 1부터 8까지로 변환
# 1부터 8까지 차례대로 연주 == ascending
# 8부터 1까지 차례대로 연주 == descending
# 둘 다 아니라면 == mixed

music = list(map(int, input().split()))

# 이 문제 sorted 사용하면 금방 풀리긴함.
ans = ''

# flag 사용
flag_asc = 0
flag_des = 0

for i in range(len(music)-1):
    # 1 2 3 4 5 6 7 8 일 때
    if music[i+1] == music[i] + 1:
        flag_asc = 1
    
    # 8 7 6 5 4 3 2 1 일 때
    elif music[i+1] == music[i] - 1:
        flag_des = 1

    # 이도저도 아닐 때
    else:
        flag_asc = 0
        flag_des = 0
        break

if flag_asc == 1 and flag_des == 0:
    ans = 'ascending'
elif flag_des == 1 and flag_asc == 0:
    ans = 'descending'
else:
    ans = 'mixed'

print(ans)