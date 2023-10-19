# SWEA 11780 응용 구현 06 그래프의 기본과 탐색 - 그룹 나누기
# 양방향 그래프다.
'''
3
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4
'''
def 함수(v):
    # 출석체크
    visited[v] = 1
    # Q에 출석번호를 넣고
    Q = [v]
    
    while Q:
        # Q에서 출석번호를 pop
        v = Q.pop(0)
        
        # v를 찍은 사람들 중
        for w in adj[v]:
            # 출석체크 안되어있다면
            if not visited[w]:
                # 출석체크 완료 ( 팀 생성 )
                visited[w] = 1
                # Q에 새로운 출석번호를 넣는다
                Q.append(w)
                

T = int(input())
for test1 in range(1, T+1):
    # 출석번호 N, 신청서 M장
    N, M = map(int, input().split())
    # M 쌍의 번호
    arr = list(map(int, input().split()))
    # 인접 리스트
    adj = [[] for _ in range(N+1)]
    # 방문체크
    visited = [0] * (N+1)
    
    # 인접 리스트에 값 추가
    for i in range(M):
        s, g = arr[i*2], arr[i*2+1]
        adj[s].append(g)
        adj[g].append(s)
    
    # 몇 개의 조 나타낼 ans
    ans = 0
    # 1번부터 출석번호 끝까지
    for i in range(1, N+1):
        # 누가 부른적 없다면
        if not visited[i]:
            # 팀 1개 생성
            ans += 1
            # 함수 호출
            함수(i)
            
    print(f"#{test1} {ans}")
