import sys; input = sys.stdin.readline

def back(long, lst):
    if long == M: # 수열의 길이가 M과 같다면
        ans.append(lst) # 완성된 수열이라고 판단 후, 추가
        return # 이전 연산으로 돌아간다
    else:
        for i in range(N): # 자연수 개수 만큼 for문 진행
            back(long + 1, lst + [arr[i]]) # 수열의 길이 1증가, 기존 수열에 자연수들을 하나씩 붙인다
            # 같은 수를 여러번 골라도 된다 = 방문체크 할 필요 없다 라고 생각


N, M = map(int, input().split()) # 자연수 개수 N, 수열 길이 M
arr = sorted(map(int, input().split())) # N개의 자연수를 오름차순으로 정렬
ans = [] # 완성된 수열을 받을 리스트
back(0, []) # 초기 수열의 길이 0, 초기 빈 수열을 입력으로 시작

for i in ans:
    print(*i)