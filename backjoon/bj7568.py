N = int(input()) # 인원수
people = [] # 인원 정보 넣을 리스트
rates = [] # 덩치 등수 넣을 리스트

for _ in range(N): # 인원수 만큼 for문 반복
    W, H = map(int, input().split()) # 몸무게, 키 정보 입력
    people.append([W, H]) # 인원 정보 리스트에 추가

for i in range(N): # 인원수들 덩치 비교
    rate = 1 # 덩치 등수 기본값 1로 설정
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rate += 1 # 나보다 큰 사람이 있으면 + 1
    rates.append(rate) # 덩치 등수 리스트에 추가

for i in rates:
    print(i, end=" ")