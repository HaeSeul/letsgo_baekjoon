def go(arr):
    move = [[list() for _ in range(N)] for _ in range(N)]
    merge = set()
    for i in range(N):
        for j in range(N):
            if not arr[i][j]: continue

            s, d = arr[i][j].pop()
            ni, nj = i + dir[d][0], j + dir[d][1]

            # 경계선에 도착한 경우
            if ni == 0 or ni == N - 1 or nj == 0 or nj == N - 1:
                # 방향 반대로, size 절반으로
                if d % 2 == 1:
                    d += 1
                else:
                    d -= 1
                s //= 2

            if s:  # 미생물이 0이 아닐 때만 추가
                # 이미 다른 게 있다면 나중에 합쳐주기 위해 인덱스 저장
                if move[ni][nj]:
                    merge.add((ni, nj))
                move[ni][nj].append((s, d))


    # 합쳐야 할 부분이 있다면
    if merge:
        # size의 총합과 size가 가장 큰 것의 방향 구하기
        for i, j in merge:
            target = move[i][j]
            target.sort(key=lambda x: -x[0])
            nxt_s = 0
            for s, d in target:
                nxt_s += s
            move[i][j] = [(nxt_s, target[0][1])]

    return move


dir = ((0,0),(-1,0),(1,0),(0,-1),(0,1))  # 상: 1, 하: 2, 좌: 3, 우: 4

T = int(input())
for tc in range(1, T+1):
    N,M,K = map(int, input().split())
    arr = [[list() for _ in range(N)] for _ in range(N)]
    for _ in range(K):
        r,c,s,d = map(int, input().split())
        arr[r][c].append((s,d))

    for _ in range(M):
        arr = go(arr)

    sm = 0
    for i in range(N):
        for j in range(N):
            if not arr[i][j]: continue
            size = arr[i][j][0][0]
            sm += size

    print(f'#{tc} {sm}')