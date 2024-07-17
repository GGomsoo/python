N = int(input())    # 회원수
signup_user = []    # 입력한 회원들 정리할 리스트

for _ in range(N):
    age, name = input().split() # 회원정보 입력
    signup_user.append([int(age), name])    # 리스트에 저장

for i in sorted(signup_user, key=lambda x : x[0]):  # 나이를 기준으로 정렬 ( lambda 함수 활용 )
    print(i[0], i[1])   # 나이, 이름 순으로 출력


# 람다 써야한다.
# 람다 기억 안나고 잘 몰라서 구글링함