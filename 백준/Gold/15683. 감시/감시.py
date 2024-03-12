def dfs(n, arr):
    global mn
    if n == len(cctv):  # 모든 cctv 다 뽑으면 종료
        # 사각지대 개수 갱신
        cnt = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j]==0: cnt += 1
        mn = min(mn, cnt)
        return

    arr_copy = [list(l) for l in arr[::]]

    cn, ci, cj = cctv[n]
    # 각 번호의 회전횟수만큼
    for x in range(len(d[cn])):
        # '#' 넣기
        arr_copy = look(arr_copy, x, cn, ci, cj)
        # 바뀐 arr_copy로 dfs
        dfs(n+1, arr_copy)
        # arr_copy 돌려주기
        arr_copy = [list(l) for l in arr[::]]


def check(ni,nj):   # 범위, 벽 체크
    if not (0 <= ni < N and 0 <= nj < M): return 0
    if arr[ni][nj] == 6: return 0
    return 1


def look(arr_copy,x,n,i,j):
    for k in d[n][x]:
        di,dj = dir[k]
        ni,nj = i+di, j+dj
        while True:
            if not check(ni, nj): break
            if arr_copy[ni][nj]==0:
                arr_copy[ni][nj] = '#'
            ni, nj = ni + di, nj + dj

    return arr_copy


N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dir = ((-1,0),(0,1),(1,0),(0,-1))
d = [[],
     [[0],[1],[2],[3]],
     [[0, 2], [1, 3]],
     [[0, 1], [1, 2], [2, 3], [3, 0]],
     [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
     [[0, 1, 2, 3]]]

cctv = []
for i in range(N):
    for j in range(M):
        if arr[i][j] in (1, 2, 3, 4, 5):
            cctv.append((arr[i][j], i, j))  # (cctv num, 좌표)
mn = 21e8
dfs(0,arr)
print(mn)