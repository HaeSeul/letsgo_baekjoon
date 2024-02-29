# N*N, M개 볼, K번 이동
N,M,K = map(int, input().split())
arr = [[0]*N for _ in range(N)]
dir = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))
balls = []
# M개 볼 초기 위지
for _ in range(M):
    r,c,m,s,d = map(int, input().split())
    arr[r-1][c-1] = 1
    balls.append([r-1, c-1, m, s, d])    # M개 입력 (처음부터 자리 같은 곳 X)

# K번 이동
for _ in range(K):

    # 현재 ball 개수만큼 각자 d 방향으로 s 만큼 이동
    for ball in balls:
        r, c, m, s, d = ball[0], ball[1], ball[2], ball[3], ball[4]
        arr[r][c] -= 1
        ball[0], ball[1] = (r + dir[d][0]*s) % N, (c + dir[d][1]*s) % N
        arr[ball[0]][ball[1]] += 1

    # 이동한 자리에 같은 게 2개 이상이라면 4개로 쪼개기
    for i in range(N):
        for j in range(N):
            if arr[i][j] < 2:   continue
            n = arr[i][j]
            # m, s, d 갱신
            new_m, new_s, new_d = 0,0,0
            for ball in balls:
                if (ball[0],ball[1]) == (i,j):
                    arr[i][j] -= 1
                    new_m += ball[2]
                    new_s += ball[3]
                    new_d += (0 if ball[4]%2==0 else 1)

                    # 이후 없애기 위해 표시
                    ball[2] = 0

            new_m //= 5
            if new_m == 0: continue        # m==0인 곳 제외
            new_s //= n
            if new_d == 0 or new_d == n:   # 모두 짝 or 홀
                new_d = [0,2,4,6]
            else:
                new_d = [1,3,5,7]

            # 4개로 쪼개기
            for b in range(4):
                arr[i][j] += 1
                balls.append([i,j,new_m,new_s,new_d[b]])

    # 질량==0인 곳 소멸
    for x in range(len(balls)-1, -1, -1):
        if balls[x][2] == 0:
            balls.pop(x)

# 총 m의 합
ans = 0
for ball in balls:
    ans += ball[2]
print(ans)