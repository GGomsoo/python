# 영수증
# 브론즈 IV

# 영수증에 적힌 총액
total = int(input())
# 물건 갯수
N = int(input())

ans = 0
for _ in range(N):
    # 물건의 가격과 갯수 입력
    cost, unit = map(int, input().split())
    # ans에 누적
    ans += cost * unit

# 영수증 총액과 ans가 같으면 yes, 다르면 no
if total == ans:
    print('Yes')
else:
    print('No')