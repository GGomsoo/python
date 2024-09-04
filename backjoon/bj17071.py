from collections import deque
import sys; input = sys.stdin.readline

def catch(subin, sister):
    visited[subin] = 1
    step = 1
    q = deque([(subin, sister)])

    while q:
        subin, sister = q.popleft()

        if sister > limit:
            return -1

        if subin == sister:
            return visited[subin] - 1
        
        # 동생 이동하는걸 어떻게 처리해야 하는가?
        else:
            for move_subin in (subin-1, subin+1, subin*2):
                if 0 <= move_subin <= limit:
                    if not visited[move_subin]:
                        visited[move_subin] = visited[subin] + 1
            
            sister += step
            step += 1
            q.append((move_subin, sister))



N, K = map(int, input().split())
limit = 500_000
visited = [0] * (limit + 1)
print(catch(N, K))