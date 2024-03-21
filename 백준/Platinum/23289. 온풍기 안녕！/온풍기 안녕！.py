from collections import defaultdict
from collections import deque

N,M,K = map(int, input().split())
arr = []
search = []     # 나중에 조사해야 할 위치
robots = defaultdict(list)
t0 = [[0]*M for _ in range(N)]  # 내 위에 벽이 있는가
t1 = [[0]*M for _ in range(N)]  # 내 오른쪽에 벽이 있는가
dir = ((0,0), (0,1), (0,-1), (-1,0), (1,0)) # 0 오른쪽 왼쪽 위 아래
choco = 0

# 값 받기
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(M):
        if not arr[i][j]: continue
        if arr[i][j] == 5: search.append((i,j))
        else: robots[arr[i][j]].append((i,j))

#  벽 설치
for _ in range(int(input())):
    x,y,t = map(int, input().split())
    if t==0: t0[x-1][y-1] = 1
    else:    t1[x-1][y-1] = 1


def right(i,j): return t1[i][j]
def left(i,j):  return t1[i][j-1]
def up(i,j):    return t0[i][j]
def down(i,j):  return t0[i+1][j]

def check(i,j,v): return 0<=i<N and 0<=j<M and not v[i][j]


def blow(ri,rj,type):
    v = [[0]*M for _ in range(N)]
    v[ri][rj] = 1

    # type 방향대로 바람 나아감
    i,j = ri+dir[type][0], rj+dir[type][1]
    # 온풍기 바로 앞은 무조건 비어있음
    wind[i][j] += 5

    v[i][j] = 1
    q = deque([(i,j)])
    k = 4
    while q and k > 0:
        for _ in range(len(q)):
            ci,cj = q.popleft()

            # 1: 오른쪽 탐색 (우상, 우, 우하)
            if type == 1:
                ni,nj = ci-1, cj+1
                if check(ni, nj, v) and not up(ci, cj) and not left(ni, nj):
                    wind[ni][nj] += k
                    v[ni][nj] = 1
                    q.append((ni,nj))
                ni,nj = ci, cj+1
                if check(ni, nj, v) and not left(ni, nj):
                    wind[ni][nj] += k
                    v[ni][nj] = 1
                    q.append((ni, nj))
                ni,nj = ci+1, cj+1
                if check(ni, nj, v) and not down(ci, cj) and not left(ni, nj):
                    wind[ni][nj] += k
                    v[ni][nj] = 1
                    q.append((ni, nj))

            # 2: 왼쪽 탐색 (좌상, 좌, 좌하)
            elif type == 2:
                ni,nj = ci-1, cj-1
                if check(ni, nj, v) and not up(ci, cj) and not right(ni, nj):
                    wind[ni][nj] += k
                    v[ni][nj] = 1
                    q.append((ni,nj))
                ni,nj = ci, cj-1
                if check(ni, nj, v) and not right(ni, nj):
                    wind[ni][nj] += k
                    v[ni][nj] = 1
                    q.append((ni, nj))
                ni,nj = ci+1, cj-1
                if check(ni, nj, v) and not down(ci, cj) and not right(ni, nj):
                    wind[ni][nj] += k
                    v[ni][nj] = 1
                    q.append((ni, nj))

            # 3: 위쪽 탐색 (좌상, 상, 우상)
            elif type == 3:
                ni,nj = ci-1, cj-1
                if check(ni, nj, v) and not left(ci, cj) and not down(ni, nj):
                    wind[ni][nj] += k
                    v[ni][nj] = 1
                    q.append((ni,nj))
                ni,nj = ci-1, cj
                if check(ni, nj, v) and not down(ni, nj):
                    wind[ni][nj] += k
                    v[ni][nj] = 1
                    q.append((ni, nj))
                ni,nj = ci-1, cj+1
                if check(ni, nj, v) and not right(ci, cj) and not down(ni, nj):
                    wind[ni][nj] += k
                    v[ni][nj] = 1
                    q.append((ni, nj))

            # 4: 아래쪽 탐색 (좌하, 하, 우하)
            elif type == 4:
                ni,nj = ci+1, cj-1
                if check(ni, nj, v) and not left(ci, cj) and not up(ni, nj):
                    wind[ni][nj] += k
                    v[ni][nj] = 1
                    q.append((ni,nj))
                ni,nj = ci+1, cj
                if check(ni, nj, v) and not up(ni, nj):
                    wind[ni][nj] += k
                    v[ni][nj] = 1
                    q.append((ni, nj))
                ni,nj = ci+1, cj+1
                if check(ni, nj, v) and not right(ci, cj) and not up(ni, nj):
                    wind[ni][nj] += k
                    v[ni][nj] = 1
                    q.append((ni, nj))

        k -= 1

def get_temp():
    temp = [l[::] for l in wind]
    done = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if not wind[i][j]: continue     # 기존에 온도 없는 곳은 패스

            for d in range(1, 5):   # 오른쪽 왼쪽 위 아래
                ni,nj = i+dir[d][0], j+dir[d][1]

                # 경계, 방문, 기존의 같은 온도 체크
                if not check(ni,nj,done): continue
                if wind[i][j] == wind[ni][nj]: continue

                # 방향에 따라 이동 위치 기준 벽 있는지 체크
                if d==1 and left(ni,nj): continue   # 오른쪽이었다면 이동 블록의 왼쪽에 벽 있는지
                elif d==2 and right(ni,nj): continue
                elif d==3 and down(ni,nj): continue
                elif d==4 and up(ni,nj): continue

                # 기존 값 기준으로 더 큰 값은 빼주고 작은 값은 더해주기
                cal = abs(wind[i][j] - wind[ni][nj]) // 4
                if wind[i][j] > wind[ni][nj]:
                    temp[i][j] -= cal
                    temp[ni][nj] += cal
                else:
                    temp[i][j] += cal
                    temp[ni][nj] -= cal

            done[i][j] = 1

    return temp


# 온풍기 바람 나오기
wind = [[0]*M for _ in range(N)]

while True:
    # 모든 로봇에서 바람 나오기
    for type, robot in robots.items():
        for ri,rj in robot:
            blow(ri,rj,type)


    # 온도 조절
    temp = get_temp()


    # 바깥 칸 온도 감소
    for i in range(N):
        if temp[i][0] > 0:  temp[i][0] -= 1
        if temp[i][M-1] > 0:  temp[i][M-1] -= 1
    for j in range(1, M-1):
        if temp[0][j] > 0:  temp[0][j] -= 1
        if temp[N-1][j] > 0:  temp[N-1][j] -= 1


    # 초코 먹기
    choco += 1
    if choco > 100:
        choco = 101
        break


    # 5인 칸의 온도 체크
    cnt = 0
    for i,j in search:
        if temp[i][j] >= K:
            cnt += 1
    if cnt == len(search):
        break

    # 조절한 온도로 wind 갱신
    wind = temp

print(choco)