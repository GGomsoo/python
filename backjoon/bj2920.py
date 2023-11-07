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
for i in range(len(music)-1):
    if music[i+1] == music[i] + 1:
        ans = 'ascending'
    elif music[i+1] == music[i] - 1:
        ans = 'descending'
    else:
        ans = 'mixed'
print(ans)