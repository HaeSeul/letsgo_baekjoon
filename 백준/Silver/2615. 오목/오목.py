def solve(arr):
    for i in range(19):
        for j in range(19):
            if arr[i][j]==0:
                continue
            else:
                n = arr[i][j]  # 1인지 2인지
                for di, dj in ((-1,1),(0,1),(1,1),(1,0)):
                    cnt = 1
                    ni, nj = i+di, j+dj
                    while 0<=ni<19 and 0<=nj<19 and arr[ni][nj]==n:
                        cnt+=1      # 연속되는 바둑알 구하기
                        if cnt==5:  # 오목의 맨앞, 맨뒤도 연속되는지 확인
                            if 0<=i-di<19 and 0<=j-dj<19 and arr[i-di][j-dj]==n:
                                break
                            if 0<=ni+di<19 and 0<=nj+dj<19 and arr[ni+di][nj+dj]==n:
                                break
                            return n, i+1, j+1
                        ni += di
                        nj += dj
    return False

arr = [list(map(int, input().split())) for _ in range(19)]
if not solve(arr):
    print(0)
else:
    n, a, b = solve(arr)
    print(n)
    print(a, b)