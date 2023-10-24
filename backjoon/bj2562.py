# 최댓값
# 브론즈 III

# 숫자 넣을 빈 리스트
number_list = []

# 숫자 9개래
for _ in range(9):
    # 숫자 입력하자
    number = int(input())
    # 리스트에 추가
    number_list.append(number)
# 리스트 내에서 최댓값 출력
print(max(number_list))

# 최댓값 인덱스로 쓸 변수 하나 설정
max_idx = 0
# 9개 숫자중에서
for i in range(9):
    # 최댓값 찾으면서
    if number_list[max_idx] < number_list[i]:
        # 인덱스값 할당
        max_idx = i
# 몇 번째 숫자냐고 했으니까 인덱스값 +1
print(max_idx + 1)