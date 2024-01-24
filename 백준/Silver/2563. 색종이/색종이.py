N = int(input())
table = [[0]*100 for _ in range(100)]
ans = 0
for n in range(N):
    ci, cj = map(int, input().split())
    for i in range(10):
        for j in range(10):
            ni, nj = ci+i, cj+j
            if table[ni][nj] == 0:
                table[ni][nj] = 1
for r in table:
    for c in r:
        if c==1:
            ans += 1
print(ans)