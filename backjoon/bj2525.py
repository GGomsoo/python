# 오븐 시계
# 브론즈 III

now_h, now_m = map(int, input().split())
need_time = int(input())
add_time = now_m + need_time

# 기존의 시간에 요리에 필요한 시간을 더했을 때
# 60분이 넘어간다면?
if add_time >= 60:
    # now_h 에 더한시간을 60으로 나눈 몫을 추가
    now_h += add_time // 60
    # 두 분을 더한 값에서 60을 빼버림
    add_time -= 60 * (add_time // 60)
    # 만약 위에서 계산한 now_h가 24라면?
    # 디지털 시계는 24시를 00시로 표현
    if now_h >= 24:
        now_h -= 24

print(now_h, add_time)

# 1회차 제출 - 실패
# 24시 넘어가는걸 설정했어야 했는데
# 그냥 24시면 0으로 설정해버림. 25시 26에 대한걸 생각하지 않았음

# 2회차 제출 - 실패
# 분 계산하는 부분에서 잘못함

# 3회차 제출 - 실패
# 분 출력하는 부분 계산 잘못함