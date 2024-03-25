from collections import deque

def bfs(i,j):
    global gram
    v = [[-1]*M for _ in range(N)]
    v[i][j] = 0
    q = deque([(i,j)])
    while q:
        ci,cj = q.popleft()

        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if not (0<=ni<N and 0<=nj<M): continue
            if v[ni][nj] != -1: continue
            if arr[ni][nj]==1: continue

            # 검 장착 => 공주까지 최단거리
            if arr[ni][nj] == 2:
                gram = v[ci][cj]+1 + abs(N-1-ni) + abs(M-1-nj)

            if (ni, nj) == (N-1, M-1):  # 공주 탈출
                return min(v[ci][cj] + 1, gram)

            v[ni][nj] = v[ci][cj] + 1
            q.append((ni, nj))

    return gram


N,M,T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
gram = 21e8
mn = bfs(0,0)

if mn > T : print('Fail')
else: print(mn)