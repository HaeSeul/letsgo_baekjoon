N,M,ci,cj,K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cmds = map(int, input().split())

# (전개도번호, 주사위에 쓰인 번호)
dice = [[i,0] for i in range(1,7)]  # [0] : 주사위 윗면, [5] : 밑면

# cmd에 따라 달라지는 방향, 전개도 인덱스
dir = {1:(0,1), 2:(0,-1), 3:(-1,0), 4:(1,0)}
idx = {1:(4,2,1,6,5,3), 2:(3,2,6,1,5,4), 3:(5,1,3,4,6,2), 4:(2,6,3,4,1,5)}

for cmd in cmds:
    ni,nj = ci+dir[cmd][0], cj+dir[cmd][1]

    # 범위체크
    if not (0<=ni<N and 0<=nj<M):   continue

    # 주사위 갱신
    tmp = [0]*6
    for i in range(6):
        tmp[i] = dice[idx[cmd][i]-1]
    dice = tmp

    # 이동한 칸이 0인 경우
    if arr[ni][nj]==0:
        arr[ni][nj] = dice[5][1]    # 주사위 밑면 갱신
    else:
        dice[5][1] = arr[ni][nj]
        arr[ni][nj] = 0

    # 이동
    ci,cj = ni,nj

    print(dice[0][1])       # 주사위 윗면 출력