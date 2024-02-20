from collections import deque

# 빈 칸은 '0' 처리 (왼손:0~2행, 오른손:3~5행)
keyboard = [['q','w','e','r','t','0'],
            ['a','s','d','f','g','0'],
            ['z','x','c','v','0','0'],
            ['0','y','u','i','o','p'],
            ['0','h','j','k','l','0'],
            ['b','n','m','0','0','0']]

def bfs(si,sj,N):
    v = [[0]*6 for _ in range(6)]
    v[si][sj]=1
    q=deque([(si,sj)])
    while q:
        ci,cj = q.popleft()
        # 해당 키를 찾은 경우
        if keyboard[ci][cj] == keyboard[i][j]:
            return ci, cj, v[ci][cj] - 1
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if N<=ni<N+3 and 0<=nj<6 and not v[ni][nj]:
                v[ni][nj] = v[ci][cj]+1
                q.append((ni,nj))
    return -1

sl,sr = input().split()
a = list(input())
key = []
li,lj,ri,rj=0,0,0,0
tmp,d=0,0

# 양 손의 첫 위치 & 눌러야 하는 키보드 좌표 구하기
for k in a:
    for i in range(6):
        for j in range(6):
            if keyboard[i][j] == sl:
                li,lj = i,j
            if keyboard[i][j] == sr:
                ri,rj = i,j
            if keyboard[i][j] == k:
                key.append((i,j))
# 눌러야하는 키의 행에 따라 왼/오 손가락 이동거리 계산
for i,j in key:
    if i<=2:
        li,lj,tmp = bfs(li,lj,0)   # 왼손 이동거리
    else:
        ri,rj,tmp = bfs(ri,rj,3)   # 오른손 이동거리
    d += tmp + 1    # 이동하고 키 누르기
print(d)