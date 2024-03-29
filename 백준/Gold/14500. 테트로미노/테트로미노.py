def dfs(sm,lst):
    global mx
    # 지금 sum에 지금 있는 lst*MAX 를 해도 mx보다 작으면 가지치기
    if sm + (4-len(lst))*MAX < mx: return

    if len(lst)==4:
        mx = max(mx, sm)
        return

    for ci,cj in lst:
        for d in range(4):
            ni,nj = ci+dir[d][0], cj+dir[d][1]
            if not (0<=ni<N and 0<=nj<M): continue
            if v[ni][nj]: continue
            v[ni][nj] = 1
            dfs(sm+arr[ni][nj], lst+[(ni,nj)])
            v[ni][nj] = 0

N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dir = ((-1,0),(0,1),(1,0),(0,-1))

MAX = max(map(max, arr))
mx = -1
v = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        v[i][j] = 1
        dfs(arr[i][j],[(i,j)])
        v[i][j] = 0
print(mx)