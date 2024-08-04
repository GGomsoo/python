import sys

N = int(sys.stdin.readline())

# 내장함수 round를 대체할 반올림 함수
def half_up(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

# 의견이 없는 경우
if N == 0:
    print(0)

# 의견이 있는 경우
else:
    lst = []
    for _ in range(N):
        lst.append(int(sys.stdin.readline())) # 의견들을 lst에 추가
    lst.sort() # 오름차순으로 정렬

    # 절사평균값을 반올림 함수에 넣은 후 값을 설정
    js = half_up(N * 0.15) 

    # 의견 모음 리스트에서, 절사평균값 만큼 앞, 뒤에서 갯수를 뺀 후
    # 남은 의견들을 더한 값에서
    # 절사평균값만큼 앞뒤 의견을 뺀 만큼의 길이만큼 나눈걸
    # 반올림 함수에 넣는다
    print(half_up(sum(lst[js:N-js]) / len(lst[js:N-js])))