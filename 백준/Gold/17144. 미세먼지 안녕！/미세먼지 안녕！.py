N,M,T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
air = [[(0,1),(-1,0),(0,-1),(1,0)], [(0,1),(1,0),(0,-1),(-1,0)]]

# 청정기 위치 찾기
m = []
for i in range(N):
    if arr[i][0] == -1:
        m.append(i)
        m.append(i+1)
        break

for _ in range(T):
    # 미세먼지 확산
    new = [[0]*M for _ in range(N)]
    new[m[0]][0] = new[m[1]][0] = -1
    for i in range(N):
        for j in range(M):
            if not arr[i][j] or arr[i][j] == -1: continue
            cnt = 0
            spread = arr[i][j] // 5
            for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
                ni,nj = i+di, j+dj
                if not (0<=ni<N and 0<=nj<M): continue
                if arr[ni][nj] == -1: continue
                new[ni][nj] += spread
                cnt += 1
            new[i][j] += arr[i][j] - spread * cnt
    arr = new

    # 청정기 (위/아래)
    for x in range(2):
        si,sj,sd = m[x],1,0     # 기계에서 나오는 것부터 시작

        tmp = arr[si][sj]
        arr[si][sj] = 0     # 새로운 바람

        while True:
            ni,nj = si+air[x][sd][0], sj+air[x][sd][1]  # 기계 위/아래의 방향

            if not (0<=ni<N and 0<=nj<M):   # 벗어나면 방향 바꾼 것으로 갱신
                sd += 1
                continue
            if arr[ni][nj] == -1:   # 청정기 만날때까지 반복
                break

            arr[ni][nj], tmp = tmp, arr[ni][nj] # 계속 옆의 것과 교체
            si,sj = ni,nj

print(sum(map(sum, arr)) + 2)