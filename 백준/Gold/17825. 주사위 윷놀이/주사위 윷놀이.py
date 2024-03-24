# 현재 칸 id : 연결된 칸 id
board = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5,
         5: 6, 6: 7, 7: 8, 8: 9, 9: 10,
         10: 11, 11: 12, 12: 13, 13: 14, 14: 15,
         15: 16, 16: 17, 17: 18, 18: 19, 19: 20,
         21: 22, 22:23, 23: 29,
         24: 25, 25: 29,
         26: 27, 27: 28, 28: 29,
         29: 30, 30: 31, 31: 20, 20: 32}

# 파란 칸 id
blue = {5: 21, 10: 24, 15: 26}

# score[id]의 점수
scores = [0, 2, 4, 6, 8, 10,
         12, 14, 16, 18, 20,
         22, 24, 26, 28, 30,
         32, 34, 36, 38, 40,
         13, 16, 19, 22, 24,
         28, 27, 26, 25, 30,
         35, 0]

mx = -1
dice = list(map(int, input().split()))
horses = [0,0,0,0]

def find(cur, move):
    if cur in (5, 10, 15):  # 파란칸 말
        nxt = blue[cur]
        for _ in range(move - 1):
            nxt = board[nxt]
    else:
        nxt = cur
        for _ in range(move):
            if nxt == 32: return 32
            nxt = board[nxt]

    if nxt in horses:
        return -1

    return nxt


def dfs(n, score, horses):
    global mx
    if n == 10:     # 10번 턴 후 끝
        mx = max(mx, score)
        return

    move = dice[n]  # n번째 주사위 숫자

    # 현재 칸에서 move 칸 이동 후 다음 칸 구하기
    for i in range(4):
        cur = horses[i]
        if cur == 32: continue  # 도착한 말 제외
        nxt = find(cur, move)   # 다음 칸 구하기
        if nxt == -1: continue  # 이미 그 칸에 말 있으면 제외

        horses[i] = nxt
        dfs(n+1, score+scores[nxt], horses)
        horses[i] = cur     # 되돌려주기


dfs(0, 0, horses)
print(mx)