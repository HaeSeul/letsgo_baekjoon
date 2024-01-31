M, N, K = map(int, input().split())     # 세로, 가로, 직사각형개수
arr = [[0] * M for _ in range(N)]
v = [[0] * M for _ in range(N)]

for _ in range(K):
    i, j, ni, nj = map(int, input().split())
    for di in range(i, ni):
        for dj in range(j, nj):
            arr[di][dj]=1

size=[]
for i in range(N):
    for j in range(M):
        if arr[i][j]==0 and not v[i][j]:
            # 초기화
            ci, cj = i, j
            s = [(ci,cj)]    # 첫 요소 stack에 추가
            v[ci][cj]=1      # 첫 요소 먼저 방문
            cnt=1

            while s:
                for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    ni, nj = ci+di, cj+dj
                    if 0<=ni<N and 0<=nj<M and not v[ni][nj]:
                        if arr[ni][nj]==0:
                            s.append((ni,nj))
                            v[ni][nj] = 1
                            cnt += 1
                            break
                else:
                    ci, cj = s.pop()
            size.append(cnt)
print(len(size))
print(*sorted(size))