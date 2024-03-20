from collections import deque

def bfs(i,j):
    v = [[0]*M for _ in range(N)]
    v[i][j] = 1
    q = deque([(i,j)])
    C = 1   # 나 포함 세기
    while q:
        ci,cj = q.popleft()
        for di, dj in dir:
            ni,nj = ci+di, cj+dj
            # 범위, 방문, 나랑 같은 값인지 체크
            if not (0 <= ni < N and 0 <= nj < M): continue
            if v[ni][nj]: continue
            if arr[ni][nj] != arr[i][j]: continue
            C += 1
            v[ni][nj] = 1
            q.append((ni,nj))
    return C


N,M,K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
score = 0

dir = ((0,1),(1,0),(0,-1),(-1,0))   # 우0 하1 좌2 상3
idx = {0:[0,4,2,5,3,1], 1:[3,0,1,2,4,5], 2:[0,5,2,4,1,3], 3:[1,2,3,0,4,5]}
d = 0
ci,cj = 0,0
dice = [2,1,5,6,4,3]

for k in range(K):
    ni,nj = ci+dir[d][0], cj+dir[d][1]

    # 범위 밖이면 반대로 한 칸 굴러감
    if not (0<=ni<N and 0<=nj<M):
        d = (d+2)%4
        ni, nj = ci + dir[d][0], cj + dir[d][1]

    tmp = [0] * 6
    for i in range(6):
        tmp[i] = dice[idx[d][i]]
    dice = tmp

    # 도착 칸 점수 획득
    B = arr[ni][nj]
    C = bfs(ni,nj)
    score += B * C

    # 방향 바꾸기
    A = dice[3]
    if A > B:   d = (d+1)%4
    elif A < B: d = (d-1)%4

    ci,cj = ni,nj
print(score)