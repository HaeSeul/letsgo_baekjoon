def dfs(op, n, i, j, cnt, v):  # 움직일 방향, n번 이동, 상어위치, 물고기개수
    global mx_fish
    if n == 3:  # 3번 이동하면 끝
        mx_fish.append((cnt, op))  # 물고기개수, 사전순 방향
        return

    sd = op[n]  # 움직일 방향
    ni, nj = i + dir_s[sd][0], j + dir_s[sd][1]
    # 범위 밖이라면 불가능
    if not (0 <= ni < 4 and 0 <= nj < 4): return

    if v[ni][nj]:  # 방문했던 곳이면 카운트 X (중복)
        dfs(op, n + 1, ni, nj, cnt, v)
    else:
        v[ni][nj] = 1
        dfs(op, n + 1, ni, nj, cnt + len(arr[ni][nj]), v)


arrow = {0:'←', 1:'↖', 2:'↑', 3:'↗', 4:'→', 5:'↘', 6:'↓', 7:'↙'}
arrow_idx = {v:k for k,v in arrow.items()}


arr = [[list() for _ in range(4)] for _ in range(4)]
smell = [[0 for _ in range(4)] for _ in range(4)]
dir = ((0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1))
dir_s = ((0,0), (-1,0), (0,-1), (1,0), (0,1))
M, S = map(int, input().split())

for _ in range(M):
    x,y,D = map(int, input().split())
    arr[x-1][y-1].append(arrow[D-1])
si,sj = map(lambda x:x-1, map(int, input().split()))


# 사전순 이동방법 만들기
order = []
for i in range(4):
    tmp = []
    for j in range(4):
        for k in range(4):
            tmp.append([i + 1, j + 1, k + 1])
    order += tmp


for _ in range(S):

    ### 복제할 물고기 저장
    fish = []
    for i in range(4):
        for j in range(4):
            if not arr[i][j]: continue
            for k in range(len(arr[i][j])):
                fish.append((i,j,arrow_idx[arr[i][j][k]]))


    ### 모든 칸의 물고기 한 칸 이동
    move = [[list() for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if not arr[i][j]: continue

            # 한 칸에 물고기 여러 마리 있을 수 있음
            while arr[i][j]:
                fi,fj = i,j
                dr = arr[i][j].pop()
                dr = arrow_idx[dr]
                for d in range(dr, dr-8, -1):   # 반시계 회전
                    d %= 8
                    ni,nj = fi+dir[d][0], fj+dir[d][1]

                    # 격자 밖, 상어, 물고기냄새 체크
                    if not (0<=ni<4 and 0<=nj<4): continue
                    if ni==si and nj==sj: continue
                    if smell[ni][nj]: continue

                    # 이동 가능하면 좌표 갱신
                    fi,fj,dr = ni,nj,d
                    break
                move[fi][fj].append(arrow[dr])
    arr = move


    ### 상어가 갈 수 있는 곳과 잡을 수 있는 물고기 개수 구하기
    mx_fish = []

    for op in order:
        v = [[0]*4 for _ in range(4)]
        dfs(op, 0, si, sj, 0, v)

    # 물고기 잡은 개수 큰 순, 사전순 정렬
    mx_fish.sort(key = lambda x:(-x[0], x[1]))

    # 상어 3번 이동
    nxt_move = mx_fish[0][1]
    for nxt_d in nxt_move:
        si,sj = si+dir_s[nxt_d][0], sj+dir_s[nxt_d][1]
        # 상어가 이동하는 도중에 물고기가 있다면 없애고 냄새 뿌리기
        if arr[si][sj]:
            arr[si][sj] = []
            smell[si][sj] = -1

    ### 냄새 -1씩
    for i in range(4):
        for j in range(4):
            if not smell[i][j]: continue
            if smell[i][j] == -1:
                smell[i][j] = 2
            else:
                smell[i][j] -= 1

    # 물고기 복제
    for fi,fj,fd in fish:
        arr[fi][fj].append(arrow[fd])


# 물고기 수 카운트
ans = 0
for i in range(4):
    for j in range(4):
        if arr[i][j]:
            ans += len(arr[i][j])
print(ans)