from collections import deque


def spread(arr_t, remain):
    v = [[0]*M for _ in range(N)]
    q = deque()
    for i,j in virus:
        q.append((i,j))
    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and not v[ni][nj] and arr_t[ni][nj]==0:
                v[ni][nj] = 2
                arr_t[ni][nj] = 2
                remain -= 1
                q.append((ni,nj))
    return remain


# 0의 좌표 중 중복 없이 3개 뽑기
def get_pos(n,s):
    global ans
    if n==3:
        arr_t = [x[::] for x in arr]

        # 3개 뽑은 곳에 벽 세우기
        for r,c in tmp:
            arr_t[r][c] = 1
        safe = len(zeros)-3

        # 벽 세워진 arr_t 기준으로 바이러스 퍼뜨리기
        remain = spread(arr_t, safe)

        ans = max(ans, remain)
        return
    for i in range(s, len(zeros)):
        tmp.append(zeros[i])
        get_pos(n+1, i+1)
        tmp.pop()


N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
tmp = []
zeros = []
virus = deque()

# arr 순회하며 0과 2 위치 저장
for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            zeros.append((i,j))
        elif arr[i][j]==2:
            virus.append((i,j))

get_pos(0,0)
print(ans)