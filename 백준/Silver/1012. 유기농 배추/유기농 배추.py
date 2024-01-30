T = int(input())
for _ in range(1, T+1):
    M, N, K = map(int, input().split())     # 가로, 세로, 배추위치개수
    arr = [[0]*M for _ in range(N)]
    v = [[0]*M for _ in range(N)]

    for _ in range(K):
        a,b = map(int, input().split())
        arr[b][a] = 1

    ans = 0
    for i in range(N):
        for j in range(M):
            # 배추가 있고 방문한 적이 없는 위치
            if arr[i][j] == 1 and not v[i][j]:
                ci, cj = (i,j)       # 현재위치
                s=[(ci, cj)]           # stk 초기화
                v[ci][cj]=1
                ans+=1        # 새로운 집합 탐색

                while s:
                    ci, cj=s.pop()
                    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                        ni, nj = ci+di, cj+dj
                        if 0<=ni<N and 0<=nj<M and not v[ni][nj]:
                            if arr[ni][nj] == 1:
                                s.append((ni, nj))
                                v[ni][nj]=1
    print(ans)