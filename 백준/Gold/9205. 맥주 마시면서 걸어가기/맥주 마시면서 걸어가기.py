from collections import deque
import sys
input = sys.stdin.readline

def bfs(i,j):
    global ans
    q = deque()
    q.append((i,j))
    while q:
        ci, cj = q.popleft()
        if abs(ei-ci) + abs(ej-cj) <= 1000:
            return 'happy'
        for i in range(n):
            ni,nj = stores[i][0],stores[i][1]
            if abs(ni-ci)+abs(nj-cj) <= 1000 and not v[i]:
                q.append((ni,nj))
                v[i]=1
    return 'sad'

T = int(input())
for _ in range(T):
    n = int(input())
    si,sj = map(int, input().split())
    stores = [list(map(int, input().split())) for _ in range(n)]
    ei,ej = map(int, input().split())
    v = [0]*n
    print(bfs(si, sj))