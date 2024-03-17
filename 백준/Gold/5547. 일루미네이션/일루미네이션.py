import sys
input = sys.stdin.readline
from collections import deque

def bfs(i,j):
    global cnt
    q = deque([(i,j)])
    while q:
        ci,cj = q.popleft()
        if ci % 2 == 1:  # 홀수 행
            for d in range(2, 8):
                ni, nj = ci + dir[d][0], cj + dir[d][1]
                if not (0<=ni<N+2 and 0<=nj<M+2): continue
                if v[ni][nj]: continue
                if arr[ni][nj] == 1:
                    cnt += 1
                    continue
                v[ni][nj] = 1
                q.append((ni,nj))
        else:
            for d in range(0, 6):
                ni, nj = ci + dir[d][0], cj + dir[d][1]
                if not (0<=ni<N+2 and 0<=nj<M+2): continue
                if v[ni][nj]: continue
                if arr[ni][nj] == 1:
                    cnt += 1
                    continue
                v[ni][nj] = 1
                q.append((ni, nj))


M,N = map(int, input().split())
arr = [[0]*(M+2)] + [[0]+list(map(int, input().split()))+[0] for _ in range(N)] + [[0]*(M+2)]
v = [[0]*(M+2) for _ in range(N+2)]

# 4방탐색 : 2~5, j 홀수 : 2~7, j 짝수 : 0~5
dir = ((-1,-1),(1,-1),(-1,0),(0,1),(1,0),(0,-1),(-1,1),(1,1))

cnt = 0
bfs(0,0)
print(cnt)