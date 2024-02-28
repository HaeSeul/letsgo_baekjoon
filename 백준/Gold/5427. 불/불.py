from collections import deque

def spread():
    while fire:
        ci,cj = fire.popleft()
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if not (0<=ni<N and 0<=nj<M): continue
            if arr[ni][nj]=='#': continue
            if t[ni][nj]:   continue
            t[ni][nj] = t[ci][cj] + 1
            fire.append((ni,nj))

def move(si,sj):
    v = [[0]*M for _ in range(N)]
    v[si][sj] = 1
    q = deque([(si,sj)])
    while q:
        ci,cj = q.popleft()
        if ci == 0 or ci == N - 1 or cj == 0 or cj == M - 1:
            if arr[ci][cj] == '.' or arr[ci][cj] == '@':
                return v[ci][cj]
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if not (0<=ni<N and 0<=nj<M): continue
            if arr[ni][nj]=='#': continue
            if v[ni][nj]:   continue
            if not t[ni][nj] or t[ni][nj] > v[ci][cj]+1:
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni,nj))

    return 'IMPOSSIBLE'

T = int(input())
for _ in range(T):
    M,N = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    t = [[0] * M for _ in range(N)]   # 불 퍼지는 시간
    fire = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j]=='@':
                si,sj = i,j
            elif arr[i][j]=='*':
                fire.append((i,j))
                t[i][j] = 1

    spread()    # 불 퍼지기
    print(move(si,sj))