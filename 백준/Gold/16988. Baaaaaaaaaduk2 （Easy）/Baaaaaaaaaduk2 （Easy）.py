import sys
import copy
input=sys.stdin.readline
from collections import deque


def bfs(i, j, arr, v):
    global flag
    tmp = 1  # 2가 있는 그룹마다 개수 세기
    v[i][j] = 1
    q = deque([(i,j)])
    while q:
        ci,cj = q.popleft()
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            if arr[ni][nj] == 0:  # 주변에 0이 있다면 return 0 (해당 그룹은 더 볼 필요 X)
                flag=0
            if arr[ni][nj] == 2 and not v[ni][nj]:
                tmp += 1
                v[ni][nj] = tmp
                q.append((ni,nj))
    return tmp


# 1을 놓을 수 있는 곳 중 2곳 뽑기
def find(n,s):
    global cnt, mx, flag
    if n==2 or len(blank)==1:
        arr_copy = copy.deepcopy(arr)
        v = [[0] * (M + 2) for _ in range(N + 2)]
        cnt = 0

        if len(blank)==1:
            for i,j in blank:
                black.append((i,j))

        # 검은 바둑알 2곳에 두기
        for ci, cj in black:
            arr_copy[ci][cj] = 1

        # 검은 바둑알 놓은 곳 주변의 2 탐색
        for ci, cj in black:
            for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                flag=1
                ni, nj = ci + di, cj + dj
                if arr[ni][nj] == 2 and not v[ni][nj]:
                    tmp = bfs(ni,nj,arr_copy,v)
                    if flag:
                        cnt += tmp

        # cnt 갱신
        mx = max(mx, cnt)
        return

    for i in range(s,len(blank)):
        black.append(blank[i])
        find(n+1,i+1)
        black.pop()

N,M = map(int, input().split())
arr = [[1]*(M+2)]+[[1]+list(map(int, input().split()))+[1] for _ in range(N)]+[[1]*(M+2)]

mx = 0
black=[]  # 1을 놓을 두 곳

# 2의 4방에 0이 있는 곳 좌표 저장
blank = []
for i in range(N+2):
    for j in range(M+2):
        if arr[i][j]!=2:    continue
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj=i+di,j+dj
            if arr[ni][nj]==0 and (ni,nj) not in blank:
                blank.append((ni,nj))
find(0,0)
print(mx)