import sys
input = sys.stdin.readline

def upper():
    for i in range(a-2, -1, -1):
        arr[i+1][0] = arr[i][0]
    arr[0][:M-1] = arr[0][1:]
    for i in range(1, a+1):
        arr[i-1][M-1] = arr[i][M-1]
    arr[a][1:M] = [0]+arr[a][1:M-1]

def lower():
    for i in range(b+2, N):
        arr[i-1][0] = arr[i][0]
    arr[N-1][:M-1] = arr[N-1][1:M]
    for i in range(N-2, b-1, -1):
        arr[i+1][M-1] = arr[i][M-1]
    arr[b][1:M] = [0] + arr[b][1:M-1]

def spread(arr, dusts):
    # 미세먼지 확산
    new = [[0] * M for _ in range(N)]
    for dust in dusts:
        ci, cj = dust
        now = arr[ci][cj]
        cnt = 0
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < N and 0 <= nj < M): continue
            if arr[ni][nj] == -1: continue
            new[ni][nj] += now // 5
            cnt += 1
        new[ci][cj] += now - now // 5 * cnt
    new[a][0], new[b][0] = -1, -1
    return new


N,M,T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for t in range(T):
    m = []      # 공기청정기 위치
    dusts = []  # 먼지
    for i in range(N):
        for j in range(M):
            if not arr[i][j]: continue
            if arr[i][j] == -1:
                m.append(i)
            else:
                dusts.append((i, j))
    a, b = m[0], m[1]       # 공기청정기 a=위 / b=아래
    arr = spread(arr, dusts)
    upper()
    lower()

ans = 2
for l in arr:
    ans += sum(l)
print(ans)