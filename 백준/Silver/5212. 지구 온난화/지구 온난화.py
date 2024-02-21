# 각 섬을 둘러싸는 바다의 개수
def count(ci,cj):
    cnt = 0
    for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
        ni,nj = ci+di, cj+dj
        if 0<=ni<N+2 and 0<=nj<M+2:
            if arr[ni][nj]=='.':
                cnt += 1
        if cnt >= 3:
            return True
    return False

N,M=map(int, input().split())
arr = [['.']*(M+2)]+[list('.'+ input().rstrip()+ '.') for _ in range(N)]+[['.']*(M+2)]
land = []
mx_i, mx_j, mn_i, mn_j = 0,0,N+2,M+2

# 각 섬 탐색
for i in range(1,N+1):
    for j in range(1,M+1):
        if arr[i][j] == 'X':
            # 주변에 바다가 3개 이상이라면 바다에 잠김
            if count(i,j):
                land.append((i,j))
            else:
                mx_i, mx_j = max(mx_i,i), max(mx_j,j)
                mn_i, mn_j = min(mn_i,i), min(mn_j,j)
# 바다에 잠김
for i,j in land:
    arr[i][j] = '.'

for i in range(mn_i,mx_i+1):
    for j in range(mn_j,mx_j+1):
        print(arr[i][j], end='')
    print()