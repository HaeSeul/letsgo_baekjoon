N,M = map(int, input().split())
ci,cj,d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dir = ((-1,0),(0,1),(1,0),(0,-1))
cnt = 0

while True:
    # [ 1 ] 현재 칸이 청소되지 않은 경우, 청소하기
    if arr[ci][cj] == 0:
        arr[ci][cj] = 2
        cnt += 1

    # [ 3 ] 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    for i in range(4, -1, -1):
        # 반시계 90 회전
        nd = (d+i-1) % 4
        ni,nj = ci + dir[nd][0], cj + dir[nd][1]
        if arr[ni][nj]==0:
            ci,cj = ni,nj
            d = nd
            break

    # [ 2 ] 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    else:
        ci,cj = ci - dir[d][0], cj - dir[d][1]
        if arr[ci][cj]==1:  # 벽인 경우 stop
            break

print(cnt)