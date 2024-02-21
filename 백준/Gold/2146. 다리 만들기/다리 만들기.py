from collections import deque

def bfs(i,j,num):
    MAP[i][j]=num
    q=deque([(i,j)])
    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0), (0,1), (1,0), (0,-1)):
            ni,nj = ci+di, cj+dj
            if not (0<=ni<N and 0<=nj<N):   continue
            if MAP[ni][nj]:                 continue
            if arr[ni][nj]==0:      # 바다와 맞닿은 육지 (좌표,섬번호) 저장
                lands.add((ni,nj,num))
                continue
            MAP[ni][nj] = num         # 섬번호 부여
            q.append((ni,nj))


def search(i,j,num):
    global mn
    v = [[0] * N for _ in range(N)]
    v[i][j]=1
    q=deque([(i,j)])
    while q:
        ci,cj = q.popleft()
        if v[ci][cj] > mn:  continue
        for di,dj in ((-1,0), (0,1), (1,0), (0,-1)):
            ni,nj = ci+di, cj+dj
            if not (0<=ni<N and 0<=nj<N): continue
            # 어딘가의 섬이면서 내 섬과 다른 육지를 만난 경우
            if MAP[ni][nj] and MAP[ni][nj]!=num:
                mn = min(mn, v[ci][cj])
                break
            # 바다이면서 아직 방문하지 않은 경우
            if not MAP[ni][nj] and not v[ni][nj]:
                v[ni][nj] = v[ci][cj]+1
                q.append((ni,nj))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
MAP = [[0] * N for _ in range(N)]
num = 0         # 섬의 개수 = 섬번호
lands = set()   # (섬좌표, 섬번호)

# [ 1 ] 섬을 만나면 섬의 영역 파악 + 번호 부여
for i in range(N):
    for j in range(N):
        if arr[i][j] and not MAP[i][j]:
            num += 1
            bfs(i, j, num)  # 시작 i,j, 섬번호

# [ 2 ] 내 섬과 다른 섬이 나올 때까지의 최소 거리 구하기
mn = 100000
for land in lands:
    i,j,num = land
    search(i, j, num)  # 시작좌표, 섬번호

print(mn)