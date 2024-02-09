from collections import deque

'''
1. arr[i][j]의 25개 중 7개 중복 없는 조합
2. S가 4개 미만인 것 가지치기
3. 연속된 위치에 있는지 조사
'''

# bfs로 서로 연결되는지 확인
def connected(lst):
    # v에 tmp의 요소 집어넣기
    v=[[-1]*5 for _ in range(5)]
    for l in lst:
        v[l[0]][l[1]]=0

    # tmp의 첫 요소부터 탐색
    v[lst[0][0]][lst[0][1]] = 1
    q = deque([(lst[0][0], lst[0][1])])
    cnt=1
    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<5 and 0<=nj<5 and v[ni][nj]==0:
                v[ni][nj]=cnt+1
                q.append((ni,nj))
                cnt+=1

    # 7개가 연결되어 있는지 확인
    if cnt < 7:
        return False
    return True


# 중복 없는 조합으로 25명 중 7명 뽑기
def dfs(n, s, y_count):
    global ans
    # Y가 3개를 넘어간다면 가지치기
    if y_count > 3:   return

    if n==7:
        # 7명이 연결되어 있다면 정답
        if connected(tmp):
            ans += 1
        return

    for c in range(s, 25):
        # tmp에 학생 위치 저장
        idx = student[c]
        tmp.append((idx[0],idx[1]))

        # 다음 학생이 Y인 경우
        if arr[idx[0]][idx[1]] == 'Y':
            dfs(n+1, c+1, y_count+1)
        else:
            dfs(n+1, c+1, y_count)
        tmp.pop()


arr = [list(input()) for i in range(5)]
tmp = []
ans = 0

# (0,0) ~ (4,4) 조합 만들기
student = []
for i in range(5):
    for j in range(5):
        student.append((i,j))

# 0명 뽑은 상태, start, Y 학생수
dfs(0,0, 0)
print(ans)