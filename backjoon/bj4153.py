# 직각삼각형
# 브론즈 III

# # 실패
# # c가 가장 큰 수가 아닐수도 있음.
# # 입력을 list로 받아야 할 듯

# while True:
#     # 숫자 3개 입력
#     a, b, c = map(int, input().split())

#     # 0 0 0이 들어오면 멈춘다 == 마지막 줄
#     if (a==0) and (b==0) and (c==0):
#         break

#     else:
#         # 피타고라스 법칙 = a**2 + b**2 = c**2
#         # 직각 삼각형이 맞으면 right
#         if a**2 + b**2 == c**2:
#             print('right')

#         # 아니면 wrong
#         else:
#             print('wrong')


while True:
    # 숫자 list로 입력받음
    nums = list(map(int, input().split()))
    # 크기순대로 정렬
    nums.sort()

    # 다 0이면 break
    if nums[0] == 0  and nums[1] == 0 and nums[2] == 0:
        break

    # 0은 아닌데
    else:
        # 1번숫자 제곱 + 2번숫자 제곱이 3번숫자 제곱이랑 같으면
        # 직각 삼각형
        if nums[0]**2 + nums[1]**2 == nums[2]**2:
            # right 출력
            print('right')
            
        # 아니면 wrong출력
        else:
            print('wrong')