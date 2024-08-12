ans = []

# 7개의 자연수
for _ in range(7):
    num = int(input())

    # 홀수만 리스트에 담기
    if num % 2 != 0:
        ans.append(num)

# 리스트에 홀수가 있으면, 홀수들의 합과 최소값을 출력
if len(ans) != 0:
    print(sum(ans))
    print(min(ans))
    
# 없으면 -1 출력
else:
    print(-1)