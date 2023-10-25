# 나머지
# 브론즈 II

# 수 10개 입력받는다
N = 10

# 10개 숫자 나눠서 나머지가 동일한 값이 나오면
# 1개
ans = 1

# 입력받은 숫자를 42로 나눈 값을 넣을 리스트
num_42_list = []

for _ in range(N):
    # 10개 숫자 입력
    number = int(input())
    # 숫자 42로 나눔
    num_42 = number % 42
    # 리스트에 넣음
    num_42_list.append(num_42)
    # 정렬해버림
    num_42_list.sort()
    
# 리스트의 길이 동안 for문 돌려버림
for i in range(len(num_42_list)-1):
    # 나머지값이 다르면
    if num_42_list[i] != num_42_list[i+1]:
        # 정답에 1씩 누적
        ans += 1
        
print(ans)