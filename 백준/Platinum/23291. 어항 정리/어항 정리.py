def adjust(stack):
    new = [l[::] for l in stack]
    stk_N, stk_M = len(stack), len(stack[0])
    done = [[0] * stk_M for _ in range(stk_N)]

    for i in range(stk_N):
        for j in range(stk_M):
            if not new[i][j]: continue

            for d in range(4):
                ni, nj = i + dir[d][0], j + dir[d][1]

                if not (0 <= ni < stk_N and 0 <= nj < stk_M): continue
                if not stack[ni][nj]: continue  # padding 칸은 제외
                if done[ni][nj]: continue

                # 큰 곳에서 빼고 작은 곳에 더해주기
                cal = abs(stack[i][j] - stack[ni][nj]) // 5
                if stack[i][j] > stack[ni][nj]:
                    new[i][j] -= cal
                    new[ni][nj] += cal
                else:
                    new[i][j] += cal
                    new[ni][nj] -= cal

            done[i][j] = 1
    return new


def align(stack):
    stk_N, stk_M = len(stack), len(stack[0])
    floor = []
    for j in range(stk_M):
        for i in range(stk_N):
            if not stack[i][j]: continue
            floor.append(stack[i][j])
    return floor


N,K = map(int, input().split())
floor = list(map(int, input().split()))
dir = ((-1,0),(0,1),(1,0),(0,-1))
INF = 10e7
turn = 1

while True:
    ### 1. 물고기 가장 적은 모든 어항에 한마리씩 넣기 (지금은 무조건 1차원 리스트임)
    mn = INF
    mn_idx = []
    for i in range(len(floor)):
        if floor[i] < mn:
            mn_idx = []
            mn_idx.append(i)
            mn = floor[i]
        elif floor[i] == mn:
            mn_idx.append(i)

    for idx in mn_idx:
        floor[idx] += 1


    ### 2. 어항쌓기 : 가장 왼쪽 어항 -> stack의 아래에 추가
    left = floor[0]
    floor = floor[1:]
    stack = [[l for l in floor]]
    stack.append([left] + [0]*(len(floor)-1))


    ### 3. 2개 이상 쌓인 어항 열 구하기
    while True:
        # 2개 이상 쌓인 어항 max 열 구하기
        col = 0
        for j in range(len(stack[0])):
            cnt = 0
            for i in range(len(stack)):
                if not stack[i][j]: break
                cnt += 1
            if cnt >= 2:
                col = max(col, j)

        # 공중부양 시킬 열끼리 합해주기 ==> 아래에 합하기 때문에 회전 안 해도 됨
        up = []
        for j in range(col + 1):
            tmp = []
            for i in range(len(stack)):
                tmp.append(stack[i][col-j])
            up.append(tmp)

        # 공중부양 할 열 제외하고 바닥 갱신
        floor = floor[col+1:]

        # 바닥 길이가 공중부양 길이보다 짧으면 종료
        if len(floor) < len(up[0]):
            break

        # 어항 쌓기
        stack = [[l for l in floor]]
        for x in range(len(up)):
            stack += [up[x] + [0]*(len(floor) - len(up[x]))]



    ### 4. 물고기 수 조절 => 모든 칸 동시 발생!!! arr copy후 새롭게 생성
    stk_N, stk_M = len(stack), len(stack[0])
    stack = adjust(stack)


    ### 5. 어항 일렬로 놓기
    floor = align(stack)


    ### 6. 절반 잘라서 공중부양 2번
    half = floor[:len(floor)//2][::-1]
    stack = [floor[len(floor)//2:]]
    stack.append(half)

    half = []
    for i in range(len(stack)):
        half.append(stack[i][:len(stack[i])//2][::-1])
        stack[i] = stack[i][len(stack[i])//2:]
    stack += half[::-1]


    ### 7. 또다시 물고기 수 조절
    stack = adjust(stack)


    ### 8. 일렬로 놓기
    floor = align(stack)


    ### 9. 물고기 수 차이 확인
    if (max(floor) - min(floor)) <= K :
        print(turn)
        break
    else:
        turn += 1