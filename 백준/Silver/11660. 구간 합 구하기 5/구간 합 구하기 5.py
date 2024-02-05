import sys
input = sys.stdin.readline

N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
tmp = [[0]*(N+1) for _ in range(N+1)]

# 구간합
for i in range(1, N+1):
    for j in range(1, N+1):
        tmp[i][j] = arr[i-1][j-1]+tmp[i-1][j]+tmp[i][j-1]-tmp[i-1][j-1]

for _ in range(M):
    si,sj,ei,ej = map(int, input().split())
    print(tmp[ei][ej] - tmp[si-1][ej] - tmp[ei][sj-1] + tmp[si-1][sj-1])