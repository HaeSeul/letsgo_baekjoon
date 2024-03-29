N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

mx = -1

shapes = [[[1,1],[1,1]]]
r1 = [[[1,1,1,1]], [[1,0],[1,1],[0,1]], [[0,1],[1,1],[1,0]]]
r4 = [[[1,0],[1,0],[1,1]], [[0,1],[0,1],[1,1]], [[1,1,1],[0,1,0]]]
for r in r1:
    shapes.append(r)
    shapes.append(list(map(list, zip(*r[::-1]))))
for r in r4:
    for _ in range(4):
        r = list(map(list, zip(*r[::-1])))
        shapes.append(r)

for shape in shapes:
    n,m = len(shape), len(shape[0])
    for i in range(N-n+1):
        for j in range(M-m+1):
            sm = 0
            for r in range(n):
                for c in range(m):
                    if shape[r][c]:
                        sm += arr[i+r][j+c]
            mx = max(mx, sm)
print(mx)