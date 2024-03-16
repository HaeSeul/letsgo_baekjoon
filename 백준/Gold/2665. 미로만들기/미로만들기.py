from collections import deque

def search(i,j):
    v = [[INF]*N for _ in range(N)]
    v[0][0] = 0     # 시작 -> 무조건 흰 방
    q = deque([(i,j)])
    while q:
        ci,cj = q.popleft()
        # 끝 방 가장 먼저 도착한 것 리턴
        if (ci,cj) == (N-1, N-1):
            return v[ci][cj]

        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if not (0<=ni<N and 0<=nj<N): continue

            # 검은 방 : 새로운 갱신값이 더 작다면 갱신
            if arr[ni][nj] == 0 and v[ni][nj] > v[ci][cj]+1:
                v[ni][nj] = v[ci][cj]+1
                q.append((ni,nj))

            # 흰 방 : 작은 것의 개수 그대로
            if arr[ni][nj] == 1 and v[ni][nj] > v[ci][cj]:
                v[ni][nj] = v[ci][cj]
                q.appendleft((ni,nj))


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
INF = N*N+100  # 최대 N*N개 바꾸기
print(search(0,0))