from collections import deque

def bfs(i,j):
    global mx_cnt, mx_rbw, mxi, mxj, mx_m
    v = [[0]*N for _ in range(N)]
    color = arr[i][j]
    v[i][j] = color
    q = deque([(i,j)])
    cnt, rainbow, mi, mj = 0, 0, 21e8, 21e8
    member = []
    while q:
        ci,cj = q.popleft()
        cnt += 1
        member.append((ci,cj))
        if arr[ci][cj] == color:
            (mi, mj) = min((mi, mj), (ci, cj))
        elif arr[ci][cj] == 0:
            rainbow += 1

        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if not (0<=ni<N and 0<=nj<N): continue
            if v[ni][nj]: continue
            if arr[ni][nj] == color or arr[ni][nj] == 0:
                done[ni][nj] = 1
                v[ni][nj] = color
                q.append((ni, nj))

    if cnt > 1:
        if (mx_cnt, mx_rbw, mxi, mxj) < (cnt, rainbow, mi, mj):
            (mx_cnt, mx_rbw, mxi, mxj) = max((mx_cnt, mx_rbw, mxi, mxj), (cnt, rainbow, mi, mj))
            mx_m = member

def gravity(arr):
    # 중력
    for col in range(N):
        for i in range(N - 1, 0, -1):
            if arr[i][col] == -1: continue
            for j in range(i - 1, -1, -1):
                if arr[j][col] == -1: break
                if arr[i][col] == -2 and arr[j][col] > -1:
                    arr[i][col], arr[j][col] = arr[j][col], arr[i][col]
    return arr

N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
score = 0

while True:
    mx_cnt, mx_rbw, mxi, mxj, mx_m = 0,0,0,0,[]
    done = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                if done[i][j]: continue
                done[i][j] = 1
                bfs(i,j)

    if not mx_m: break

    for i,j in mx_m:
        arr[i][j] = -2
    score += mx_cnt ** 2

    arr = gravity(arr)
    arr = list(map(list, zip(*arr)))[::-1]
    arr = gravity(arr)

print(score)