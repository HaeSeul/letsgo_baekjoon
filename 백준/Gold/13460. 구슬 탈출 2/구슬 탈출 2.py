def tilt(d, i, j, color):       # d로 기울였을 때 가능한 위치 (0:red, 1:blue)
    dist = 0
    ni,nj = i+dir[d][0], j+dir[d][1]
    while arr[ni][nj]=='.' or arr[ni][nj]=='O':
        if arr[ni][nj]=='O':
            if color == 0:      # red가 구멍 만난 경우
                return dist + 1
            else:               # blue가 구멍 만난 경우
                return -1
        ni,nj = ni+dir[d][0], nj+dir[d][1]
        dist += 1
    # (ri+dir[d][0]*dist, rj+dir[d][1]*dist)
    return dist


def dfs(n, ri, rj, bi, bj, now_d):  # r/b의 현재위치, 회전방향
    global ans
    # 종료조건
    if arr[ri][rj] == 'O':
        ans.add(n)
        return
    if n == 10:     # 10까지 왔는데 빨간 구슬이 못 간 경우
        if arr[ri][rj] != 'O':
            ans.add(21e8)
        return


    for d in range(4):
        # 현재 방향과 다른 방향만 탐색
        if d == now_d: continue

        # b의 방향으로 구슬이 없는 경우만 탐색
        b_dist = tilt(d, bi, bj, 1)
        if b_dist == -1: continue

        b_ni, b_nj = bi + dir[d][0] * b_dist, bj + dir[d][1] * b_dist
        r_dist = tilt(d, ri, rj, 0)
        r_ni, r_nj = ri + dir[d][0] * r_dist, rj + dir[d][1] * r_dist

        if d == 0:
            # 0) 오른쪽 기울이기
            if ri == bi and r_nj == b_nj:  # 같은 행에 같은 지점인데
                if rj < bj:  # blue가 오른쪽이라면 red를 한 칸 왼쪽으로
                    dfs(n + 1, r_ni, r_nj - 1, b_ni, b_nj, 0)
                else:  # red가 더 오른쪽이라면 blue를 한 칸 왼쪽으로
                    dfs(n + 1, r_ni, r_nj, b_ni, b_nj - 1, 0)
            else:
                dfs(n + 1, r_ni, r_nj, b_ni, b_nj, 0)

        elif d == 1:
            # 1) 아래쪽 기울이기
            if rj == bj and r_ni == b_ni:  # 같은 열에
                if ri < bi:  # blue가 아래라면 red를 한 칸 위으로
                    dfs(n + 1, r_ni - 1, r_nj, b_ni, b_nj, 1)
                else:  # red가 더 아래라면 blue를 한 칸 위로
                    dfs(n + 1, r_ni, r_nj, b_ni - 1, b_nj, 1)
            else:
                dfs(n + 1, r_ni, r_nj, b_ni, b_nj, 1)

        elif d == 2:
            # 2) 왼쪽으로 기울이기
            if ri == bi and r_nj == b_nj:  # 같은 행에
                if rj < bj:  # red가 왼쪽이라면 blue를 한 칸 오른쪽으로
                    dfs(n + 1, r_ni, r_nj, b_ni, b_nj + 1, 2)
                else:  # blue가 더 왼쪽이라면 red를 한 칸 오른쪽으로
                    dfs(n + 1, r_ni, r_nj + 1, b_ni, b_nj, 2)
            else:
                dfs(n + 1, r_ni, r_nj, b_ni, b_nj, 2)

        else:
            # 3) 위로 기울이기
            if rj == bj and r_ni == b_ni:  # 같은 열에
                if ri < bi:  # red가 더 위라면 blue를 한 칸 아래로
                    dfs(n + 1, r_ni, r_nj, b_ni + 1, b_nj, 3)
                else:  # blue가 위라면 red를 한 칸 아래로
                    dfs(n + 1, r_ni + 1, r_nj, b_ni, b_nj, 3)
            else:
                dfs(n + 1, r_ni, r_nj, b_ni, b_nj, 3)



N,M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
dir = ((0,1),(1,0),(0,-1),(-1,0))       # 우 하 좌 상
ans = set()
end = 0

ri,rj,bi,bj = 0,0,0,0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            ri,rj = i,j
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            bi,bj = i,j
            arr[i][j] = '.'

dfs(0,ri,rj,bi,bj,-1)

mn = min(ans)
if mn == 21e8:
    print(-1)
else:
    print(mn)