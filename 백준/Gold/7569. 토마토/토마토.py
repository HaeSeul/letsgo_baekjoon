from collections import deque
import sys
input = sys.stdin.readline

# 위,아래,앞,뒤,좌,우
dh = [-1,1,0,0,0,0]
di = [0,0,-1,1,0,0]
dj = [0,0,0,0,-1,1]

def bfs():
    global not_tomato
    while q:
        ch, ci, cj = q.popleft()
        for d in range(6):
            nh, ni, nj = ch+dh[d], ci+di[d], cj+dj[d]
            if 0<=nh<H and 0<=ni<N and 0<=nj<M and not v[nh][ni][nj] and box[nh][ni][nj]==0:
                v[nh][ni][nj] = v[ch][ci][cj]+1
                q.append((nh,ni,nj))
                not_tomato -= 1     # 토마토가 익을 때마다 삭제
    if not_tomato > 0:      # 남은 토마토가 있다면 -1
        return -1
    else:
        return v[ch][ci][cj]-1


M,N,H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
v = [[[0]*M for _ in range(N)] for _ in range(H)]
q = deque()

not_tomato = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if box[h][i][j]==0:
                not_tomato+=1
            elif box[h][i][j]==1:   # 익어있는 토마토 저장
                q.append((h,i,j))
                v[h][i][j] = 1
print(bfs())