def OOB(i,j): return not (0<=i<N and 0<=j<N)

def make_order():
    # 000 001 002 003 ...
    order = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                order.append((i,j,k))
    return order

def move(arr):
    move = [[list() for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not arr[i][j]: continue

            # 여러 마리 있을 수 있음
            while arr[i][j]:
                fd = arrow_idx[arr[i][j].pop()]

                # 상어칸, 물고기냄새칸, 격자밖 불가능
                fi,fj,nd = i,j,fd
                for _ in range(8):
                    ni,nj = fi+dir[nd][0], fj+dir[nd][1]
                    # 이동 가능한 칸 향할 때까지 45 반시계 회전 후 이동 (없으면 안 감)
                    if OOB(ni,nj) or (ni,nj)==(si,sj) or smell[ni][nj]:
                        nd = (nd-1)%8
                    else:
                        fi,fj,fd = ni,nj,nd
                        break
                move[fi][fj].append(arrow[fd])

    return move


#################################################################################################

arrow = {0:'←', 1:'↖', 2:'↑', 3:'↗', 4:'→', 5:'↘', 6:'↓', 7:'↙' }
arrow_idx = {v:k for k,v in arrow.items()}
dir = ((0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1))
dir4 = ((-1,0),(0,-1),(1,0),(0,1))  # 위 왼 아래 오

N = 4
M, S = map(int, input().split())
arr = [[list() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x,y,d = map(lambda x:x-1, map(int, input().split()))
    arr[x][y].append(arrow[d])
si,sj = map(lambda x:x-1, map(int, input().split()))

smell = [[0]*N for _ in range(N)]
order = make_order()


##################################################################################################

for _ in range(S):
    # [ 1 ] 모든 물고기 복제
    now_fish = [[col[:] for col in row] for row in arr]

    # [ 2 ] 모든 물고기 한 칸 이동 (인접8방)
    arr = move(arr)

    # [ 3 ] 상어 연속 3칸 이동 (인접4방)
    mx, mxi, mxj, mx_copy, mx_smell = -1, 0, 0, [], []
    for op in order:
        copy = [[col[:] for col in row] for row in arr]
        smell_c = [l[:] for l in smell]
        catch = 0
        possible = True
        tmp = []

        ni,nj = si,sj
        for d in op:
            ni,nj = ni+dir4[d][0], nj+dir4[d][1]

            # 격자 범위 넘어가면 불가능한 방법
            if OOB(ni,nj):
                possible = False
                break

            tmp.append((ni,nj))
            if not copy[ni][nj]: continue

            # 이동하는 중에 물고기 있는 칸이면 그 칸 모든 물고기 제외 -> 냄새 남김
            catch += len(copy[ni][nj])
            copy[ni][nj] = []
            smell_c[ni][nj] = 3

        # 중간에 안 끊기고 3번 이동 성공했다면 max 비교
        else:
            # 사전순으로 가장 앞서는 방법 이용
            if mx < catch:
                mx = catch
                mx_copy = copy
                mx_smell = smell_c
                mxi, mxj = ni,nj

        if not possible: continue

    # 가능한 방법 중 제외되는 물고기 가장 많은 방법으로 이동
    arr = mx_copy
    smell = mx_smell
    si, sj = mxi, mxj

    # [ 4 ] 2턴 전 물고기 냄새 사라짐
    for i in range(N):
        for j in range(N):
            if smell[i][j]: smell[i][j] -= 1


    # [ 5 ] 1번에서의 물고기 복제
    for i in range(N):
        for j in range(N):
            if now_fish[i][j]: arr[i][j] += now_fish[i][j]

cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]: cnt += len(arr[i][j])
print(cnt)