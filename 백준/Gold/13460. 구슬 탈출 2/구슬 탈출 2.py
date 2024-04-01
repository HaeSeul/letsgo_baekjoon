import sys
input = sys.stdin.readline

from collections import deque

def tilt(ni,nj,d):
    while arr[ni+dir[d][0]][nj+dir[d][1]] != '#' and arr[ni][nj] != 'O':
        ni,nj = ni+dir[d][0], nj+dir[d][1]
    return ni,nj

def bfs(ri,rj,bi,bj):
    v = set()
    v.add((ri,rj,bi,bj))
    q = deque([(ri,rj,bi,bj)])
    cnt = 1
    while q:
        for _ in range(len(q)):
            ri, rj, bi, bj = q.popleft()

            # 종료조건
            if cnt > 10:
                print(-1)
                return

            for d in range(4):
                nri, nrj = tilt(ri, rj, d)
                nbi, nbj = tilt(bi, bj, d)
                if arr[nbi][nbj] == 'O': continue # 파랑 -> 구멍으로 가면 패스
                if arr[nri][nrj] == 'O':          # 빨강 -> 구멍으로 가면 끝!
                    print(cnt)
                    return

                # 움직인 곳이 같은 경우 더 많이 온 곳을 한 칸 뒤로
                if (nri, nrj) == (nbi, nbj):
                    if abs(ri-nri)+abs(rj-nrj) > abs(bi-nbi)+abs(bj-nbj):
                        nri, nrj = nri-dir[d][0], nrj-dir[d][1]
                    else:
                        nbi, nbj = nbi-dir[d][0], nbj-dir[d][1]

                if (nri, nrj, nbi, nbj) in v: continue  # 이미 왔던 곳 패스
                v.add(((nri, nrj, nbi, nbj)))
                q.append(((nri, nrj, nbi, nbj)))
        cnt += 1
    # 못 가는 경우
    print(-1)

N,M = map(int, input().split())
arr = [list() for _ in range(N)]
dir = ((-1,0),(0,1),(1,0),(0,-1))

ri,rj,bi,bj = 0,0,0,0
for i in range(N):
    a = list(input())
    for j in range(M):
        arr[i].append(a[j])
        if a[j] == 'R':
            ri,rj = i,j
        if a[j] == 'B':
            bi,bj = i,j

bfs(ri,rj,bi,bj)