import sys
input = sys.stdin.readline

# 현재 큐브의 아래 구하기
def find(cube, down):
    # 현재 큐브의 윗면 구하기
    for i in range(6):
        # 윗 큐브의 아래에 해당하는 숫자
        if cube[i] == down:
            up_idx = i
            break

    # 윗면이 결정된 후 아래 & 옆의 max 구하기
    down_idx = pair[up_idx]
    if up_idx==0 or up_idx==5:
        return [cube[down_idx], max(cube[1],cube[2],cube[3],cube[4])]
    elif up_idx==1 or up_idx==3:
        return [cube[down_idx], max(cube[0],cube[2],cube[4],cube[5])]
    elif up_idx==2 or up_idx==4:
        return [cube[down_idx], max(cube[0],cube[1],cube[3],cube[5])]


N = int(input())
cubes = [list(map(int, input().split())) for _ in range(N)]
ans = 0
pair = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}   # 서로 마주보는 면

# 1번 주사위 A~F 각각의 아래 구하기
for i in range(6):
    down, cnt = find(cubes[0], cubes[0][i])
    # 2~N 주사위 아래 구하기
    for j in range(1, N):
        down, tmp = find(cubes[j], down)
        cnt += tmp
    ans = max(ans, cnt)
print(ans)