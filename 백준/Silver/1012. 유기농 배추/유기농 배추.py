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
                c = (i,j)       # 현재위치
                s=[c]           # stk 초기화
                ans+=1        # 새로운 집합 탐색

                while s:
                    c=s.pop()
                    v[c[0]][c[1]]=1
                    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                        ni, nj = c[0]+di, c[1]+dj
                        if 0<=ni<N and 0<=nj<M and not v[ni][nj]:
                            if arr[ni][nj] == 1:
                                s.append((ni, nj))
    print(ans)