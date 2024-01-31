import sys
sys.setrecursionlimit(10**5)

N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]
cnt = [0]
hour = 0

def cheese_count(arr):
    cheese = 0
    for i in arr:
        cheese += i.count(1)
    return cheese

def find(x):            # arr, v 모두 x인 곳
    for i in range(N):
        for j in range(M):
            if arr[i][j]==x and v[i][j]==x:
                return i, j

def dfs(ci, cj, x, y):        # i, j, 찾을숫자, 바꿀숫자
    v[ci][cj]=y
    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = ci+di, cj+dj
        if 0<=ni<N and 0<=nj<M and not v[ni][nj] and arr[ni][nj]==x:
            dfs(ni,nj,0,2)


while True:
    cheese = cheese_count(arr)
    if cheese == 0:
        print(hour)
        print(cnt[-1])
        break
    hour += 1
    cnt.append(cheese)

    ci,cj = find(0)     # 0의 위치 찾기
    dfs(ci,cj,0,2)      # 연속되는 0 -> 2로 마킹

    # 2로 둘러싸인 1 -> 0로 바꾸기 (녹은 치즈)
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and not v[i][j]:
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 2:
                        arr[i][j] = 0
                        v[i][j] = 1
                        break
    v = [[0]*M for _ in range(N)]