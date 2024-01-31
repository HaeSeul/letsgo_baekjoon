import sys
sys.setrecursionlimit(10000)
N = int(input())
arr = [input() for _ in range(N)]

def dfs(ci, cj):
    v[ci][cj] = 1
    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = ci+di, cj+dj
        # 현재 좌표와 같은 색상인 영역 탐색
        if 0<=ni<N and 0<=nj<N and not v[ni][nj] and arr[ni][nj]==arr[ci][cj]:
            dfs(ni, nj)

for _ in range(2):
    v = [[0] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if not v[i][j]:
                dfs(i,j)
                cnt+=1
    print(cnt, end=' ')

    # 적록색약이 아닌 경우 출력 후 R->G
    for i in range(N):
        arr[i] = arr[i].replace('R', 'G')