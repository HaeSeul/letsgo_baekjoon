def OOB(i,j):
    return not (0<=i<N and 0<=j<N)

def get_list(arr):
    lst = []
    i,j = si,sj
    d, move = 0, 1
    while True:
        for _ in range(2):
            for _ in range(move):
                i,j = i+dir[d][0], j+dir[d][1]
                if arr[i][j]:
                    lst.append(arr[i][j])
                if (i,j) == (0,0): return lst
            d = (d + 1) % 4
        move += 1

def make_arr(lst):
    arr = [[0] * N for _ in range(N)]
    i, j = si, sj
    d, move = 0, 1
    while True:
        for _ in range(2):
            for _ in range(move):
                i, j = i + dir[d][0], j + dir[d][1]
                if not lst: return arr
                arr[i][j] = lst.pop()
                if (i, j) == (0, 0): return arr
            d = (d + 1) % 4
        move += 1


N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dir = ((0,-1),(1,0),(0,1),(-1,0))   # 좌하우상
dr = {1:3, 2:1, 3:0, 4:2}           # 상하좌우
si,sj = N//2, N//2

score = [0, 0, 0, 0]

for _ in range(M):
    # 얼음던지기
    D, S = map(int, input().split())
    for s in range(1,S+1):
        ni,nj = si+dir[dr[D]][0]*s, sj+dir[dr[D]][1]*s
        if OOB(ni,nj): continue
        arr[ni][nj] = 0

    # 1차원으로 받기
    lst = get_list(arr)

    # 구슬폭발
    while True:
        explode = False
        new = []
        tmp = []
        while lst:
            now = lst.pop()
            if not tmp or now == tmp[0]:    # 비어있거나 같은 수거나
                tmp.append(now)
            else:   # 다른 게 나온 경우
                if len(tmp) >= 4:   # 4개 이상이었다면 폭발
                    explode = True
                    n = tmp[0]
                    score[n] += len(tmp)
                else:
                    new += tmp
                tmp = [now]
        if tmp:
            if len(tmp) >= 4:
                score[tmp[0]] += len(tmp)
            else: new += tmp
            tmp = []
        lst = new[::-1]
        if not explode: break

    # 구슬변화
    new = []
    tmp = []
    while lst:
        now = lst.pop()
        if not tmp or now == tmp[0]:
            tmp.append(now)
        else:
            new.append((len(tmp), tmp[0]))
            tmp = [now]
    if tmp:
        new.append((len(tmp), tmp[0]))

    lst = []
    for i in new[::-1]:
        for j in i:
            lst.append(j)

    arr = make_arr(lst[::-1])

print(score[1] + 2*score[2] + 3*score[3])