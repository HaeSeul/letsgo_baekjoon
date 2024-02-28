def flip(origin, R, C):
    new = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            new[i][j] = origin[i][C-1-j]
    return new


def rotate90(origin, R, C):
    R,C = C,R
    new = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            new[i][j] = origin[C-1-j][i]
    return new, R, C

T1 = [[1,1,1,1]]
T2 = [[1,0],[1,0],[1,1]]
T3 = [[1,0],[1,1],[0,1]]
T4 = [[1,1,1],[0,1,0]]
T5 = [[1,1],[1,1]]
T = [T1,T2,T3,T4,T5]

def check(t, r, c, R, C):
    cnt = 0
    for i in range(R):
        for j in range(C):
            if t[i][j] == 1:
                cnt += arr[i+r][j+c]
    return cnt

N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
mx = 0

for t in T:
    R,C = len(t), len(t[0])

    # 기존 모형에서 회전 4회
    for _ in range(4):
        t, R, C = rotate90(t, R, C)
        for r in range(N-R+1):
            for c in range(M-C+1):
                tmp = check(t, r, c, R, C)
                mx = max(mx, tmp)

    # flip
    t = flip(t, R, C)

    # flip 모형에서 회전 4회
    for _ in range(4):
        t, R, C = rotate90(t, R, C)
        for r in range(N-R+1):
            for c in range(M-C+1):
                tmp = check(t, r, c, R, C)
                mx = max(mx, tmp)

print(mx)