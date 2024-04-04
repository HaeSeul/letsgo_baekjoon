from collections import defaultdict

DEAD = [-1,-1,-1]
AWAKE, ORIGIN, LEFT = 0,1,2
dir = ((-1,0),(0,1),(1,0),(0,-1))

T = int(input())
for tc in range(1, T+1):
    N,M,K = map(int, input().split())
    cells = dict()
    # 보드 초기에 받고 좌표만 저장함 - 초기상태 : 비활성(0, X, X)
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                cells[(i,j)] = [0, arr[i][j], arr[i][j]]

    for t in range(1,K+1):

        # 현재 시점에서 번식 가능한 지점
        spread = defaultdict(int)
        # 매 시간 세포 돌면서
        for loc, state in cells.items():
            # 죽은 세포는 패스
            if state == DEAD: continue

            # 비활성인 세포의 LEFT --
            if state[AWAKE] == 0:

                if state[LEFT] > 1:
                    state[LEFT] -= 1

                # LEFT==1 이면 활성으로 돌리기
                elif state[LEFT] == 1:
                    cells[loc] = [1, state[ORIGIN], state[ORIGIN]]

            # 활성 세포의 LEFT --
            else:
                # 직전에 활성화된 것
                if state[ORIGIN] == state[LEFT]:
                    state[LEFT] -= 1
                    # 활성상태 되면 현재 시점에서 번식 가능한 지점들 모으기
                    ci, cj = loc
                    for di, dj in dir:
                        ni, nj = ci + di, cj + dj
                        if (ni, nj) in cells: continue
                        # 동시에 번식하려는 곳이 있으면 큰 것만 남기기
                        if not spread[(ni, nj)] or spread[(ni, nj)] < state[ORIGIN]:
                            spread[(ni, nj)] = state[ORIGIN]

                elif state[LEFT]:
                    state[LEFT] -= 1

                # LEFT==1 남으면 죽음으로 돌리기
                if state[LEFT] == 0:
                    cells[loc] = DEAD

        # 세포 딕셔너리에 추가해주기
        for k,v in spread.items():
            cells[k] = [0, v, v]

    ans = 0
    for loc, state in cells.items():
        if state == DEAD: continue
        ans += 1
    print(f'#{tc} {ans}')