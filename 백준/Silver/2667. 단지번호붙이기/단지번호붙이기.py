import sys
from collections import deque
input = sys.stdin.readline

def bfs(si,sj):
    # 첫 요소 방문 처리
    v[si][sj]=1
    q=deque([(si,sj)])
    num=1
    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and not v[ni][nj] and arr[ni][nj]==1:
                v[ni][nj] = num+1
                q.append((ni,nj))
                num+=1
    return num


N = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
v = [[0] * N for _ in range(N)]

cnt=[]
for i in range(N):
    for j in range(N):
        if arr[i][j]==1 and not v[i][j]:
            cnt.append(bfs(i,j))

cnt.sort()

print(len(cnt))
[print(cnt[i]) for i in range(len(cnt))]