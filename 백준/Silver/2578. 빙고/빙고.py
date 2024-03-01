def check(n):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == n:
                return i,j

def solve():
    global bingo, cross1, cross2
    for r in range(5):
        for c in range(5):
            i,j = check(num[r][c])
            row[i] += 1
            if row[i] == 5:
                bingo += 1
            col[j] += 1
            if col[j] == 5:
                bingo += 1
            if i - j == 0:
                cross1 += 1
                if cross1 == 5:
                    bingo+=1
            if i + j == 4:
                cross2 += 1
                if cross2 == 5:
                    bingo+=1

            if bingo >= 3:
                return (5 * r) + (c + 1)

arr = [list(map(int, input().split())) for _ in range(5)]
num = [list(map(int, input().split())) for _ in range(5)]
row = [0]*5
col = [0]*5
cross1 = 0  # 좌상->우하 대각선
cross2 = 0  # 우상->좌하 대각선
bingo = 0
print(solve())