def shark_move(arr):
    new = [[list() for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not arr[i][j]: continue
            s, dr, size = arr[i][j].pop()  # (속력, 방향, 크기)

            ci, cj = i, j
            move = s
            while move:  # move 만큼 이동
                ni, nj = ci + dir[dr][0], cj + dir[dr][1]
                if not (0 <= ni < N and 0 <= nj < M):  # 경계 넘어가면 방향 바꾸기
                    if dr % 2 == 0: dr -= 1
                    else:           dr += 1
                ci, cj = ci + dir[dr][0], cj + dir[dr][1]
                move -= 1

            # 바뀐 위치에 다른 상어가 있다면 내가 클 때만 추가
            if new[ci][cj]:
                if new[ci][cj][0][2] < size:
                    new[ci][cj].pop()  # 기존 상어 먹기
                    new[ci][cj].append([s, dr, size])
            else:
                new[ci][cj].append([s, dr, size])
    return new


N,M,K = map(int, input().split())
arr = [[list() for _ in range(M)] for _ in range(N)]
dir = ((0,0),(-1,0),(1,0),(0,1),(0,-1))   # 1상 2하 3우 4좌
for _ in range(K):
    n,m,s,d,z = map(int, input().split())
    if d==1 or d==2:
        s = s % ((N-1)*2)
    else:
        s = s % ((M-1)*2)
    arr[n-1][m-1].append([s, d, z])     # (속력, 방향, 크기)

score = 0

# 열만큼 낚시꾼 이동
for col in range(M):
    # 가장 가까이 있는 상어 잡기
    row = 0
    while row < N:
        if arr[row][col]: break
        row += 1
    if row < N and arr[row][col]:
        catch = arr[row][col].pop()     # 상어 잡기
        score += catch[2]

    # 상어 이동
    arr = shark_move(arr)

print(score)