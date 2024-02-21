from collections import deque
import sys
input = sys.stdin.readline

'''
십자가의 크기 = 가운데를 중심으로 상하좌우에 있는 * 개수
십자가로 격자판 만들기
십자가 개수 = N*M 이하
(1,1)부터 시작
'''

def bfs(i,j,q):
    # q : (ni,nj,d)
    size = 1     # 십자가의 크기
    tmp = []     # 4방에 있는지 카운트
    while q:
        for t in range(4):
            ci,cj,d = q.popleft()
            # 현재 바라보고 있는 방향에 '*'이 있는지 확인
            ni, nj = ci + dir[d][0], cj + dir[d][1]
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == '*' or arr[ni][nj] == '0':
                    tmp.append((ni,nj,d))
        # 4방에 '*'가 있다면 q에 추가해서 탐색
        if len(tmp) == 4:
            size += 1
            for _ in range(4):
                t = tmp.pop()
                arr[t[0]][t[1]] = '0'
                q.append(t)
        else:
            tmp = []
            while size>0:
                ans.append((i+1,j+1,size))
                size-=1


N,M=map(int, input().split())
arr=[list(input().rstrip()) for _ in range(N)]
dir = ((-1,0),(0,1),(1,0),(0,-1))

ans = []
for i in range(N):
    for j in range(M):
        # '*' 사방 모두 '*'인 곳 찾기
        tmp = 0
        if arr[i][j]=='*' or arr[i][j]=='0':
            for d in range(4):
                ni, nj = i + dir[d][0], j + dir[d][1]
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] == '*' or arr[ni][nj] == '0':
                        tmp += 1
            if tmp==4:
                # 4방+방향 => q에 저장
                arr[i][j] = '0'
                q = deque()
                for d in range(4):
                    ni, nj = i + dir[d][0], j + dir[d][1]
                    arr[ni][nj] = '0'
                    q.append((ni,nj,d))
                # 현재 중심 좌표 => bfs
                bfs(i,j,q)


def check(arr):
    for l in arr:
        if l.count('*')>0:
            return False
    return True

if check(arr):
    print(len(ans))
    for a in ans:
        print(*a)
else:
    print(-1)