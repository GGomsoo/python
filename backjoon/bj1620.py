## 아래 코드는 시간 초과
# import sys

# N, M = map(int, sys.stdin.readline().split())

# poketmon_dict = [0]

# for i in range(1, N+1):
#     poketmon_dict.append(sys.stdin.readline().strip()) 

# for _ in range(M):
#     find_item = sys.stdin.readline().strip() 

#     if find_item.isdigit() == True: 
#         print(poketmon_dict[int(find_item)]) 
#     else: 
#         print(poketmon_dict.index(find_item)) 

import sys

N, M = map(int, sys.stdin.readline().split())

poketmon_name = {}
poketmon_num = {}

for i in range(1, N+1):
    poketmon = sys.stdin.readline().strip()
    poketmon_num[i] = poketmon
    poketmon_name[poketmon] = i

for _ in range(M):
    poketmon_info = sys.stdin.readline().strip()

    if poketmon_info.isdigit() == True:
        print(poketmon_num[int(poketmon_info)])
    else:
        print(poketmon_name[poketmon_info])


# 입력받는 포켓몬 정보를 list로 받으면 시간초과
# 빠른 입력을 사용하지 않고 일반 input을 사용하면 시간초과