def check_cross(i,j,x):
    for d in range(9):
        if x==arr[i][d] or x==arr[d][j]:
            return False
    return True

def check_box(i,j,x):
    refi, refj = i//3 * 3, j//3 * 3
    for di in range(refi, refi+3):
        for dj in range(refj, refj+3):
            if arr[di][dj]==x:
                return False
    return True

def dfs(n):
    global flag
    if n==len(blank):   # 모든 빈 칸을 다 채웠다면 끝
        for l in arr:
            print(*l)
        flag=1
        return

    # 제일 첫 답 나오면 끝
    if flag:    return

    ci,cj = blank[n][0], blank[n][1]
    for x in range(1,10):
        if check_cross(ci,cj,x) and check_box(ci,cj,x):
            arr[ci][cj]=x
            dfs(n+1)    # 다음 숫자 탐색
            arr[ci][cj]=0


arr=[list(map(int, input().split())) for _ in range(9)]
flag = 0

# 채워야하는 곳 저장
blank = []
for i in range(9):
    for j in range(9):
        if arr[i][j]==0:
            blank.append((i,j))

# 첫번째 채워야하는 곳부터 시작
dfs(0)