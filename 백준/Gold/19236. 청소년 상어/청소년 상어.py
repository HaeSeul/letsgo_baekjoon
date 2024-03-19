def fish_move(arr, fish):
    # 물고기 작은 번호부터 이동
    for f in range(1, 17):
        if fish[f] == (-1, -1): continue  # 먹힌 물고기 제외
        ci, cj = fish[f]
        cd = arr[ci][cj][1]

        # 물고기 8방탐색
        for d in range(8):
            nd = (cd + d) % 8
            ni, nj = ci + dir[nd][0], cj + dir[nd][1]

            # 범위, 상어 체크
            if not (0 <= ni < 4 and 0 <= nj < 4): continue
            if arr[ni][nj][0] == 20: continue

            # 다른 물고기 칸 -> 서로 바꾸기 (0인 칸은 빈 칸)
            nxt = arr[ni][nj]
            if nxt[0]:
                fish[nxt[0]] = (ci, cj)  # 상대편 위치 업데이트
            fish[f] = (ni, nj)  # 물고기 위치 업데이트
            arr[ci][cj] = nxt
            arr[ni][nj] = (f, nd)
            break
    return arr, fish


def shark_food(arr, fish):
    # 상어가 먹을 수 있는 물고기
    mul = 1
    food = []
    si, sj = fish[20]   # 상어위치, 방향
    sd = arr[si][sj][1]
    while True:
        ni, nj = si + dir[sd][0] * mul, sj + dir[sd][1] * mul
        if not (0 <= ni < 4 and 0 <= nj < 4): break
        if arr[ni][nj][0] and arr[ni][nj][0] != 20:  # 빈 칸이 아닌 물고기만 먹음
            food.append(arr[ni][nj])
        mul += 1
    return food


# 현재 arr, 물고기위치정보, 먹을 수 있는 물고기, 지금까지 먹은 score
def dfs(arr, fish, food, score):
    global mx
    if not food:  # 상어가 먹을 게 없으면 종료
        mx = max(mx, score)
        return

    arr_copy = [[row[::] for row in rows] for rows in arr]
    fish_copy = {k:v for k,v in fish.items()}

    for x in range(len(food)):

        ###  상어 -> 물고기 먹기
        eat_fish, eat_dr = food[x]  # 현재 먹을 물고기 번호, 방향
        si, sj = fish_copy[20]  # 현재 상어위치
        ti, tj = fish_copy[eat_fish]  # 먹을 물고기 위치

        arr_copy[si][sj] = (0, 0)  # 상어 이동 -> 원래 위치 빈 칸으로
        arr_copy[ti][tj] = (20, eat_dr)
        fish_copy[20] = ti, tj

        fish_copy[eat_fish] = (-1, -1)  # 물고기 먹힘

        ### 물고기 이동
        arr_copy, fish_copy = fish_move(arr_copy, fish_copy)
        ### 가능한 먹이 찾기
        new_food = shark_food(arr_copy, fish_copy)

        ### 현재 arr과 먹은 먹이 바탕으로 dfs
        dfs(arr_copy, fish_copy, new_food, score + eat_fish)

        ### 되돌려주기
        arr_copy = [[row[::] for row in rows] for rows in arr]
        fish_copy = {k: v for k, v in fish.items()}


arr = [list() for _ in range(4)]
dir = ((-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)) # 위부터 반시계 45
fish = dict()
mx = 0
for i in range(4):
    a = list(map(int, input().split()))
    for j in range(4):
        arr[i].append((a[j*2], a[j*2 + 1]-1))  # (번호, 방향)
        fish[a[j*2]] = (i,j)
fish = dict(sorted(fish.items()))

# 초기 상어(20번)
first = arr[0][0]
score = first[0]            # (0,0) 물고기 점수로 시작
fish[20] = (0, 0)           # 상어(20) : (0,0)
fish[first[0]] = (-1, -1)   # 첫 물고기 먹기 -> (-1,-1)
arr[0][0] = (20, first[1])

arr, fish = fish_move(arr, fish)     # 물고기 이동
food = shark_food(arr, fish) # 상어가 먹을 수 있는 먹이
dfs(arr, fish, food, score)

print(mx)