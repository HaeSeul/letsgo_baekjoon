from collections import deque

def move():
    # 적 이동하기
    arr_T.pop(0)
    arr_T.append([0] * M)


def bfs(si,sj):
    global kill, arr_T
    v = [[0]*M for _ in range(N)]
    v[si][sj] = 1
    q = deque([(si,sj)])
    while q:
        ci,cj = q.popleft()
        # 가장 가까운 적을 만난 경우
        if arr_T[ci][cj] == 1:
            kill.add((ci, cj))  # 궁수마다 같은 적 쏠 수 있음
            break
        # 거리가 같은 것 중 가장 왼쪽부터
        for di,dj in ((0,-1),(1,0),(0,1)):
            ni,nj = ci+di, cj+dj
            if not (0<=ni<N and 0<=nj<M):   continue
            if v[ni][nj]:       continue
            if v[ci][cj]+1 > D: continue    # D 거리 이내
            v[ni][nj] = v[ci][cj] + 1
            q.append((ni,nj))


def play(p):
    global kill, arr_T
    # 매 조합마다 cnt 갱신
    cnt = 0
    while True:
        if sum(sum(x) for x in arr_T)==0: break
        kill = set()
        for si, sj in p:    # (0행, j열) -> 궁수 위치
            bfs(si, sj)     # 궁수마다 bfs로 공격할 적 탐색
        for ki, kj in kill: # 적 쏘기
            arr_T[ki][kj] = 0
            cnt += 1
        move()
    return cnt


def permute(n):
    global mx, arr_T
    if n==3:    # 궁수 3명 뽑으면 끝
        arr_T = [x[::] for x in arr[::-1]]
        mx = max(mx, play(p))
        return
    for i in range(M):
        if not v[i]:
            v[i]=1
            p.append((0,i))     # 첫 행에 궁수 배치
            permute(n+1)
            p.pop()
            v[i]=0

N,M,D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 궁수 3군데 배치
mx = 0
v = [0]*M
p = []      # 궁수의 위치
permute(0)
print(mx)