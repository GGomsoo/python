N = int(input())
end_num = 666 # 종말의 숫자
end_num_cnt = 0 # 종말의 숫자 카운트
start_num = 0 # 시작 숫자

while(True): # while 문 진행동안
    if str(end_num) in str(start_num): # 시작 숫자 안에 종말의 숫자가 포함되어 있다면
        end_num_cnt += 1 # 카운트 + 1
        if N == end_num_cnt: # 그 카운트랑 입력한 숫자 N이랑 같으면
            break # while 문 종료
    start_num += 1

print(start_num)