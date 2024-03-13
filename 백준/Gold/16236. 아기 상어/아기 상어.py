import sys
input = sys.stdin.readline
from collections import deque

def cal(i,j,fi,fj):
    v = [[0]*N for _ in range(N)]
    v[i][j] = 0
    q = deque([(i,j)])
    while q:
        ci,cj = q.popleft()
        if (ci,cj)==(fi,fj):
            eat.append([ci,cj,v[ci][cj]])   # [먹이위치, 거리]
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if not (0<=ni<N and 0<=nj<N): continue
            if v[ni][nj]: continue
            if arr[ni][nj] > size: continue
            v[ni][nj] = v[ci][cj]+1
            q.append((ni,nj))


def find():
    fish = []   # 가능한 물고기들
    for i in range(N):
        for j in range(N):
            if 0 < arr[i][j] < size:
                fish.append((i, j))
    return fish


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 상어위치, 2보다 작은 물고기위치
ci,cj,size = 0,0,2
for i in range(N):
    for j in range(N):
        if not arr[i][j]: continue
        if arr[i][j]==9:
            ci,cj = i,j
            arr[i][j] = 0

time = 0
cnt = 0         # 먹은 물고기 수

while True:
    fish = find()       # 가능한 물고기 찾기

    eat = []
    for fi,fj in fish:  # 현재 위치에서 물고기까지 거리 계산
        cal(ci,cj,fi,fj)

    if not eat: break

    eat.sort(key=lambda x:(x[2],x[0],x[1]))    # 거리,행,열 순 정렬

    ti, tj, td = eat[0][0], eat[0][1], eat[0][2]
    ci, cj = ti, tj     # 상어이동
    time += td          # 거리만큼 시간 ++
    arr[ti][tj] = 0     # 물고기먹기
    cnt += 1            # 먹으면 ++
    if cnt == size:
        size += 1       # 크기증가
        cnt = 0

print(time)