import sys
sys.setrecursionlimit(10000)

N = int(input())
arr = [list(input()) for _ in range(N)]

def dfs(ci, cj):
    v[ci][cj] = 1
    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = ci+di, cj+dj
        # 현재 좌표와 같은 색상인 영역 탐색
        if 0<=ni<N and 0<=nj<N and not v[ni][nj] and arr[ni][nj]==arr[ci][cj]:
            dfs(ni, nj)

def dfs_blue(ci, cj):
    v[ci][cj] = 1
    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = ci+di, cj+dj
        # 현재 좌표와 같은 색상인 영역 탐색
        if 0<=ni<N and 0<=nj<N and not v[ni][nj] and arr[ni][nj]=='B':
            dfs_blue(ni, nj)

def dfs_notBlue(ci, cj):
    v[ci][cj] = 1
    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = ci+di, cj+dj
        # 현재 좌표와 같은 색상인 영역 탐색
        if 0<=ni<N and 0<=nj<N and not v[ni][nj] and arr[ni][nj]!='B':
            dfs_notBlue(ni, nj)

cnt_1 = cnt_blue = cnt_notBlue = 0

for n in range(2):
    v = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if n==0 and not v[i][j]:
                dfs(i,j)
                cnt_1+=1
            elif n==1 and not v[i][j]:
                if arr[i][j]=='B':
                    dfs_blue(i, j)
                    cnt_blue += 1
                else:
                    dfs_notBlue(i, j)
                    cnt_notBlue += 1
print(cnt_1, cnt_blue+cnt_notBlue)