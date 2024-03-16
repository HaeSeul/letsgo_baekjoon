from collections import deque

def bfs():
    v = [list(l) for l in arr[::]]
    time = 0
    while q and time < S:
        for _ in range(len(q)):
            ci,cj = q.popleft()
            for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
                ni,nj = ci+di, cj+dj
                if not (0<=ni<N and 0<=nj<N): continue
                if v[ni][nj]: continue
                v[ni][nj] = v[ci][cj]
                q.append((ni,nj))
        time += 1
    return v[X-1][Y-1]


N,K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S,X,Y = map(int, input().split())

tmp = []
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            tmp.append((arr[i][j], i,j))
# 바이러스 번호순 정렬
tmp.sort(key = lambda x: x[0])
# q에 작은 바이러스부터 넣기
q = deque()
for i in range(len(tmp)):
    q.append((tmp[i][1], tmp[i][2]))
print(bfs())