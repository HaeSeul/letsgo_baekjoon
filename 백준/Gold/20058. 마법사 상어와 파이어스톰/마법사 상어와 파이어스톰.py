from collections import deque

def bfs(si,sj):
    group = 1   # 현재 얼음 덩어리 그룹 개수
    v[si][sj] = group
    q = deque([(si,sj)])
    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = ci+di, cj+dj

            # 범위, 얼음, 방문 체크
            if not (0<=ni<2**N and 0<=nj<2**N): continue
            if not arr[ni][nj]: continue
            if v[ni][nj]: continue

            group += 1
            v[ni][nj] = group
            q.append((ni,nj))
    return group


N,Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**N)]
cmd = map(int, input().split())

# Q개의 Level
for L in cmd:

    # 격자 90도 회전
    for i in range(2**(N-L)):
        for j in range(2**(N-L)):

            # 격자 나누기
            tmp = [[0]*2**L for _ in range(2**L)]
            for ii in range(2**L):
                for jj in range(2**L):
                    tmp[ii][jj] = arr[i*2**L + ii][j*2**L + jj]

            # 90도 회전
            tmp = list(map(list, zip(*tmp[::-1])))

            # arr 갱신
            for ii in range(2**L):
                for jj in range(2**L):
                    arr[i*2**L + ii][j*2**L + jj] = tmp[ii][jj]

    # 얼음과 맞닿아 있는지 확인
    check = []
    for i in range(2**N):
        for j in range(2**N):
            # 얼음이 있는 곳만 확인
            if not arr[i][j]: continue

            cnt = 0
            for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
                ni,nj = i+di, j+dj
                if not (0<=ni<2**N and 0<=nj<2**N): continue
                if not arr[ni][nj]: continue
                cnt += 1
            # 사방에 얼음 있는 곳이 3개 미만이라면 얼음 녹음
            if cnt < 3:
                check.append((i,j))
    for i,j in check:
        arr[i][j] -= 1

# 남은 얼음 개수 & 최대 얼음 덩어리
ice = 0
mx = 0
v = [[0]*2**N for _ in range(2**N)]
for i in range(2 ** N):
    for j in range(2 ** N):
        if not arr[i][j]: continue
        ice += arr[i][j]
        if not v[i][j]:
            mx = max(mx, bfs(i,j))
print(ice)
print(mx)