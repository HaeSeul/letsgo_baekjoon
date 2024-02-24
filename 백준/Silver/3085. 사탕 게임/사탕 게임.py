# 행에서 가장 긴 연속 부분
def max_row(ci):
    mx_col=0
    for i in range(0,N):
        col=1
        for j in range(i+1,N):
            if arr[ci][i] != arr[ci][j]: break
            col+=1
        mx_col = max(mx_col, col)
    return mx_col

# 열에서 가장 긴 연속 부분
def max_col(cj):
    mx_row=0
    for i in range(0,N):
        row=1
        for j in range(i+1,N):
            if arr[i][cj] != arr[j][cj]: break
            row+=1
        mx_row = max(mx_row, row)
    return mx_row


N = int(input())
arr = [list(input()) for _ in range(N)]
dir = ((0, 1), (1, 0))

# [ 1 ] 기존 arr에서 가장 긴 연속부분 찾기
mx = 0
for i in range(N):
    mx = max(mx, max_row(i))
for j in range(N):
    mx = max(mx, max_col(j))

# [ 2 ] arr을 순회하며 우/하와 다르다면 위치 바꾸기
for i in range(N):
    for j in range(N):
        for d in range(2):
            ni,nj = i+dir[d][0], j+dir[d][1]
            if not (0<=ni<N and 0<=nj<N): continue
            if arr[i][j] == arr[ni][nj]:   continue
            
            # 위치 바꾸기
            arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]

            # 우측과 바꿨다면 (동일행:i, 2개열:j/nj 탐색)
            if d==0:
                mx = max(mx, max_row(i), max_col(j), max_col(nj))
            # 아래와 바꿨다면 (2개행:i/ni, 동일열:j 탐색)
            else:
                mx = max(mx, max_row(i), max_row(ni), max_col(j))

            # 위치 되돌리기
            arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]

print(mx)