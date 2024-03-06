def take_seat(k,ti,tj):
    # arr에 놓기, arr 인접 4방 좌표의 빈칸개수-1
    arr[ti][tj][0] = k
    seat[k] = [ti, tj]
    for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
        ni, nj = ti + di, tj + dj
        if not (0 <= ni < N and 0 <= nj < N): continue
        arr[ni][nj][1] -= 1

N = int(input())

# [학생번호, 인접 빈칸 개수]
arr = [[[0,4] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i==0 or i==N-1 or j==0 or j==N-1:
            if (i,j) in ((0,0),(0,N-1),(N-1,0),(N-1,N-1)):
                arr[i][j][1] = 2
            else:
                arr[i][j][1]=3

# [학생좌표 i,j] <= (학생이 자리에 있는지 확인)
seat = [[] for _ in range(N**2+1)]

# 학생 리스트 생성
people = dict()
for _ in range(N**2):
    tmp = list(map(int, input().split()))
    people[tmp[0]] = tmp[1:]

# 특정 학생의 리스트 순회하며 좋아하는 학생이 앉아있는지 확인
for k, v in people.items():
    like = []       # [현재 학생 i,j, 인접 좋아하는 학생수, 빈칸개수]
    cnt = 0

    for person in v:
        # 좋아하는 학생 중 자리에 있는 경우
        if seat[person]:
            # seat[i]에 저장된 좌표의 4방을 like에 저장
            ti,tj = seat[person]
            for di,dj in ((-1,0),(0,-1),(0,1),(1,0)):
                ni, nj = ti + di, tj + dj
                if not (0 <= ni < N and 0 <= nj < N): continue
                if arr[ni][nj][0]:  continue    # 다른 사람 앉아있음
                cnt += 1
                like.append([ni,nj,0,arr[ni][nj][1]])

    # 좋아하는 학생이 자리에 없거나 주변이 이미 다 찬 경우
    if cnt==0:
        mx_blank = -1
        ti,tj = 0,0 # 앉을 자리
        for i in range(N):
            for j in range(N):
                if arr[i][j][0]: continue   # 다른 사람 앉아있음
                if mx_blank < arr[i][j][1]:
                    mx_blank = arr[i][j][1]
                    ti,tj = i,j
        # 자리 앉기
        take_seat(k,ti,tj)

    if like:
        # like의 4방 탐색
        for n in range(len(like)):
            li, lj = like[n][0], like[n][1]
            for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                ni, nj = li + di, lj + dj
                if not (0 <= ni < N and 0 <= nj < N): continue
                # 근처에 다른 좋아하는 사람 있다면
                if arr[ni][nj][0] and arr[ni][nj][0] in v:
                    like[n][2] += 1

        # 좋아하는 사람 -> 빈 칸 순으로 정렬
        like.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))
        target = like[0]
        take_seat(k, target[0], target[1])

# 학생 만족도 구하기
ans = 0
for i in range(N):
    for j in range(N):
        student = arr[i][j][0]
        happy = 0
        # 학생 주변 좋아하는 학생 수 구하기
        for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            ni,nj = i+di, j+dj
            if not (0 <= ni < N and 0 <= nj < N): continue
            if arr[ni][nj][0] in people[student]:
                happy += 1
        if happy > 0:
            ans += 10 ** (happy-1)
print(ans)