from collections import deque

def bfs(v,i,j):
    v[i][j] = 1
    q = deque([(i,j)])
    united = [(i,j)]
    cnt = 1
    people = arr[i][j]

    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if not (0<=ni<N and 0<=nj<N): continue
            if v[ni][nj]: continue
            if L <= abs(arr[ci][cj] - arr[ni][nj]) <= R:
                cnt += 1
                people += arr[ni][nj]
                v[ni][nj] = cnt
                q.append((ni,nj))
                united.append((ni,nj))
    return united, people, cnt


def solve():
    global time
    while True:
        v = [[0] * N for _ in range(N)]
        not_move = 0

        for i in range(N):
            for j in range(N):
                if v[i][j]: continue

                united, people, cnt = bfs(v, i, j)

                # 종료조건 : 더이상 인구 이동 없는 경우
                if cnt == 1:
                    not_move += 1
                if not_move == N*N: return

                for ui, uj in united:
                    arr[ui][uj] = people // cnt
        time += 1

N,L,R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
time = 0

solve()
print(time)