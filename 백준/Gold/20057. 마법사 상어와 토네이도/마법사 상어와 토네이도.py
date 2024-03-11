def wind():
    global ci,cj,ratio,ans
    d = 0
    move = 1
    while True:
        for _ in range(2):
            for _ in range(move):
                # x = (ci,cj) -> y = (ni,nj) 이동
                ni,nj = ci+dir[d][0], cj+dir[d][1]

                # 현재 방향에 맞춰 ratio 결정
                if d==0:    # 좌
                    n,m = 5,4
                    si,sj = ni-2, nj-2
                elif d==1:  # 상
                    n,m = 4,5
                    si,sj = ni-2, nj-2
                elif d==2:  # 우
                    n,m = 5,4
                    si,sj = ni-2, nj-1
                elif d==3:  # 하
                    n,m = 4,5
                    si,sj = ni-1, nj-2

                # ratio 위치에 맞게 모래 날리기
                tmp = 0
                for ri in range(n):
                    for rj in range(m):
                        # 비율이 적힌 곳만 계산
                        if not ratio[ri][rj]: continue

                        spread = ratio[ri][rj] * arr[ni][nj] // 100
                        tmp += spread

                        # 범위 밖으로 나간 모래
                        if not (0<=si+ri<N and 0<=sj+rj<N):
                            ans += spread
                            continue

                        # 계산된 양만큼 모래 날리기
                        arr[si+ri][sj+rj] += spread

                # 계산된 양만큼 모래 빼주기
                arr[ni][nj] -= tmp

                # a 위치에 남은 모래 옮기기
                ai,aj = ni+dir[d][0], nj+dir[d][1]
                if not (0<=ai<N and 0<=aj<N):
                    ans += arr[ni][nj]
                else:
                    arr[ai][aj] += arr[ni][nj]
                    arr[ni][nj] = 0
                # 종료조건
                if (ni,nj) == (0,0): return

                # y -> x 갱신
                ci,cj = ni,nj

            d = (d-1) % 4
            for _ in range(3):  # 270도 회전
                ratio = list(map(list, zip(*ratio[::-1])))
        move += 1

ratio = [[0, 0, 2, 0],
         [0, 10, 7, 1],
         [5, 0, 0, 0],
         [0, 10, 7, 1],
         [0, 0, 2, 0]]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dir = ((0,-1),(-1,0),(0,1),(1,0))
ci, cj = N // 2, N // 2
ans = 0
wind()
print(ans)