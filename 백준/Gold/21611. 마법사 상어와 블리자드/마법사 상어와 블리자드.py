from collections import defaultdict

def make_id():
    d = 0
    go = 1
    idx = 1
    ni, nj = si, sj
    while True:
        for _ in range(2):
            for _ in range(go):
                ni, nj = ni+dir[d][0], nj+dir[d][1]
                id_arr[ni][nj] = idx
                id[idx] = (ni,nj)
                if (ni,nj)==(0,0): return
                idx += 1
            d = (d+1)%4
        go += 1


N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dir = ((0,-1),(1,0),(0,1),(-1,0))   # 왼쪽 아래 오른쪽 위 (반시계)
dr = {1:3, 2:1, 3:0, 4:2}           # 마법사의 방향

si,sj = N // 2, N // 2
d = 0   # 시작방향 : 왼쪽

id_arr = [[0] * N for _ in range(N)]
score = [0, 0, 0, 0]  # 폭발한 구슬 개수 카운팅

##### 회오리 방향대로 좌표에 id 부여하기
id = defaultdict(tuple)
id[0] = (si, sj)
make_id()

for _ in range(M):
    D, S = map(int, input().split())

    ##### D 방향으로 S 만큼 얼음 던지기
    D = dr[D]   # 마법사의 방향으로 바꾸기
    ice = []    # 파괴한 구슬
    for s in range(1,S+1):
        ni, nj = si+dir[D][0]*s, sj + dir[D][1]*s
        # 범위 밖이면 그만
        if not (0<=ni<N and 0<=nj<N): break
        # 구슬파괴
        arr[ni][nj] = 0
        ice.append((ni,nj))

    # 파괴한 방향에 따라 땡겨야 할 위치의 우선순위 변경
    if D==0:    # 왼쪽 : 열 작은 순
        ice.sort(key=lambda x:x[1])
    elif D==1:  # 아래 : 행 큰 순
        ice.sort(key=lambda x:-x[0])
    elif D==2:  # 오른쪽 : 열 큰 순
        ice.sort(key=lambda x:-x[1])
    else:       # 위 : 행 작은 순
        ice.sort(key=lambda x:x[0])



    ##### 구슬 땡기기
    for mi,mj in ice:
        # 파괴한 구슬의 이후 번호부터 탐색
        for num in range(id_arr[mi][mj] + 1, N*N):
            # 현재 구슬과 앞 구슬 비교
            bi,bj = id[num - 1]     # before
            ci,cj = id[num]         # current

            # 0을 만나면 종료
            if arr[ci][cj] == 0: break

            # 빈 칸이라면 옮겨주고 내 자리 0으로 만들기
            if arr[bi][bj] == 0:
                arr[bi][bj] = arr[ci][cj]
                arr[ci][cj] = 0


    ##### 구슬 폭발
    while True:
        explode = False
        v = [[0]*N for _ in range(N)]
        for cur in range(N*N-1, 1, -1):
            ci,cj = id[cur]
            if arr[ci][cj] == 0: continue
            if v[ci][cj]: continue

            tmp = [(ci,cj)]
            for nxt in range(cur-1, 0, -1):
                ni,nj = id[nxt]
                if arr[ci][cj] == arr[ni][nj]:  # 연속되는 같은 구슬 찾기
                    tmp.append((ni,nj))
                    v[ni][nj] = 1
                else: break


            if len(tmp) >= 4:           # 4개 이상 연속될 때만 폭발
                explode = True
                score[arr[ci][cj]] += len(tmp)  # 폭발한 구슬 숫자에 맞게 점수 ++

                # 폭발시킨 만큼 땡기기 -> 맨 앞 좌표의 다음 숫자부터 길이만큼 땡기기
                start_i, start_j = tmp[0]
                length = len(tmp)
                for x in range(id_arr[start_i][start_j] + 1, N*N):
                    xi, xj = id[x]
                    ti, tj = id[x-length]   # 폭발한 길이만큼
                    arr[ti][tj] = arr[xi][xj]
                    arr[xi][xj] = 0

        # 폭발한 게 없을 때까지 반복
        if not explode:
            break



    ##### 구슬 변화
    change = []
    v = [[0]*N for _ in range(N)]
    for cur in range(1, N*N-1):
        ci,cj = id[cur]
        if arr[ci][cj] == 0: break
        if v[ci][cj]: continue

        cnt = 1
        for nxt in range(cur+1, N*N):
            ni,nj = id[nxt]
            if arr[ci][cj] == arr[ni][nj]:  # 연속되는 같은 구슬 찾기
                cnt += 1
                v[ni][nj] = 1
            else: break
        change.append(cnt)
        change.append(arr[ci][cj])

    new = [[0]*N for _ in range(N)]
    for num in range(len(change)):
        if num > N*N-2: break
        ti, tj = id[num+1]
        new[ti][tj] = change[num]

    arr = new

print(1*score[1] + 2*score[2] + 3*score[3])