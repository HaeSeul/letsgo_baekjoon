from collections import deque

def solve():
    global turn,num
    while True:
        # 벨트 회전
        turn += 1
        belt.appendleft(belt.pop())
        # 내리는 곳에 있는 로봇 내려주기
        if belt[N - 1][1] == 1:
            belt[N - 1][1] = 0

        # 올리는 곳 내구도>0 & 로봇이 없을 때
        if belt[0][0] > 0 and not belt[0][1]:
            belt[0][1] = 1  # 로봇올리기
            belt[0][0] -= 1  # 내구도--
            if belt[0][0] == 0:
                num += 1
                if num >= K:
                    return turn

        # 먼저 올라간 로봇부터 이동
        for i in range(N - 2, 0, -1):
            # 현재 로봇이 있고 옆에 내구도>0 & 로봇이 없을 때
            if belt[i][1] and belt[i + 1][0] > 0 and not belt[i + 1][1]:
                belt[i][1] = 0  # 로봇옮기기
                if i + 1 != N - 1:  # 내리는 위치가 아닐 때만 옮겨주기
                    belt[i + 1][1] = 1
                belt[i + 1][0] -= 1  # 내구도--
                if belt[i + 1][0] == 0:
                    num += 1
                    if num >= K:
                        return turn


N,K=map(int, input().split())
a=list(map(int, (input().split())))

# (내구도, 로봇여부) deque 생성
belt = deque([[i,0] for i in a])
turn = 0    # 벨트 회전 횟수 (= 단계)
num = 0     # 내구도 0인 것의 개수

print(solve())