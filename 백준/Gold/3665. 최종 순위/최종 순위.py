import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
for _ in range(T):
    N = int(input())
    last = [0] + list(map(int, input().split()))

    adj = [list() for _ in range(N+1)]
    dir = [[0]*(N+1) for _ in range(N+1)]   # dir[x][y] : x -> y
    indeg = [0]*(N+1)

    for i in range(1, N):
        x = last[i]
        for j in range(i+1, N+1):
            y = last[j]
            adj[x].append(y)
            dir[x][y] = 1
            indeg[y] += 1

    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        if dir[a][b]:
            adj[b].append(a)
            dir[a][b], dir[b][a] = 0, 1
            indeg[a] += 1
            indeg[b] -= 1
        else:
            adj[a].append(b)
            dir[a][b], dir[b][a] = 1, 0
            indeg[a] -= 1
            indeg[b] += 1

    ans = []
    q = deque()
    for i in range(1, N+1):
        if indeg[i] == 0:
            q.append(i)
            ans.append(i)

    while q:
        now = q.popleft()
        for nxt in adj[now]:
            if not dir[now][nxt]: continue
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
                ans.append(nxt)

    if q or len(ans)!= N:
        print('IMPOSSIBLE')
    else:
        print(*ans)
