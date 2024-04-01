def upper():
    # 위쪽 청정기 돌리기
    for i in range(a-1, 0, -1):
        arr[i][0] = arr[i-1][0]
    arr[0] = arr[0][1:] + [arr[1][M-1]]
    for i in range(1, a):
        arr[i][M-1] = arr[i+1][M-1]
    arr[a][1:] = [0] + arr[a][1:M-1]

def lower():
    # 아래쪽 청정기
    for i in range(b+1, N-1):
        arr[i][0] = arr[i+1][0]
    arr[N-1] = arr[N-1][1:] + [arr[N-2][M-1]]
    for i in range(N-1, b, -1):
        arr[i][M-1] = arr[i-1][M-1]
    arr[b][1:] = [0] + arr[b][1:M-1]


N,M,T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 청정기 위치 찾기
a, b = 0,0
for i in range(N):
    if arr[i][0] == -1:
        a,b = i, i+1
        break

for _ in range(T):
    # 미세먼지 확산
    new = [[0]*M for _ in range(N)]
    new[a][0] = new[b][0] = -1
    for i in range(N):
        for j in range(M):
            if not arr[i][j] or arr[i][j] == -1: continue
            cnt = 0
            spread = arr[i][j] // 5
            for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
                ni,nj = i+di, j+dj
                if not (0<=ni<N and 0<=nj<M): continue
                if arr[ni][nj] == -1: continue
                new[ni][nj] += spread
                cnt += 1
            new[i][j] += arr[i][j] - spread * cnt
    arr = new

    upper()
    lower()

ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] > 0:
            ans += arr[i][j]
print(ans)