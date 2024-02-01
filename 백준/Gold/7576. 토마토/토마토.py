from collections import deque
import sys
input = sys.stdin.readline

def bfs(cnt):
    while q:
        ci,cj=q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and not v[ni][nj] and arr[ni][nj]==0:
                v[ni][nj]=v[ci][cj]+1
                q.append((ni,nj))
                cnt-=1
    if cnt>0:
        return -1
    else:
        return v[ci][cj]-1

M,N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]
q = deque()
cnt = 0

for i in range(N):
    for j in range(M):
        if arr[i][j]==1:        # 초기 1의 값 q에 모두 저장
            q.append((i,j))
            v[i][j] = 1
        elif arr[i][j]==0:
            cnt+=1
print(bfs(cnt))