N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 0번째에 padding 추가
dir = ((0,0),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1))
# 초기 구름 위치
now = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]

# M번 반복
for n in range(M):
    d, s = map(int, input().split())
    prev = []  # (직전 구름 위치 i, j, 대각선체크)
    v = [[0] * N for _ in range(N)]

    # now에 있는 구름 이동
    for ci, cj in now:
        di, dj = (ci + dir[d][0] * s) % N, (cj + dir[d][1] * s) % N
        prev.append([di, dj, 0])  # (옮긴 위치, 대각선체크)
        v[di][dj] = 1
        arr[di][dj] += 1  # 비내리기

    # 구름 사라짐
    now = []

    # 현재 구름이 있는 곳(prev) 요소 하나씩 탐색하며 대각선 4방에 1 이상인 개수 세기
    for i in range(len(prev)):
        ci, cj = prev[i][0], prev[i][1]
        for di, dj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < N and 0 <= nj < N):   continue
            if arr[ni][nj]:
                prev[i][2] += 1
    for i in range(len(prev)):
        arr[prev[i][0]][prev[i][1]] += prev[i][2]

    # prev인 곳 제외 2 이상인 칸 탐색
    for i in range(N):
        for j in range(N):
            if arr[i][j] < 2:   continue
            if v[i][j]:         continue
            now.append((i, j))
            arr[i][j] -= 2

ans = 0
for l in arr:
    ans += sum(l)
print(ans)