from collections import deque

def dummy():
    time = 1
    d = 0
    ci, cj = 0, 0
    snake = deque([(ci, cj)])
    arr[ci][cj] = 1
    for op in cmd:

        # 방향 바뀌기 전까지 앞으로 가기
        while time <= int(op[0]):
            ni, nj = ci + dir[d][0], cj + dir[d][1]

            # 종료조건
            if not (0 <= ni < N and 0 <= nj < N): return time
            if arr[ni][nj] == 1: return time

            # 앞에 사과가 없다면 꼬리 잘라주기
            if arr[ni][nj] != 2:
                tail = snake.popleft()
                arr[tail[0]][tail[1]] = 0

            snake.append((ni,nj))
            arr[ni][nj] = 1

            # 앞으로 나아가기
            ci, cj = ni, nj
            time += 1

        # 방향 바꾸기
        if op[1] == 'L':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4

    # cmd가 끝난 이후
    while True:
        ni, nj = ci + dir[d][0], cj + dir[d][1]

        # 종료조건
        if not (0 <= ni < N and 0 <= nj < N): return time
        if arr[ni][nj] == 1: return time

        # 앞에 사과가 없다면 꼬리 잘라주기
        if arr[ni][nj] != 2:
            tail = snake.popleft()
            arr[tail[0]][tail[1]] = 0

        snake.append((ni, nj))
        arr[ni][nj] = 1

        # 앞으로 나아가기
        ci, cj = ni, nj
        time += 1


N = int(input())
arr = [[0]*N for _ in range(N)]
dir = ((0,1),(1,0),(0,-1),(-1,0))

# 사과 개수만큼 사과 찍기
K = int(input())
for _ in range(K):
    ai,aj = map(lambda x:x-1, map(int, input().split()))
    arr[ai][aj] = 2

# 방향 정보 저장 (X가 증가하는 순으로)
cmd = []
L = int(input())
for _ in range(L):
    cmd.append(list(input().split()))   # 문자로 받음!! 주의

print(dummy())