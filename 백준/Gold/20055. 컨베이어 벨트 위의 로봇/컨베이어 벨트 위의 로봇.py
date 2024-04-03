N,K = map(int, input().split())
belt = list(map(int, input().split()))
robot = [0 for _ in range(2*N)]
turn = 1

while True:
    # 1. 벨트 & 로봇회전
    belt = [belt[-1]] + belt[:-1]
    robot = [robot[-1]] + robot[:-1]
    if robot[N-1]:   # 로봇 내리기
        robot[N-1] = 0

    # 2. 로봇이동
    for i in range(N-2, -1, -1):
        if not robot[i]: continue
        if robot[i+1]: continue     # 다른로봇
        if not belt[i+1]: continue  # 내구도 없음
        robot[i], robot[i+1] = robot[i+1], robot[i]
        belt[i+1] -= 1
    if robot[N-1]:   # 로봇 내리기
        robot[N-1] = 0

    # 3. 올리는 칸에 올리기
    if belt[0]:
        robot[0] = 1
        belt[0] -= 1

    # 4. 내구도
    if belt.count(0) >= K:
        print(turn)
        break

    turn += 1