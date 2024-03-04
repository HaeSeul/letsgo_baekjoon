from collections import deque

def bfs(si,sj):
    v = [[-1]*M for _ in range(N)]
    v[si][sj] = 0
    q = deque([(si,sj,0)])
    while q:
        ci,cj,cd = q.popleft()

        # 끝까지 도달한 경우
        if ci == N-1 and cj == M-1:
            return cd

        for d in range(4):
            ni,nj = ci+monkey[d][0], cj+monkey[d][1]
            if not (0 <= ni < N and 0 <= nj < M):   continue
            if arr[ni][nj]:     continue
            if v[ni][nj] == -1 or v[ni][nj] > v[ci][cj]:
                v[ni][nj] = v[ci][cj]
                q.append((ni, nj, cd + 1))

        if v[ci][cj] == K:  continue

        for d in range(8):
            ni,nj = ci+horse[d][0], cj+horse[d][1]
            if not (0 <= ni < N and 0 <= nj < M):   continue
            if arr[ni][nj]:     continue
            if v[ni][nj] == -1 or v[ni][nj] > v[ci][cj] + 1:
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj, cd + 1))
    return -1

K = int(input())
M,N = map(int, input().split())
horse = ((-1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2))
monkey = ((-1,0),(0,1),(1,0),(0,-1))
arr = [list(map(int, input().split())) for _ in range(N)]
print(bfs(0,0))