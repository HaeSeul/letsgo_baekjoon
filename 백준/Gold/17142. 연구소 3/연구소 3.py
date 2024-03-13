from collections import deque

def bfs(v,q):
    global mn
    time = 0
    change = 0
    while q:
        ci,cj = q.popleft()
        if arr[ci][cj]!=2:
            time = max(time, v[ci][cj]-1)
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if arr[ni][nj]==1:  continue
            if v[ni][nj]:       continue
            if arr[ni][nj]==0:
                change += 1
            v[ni][nj] = v[ci][cj] + 1
            q.append((ni,nj))
    return time, change


def combination(n,s):
    global cnt, mn
    if n==M:

        v = [[0] * (N+2) for _ in range(N+2)]
        q = deque()

        for i,j in choose:
            v[i][j] = 1
            q.append((i,j))

        time, change = bfs(v, q)

        # 다 못 바꾸면 -1
        if cnt != change:
            time = -1
        if time != -1:
            mn = min(mn, time)
        return

    for x in range(s, len(virus)):
        choose.append(virus[x])
        combination(n+1, x+1)
        choose.pop()


N,M = map(int, input().split())
arr = [[1]*(N+2)]
virus = []
cnt = 0     # 빈 칸 개수
mn = 21e8   # 최소시간

for i in range(1,N+1):
    arr.append([1]+list(map(int, input().split()))+[1])
    for j in range(1,N+1):
        if arr[i][j]==2:
            virus.append((i,j))
        elif arr[i][j]==0:
            cnt += 1
arr.append([1]*(N+2))

# virus 중 M개 뽑기
choose = []
combination(0,0)

if mn == 21e8:
    print(-1)
else:
    print(mn)