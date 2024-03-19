def reduce_smell():
    # 현재 상어 위치가 아니면서 냄새가 1보다 클 때만 갱신
    sharks_loc = [v for v in shark.values()]
    for i in range(N):
        for j in range(N):
            if not arr[i][j]: continue
            if (i,j) in sharks_loc: continue
            n, smell = arr[i][j].pop()
            if smell > 1:
                arr[i][j].append((n, smell-1))


def get_nxt():
    global death
    new = [[row[:] for row in rows] for rows in arr]

    # 각 상어 새롭게 배치
    for num in range(1, M+1):
        # 상어위치, 현재방향, 가능한 방향 받아오기
        ci, cj = shark[num]
        if (ci,cj) == (-1,-1) : continue
        cur_d = shark_d[num]
        d_lst = dr[num][cur_d]

        for d in range(4):
            nd = d_lst[d]
            ni, nj = ci+dir[nd][0], cj+dir[nd][1]
            # 경계, 빈 칸 아닌 곳 체크
            if not (0<=ni<N and 0<=nj<N): continue
            if arr[ni][nj]: continue

            # 다른 상어가 있으면 내가 더 작을 때만 갱신
            if new[ni][nj]:
                other = new[ni][nj].pop()
                if other[0] > num:
                    new[ni][nj].append((num, K))
                    shark[other[0]] = (-1,-1)
                    shark[num] = (ni, nj)
                    shark_d[num] = nd
                else:   # 내가 더 크면 나 죽음
                    new[ni][nj].append(other)
                    shark[num] = (-1,-1)
                    death += 1
            # 없을 땐 그냥 갱신
            else:
                new[ni][nj].append((num, K))
                shark[num] = (ni, nj)
                shark_d[num] = nd
            break

        # 갈 수 있는 곳이 없다면 내 냄새 있는 곳으로
        else:
            for d in range(4):
                nd = d_lst[d]
                ni, nj = ci + dir[nd][0], cj + dir[nd][1]
                # 경계, 다른 냄새 체크
                if not (0<=ni<N and 0<=nj<N): continue
                if arr[ni][nj][0][0] != num: continue

                # 다른 상어가 있으면 나이거나 내가 더 작을 때만 갱신
                if new[ni][nj]:
                    other = new[ni][nj].pop()
                    if other[0] >= num:
                        new[ni][nj].append((num, K))
                        shark[other[0]] = (-1, -1)
                        shark[num] = (ni, nj)
                        shark_d[num] = nd
                    else:  # 내가 더 크면 나 죽음
                        new[ni][nj].append(other)
                        shark[num] = (-1, -1)
                        death += 1
                # 없을 땐 그냥 갱신
                else:
                    new[ni][nj].append((num, K))
                    shark[num] = (ni, nj)
                    shark_d[num] = nd
                break

    # 갱신된 상어 위치 리턴
    return new


N,M,K = map(int, input().split())
dir = ((0,0),(-1,0),(1,0),(0,-1),(0,1))     # 1상 2하 3좌 4우
arr = [[[] for _ in range(N)] for _ in range(N)]
shark = dict()
smells = []
death = 0

for i in range(N):
    a = list(map(int, input().split()))
    for j in range(N):
        if not a[j]: continue
        shark[a[j]] = (i,j)

# 각 상어의 시작방향
shark_d = dict()
a = list(map(int, input().split()))
for i in range(1, M+1):
    shark_d[i] = a[i-1]

# arr에 (상어, 남은시간) 배치
for num, loc in shark.items():
    si,sj = loc
    arr[si][sj].append((num, K))

# M마리 만큼 4방향씩 반복
dr = dict()
for m in range(1, M+1):
    dr[m] = dict()
    for d in range(1, 5):
        dr[m][d] = tuple(map(int, input().split()))

# 1000초까지 반복
for time in range(1001):
    if death == M-1:
        print(time)
        break
    arr = get_nxt()
    reduce_smell()
else:
    print(-1)