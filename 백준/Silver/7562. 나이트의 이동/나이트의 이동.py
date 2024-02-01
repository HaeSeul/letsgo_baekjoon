import sys
sys.setrecursionlimit(10**5)

di = [-1,-2,-2,-1,1,2,2,1]
dj = [-2,-1,1,2,2,1,-1,-2]

def bfs(i,j):
    v = [[0] * N for _ in range(N)]
    q = [(i,j,1)]
    v[i][j] = 1
    while q:
        ci, cj, dist = q.pop(0)
        if arr[ci][cj]==3:
            print(dist-1)
            break
        for d in range(8):
            ni,nj = ci+di[d], cj+dj[d]
            if 0<=ni<N and 0<=nj<N and not v[ni][nj]:
                v[ni][nj]=dist+1
                q.append((ni,nj,dist+1))

T = int(input())
for _ in range(T):
    N = int(input())
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())
    ans = 0

    # 시작점과 끝점이 다른 경우에만 탐색
    if si==ei and sj==ej:
        print(0)
    else:
        arr = [[0]*N for _ in range(N)]
        arr[si][sj] = 2
        arr[ei][ej] = 3
        bfs(si, sj)