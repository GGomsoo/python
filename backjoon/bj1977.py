M = int(input())
N = int(input())

# 오답코드
# # 완전 제곱수를 찾기 위해서, 주어진 M과 N에 루트를 씌움
# # M은 +1을 해줌. 정수화하면 뒷 소수점은 반올림이 아니라 날라간다
# # 예를 들어 M이 50인데, 그럼 7.~~~ 인데, int로 감싸면 7이 되기 때문에
# # 계산상에 문제가 생길 수 있다.
# m = int(M ** 0.5)
# n = int(N ** 0.5)

# lst = [] # 완전제곱수 리스트
# total = 0 # 그들의 합
# ans = 0 # 최소값

# for i in range(m, n+1): # lst에 제곱수들을 추가
#     lst.append(i)

# if lst: # 만약 리스트에 숫자가 있다면
#     for i in lst: # 여기서 리스트 안에 담긴 숫자는 제곱된 숫자가 아닌 제곱근
#         total += i ** 2 # 여기서 제곱을 해준다
#         ans = min(lst) ** 2 # 최소값도 마찬가지
#     print(total)
#     print(ans)

# else: # 숫자가 없으면 -1 출력
#     print(-1)

lst = [] # 완전제곱수 담을 리스트

for i in range(M, N+1): # M 부터 N 까지
    s = int(i ** 0.5) ** 2 # 여기서 i 값에 제곱근을 씌운 후, 다시 제곱한다
    if s == i: # 범위 내 완전제곱수가 있다면
        lst.append(i) # 리스트에 추가

if lst: # 리스트에 숫자가 있다면
    print(sum(lst)) # 리스트 내 완전제곱수 총합
    print(min(lst)) # 리스트 내 최솟값
else: # 숫자가 없다면
    print(-1) # -1 출력