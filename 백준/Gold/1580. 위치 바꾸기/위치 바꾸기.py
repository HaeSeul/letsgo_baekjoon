from collections import deque
import sys
input = sys.stdin.readline

'''
서로의 위치를 바꾸는 데에 드는 턴의 최솟값 구하기

한 턴에 하나 또는 두 명의 플레이어 이동 (8방 + 현재위치 -> 이동하지 않을 수도 있음)
각 턴 마지막에 두 플레이어는 같은 곳 X
한 턴에 두 플레이어 서로 위치 바꾸기 X
    
- 범위 밖 X, 벽 X
- 다음 A == 현재 B and 다음 B == 현재 A X
- 다음 A == 다음 B X
'''

def print_func(arr):
    for i in range(N):
        for j in range(M):
            print('%2s' %arr[i][j], end=' ')
        print()

def bfs():
    v[ai][aj][bi][bj]=0
    q = deque([(ai,aj,bi,bj)])

    while q:
        cai,caj,cbi,cbj = q.popleft()

        # A, B 위치 바뀜
        if cai==bi and caj==bj and cbi==ai and cbj==aj:
            return v[cai][caj][cbi][cbj]

        # A의 다음 위치 선정 (범위내, 벽이 아닌 경우만 가능)
        for di in range(9):
            nai,naj = cai + d[di][0], caj + d[di][1]
            if not (0<=nai<N and 0<=naj<M) or arr[nai][naj] == 'X':    continue

            # 동시에 B도 다음 위치 선정
            for dj in range(9):
                nbi, nbj = cbi + d[dj][0], cbj + d[dj][1]
                if not (0<=nbi<N and 0<=nbj<M) or arr[nbi][nbj]=='X': continue

                # A <-> B 교차 제외
                if nai==cbi and naj==cbj and nbi==cai and nbj==caj: continue
                # 다음 A,B가 같은 경우 제외
                if nai==nbi and naj==nbj:   continue

                if not v[nai][naj][nbi][nbj]:
                    v[nai][naj][nbi][nbj] = v[cai][caj][cbi][cbj]+1
                    q.append((nai,naj,nbi,nbj))

    return -1



N,M=map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]    # 문자열로 받음
v = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
d = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (0, 0))

# print_func(arr)

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'A':
            ai, aj = i,j
        elif arr[i][j] == 'B':
            bi, bj = i,j

# print('(ai,aj)', ai,aj, '(bi,bj)',bi,bj)

print(bfs())
# print_func(v)