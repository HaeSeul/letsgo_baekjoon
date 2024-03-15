N = int(input())
arr = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
mn = 21e8

# 가능한 기준점, 경계 길이
tmp = []
for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1,N+1):
                if 1<=x<x+d1+d2<=N and 1<=y-d1<y<y+d2<=N:
                    tmp.append(((x,y), (d1,d2)))

# 가능한 경우의 수로 선거구 나누기
for (x,y), (d1,d2) in tmp:
    v = [[0]*(N+1)] + [[0] + [0]*N for _ in range(N)]

    # 1번 선거구
    for r in range(1, x+d1):
        for c in range(1, y+1):
            v[r][c] = 1

    # 2번 선거구
    for r in range(1, x+d2+1):
        for c in range(y+1, N+1):
            v[r][c] = 2

    # 3번 선거구
    for r in range(x+d1, N+1):
        for c in range(1, y-d1+d2):
            v[r][c] = 3

    # 4번 선거구
    for r in range(x+d2+1, N+1):
        for c in range(y-d1+d2, N+1):
            v[r][c] = 4

    # 5번 선거구 경계선
    for i in range(d1+1):
        for j in range(d2+1):
            v[x+i][y-i] = 5
            v[x+j][y+j] = 5
            v[x+d1+j][y-d1+j] = 5
            v[x+d2+i][y+d2-i] = 5

    # 5번 선거구 내부 채우기
    for i in range(x+1, x+d1+d2):
        j = 1
        while True:     # j 범위 벗어날 일 없음
            if v[i][j] == 5:
                if v[i][j+1] == 5: break
                v[i][j+1] = 5
            j += 1

    # 각 선거구의 인구 구하기
    population = [0,0,0,0,0]
    for r in range(1, N+1):
        for c in range(1, N+1):
            population[v[r][c]-1] += arr[r][c]

    tmp_mx, tmp_mn = max(population), min(population)
    mn = min(mn, tmp_mx - tmp_mn)

print(mn)