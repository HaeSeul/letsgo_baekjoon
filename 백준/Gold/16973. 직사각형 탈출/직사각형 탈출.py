from collections import deque

def check(ni,nj,d):   # 상우하좌
    if d==0:
        if ni < 0 or nj+C > M: return False
        for c in range(C):
            if arr[ni][nj+c] == 1: return False
    elif d==1:
        if ni+R > N or nj+C > M: return False
        for r in range(R):
            if arr[ni+r][nj+C-1] == 1: return False
    elif d==2:
        if ni+R > N or nj+C > M: return False
        for c in range(C):
            if arr[ni+R-1][nj+c] == 1: return False
    elif d==3:
        if ni+R > N or nj < 0: return False
        for r in range(R):
            if arr[ni+r][nj] == 1: return False
    return True

def bfs(i,j):
    v = [[0] * M for _ in range(N)]
    v[i][j] = 1
    q = deque([(i,j)])
    while q:
        ci,cj = q.popleft()
        for d in range(4):
            ni, nj = ci + dir[d][0], cj + dir[d][1]
            if not (0 <= ni < N and 0 <= nj < M): continue
            if v[ni][nj]: continue
            if check(ni, nj, d):
                if ni==ei-1 and nj==ej-1:
                    return v[ci][cj]
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni,nj))
    return -1

N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
R,C,si,sj,ei,ej = map(int, input().split())
dir = ((-1,0),(0,1),(1,0),(0,-1))
print(bfs(si-1, sj-1))