M, N, K = map(int, input().split())     # 세로, 가로, 직사각형개수
arr = [[0]*N for _ in range(M)]
v = [[0]*N for _ in range(M)]

for _ in range(K):
    j, i, nj, ni = map(int, input().split())
    for di in range(i, ni):
        for dj in range(j, nj):
            arr[di][dj]=1

size=[]
for i in range(M):
    for j in range(N):
        if arr[i][j]==0 and not v[i][j]:
            s = [(i,j)]     # 다시 시작되는 구간
            cnt=0
            while s:
                c = s.pop()
                if not v[c[0]][c[1]]:
                    v[c[0]][c[1]] = 1
                    cnt+=1
                    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                        ni, nj = c[0]+di, c[1]+dj
                        if 0<=ni<M and 0<=nj<N and not v[ni][nj]:
                            if arr[ni][nj]==0:
                                s.append((ni,nj))
            size.append(cnt)
print(len(size))
print(*sorted(size))