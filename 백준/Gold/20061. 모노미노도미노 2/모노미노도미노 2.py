from collections import deque

def type1(arr, y):
    i = 0
    while i < 5:
        if arr[i + 1][y]: break
        i += 1
    arr[i][y] = 1
    return arr

def type2(arr, y):
    i = 0
    while i < 5:
        if arr[i + 1][y] or arr[i + 1][y + 1]: break
        i += 1
    arr[i][y], arr[i][y + 1] = 1, 1
    return arr

def type3(arr, y):
    i = 0
    while i < 4:
        if arr[i + 2][y]:
            break
        i += 1
    arr[i][y], arr[i + 1][y] = 1, 1
    return arr

def pop(arr, n):    # n번째 행 제외하고 리턴
    new = deque()
    new += arr[:n] + arr[n + 1:]
    for _ in range(6 - len(new)):
        new.appendleft([0, 0, 0, 0])
    arr = list(new)
    return arr

def special_pop(arr, n):
    new = []
    for row in range(5 - n, -1, -1):    # 없애야하는 행 제외하고 복사
        new.append(arr[row])
    for _ in range(n):                  # 없앤 만큼 더해주기
        new.append([0, 0, 0, 0])
    new.reverse()
    arr = new
    return arr


green = [[0 for _ in range(4)] for _ in range(6)]
blue = [[0 for _ in range(4)] for _ in range(6)]
N = int(input())
score = 0
for _ in range(N):
    t,x,y = map(int, input().split())

    # 모양에 맞게 블록 쌓기
    if t==1:    # 1*1
        green = type1(green, y)
        blue = type1(blue, x)
    elif t==2:  # 1*2
        green = type2(green, y)
        blue = type3(blue, x)
    elif t==3:  # 2*1
        green = type3(green, y)
        blue = type2(blue, x)

    # 완성된 행 있는지 확인  ==> 점수 누적 구간!!
    for i in range(6):
        if sum(green[i]) == 4:      # 완성된 것 있을 때마다 점수 올리고 pop
            score += 1
            green = pop(green, i)
        if sum(blue[i]) == 4:
            score += 1
            blue = pop(blue, i)

    # 특수 행에 있는지 확인
    g_special, b_special = 0,0
    for i in range(2):      # 뭔가 있기만 하면 +=1
        if sum(green[i]) > 0: g_special += 1
        if sum(blue[i]) > 0: b_special += 1
    if g_special: green = special_pop(green, g_special)
    if b_special: blue = special_pop(blue, b_special)

print(score)
print(sum(map(sum, green)) + sum(map(sum, blue)))