def solve(si,sj):
    for t in range(4):  # 총 4번
        d = t           # 시작 방향
        ci,cj = si,sj
        cnt = 0
        v = []  # (현재방향, 행성좌표i,j) => 새 방향이면 초기화

        while True:
            # 블랙홀을 만나거나 범위 밖인 경우
            if ci<0 or ci>=N or cj<0 or cj>=M or arr[ci][cj]=='C':
                ans.append((t, cnt))
                break

            # 행성 \ 을 만난 경우
            if arr[ci][cj]=='\\':
                # 이미 해당 방향에서 현재 행성에 온 적이 있는 경우 => 무한루프
                if (d,ci,cj) in v:
                    ans.append((t, -1))
                    return
                v.append((d,ci,cj))
                if d==0 or d==2:
                    d = (d-1)%4     # 반시계
                else:
                    d = (d+1)%4     # 시계

            # 행성 / 을 만난 경우
            elif arr[ci][cj] == '/':
                # 이미 해당 방향에서 현재 행성에 온 적이 있는 경우 => 무한루프
                if (d, ci, cj) in v:
                    ans.append((t, -1))
                    return
                v.append((d, ci, cj))
                if d == 0 or d == 2:
                    d = (d + 1) % 4  # 시계
                else:
                    d = (d - 1) % 4  # 반시계

            # 해당 방향으로 이동
            ci, cj = ci + dir[d][0], cj + dir[d][1]
            cnt += 1

N,M = map(int, input().split())
arr=[list(input()) for _ in range(N)]
si,sj = map(int, input().split())
dir = ((-1,0),(0,1),(1,0),(0,-1))
cmd = {0:'U',1:'R',2:'D',3:'L'}
ans = []    # (현재방향, cnt)

solve(si-1,sj-1)

mx,mx_idx=0,0
for i in range(len(ans)):
    # ans에 Voyager가 있다면 해당 방향이 max
    if ans[i][1]==-1:
        print(cmd[ans[i][0]])
        print('Voyager')
        break
    if mx < ans[i][1]:
        # 방향이 여러가지 존재한다면 URDL 중 앞서는 것
        mx = ans[i][1]
        mx_idx = i
else:
    print(cmd[ans[mx_idx][0]])
    print(ans[mx_idx][1])