from collections import defaultdict, deque

def OOB(i,j): return not (0<=i<N and 0<=j<M)

def up_wall(i,j): return OOB(i,j) or up[i][j]   # 범위 벗어났거나 벽 있음!
def right_wall(i,j): return OOB(i,j) or right[i][j]

def blow():
    wind = [[0]*M for _ in range(N)]
    for dr, lst in warmer.items():
        for i,j in lst: # 온풍기위치
            si,sj = i+dir[dr][0], j+dir[dr][1]
            v = [[0]*M for _ in range(N)]
            v[si][sj] = 1
            q = deque([(si,sj)])
            s = 5
            while s:
                for _ in range(len(q)):
                    ci,cj = q.popleft()
                    wind[ci][cj] += s

                    tmp = []
                    # 방향에 따라 벽 체크 달라짐
                    if dr==1:
                        if not up_wall(ci,cj) and not right_wall(ci-1,cj):
                            tmp.append((ci-1,cj+1))
                        if not right_wall(ci,cj):
                            tmp.append((ci,cj+1))
                        if not up_wall(ci+1,cj) and not right_wall(ci+1,cj):
                            tmp.append((ci+1,cj+1))

                    elif dr==2:
                        if not up_wall(ci,cj) and not right_wall(ci-1,cj-1):
                            tmp.append((ci-1,cj-1))
                        if not right_wall(ci,cj-1):
                            tmp.append((ci,cj-1))
                        if not up_wall(ci+1,cj) and not right_wall(ci+1,cj-1):
                            tmp.append((ci+1,cj-1))

                    elif dr==3:
                        if not right_wall(ci,cj-1) and not up_wall(ci,cj-1):
                            tmp.append((ci-1,cj-1))
                        if not up_wall(ci,cj):
                            tmp.append((ci-1,cj))
                        if not right_wall(ci,cj) and not up_wall(ci,cj+1):
                            tmp.append((ci-1,cj+1))

                    else:
                        if not right_wall(ci,cj-1) and not up_wall(ci+1,cj-1):
                            tmp.append((ci+1,cj-1))
                        if not up_wall(ci+1,cj):
                            tmp.append(((ci+1,cj)))
                        if not right_wall(ci,cj) and not up_wall(ci+1,cj+1):
                            tmp.append(((ci+1,cj+1)))

                    if not tmp: continue

                    for ni,nj in tmp:
                        if OOB(ni,nj): continue
                        if v[ni][nj]: continue
                        v[ni][nj] = 1
                        q.append((ni,nj))
                s -= 1
    return wind

dir = ((0,0),(0,1),(0,-1),(-1,0),(1,0)) # 0, 오왼위아래

N,M,K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
warmer = defaultdict(list)
look = []

# 위, 오른쪽 벽 유무
up = [[0]*M for _ in range(N)]
right = [[0]*M for _ in range(N)]

for _ in range(int(input())):
    x,y,t = map(int, input().split())
    if t==0: up[x-1][y-1] = 1
    else: right[x-1][y-1] = 1

# 온풍기 있는 칸, 탐색해야 할 칸 탐색
for i in range(N):
    for j in range(M):
        if not arr[i][j] : continue
        if arr[i][j] == 5: look.append((i,j))
        else:
            warmer[arr[i][j]].append((i,j))
        arr[i][j] = 0

wind = blow()   # 온풍기에서 나오는 바람

choco = 0

while True:
    # [ 1 ] 모든 온풍기에서 바람 한 번 나옴
    for i in range(N):
        for j in range(M):
            arr[i][j] += wind[i][j]

    # [ 2 ] 온도 조절 => 동시발생
    temp = [l[:] for l in arr]
    for i in range(N):
        for j in range(M):
            # 모든 인접칸에 대해 오른쪽/아래만 확인하면 됨 (벽 없어야함)
            for d in (1,4):
                ni,nj = i+dir[d][0], j+dir[d][1]
                if OOB(ni,nj):continue
                if arr[i][j] == arr[ni][nj]: continue
                if d==1 and right_wall(i,j): continue
                if d==4 and up_wall(ni,nj): continue

                # cal = (온도 높은칸 -> 낮은칸으로 그 차이) // 4만큼 조절
                cal = abs(arr[i][j] - arr[ni][nj]) // 4
                # 높은칸 -= cal, 낮은칸 += cal
                if arr[i][j] > arr[ni][nj]:
                    temp[i][j] -= cal
                    temp[ni][nj] += cal
                else:
                    temp[i][j] += cal
                    temp[ni][nj] -= cal

    # [ 3 ] 온도 1 이상인 가장 바깥 칸 온도 -1
    for i in (0,N-1):
        for j in range(M):
            if temp[i][j]: temp[i][j] -= 1
    for i in range(1,N-1):
        for j in (0,M-1):
            if temp[i][j]: temp[i][j] -= 1
    arr = temp

    # [ 4 ] 초콜릿먹기
        # 먹는 초콜릿 개수가 100 넘으면 101 출력
    choco += 1
    if choco > 100:
        break

    # [ 5 ] 조사하는 모든 칸 온도가 K 이상이면 종료
    flag = True
    for i,j in look:
        if arr[i][j] < K:
            flag = False
            break
    if flag: break
print(choco)