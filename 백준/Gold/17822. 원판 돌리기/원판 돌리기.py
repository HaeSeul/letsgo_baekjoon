from collections import deque

def get():
    sm, cnt = 0, 0
    for i in range(1, N+1):
        for j in range(M):
            if not arr[i][j]: continue
            sm += arr[i][j]
            cnt += 1
    return sm, cnt

N,M,T = map(int, input().split())
# arr 처음/마지막에 padding 추가
arr = [deque([0])*M] + [deque(map(int, input().split())) for _ in range(N)] + [deque([0])*M]
dir = ((-1,0),(0,1),(1,0),(0,-1))

for t in range(T):
    X,D,K = map(int, input().split())

    # 원판 회전
    for i in range(1, N+1):
        if i % X != 0: continue  # X의 배수인 행만

        circle = arr[i]
        if D == 0:  # 시계방향 회전
            for _ in range(K):
                circle.appendleft(circle.pop())
        else:       # 반시계 회전
            for _ in range(K):
                circle.append(circle.popleft())

    # 인접한 같은 수 찾기
    v = [[0]*M for _ in range(N+2)]
    same = set()
    for i in range(1, N+1):
        for j in range(M):
            if arr[i][j] == 0: continue
            for di, dj in ((-1,0),(0,1),(1,0),(0,-1)):
                ni, nj = i+di, (j+dj)%M
                if v[ni][nj]: continue
                if arr[ni][nj] == 0: continue
                if arr[ni][nj] == arr[i][j]:
                    same.add((i,j))
                    same.add((ni,nj))
                    v[i][j] = 1     # 나만 일단 방문처리

    # 같은 수가 있다면 0 처리
    if same:
        for i,j in same:
            arr[i][j] = 0
    else:
        sm, cnt = get()
        if cnt > 0:
            avg = sm / cnt
            for i in range(1, N+1):
                for j in range(M):
                    if arr[i][j] == 0: continue
                    if arr[i][j] > avg:     arr[i][j] -= 1
                    elif arr[i][j] < avg:   arr[i][j] += 1

sm, cnt = get()
print(sm)