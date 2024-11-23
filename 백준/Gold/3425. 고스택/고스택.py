import sys
input = sys.stdin.readline

def exceed_limit(x): # 연산 후 값 확인
    return True if abs(x)>10**9 else False

quit = 0

while True:

    cmds = []    # 프로그램 명령어

    # 프로그램 설명
    while True:
        op = input().rstrip()

        if op == 'QUIT':     # 더이상 기계 없다면 끝
            quit = 1
            break
        if op == 'END': break    # 프로그램 설명 끝

        cmds.append(op) # 명령어 저장

    if quit : break

    ans = []    # 연산 후 값 저장

    # 입력영역 개수만큼 스택 생성
    for _ in range(int(input())):
        stk = [int(input())]    # stack

        # 각 스택에 프로그램 개수만큼 실행
        for cmd in cmds:
            if cmd[:3] == 'NUM':
                stk.append(int(cmd[4:]))

            elif cmd == 'POP':
                if not stk:
                    ans.append('ERROR')
                    break
                stk.pop()

            elif cmd == 'INV':
                if not stk:
                    ans.append('ERROR')
                    break
                stk[-1] = -stk[-1]

            elif cmd == 'DUP':
                if not stk:
                    ans.append('ERROR')
                    break
                stk.append(stk[-1])

            elif cmd == 'SWP':
                if len(stk) < 2:
                    ans.append('ERROR')
                    break
                stk[-1], stk[-2] = stk[-2], stk[-1]

            elif cmd == 'ADD':
                if len(stk) < 2:
                    ans.append('ERROR')
                    break
                a,b = stk.pop(), stk.pop()
                tmp = b + a
                if exceed_limit(tmp):
                    ans.append('ERROR')
                    break
                else: stk.append(tmp)

            elif cmd == 'SUB':
                if len(stk) < 2:
                    ans.append('ERROR')
                    break
                a, b = stk.pop(), stk.pop()
                tmp = b - a
                if exceed_limit(tmp):
                    ans.append('ERROR')
                    break
                else:
                    stk.append(tmp)

            elif cmd == 'MUL':
                if len(stk) < 2:
                    ans.append('ERROR')
                    break
                a, b = stk.pop(), stk.pop()
                tmp = b * a
                if exceed_limit(tmp):
                    ans.append('ERROR')
                    break
                else:
                    stk.append(tmp)

            elif cmd == 'DIV':
                if len(stk) < 2 or stk[-1] == 0:
                    ans.append('ERROR')
                    break
                a, b = stk.pop(), stk.pop()
                tmp = abs(b) // abs(a)

                # 둘 중 하나만 음수일 때 몫은 음수
                if (a<0 and b>0) or (a>0 and b<0): tmp = -tmp
                if exceed_limit(tmp):
                    ans.append('ERROR')
                    break
                else:
                    stk.append(tmp)

            elif cmd == 'MOD':
                if len(stk) < 2 or stk[-1] == 0:
                    ans.append('ERROR')
                    break
                a, b = stk.pop(), stk.pop()
                tmp = abs(b) % abs(a)

                # 피제수(b)가 음수면 나머지도 음수
                if b<0: tmp = -tmp

                if exceed_limit(tmp):
                    ans.append('ERROR')
                    break
                else:
                    stk.append(tmp)

        else:
            # 모든 수행 종료 후 스택에 남은 개수가 하나가 아니라면 에러
            if len(stk) != 1: ans.append('ERROR')
            else: ans.append(stk[-1])

    input()  # 다음 기계로 넘어감

    for i in ans: print(i)
    print()