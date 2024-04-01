from collections import deque

N,M,K = map(int, input().split())
dir = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
food = [[5]*N for _ in range(N)]    # 양분
tree = [[deque() for _ in range(N)] for _ in range(N)]  # 나무
plus = [list(map(int, input().split())) for _ in range(N)]
for i in range(M):
    x,y,z = map(int, input().split())
    tree[x - 1][y - 1].append(z)

for k in range(K):
    grow = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not tree[i][j]: continue
            trees = tree[i][j]
            new = deque()
            more_food = 0
            while trees:
                t = trees.popleft()
                if food[i][j] >= t:
                    food[i][j] -= t
                    new.append(t+1)
                    if (t+1) % 5 == 0:
                        grow[i][j] += 1
                else:
                    more_food += t // 2
            tree[i][j] = new
            food[i][j] += more_food

    for i in range(N):
        for j in range(N):
            if grow[i][j]:
                cnt = grow[i][j]
                for di, dj in dir:
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < N and 0 <= nj < N): continue
                    for _ in range(cnt):
                        tree[ni][nj].appendleft(1)
            food[i][j] += plus[i][j]

alive = 0
for i in range(N):
    for j in range(N):
        if not tree[i][j]:continue
        alive += len(tree[i][j])

print(alive)