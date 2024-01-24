N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
table = [[0]*1000 for _ in range(1000)]
total = [0 for _ in range(N+1)]
num = 0
for ci, cj, di, dj in arr:
    num += 1
    ni = ci + di - 1
    nj = cj + dj - 1
    for i in range(di):
        for j in range(dj):
            table[ci+i][cj+j] = num

for tr in range(1000):
    for tc in range(1000):
        if table[tr][tc] == 0:
            continue
        total[table[tr][tc]] += 1

for i in total[1:]:
    print(i)