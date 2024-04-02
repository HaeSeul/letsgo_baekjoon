class Horse:
    def __init__(self, num, i, j, dr):
        self.num = num
        self.i, self.j = i,j
        self.dr = dr
    def __str__(self):
        return f'{self.num}번째 말 {self.i, self.j}의 방향 {self.dr}'


def play():
    global end
    # 1번부터 이동
    for h in horses[1:]:
        # 내 위에 있는 말들 다같이 이동
        idx = arr[h.i][h.j].index(h.num)
        move = arr[h.i][h.j][idx:]
        arr[h.i][h.j] = arr[h.i][h.j][:idx]

        ni,nj = h.i+dir[h.dr][0], h.j+dir[h.dr][1]
        blue = False

        if MAP[ni][nj] == WHITE:
            arr[ni][nj] += move
            if len(arr[ni][nj]) >= 4:
                end = True
                return

        elif MAP[ni][nj] == RED:
            arr[ni][nj] += move[::-1]
            if len(arr[ni][nj]) >= 4:
                end = True
                return

        else:
            if h.dr % 2 == 1: h.dr += 1
            else : h.dr -= 1
            ni, nj = h.i + dir[h.dr][0], h.j + dir[h.dr][1]

            if MAP[ni][nj] == WHITE:
                arr[ni][nj] += move
                if len(arr[ni][nj]) >= 4:
                    end = True
                    return
            elif MAP[ni][nj] == RED:
                arr[ni][nj] += move[::-1]
                if len(arr[ni][nj]) >= 4:
                    end = True
                    return
            else:   # 그위치에 그대로
                arr[h.i][h.j] += move
                blue = True

        # 해당 말들 위치 갱신
        if not blue:
            for x in move:
                horses[x].i, horses[x].j = ni, nj
    return

WHITE, RED, BLUE = 0,1,2
dir = ((0,0),(0,1),(0,-1),(-1,0),(1,0))   # 오왼위아

N,K = map(int, input().split())
MAP = [[2]*(N+2)]+[[2]+list(map(int, input().split()))+[2] for _ in range(N)]+[[2]*(N+2)]
arr = [[list() for _ in range(N+2)] for _ in range(N+2)]
horses = [None]

for k in range(1,K+1):
    r,c,d = map(int, input().split())
    arr[r][c].append(k)     # 번호만 담아두기
    horses.append(Horse(k,r,c,d))

end = False
for turn in range(1,1001):
    play()
    if end :
        print(turn)
        break
else:
    print(-1)