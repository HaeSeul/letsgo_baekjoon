N = int(input())
arr=[list(map(int, input().split())) for _ in range(N)]
mx = 0

# 최대, 최소 높이 구하기
mx_h, mn_h = 1, 100
for i in range(N):
    for j in range(N):
        mx_h= max(mx_h, arr[i][j])
        mn_h= min(mn_h, arr[i][j])

for rain in range(mn_h-1, mx_h+1):
    cnt = 0
    v = [[0] * N for _ in range(N)]     # rain 마다 visited 갱신

    for i in range(N):
        for j in range(N):

            # rain 보다 큰 첫 값 구하기
            if arr[i][j]>rain and v[i][j]==0:
                cnt += 1
                s = [(i, j)]
                v[i][j] = 1
                # rain 보다 큰 영역 탐색
                while s:
                    ci, cj = s.pop()
                    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                        ni, nj = ci+di, cj+dj
                        if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj]>rain:
                            s.append((ni,nj))
                            v[ni][nj]=1
                mx = max(mx, cnt)
print(mx)