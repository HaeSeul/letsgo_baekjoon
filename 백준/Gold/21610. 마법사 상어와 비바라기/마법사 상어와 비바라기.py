N,M = map(int, input().split())
dir = ((0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1))  # 1,3,5,7: 대각선
arr = [list(map(int, input().split())) for _ in range(N)]
nxt = [[0]*N for _ in range(N)]
for i,j in ((N, 1), (N, 2), (N-1, 1), (N-1, 2)):
    nxt[i-1][j-1] = 1

for _ in range(M):
    d,s = map(int, input().split())
    d -= 1

    # 구름 이동 : now 배열에 새롭게 추가
    now = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not nxt[i][j]: continue
            nxt[i][j] = 0
            ni,nj = (i+dir[d][0] * s)%N, (j+dir[d][1] * s)%N
            now[ni][nj] = 1
            arr[ni][nj] += 1    # now 배열을 기준으로 물 내리기

    # now 배열 기준으로 물복사버그
    arr_copy = [l[::] for l in arr]
    for i in range(N):
        for j in range(N):
            if not now[i][j]: continue
            cnt = 0
            for nd in (1,3,5,7):
                ni,nj = i+dir[nd][0], j+dir[nd][1]
                if not (0<=ni<N and 0<=nj<N): continue
                if not arr[ni][nj]: continue
                cnt += 1
            arr_copy[i][j] += cnt
    arr = arr_copy

    # 2 이상인 곳
    for i in range(N):
        for j in range(N):
            if now[i][j]: continue
            if arr[i][j] < 2: continue
            nxt[i][j] = 1
            arr[i][j] -= 2

print(sum(map(sum, arr)))