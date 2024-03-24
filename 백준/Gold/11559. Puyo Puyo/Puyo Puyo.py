from collections import deque

def bfs(i,j):
    global bomb
    v[i][j] = 1
    q = deque([(i,j)])
    puyo = [(i,j)]
    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if not (0<=ni<12 and 0<=nj<6): continue
            if v[ni][nj]: continue

            # 나랑 같은 뿌요일 때만
            if arr[ni][nj] == arr[i][j]:
                v[ni][nj] = 1
                q.append((ni,nj))
                puyo.append((ni,nj))

    if len(puyo) >= 4:
        bomb = True
        for pi,pj in puyo:
            arr[pi][pj] = '.'

combo = 0
arr = [list(input()) for _ in range(12)]

while True:
    # 터질 것이 있는지 확인
    bomb = False
    v = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if arr[i][j] == '.': continue
            if v[i][j]: continue
            bfs(i,j)

    # 터질 게 있을 때까지만 반복
    if not bomb: break

    combo += 1

    # 중력작용
    for i in range(11):
        for j in range(6):
            idx = i
            # 범위 내, 나는 빈 칸이 아니고 내 아래 빈 칸이 있을 때 -> 중력작용 시작
            while 0 <= idx and arr[idx][j]!='.' and arr[idx+1][j]=='.':
                arr[idx][j], arr[idx+1][j] = arr[idx+1][j], arr[idx][j]
                # 그 위에 더 내릴 게 있는지 확인
                idx -= 1

print(combo)