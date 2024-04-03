def OOB(i,j):
    return not (0<=i<N and 0<=j<N)

def solve():
    global out
    i,j = N//2, N//2
    d, move = 0, 1
    while True:
        for _ in range(2):
            for _ in range(move):
                i,j = i+dir[d][0], j+dir[d][1]

                sand = arr[i][j]
                arr[i][j] = 0
                sm = 0
                for di,dj,r in ratio[d]:
                    ni,nj,spread = i+di, j+dj, sand*r//100
                    sm += spread
                    if OOB(ni,nj): out += spread
                    else: arr[ni][nj] += spread

                ai, aj = i + dir[d][0], j + dir[d][1]
                if OOB(ai,aj): out += sand - sm
                else: arr[ai][aj] += sand - sm
                if (i,j) == (0,0): return

            d = (d+1)%4
        move += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dir = ((0,-1),(1,0),(0,1),(-1,0))
ratio = (((-2,0,2),(-1,-1,10), (-1,0,7), (-1,1,1), (0,-2,5), (1,-1,10), (1,0,7),(1,1,1),(2,0,2)),
         ((-1,-1,1),(-1,1,1),(0,-2,2),(0,-1,7),(0,1,7),(0,2,2),(1,-1,10),(1,1,10),(2,0,5)),
         ((-2,0,2),(-1,-1,1),(-1,0,7),(-1,1,10),(0,2,5),(1,-1,1),(1,0,7),(1,1,10),(2,0,2)),
         ((-2,0,5),(-1,-1,10),(-1,1,10),(0,-2,2),(0,-1,7),(0,1,7),(0,2,2),(1,-1,1),(1,1,1)))
out = 0
solve()
print(out)