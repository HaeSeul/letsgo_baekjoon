from collections import deque
from collections import defaultdict

def bfs(i,j):
    v = [[0] * N for _ in range(N)]
    v[i][j] = arr[i][j]     # 현재 색상으로 채움
    q = deque([(i,j)])
    group = []              # 현재 그룹에 있는 블록들
    rainbow, mni, mnj = 0, i, j     # 무지개 개수, 기준 블록 좌표
    while q:
        ci,cj = q.popleft()
        group.append((ci,cj))   # 같은 색이거나 무지개인 것 같은 그룹으로 묶기

        if arr[ci][cj] != 0:    # 무지개 아닌 것 중 기준 블록 고르기
            color[ci][cj] = 1   # 다음 탐색 때 중복체크 (이미 같은 그룹)
            (mni, mnj) = min((mni, mnj), (ci,cj))
        else:
            rainbow += 1

        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = ci+di, cj+dj

            # 경계, 방문, 무지개가 아닌 다른 블록 체크
            if not (0<=ni<N and 0<=nj<N): continue
            if v[ni][nj]: continue

            # 무지개이거나 나랑 같은 색
            if arr[ni][nj] == 0 or arr[ni][nj] == arr[i][j]:
                v[ni][nj] = arr[i][j]     # 현재 색상 블록으로 채우기
                q.append((ni,nj))

    if len(group) >= 2:
        groups.append((len(group), rainbow, mni, mnj))
        blocks[(mni, mnj)] = group


def gravity():
    # 열 별로 진행
    for j in range(N):
        for i in range(N-1, -1, -1):    # 아래부터 시작
            # 빈 칸만 탐색
            if arr[i][j] > -2: continue

            idx = i
            while True:
                if idx < 1: break
                # 빈 칸이 아닌데 뭔가 있으면 끝
                if arr[idx][j] != -2: break
                idx -= 1

            # 검은 블록이 아니라면
            if arr[idx][j] != -1:
                arr[i][j] = arr[idx][j]
                arr[idx][j] = -2


N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
score = 0

while True:   # 그룹이 하나도 없을 때까지 반복
    groups = []     # (블록개수, 무지개개수, 기준블록 i,j)
    blocks = defaultdict(list)
    color = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= 0: continue # 일반 블록일 때만 그룹 찾기 시작
            if color[i][j]: continue    # 이미 다른 블록에서 봤던 것
            bfs(i,j)    # 블록 나누기

    if not groups: break

    # 크기가 가장 큰 블록 찾아서 없애고 점수 획득
    groups.sort(reverse=True)
    cnt, rb, ti, tj = groups[0]
    for i,j in blocks[(ti, tj)]:
        arr[i][j] = -2     # 빈 칸으로 만들기
    score += cnt**2

    gravity()
    arr = list(map(list, zip(*arr)))[::-1]
    gravity()

print(score)