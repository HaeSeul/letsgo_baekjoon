# 현재 칸을 기준으로 주사위 숫자에 따라 다음 칸이 어떤 건지 받아오기
def get_next(num, now):
    # 현재 칸이 파란색이라면 blue 딕셔너리 사용
    if now in (5, 10, 15):
        now = blue[now]
        if now == 32: return now
        for _ in range(num-1):
            # 도착칸에 도달하면 숫자 상관없이 도착
            if now == 32: return now
            nxt = MAP[now]
            now = nxt
    else:
        for _ in range(num):
            # 도착칸에 도달하면 숫자 상관없이 도착
            if now == 32: return now
            nxt = MAP[now]
            now = nxt

    # 이동한 위치에 다른 말이 있으면 안 됨 (도착위치면 ㄱㅊ)
    if now != 32 and now in horses: return -1

    return now


def dfs(n, sm):
    global mx
    # 10개 다 이동 후 최대 갱신 (백트래킹)
    if n == 10: # 주사위 10개 숫자 끝
        mx = max(mx, sm)
        return

    num = dice[n]   # n번째 주사위 숫자

    for x in range(4):  # 네 마리 말 중복 순열
        now = horses[x] # 현재 시점 말
        if now == 32: continue  # 이미 도착한 말 제외

        nxt = get_next(num, now)
        if nxt == -1: continue  # 다음 위치에 말이 이미 있음

        horses[x] = nxt
        dfs(n+1, sm + score[nxt])
        horses[x] = now     # 되돌려주기


# 매 칸에 id 부여 (시작부터 도착까지)
# 매 칸의 다음 칸으로 딕셔너리로 연결
# 0 : 시작, 32 : 도착
MAP = {21:22, 22:23, 23:26, 26:30, 30:31, 31:20,
       24:25, 25:26, 27:28, 28:29, 29:26, 20:32}

for i in range(20):
    MAP[i] = i+1
score = [x for x in range(0,41,2)] + [13, 16, 19, 22, 24, 25, 28, 27, 26, 30, 35, 0]


# 시작칸이 파란색 -> 파란 화살표로 이동
blue = {5:21, 10:24, 15:27}
dice = list(map(int, input().split()))


# 초기 말 : [0,0,0,0] -> 매 시점마다 말들이 있는 칸 id 저장
horses = [0,0,0,0]
mx = 0
dfs(0, 0)
print(mx)