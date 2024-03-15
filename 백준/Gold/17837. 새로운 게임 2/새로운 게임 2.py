N,K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[list() for _ in range(N)] for _ in range(N)]
dir = ((0,0),(0,1),(0,-1),(-1,0),(1,0))     # padding, 1우 2좌 3상 4하
horses = []
for k in range(K):
    i,j,d = map(int, input().split())
    horses.append([k+1, i-1, j-1, d])   # 말 번호, 위치, 방향
    v[i-1][j-1].append(k+1)        # 말 번호

time = 0

def number(ci,cj,n):
    num = 0
    for item in v[ci][cj]:
        if item == n: break
        num += 1
    return num

def play():
    global time
    while True:

        if time > 1000:
            return -1

        time += 1   # 턴 시작

        for k in range(len(horses)):

            n,ci,cj,cd = horses[k]      # 말 번호, 위치, 방향
            ni,nj = ci+dir[cd][0], cj+dir[cd][1]

            # 범위 넘어간 경우 : 파란색 취급
            if not (0<=ni<N and 0<=nj<N) or arr[ni][nj] == 2:
                # 방향 반대로
                if cd % 2 == 1:
                    cd += 1
                    horses[k][3] += 1
                else:
                    cd -= 1
                    horses[k][3] -= 1

                # 앞이 파란색이면 pass
                ni,nj = ci+dir[cd][0], cj+dir[cd][1]
                if not (0<=ni<N and 0<=nj<N) or arr[ni][nj] == 2:
                    continue

                # 현재 말 위치에서 몇 번째에 있는지 확인
                num = number(ci,cj,n)

                # 현재 말 위에 쌓여있는 것 전부 이동
                move = v[ci][cj][num:]
                for h in move:
                    horses[h-1][1], horses[h-1][2] = ni,nj

                # 앞 칸이 흰색인 경우
                if arr[ni][nj] == 0:
                    v[ni][nj] += v[ci][cj][num:]
                # 앞 칸이 빨간색인 경우
                elif arr[ni][nj] == 1:
                    v[ni][nj] += v[ci][cj][num:][::-1]
                v[ci][cj] = v[ci][cj][:num]
                if len(v[ni][nj]) >= 4:
                    return time

            # 흰색으로 이동
            elif arr[ni][nj] == 0:
                num = number(ci,cj,n)
                move = v[ci][cj][num:]
                for h in move:
                    horses[h - 1][1], horses[h - 1][2] = ni, nj
                v[ni][nj] += v[ci][cj][num:]
                v[ci][cj] = v[ci][cj][:num]
                if len(v[ni][nj]) >= 4:
                    return time

            # 빨간색으로 이동
            elif arr[ni][nj] == 1:
                num = number(ci,cj,n)
                move = v[ci][cj][num:]
                for h in move:
                    horses[h - 1][1], horses[h - 1][2] = ni, nj
                v[ni][nj] += v[ci][cj][num:][::-1]
                v[ci][cj] = v[ci][cj][:num]
                if len(v[ni][nj]) >= 4:
                    return time

print(play())