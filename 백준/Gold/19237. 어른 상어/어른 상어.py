def OOB(i,j): return not (0<=i<N and 0<=j<N)


# 전처리 ################################################################################


N,M,K = map(int, input().split())
arr = [[(0,0) for _ in range(N)] for _ in range(N)]

# { 상어번호 : 상어위치 }
shark_loc = dict()
for i in range(N):
    a = list(map(int, input().split()))
    for j in range(N):
        if not a[j]: continue
        # 처음 - 모든 상어가 자신 위치에 자신의 냄새 (K) 뿌림
        arr[i][j] = (a[j], K)
        shark_loc[a[j]] = (i,j)

# 기본 : 1상 2하 3좌 4우
dir = ((0,0),(-1,0),(1,0),(0,-1),(0,1))

# { 상어번호 : 현재 상어 방향 }
shark_d = dict()
a = list(map(int, input().split()))

# { 상어번호 : [각 방향에 따른 우선순위] }
nxt_d = dict()
for m in range(1, M+1):
    shark_d[m] = a[m-1]
    nxt_d[m] = dict()
    for dr in range(1,5):
        nxt_d[m][dr] = list(map(int, input().split()))


#################################################################################


for t in range(1001):

    # 남은 상어 카운트
    left = 0

    # 1초마다 모든 상어 동시에 인접칸으로 이동 후 냄새 또 뿌림
    new = [l[::] for l in arr]
    new_loc = set()
    for num in range(1, M+1):
        si,sj = shark_loc[num]
        if (si,sj) == (-1,-1): continue
        left += 1

        sd = shark_d[num]

        # 이동방향 : 우선순위 따라 인접칸 중 아무 냄새 없는 칸으로
        for d in range(4):
            nd = nxt_d[num][sd][d]
            ni, nj = si + dir[nd][0], sj + dir[nd][1]
            # 경계 밖이거나 냄새있으면 다른 방향 탐색
            if OOB(ni,nj) or arr[ni][nj][1]: continue
            si,sj,sd = ni,nj,nd
            break
        # 없다면 내 냄새 있는 칸 방향으로
        else:
            for d in range(4):
                nd = nxt_d[num][sd][d]
                ni, nj = si + dir[nd][0], sj + dir[nd][1]
                if OOB(ni, nj) or arr[ni][nj][0] != num: continue
                si, sj, sd = ni, nj, nd
                break

        # 모든 상어 이동 후 한 칸에 여러 상어 남아있으면 가장 작은 번호 상어만 남음
        if not new[si][sj][0]:
            new[si][sj] = (num,K)
            shark_loc[num] = (si,sj)
            shark_d[num] = sd
            new_loc.add((si,sj))
        else:
            now_shark = new[si][sj][0]
            if now_shark >= num:
                new[si][sj] = (num,K)
                shark_loc[num] = (si, sj)
                shark_d[num] = sd
                new_loc.add((si, sj))

                # 기존에 있던 상어 죽음
                if now_shark != num:
                    shark_loc[now_shark] = (-1,-1)
            else:   # 나 죽음
                shark_loc[num] = (-1,-1)
    arr = new

    # 한 마리만 남음!
    if left == 1:
        print(t)
        break

    for i in range(N):
        for j in range(N):
            if arr[i][j][1] and (i,j) not in new_loc:
                smell = arr[i][j][1]
                if smell-1 == 0:
                    arr[i][j] = (0,0)
                else:
                    arr[i][j] = (arr[i][j][0], smell-1)

# 1000초 넘어도 다른 상어 남아있으면 -1
else:
    print(-1)