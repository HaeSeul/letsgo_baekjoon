from collections import deque

def OOB(i,j): return not (0<=i<N and 0<=j<M)

def bfs(i,j,B):
    v = [[0]*M for _ in range(N)]
    v[i][j] = 1
    q = deque([(i,j)])
    C = 1
    while q:
        ci,cj = q.popleft()
        for di,dj in dir:
            ni,nj = ci+di, cj+dj
            if OOB(ni,nj): continue
            if v[ni][nj]: continue
            if arr[ni][nj] != B: continue
            C += 1
            v[ni][nj] = 1
            q.append((ni,nj))
    return C

dir = ((0,1),(1,0),(0,-1),(-1,0))

N,M,K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
score = 0

# 주사위 오른쪽부터 이동
i,j = 0,0
d = 0
dice = [2,1,5,6,4,3]

for _ in range(K):
    B,U,F,D,L,R = dice[0],dice[1],dice[2],dice[3],dice[4],dice[5]
    # 현재 방향으로 주사위 한 칸 굴러감
    ni,nj = i+dir[d][0], j+dir[d][1]
    # 그 방향에 칸이 없으면
    if OOB(ni,nj):
        # 방향 반대로 바꿔서 다음 한 칸 굴러감
        d = (d+2)%4
        ni,nj = i+dir[d][0], j+dir[d][1]
    i,j = ni,nj
    if d==0:
        U,D,L,R = L,R,D,U
    elif d==1:
        B,U,F,D = D,B,U,F
    elif d==2:
        U,D,L,R = R,L,U,D
    else:
        B,U,F,D = U,F,D,B
    dice = [B,U,F,D,L,R]

    # 도착칸 점수 획득 = B * C
    B = arr[i][j]
    # 현재 칸 숫자B와 같은 수 연속되는 개수 C
    C = bfs(i,j,B)
    score += B*C

    # 주사위 아랫면 숫자A와 칸에 있는 숫자B 비교해 방향 결정
    A = dice[3]

    # A > B : 시계90
    if A > B : d = (d+1)%4
    # A < B : 반시계90
    elif A < B : d = (d-1)%4

# 각 이동에서 획득하는 점수 합
print(score)