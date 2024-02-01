from collections import deque
import sys
sys.setrecursionlimit(10**5)

def isFull(arr):
    tmp=0
    for l in arr:
        tmp+=l.count(1)+l.count(-1)
    return tmp==N*M


def bfs():
    while q:
        ci,cj,d=q.popleft()
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and not v[ni][nj] and arr[ni][nj]==0:
                v[ni][nj]=1
                q.append((ni,nj,d+1))
    if isFull(v):
        return d-1
    return -1


M,N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]
q = deque()

if isFull(arr):
    print(0)
else:
    for i in range(N):
        for j in range(M):
            if arr[i][j]==-1:       # v에 arr의 -1 복사하기
                v[i][j]=-1
            if arr[i][j]==1:        # 초기 1의 값 q에 모두 저장
                q.append((i,j,1))
                v[i][j] = 1
    print(bfs())