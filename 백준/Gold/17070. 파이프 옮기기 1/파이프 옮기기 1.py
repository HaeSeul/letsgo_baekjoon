def dfs(s,ci,cj):       # 0:가로, 1:세로, 2:대각선
    global ans
    if ci==N-1 and cj==N-1:   # 마지막에 다다른 경우
        ans += 1
        return

    # 각 모양일 때 확인
    if s==0 or s==2:        # 가로, 대각선 -> 가로
        if arr[ci][cj+1]==0:
            dfs(0, ci, cj+1)

    if s==1 or s==2:      # 세로, 대각선 -> 세로
        if arr[ci+1][cj]==0:
            dfs(1, ci+1, cj)

    # 모든 경우 -> 대각선 가능
    if arr[ci][cj+1]==0 and arr[ci+1][cj]==0 and arr[ci+1][cj+1]==0:
        dfs(2, ci+1, cj+1)


N = int(input())
arr = [list(map(int, input().split())) + [1] for _ in range(N)] + [[1]*(N+1)]
ans = 0

dfs(0, 0, 1)    # 현재모양 : 가로, 현재머리 : (0,1)

print(ans)