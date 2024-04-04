def OOB(i,j): return not (0<=i<N and 0<=j<N)

BLANK = (0,'-')
DEAD = (-1,-1)
N = 4
arrow = {0:'↑', 1:'↖', 2:'←', 3:'↙', 4:'↓', 5:'↘', 6:'→', 7:'↗'}
arrow_idx = {v:k for k,v in arrow.items()}
dir = ((-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1))
arr = [[tuple() for _ in range(N)] for _ in range(N)]
fish = dict()
for i in range(N):
    a = list(map(int, input().split()))
    for j in range(N):
        arr[i][j] = (a[2*j], arrow[a[2*j+1]-1])
        fish[a[2*j]] = (i,j)

mx = 0

# 상어(0번) - 초기 : (0,0) 물고기 먹고 해당 칸에 들어감
#             방향은 거기에 있던 물고기 방향
fish[0] = (0,0)
si,sj,sd = 0,0,arrow_idx[arr[0][0][1]]
fish[arr[0][0][0]] = DEAD
start_score = arr[0][0][0]
arr[0][0] = (0, arr[0][0][1])

def fish_move(arr, fish):
    # 1. 물고기 - 작은 번호부터 순서대로 이동
    for n in range(1, 17):
        fi, fj = fish[n]
        if (fi,fj) == DEAD: continue
        fd = arrow_idx[arr[fi][fj][1]]
        # 물고기 이동 : 빈칸, 다른 물고기 있는 칸 가능
        ni, nj = fi+dir[fd][0], fj+dir[fd][1]

        # 상어 있거나 경계 넘으면 못 감
        if OOB(ni,nj) or (ni,nj) == fish[0]:
            # 갈 수 있는 칸 찾을 때까지 방향 45 반시계 회전
            nd = fd
            for _ in range(8):
                nd = (nd+1)%8
                ni, nj = fi + dir[nd][0], fj + dir[nd][1]
                if OOB(ni,nj) or (ni,nj) == fish[0]: continue
                fd = nd     # 가능한 게 있다면 확정 후 멈춤
                arr[fi][fj] = (n, arrow[fd])
                break
            else:   # 갈 수 있는 곳 없다면 다음 물고기로
                continue
        # 빈칸이면 바로 이동
        if arr[ni][nj] == BLANK:
            fish[n] = (ni,nj)
            arr[ni][nj] = (n, arrow[fd])
            arr[fi][fj] = BLANK
        # 다른 물고기 있는 칸으로 가려면 둘이 위치 바꿈
        else:
            now_f = arr[ni][nj][0]
            arr[ni][nj], arr[fi][fj] = arr[fi][fj], arr[ni][nj]
            fish[n], fish[now_f] = fish[now_f], fish[n]
    return arr, fish

def get_food(arr,fish):
    # 2. 상어이동 - 방향에 있는 칸으로 한 번에 여러 칸 이동 가능
    si,sj = fish[0]
    sd = arrow_idx[arr[si][sj][1]]
    food = []   # 상어가 갈 수 있는 칸들
    for dist in range(1,N):
        nsi, nsj = si+dir[sd][0]*dist, sj+dir[sd][1]*dist
        # 물고기 없는 칸이 나오거나 범위 밖 나가기 전까지 반복
        if OOB(nsi, nsj): break
        if arr[nsi][nsj] == BLANK: continue
        food.append(arr[nsi][nsj])
    return food


def dfs(n,arr, fish, sm):
    global mx

    arr, fish = fish_move(arr, fish)

    food = get_food(arr,fish)

    if not food:        # 이동 가능한 칸 없으면 집으로 감!
        mx = max(mx, sm)
        return

    arr_c = [l[:] for l in arr]
    fish_c = {k:v for k,v in fish.items()}

    for x in range(len(food)):
        # 물고기 있는 칸으로 이동하면 그 칸 물고기 먹고 물고기 방향 가져감
        eat_n, eat_d = food[x][0], arrow_idx[food[x][1]]
        ei,ej = fish_c[eat_n]
        fish_c[eat_n] = DEAD

        fi,fj = fish_c[0]         # 상어위치
        fish_c[0] = (ei,ej)       # 상어위치 갱신
        arr_c[fi][fj] = BLANK     # 상어 있던 곳 빈칸으로
        arr_c[ei][ej] = (0, arrow[eat_d])    # 먹은 물고기 방향 가져감


        dfs(n+1, arr_c, fish_c, sm + eat_n)  # 다음 단계로 고

        # 되돌려주기
        arr_c = [l[:] for l in arr]
        fish_c = {k: v for k, v in fish.items()}

dfs(0,arr,fish,start_score)
print(mx)