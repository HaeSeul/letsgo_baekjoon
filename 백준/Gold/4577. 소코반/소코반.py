import sys
input = sys.stdin.readline

def play(ci, cj):
    global goal
    for cmd in cmds:
        # 목표점에 박스가 도달했는지 확인
        if goal == len(to):
            break

        d = dir[cmd]  # 명령어 별 방향 설정
        ni,nj = ci+d[0], cj+d[1]
        if arr[ni][nj]=='#': continue

        # 빈 칸, 목표점 -> 바로 이동
        if arr[ni][nj]=='.' or arr[ni][nj]=='+':
            ci,cj = ni,nj

        # 박스 -> 한 칸 더 앞이 빈 경우만 이동
        elif arr[ni][nj]=='b' or arr[ni][nj]=='B':
            nni,nnj = ni+d[0], nj+d[1]
            if arr[nni][nnj] in '#bB':  continue

            # 박스 다음이 목표점
            if arr[nni][nnj]=='+':
                goal += 1
            arr[ni][nj] = '.'
            arr[nni][nnj] = 'b'

            # 박스가 목표점을 지나친 경우
            if (ni,nj) in to:
                arr[ni][nj] = '+'
                goal -= 1

            # 현재 위치 갱신
            ci,cj = ni,nj

    arr[ci][cj] = 'w'

    return goal


dir = {'U':(-1,0), 'R':(0,1), 'D':(1,0), 'L':(0,-1)}
game = 1

while True:
    N,M = map(int, input().rstrip().split())
    if (N,M) == (0,0):  break

    arr = [list(input().rstrip()) for _ in range(N)]
    cmds = list(input().rstrip())

    # 캐릭터, 목표점 위치 확인
    ci,cj = 0,0
    to = []
    goal = 0    # 목표점에 있는 박스 개수
    for i in range(N):
        for j in range(M):
            if arr[i][j]=='w':
                arr[i][j] = '.'
                ci,cj = i,j
            elif arr[i][j]=='W':
                arr[i][j] = '+'
                ci,cj = i,j
                to.append((i,j))
            elif arr[i][j]=='B':
                goal += 1
                to.append((i,j))
            elif arr[i][j]=='+':
                to.append((i,j))

    goal = play(ci,cj)
    if goal == len(to):
        ans = 'complete'
    else:
        ans = 'incomplete'

    print(f'Game {game}: {ans}')
    for i in range(N):
        for j in range(M):
            # 목표점에 있다면 대문자로 출력
            if (i,j) in to and arr[i][j] in 'wb':
                print(arr[i][j].upper(), end='')
            else:
                print(arr[i][j], end='')
        print()

    game += 1