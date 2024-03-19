from collections import deque

def find_clients(ti,tj):
    v = [[-1]*N for _ in range(N)]
    v[ti][tj] = 0
    q = deque([(ti,tj)])
    clients = []
    m = 0           # 지금까지 찾은 손님 수
    while q:
        ci,cj = q.popleft()
        if arr[ci][cj] == 2:        # 택시 위치에 있을 수도 있음
            clients.append((v[ci][cj], ci, cj))     # (택시에서 손님까지 거리, 손님좌표)
            m += 1
        if m == M: return clients   # M명 다 찾았으면 리턴

        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = ci+di, cj+dj

            # 경계, 방문, 벽 체크
            if not (0<=ni<N and 0<=nj<N): continue
            if not v[ni][nj]==-1 or arr[ni][nj]==1: continue

            v[ni][nj] = v[ci][cj] + 1
            q.append((ni,nj))
    return clients


def to_goal(ti,tj,ei,ej):
    v = [[-1]*N for _ in range(N)]
    v[ti][tj] = 0
    q = deque([(ti,tj)])
    while q:
        ci,cj = q.popleft()
        if ci==ei and cj==ej:   # 도착지
            return v[ci][cj]

        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = ci+di, cj+dj

            # 경계, 방문, 벽 체크
            if not (0<=ni<N and 0<=nj<N): continue
            if not v[ni][nj]==-1 or arr[ni][nj]==1: continue

            v[ni][nj] = v[ci][cj] + 1
            q.append((ni,nj))
    return -1


N,M,fuel = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ti,tj = map(lambda x:x-1, map(int, input().split()))
end = dict()    # { (손님좌표) : (도착좌표) }

# 손님(2) 배치
for _ in range(M):
    si,sj,ei,ej = map(lambda x:x-1, map(int, input().split()))
    end[(si,sj)] = (ei,ej)
    arr[si][sj] = 2

while M:
    # 손님과의 거리 계산
    clients = find_clients(ti, tj)

    # 갈 수 있는 손님이 없는 경우
    if not clients:
        fuel = -1
        break

    # 손님 태우기
    clients.sort()          # 거리 - 행 - 열 순으로 정렬
    dist, nxt_i, nxt_j = clients[0]
    if fuel < dist:         # 연료부족
        fuel = -1
        break
    ti,tj = nxt_i, nxt_j    # 택시이동
    arr[ti][tj] = 0         # 손님태움
    fuel -= dist            # 손님과의 거리만큼 연료 사용

    # 현재 손님의 목적지까지 거리 구하기
    ei, ej = end[(ti,tj)]
    goal = to_goal(ti,tj, ei,ej)

    # 현재 손님 위치에서 목적지까지 못 가거나 연료부족
    if goal == -1 or fuel < goal:
        fuel = -1
        break
    ti,tj = ei,ej   # 택시이동
    fuel += goal    # 연료충전

    M -= 1

print(fuel)