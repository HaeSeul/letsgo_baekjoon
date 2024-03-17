win = False
i, j = 0, 0
turn = 1
while True:
    try:
        ipt = input()
        if len(ipt) < 4: break
    except EOFError:
        break

    go = ipt.count('0')
    if go == 0: go = 5  # 1111
    j += go

    if i == 0:
        if j == 5:
            i, j = 1, 0
        elif j == 10:
            i, j = 2, 0
        elif j > 20 and turn < 11:
            win = True
    elif i == 1:
        if j == 3:
            i, j = 3, 0
        elif j > 11 and turn < 11:
            win = True
    elif i == 2 and j > 6 and turn < 11:
        win = True
    elif i == 3 and j > 3 and turn < 11:
        win = True

    # 윷(4)/모(5)의 경우 turn 추가 X
    if go == 4 or go == 5:
        continue
    turn += 1

if win:
    print('WIN')
else:
    print('LOSE')