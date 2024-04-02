N,M,T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(T):
    X,D,K = map(int, input().split())

    for i in range(N):
        if (i+1)%X != 0: continue   # X의 배수인 원만

        for _ in range(K):
            if D == 0:
                arr[i] = [arr[i][-1]] + arr[i][:-1]
            else:
                arr[i] = arr[i][1:] + [arr[i][0]]

    nothing = True
    new = [l[:] for l in arr]
    sm, cnt = 0, 0
    for i in range(N):
        for j in range(M):
            if not arr[i][j]: continue
            sm += arr[i][j]
            cnt += 1
            for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
                ni,nj = i+di, (j+dj)%M
                if not (0<=ni<N): continue
                if not arr[ni][nj]: continue
                if arr[i][j] == arr[ni][nj]:
                    new[i][j], new[ni][nj] = 0,0
                    nothing = False
    if nothing and cnt:
        mean = sm/cnt
        for i in range(N):
            for j in range(M):
                if not new[i][j]: continue
                if new[i][j] > mean: new[i][j] -= 1
                elif new[i][j] < mean: new[i][j] += 1

    arr = new

print(sum(map(sum, arr)))