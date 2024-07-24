import sys

N, M = map(int, input().split())
my_site = {}

for _ in range(N):
    site, pwd = sys.stdin.readline().split()
    my_site[site] = pwd

for _ in range(M):
    find_site = sys.stdin.readline().rstrip()
    print(my_site[find_site])