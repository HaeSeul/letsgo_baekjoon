import sys
input = sys.stdin.readline
N,M = map(int, input().split())
lst = list(map(int, input().split()))
tmp = [0]*(N+1)

for i in range(1, N+1):
    tmp[i] = tmp[i-1]+ lst[i-1]

for _ in range(M):
    i, j = map(int, input().split())
    print(tmp[j]-tmp[i-1])