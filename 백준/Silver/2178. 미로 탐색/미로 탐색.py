def bfs(i,j):
    v=[[0]*M for _ in range(N)]
    q=[(i,j,1)]   # 시작위치 포함해서 카운트
    v[i][j]=1

    while q:
        ci,cj,d = q.pop(0)
        if ci==N-1 and cj==M-1:
            return d
        for di,dj in ((-1,0),(0,-1),(1,0),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and not v[ni][nj] and arr[ni][nj]==1:
                v[ni][nj]=d+1
                q.append((ni,nj,d+1))
    return

N,M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

print(bfs(0,0))