N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]
dp[0][0] = arr[0][0]    # 초기값

for i in range(N):
    for j in range(M):
        if i==0 and j==0:   continue
        mx=0
        for di,dj in ((0,-1),(-1,-1),(-1,0)):
            ni,nj=i+di,j+dj
            if 0<=ni<N and 0<=nj<M:
                mx = max(mx, dp[ni][nj])
        dp[i][j] = mx + arr[i][j]

print(dp[N-1][M-1])