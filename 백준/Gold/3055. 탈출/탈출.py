import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while water or hedge:
        # 물 먼저
        for _ in range(len(water)):
            wi, wj = water.popleft()
            for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
                ni,nj = wi+di, wj+dj
                if arr[ni][nj] == 'X': continue
                if arr[ni][nj] == 'D': continue
                if not v[ni][nj] == -1: continue
                v[ni][nj] = v[wi][wj] + 1
                water.append((ni,nj))

        # 고슴도치 이동
        for _ in range(len(hedge)):
            hi, hj = hedge.popleft()
            for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
                ni,nj = hi+di, hj+dj
                if arr[ni][nj] == 'X': continue
                if arr[ni][nj] == 'D': return v[hi][hj] + 1
                if not v[ni][nj] == -1: continue
                v[ni][nj] = v[hi][hj] + 1
                hedge.append((ni,nj))
    return 'KAKTUS'

N,M = map(int, input().split())
arr = [['X']*(M+2)]+[['X'] + list(input().rstrip())+['X'] for _ in range(N)] + [['X']*(M+2)]
v = [[-1] * (M+2) for _ in range(N+2)]
water = deque()
hedge = deque()
for i in range(1, N+1):
    for j in range(1, M+1):
        if arr[i][j] == 'S':
            hedge.append((i,j))
            arr[i][j] = '.'
            v[i][j] = 0
        elif arr[i][j] == '*':
            water.append((i,j))
            arr[i][j] = '.'
            v[i][j] = 0
print(bfs())