def block(i,j):
    # 사방에 0이 없다면 막힘
    for x in range(1,5):
        di,dj = i+dir[x][0], j+dir[x][1]
        if 0<=di<N and 0<=dj<M and arr[di][dj]==0:
            return False    # 막히지 않은 경우
    return True

def change_dir(i,j):
    global d
    ni,nj = i+dir[cmd[d]][0], j+dir[cmd[d]][1]
    # 벽을 만난 경우
    if ni<0 or ni>=N or nj<0 or nj>=M:
        return True
    # 앞에 갔던 곳 or 장애물이 있는 경우
    if arr[ni][nj] > 0 or arr[ni][nj]==-1:
        return True
    return False

def solve(ci,cj):
    global d
    num=1
    while True:
        if block(ci,cj):        # 더이상 못 가는 경우
            return ci,cj
        if change_dir(ci,cj): # 방향을 바꿔야하는 경우
            d = (d+1)%4
        else:
            ci,cj = ci+dir[cmd[d]][0], cj+dir[cmd[d]][1]
            num+=1
            arr[ci][cj]=num

N,M = map(int,input().split())
arr = [[0]*M for _ in range(N)]

# 장애물 표시
k = int(input())
for _ in range(k):
    i,j = map(int,input().split())
    arr[i][j] = -1

# 현재 위치와 지정한 방향
si,sj = map(int,input().split())
cmd = list(map(int,input().split()))
dir = {1:(-1,0), 2:(1,0), 3:(0,-1), 4:(0,1)}
d = 0
arr[si][sj]=1
print(*solve(si,sj))