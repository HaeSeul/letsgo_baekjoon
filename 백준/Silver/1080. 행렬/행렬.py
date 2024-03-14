N,M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]

cnt = 0

if (N<3 or M<3) and A != B:
    cnt = -1
else:
    for i in range(0, N-2):
        for j in range(0, M-2):
            # A,B 서로 다르면
            if A[i][j] != B[i][j]:
                cnt += 1
                # 행렬 뒤집기
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        A[r][c] ^= 1
    if A != B:
        cnt = -1

print(cnt)