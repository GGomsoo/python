# 과제 안 내신 분..?
# 브론즈 V

# 학생 목록, 1번부터 30번까지
students = list(range(1, 31))

# 과제 한 친구들 명단 부른다
for _ in range(28):
    student = int(input())
    # 부른애는 명단에서 제외
    # append, pop 만 해봤지 remove될 줄 몰랐음
    students.remove(student)

# 안 부른 애 중 번호 가장 작은애
print(min(students))
# 번호 가장 큰애
print(max(students))