import sys
input = sys.stdin.readline

def upper():    # 반시계
    for i in range(a-2, -1, -1):
        arr[i+1][0] = arr[i][0]
    arr[0][:M-1] = arr[0][1:]
    for i in range(1, a+1):
        arr[i-1][M-1] = arr[i][M-1]
    arr[a][1:M] = [0] + arr[a][1:M-1]   # 미세먼지 없는 바람 추가


def lower():    # 시계
    for i in range(b+2, N):
        arr[i-1][0] = arr[i][0]
    arr[N-1][:M-1] = arr[N-1][1:M]
    for i in range(N-2, b-1, -1):
        arr[i+1][M-1] = arr[i][M-1]
    arr[b][1:M] = [0] + arr[b][1:M-1]   # 미세먼지 없는 바람 추가


def spread(arr):
    # 미세먼지 확산
    new = [[0] * M for _ in range(N)]
    for ci in range(N):
        for cj in range(M):
            if arr[ci][cj] <= 0: continue
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

for i in range(N):
    if arr[i][0] == -1:
        a,b = i, i+1    # 공기청정기 a=위 / b=아래
        break

for t in range(T):
    arr = spread(arr)
    upper()
    lower()

ans = 2 + sum(map(sum, arr))
print(ans)