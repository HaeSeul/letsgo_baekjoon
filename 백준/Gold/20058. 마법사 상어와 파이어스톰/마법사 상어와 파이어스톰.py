from collections import deque

def OOB(i,j):
    return not (0<=i<2**N and 0<=j<2**N)

def turn(arr, L):
    new = [[0]*(2**N) for _ in range(2**N)]
    for r in range(0, 2**N, 2**L):
        for c in range(0, 2**N, 2**L):  # 격자 시작점

            tmp = [[0]*(2**L) for _ in range(2**L)]
            for i in range(2**L):
                for j in range(2**L):
                    tmp[i][j] = arr[r+i][c+j]

            tmp = list(map(list, zip(*tmp[::-1])))

            for i in range(2**L):
                for j in range(2**L):
                    new[r+i][c+j] = tmp[i][j]
    return new

def reduce(arr):
    new = [l[::] for l in arr]
    for i in range(2**N):
        for j in range(2**N):
            if not arr[i][j]: continue
            cnt = 0
            for di,dj in dir:
                ni,nj = i+di, j+dj
                if OOB(ni,nj): continue
                if arr[ni][nj]: cnt += 1
            if cnt < 3:
                new[i][j] -= 1
    return new

def find_unit(i,j):
    cnt = 1
    v[i][j] = cnt
    q = deque([(i,j)])
    while q:
        ci,cj = q.popleft()
        for di,dj in dir:
            ni,nj = ci+di, cj+dj
            if OOB(ni,nj): continue
            if v[ni][nj] : continue
            if not arr[ni][nj]: continue
            cnt += 1
            v[ni][nj] = cnt
            q.append((ni,nj))
    return cnt


N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**N)]
dir = ((-1,0),(0,1),(1,0),(0,-1))

mx = 0
cmd = map(int, input().split())
for L in cmd:
    arr = turn(arr, L)
    arr = reduce(arr)

v = [[0]*(2**N) for _ in range(2**N)]
for i in range(2 ** N):
    for j in range(2 ** N):
        if not arr[i][j]: continue
        if v[i][j]: continue
        mx = max(mx, find_unit(i,j))

print(sum(map(sum, arr)))
print(mx)